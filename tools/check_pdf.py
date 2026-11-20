"""Pre-upload check for a guide PDF.

Usage:  python tools/check_pdf.py Renting-an-Apartment-in-Japan.pdf [expected_pages]

Checks: page count, leftover words (draft, TODO, placeholders), every URL in the PDF
(HTTP status), and writes a contact sheet image of all pages for a visual review.
This does NOT upload anything. Upload to Payhip only after the owner confirms.
"""
import re
import sys
import pathlib
import urllib.request

import fitz  # PyMuPDF
from PIL import Image

BAD = [r"\bdraft\b", r"\bTODO\b", r"\[Add ", r"lorem ipsum", r"\bXXX\b"]
ROOT = pathlib.Path(__file__).resolve().parent.parent
THIN_CHARS = 250
THIN_CHARS_WITH_FIGURES = 40
MIN_EXEMPT_CHARS = 100
MAX_URLS = 20


def is_chapter_opener(page_text):
    """Chapter cover pages are deliberately short: a letter-spaced
    'C H A P T E R n' line, a title and one sentence. They are not empty."""
    return re.match(r"^\d*CHAPTER\d", re.sub(r"\s+", "", page_text), flags=re.I) is not None


def http_status(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.status
    except Exception as e:  # noqa: BLE001
        return getattr(e, "code", f"ERR {type(e).__name__}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    pdf = pathlib.Path(sys.argv[1])
    if not pdf.is_absolute():
        pdf = ROOT / pdf
    sheet_path = ROOT / "tools" / "pv-check" / f"{pdf.stem}-sheet.png"

    def fail(msg):
        if sheet_path.exists():
            sheet_path.unlink()
        print(f"  NG: {msg}")
        print("RESULT: PROBLEMS FOUND (fix before asking the owner)")
        sys.exit(1)

    try:
        expected = int(sys.argv[2]) if len(sys.argv) > 2 else None
    except ValueError:
        fail(f"invalid expected page count: {sys.argv[2]}")
    try:
        doc = fitz.open(pdf)
        size_kb = pdf.stat().st_size / 1024
    except Exception as e:  # noqa: BLE001
        fail(f"cannot read {pdf}: {e}")
    if not len(doc):
        fail("PDF has no pages")
    ok = True
    print(f"File: {pdf.name}  pages: {len(doc)}  size: {size_kb:.0f} KB")
    if expected is None:
        print("  OK: page count not checked (no expected value given)")
    elif len(doc) != expected:
        print(f"  NG: expected {expected} pages"); ok = False

    text = "\n".join(str(p.get_text()) for p in doc)
    for pat in BAD:
        for m in re.finditer(pat, text, flags=re.I):
            ctx = text[max(0, m.start() - 30): m.end() + 30].replace("\n", " ")
            print(f"  NG: found '{m.group(0)}' ... {ctx}"); ok = False

    skipped_thin = 0
    for idx in range(len(doc)):
        i = idx + 1
        page = doc.load_page(idx)
        page_text = " ".join(str(page.get_text()).split())
        figures = len(page.get_drawings())
        if len(page_text) >= THIN_CHARS or (len(page_text) >= THIN_CHARS_WITH_FIGURES and figures >= 10):
            continue
        if (i == 1 or is_chapter_opener(page_text)) and len(page_text) >= MIN_EXEMPT_CHARS and figures >= 1:
            skipped_thin += 1
            continue
        print(f"  NG: page {i} is nearly empty ({len(page_text)} characters, {figures} drawings)")
        ok = False
    if skipped_thin:
        print(f"  OK: {skipped_thin} short page(s) are cover/chapter openers (expected)")

    urls = set(re.findall(r"https?://[^\s)>\]]+", text))
    skipped = set()
    for page in doc:
        for link in page.get_links():
            uri = link.get("uri")
            if not uri:
                continue
            if uri.lower().startswith(("http://", "https://")):
                urls.add(uri)
            else:
                skipped.add(uri)
    for u in sorted(skipped):
        print(f"  SKIP: {u} (non-http scheme, not checked)")
    if len(urls) > MAX_URLS:
        print(f"  NG: {len(urls)} URLs exceed the limit of {MAX_URLS}; not all checked")
        ok = False
    for u in sorted(urls)[:MAX_URLS]:
        st = http_status(u)
        good = st == 200
        print(f"  {'OK' if good else 'NG'}: {st} {u}")
        ok = ok and good

    out = ROOT / "tools" / "pv-check"
    out.mkdir(exist_ok=True)
    pm = doc.load_page(0).get_pixmap(dpi=45)
    w, h = pm.width, pm.height
    cols = 8
    rows = (len(doc) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * w, rows * h), "white")
    for i, page in enumerate(doc):
        pm = page.get_pixmap(dpi=45)
        im = Image.frombytes("RGB", (pm.width, pm.height), pm.samples)
        sheet.paste(im, ((i % cols) * w, (i // cols) * h))
    sp = sheet_path
    sheet.save(sp)
    print(f"Contact sheet: {sp}")
    result = "ALL CHECKS PASSED (now ask the owner to confirm before uploading)" if ok else "PROBLEMS FOUND (fix before asking the owner)"
    if expected is None:
        result += " (page count not checked)"
    print("RESULT:", result)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
