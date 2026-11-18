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
    expected = int(sys.argv[2]) if len(sys.argv) > 2 else None
    doc = fitz.open(pdf)
    ok = True
    print(f"File: {pdf.name}  pages: {len(doc)}  size: {pdf.stat().st_size / 1024:.0f} KB")
    if expected and len(doc) != expected:
        print(f"  NG: expected {expected} pages"); ok = False

    text = "\n".join(p.get_text() for p in doc)
    for pat in BAD:
        for m in re.finditer(pat, text, flags=re.I):
            ctx = text[max(0, m.start() - 30): m.end() + 30].replace("\n", " ")
            print(f"  NG: found '{m.group(0)}' ... {ctx}"); ok = False

    for i, page in enumerate(doc, 1):
        page_text = " ".join(page.get_text().split())
        if len(page_text) < 250 and len(page.get_drawings()) < 10:
            print(f"  NG: page {i} is nearly empty ({len(page_text)} characters)")
            ok = False

    urls = set(re.findall(r"https?://[^\s)>\]]+", text))
    for p in doc:
        for l in p.get_links():
            if l.get("uri"):
                urls.add(l["uri"])
    for u in sorted(urls):
        st = http_status(u)
        good = st == 200
        print(f"  {'OK' if good else 'NG'}: {st} {u}")
        ok = ok and good

    out = ROOT / "tools" / "pv-check"
    out.mkdir(exist_ok=True)
    ims = []
    for p in doc:
        pm = p.get_pixmap(dpi=45)
        ims.append(Image.frombytes("RGB", [pm.width, pm.height], pm.samples))
    w, h = ims[0].size
    cols = 8
    rows = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * w, rows * h), "white")
    for i, im in enumerate(ims):
        sheet.paste(im, ((i % cols) * w, (i // cols) * h))
    sp = out / (pdf.stem + "-sheet.png")
    sheet.save(sp)
    print(f"Contact sheet: {sp}")
    print("RESULT:", "ALL CHECKS PASSED (now ask the owner to confirm before uploading)" if ok else "PROBLEMS FOUND (fix before asking the owner)")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
