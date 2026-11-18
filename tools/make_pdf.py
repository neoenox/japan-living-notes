import re, sys, markdown, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from art import *  # noqa
import iso
import figs2
FIGS = {0: figs2.flow(), 1: plan_1k_iso() + figs2.whois() + __import__("art")._minis(), 2: figs2.costs(), 3: figs2.doccards(), 4: figs2.maisoku(), 7: figs2.timeline(), 8: figs2.lease_timeline()}

root = pathlib.Path("E:/foreigner-note")
md = (root / "rental-guide-en.md").read_text(encoding="utf-8")
md = re.sub(r"^(☐ .*)$", lambda m: "\n<div class='ck'>" + m.group(1) + "</div>\n", md, flags=re.M)
_l = md.split("\n"); _o = []
LI = r"^> (- |\d+\. )"
for i, ln in enumerate(_l):
    if re.match(LI, ln) and i and _l[i-1].startswith("> ") and not re.match(LI, _l[i-1]):
        _o.append(">")
    if not re.match(LI, ln) and i and re.match(LI, _l[i-1]) and ln.startswith("> "):
        _o.append(">")
    _o.append(ln)
md = "\n".join(_o)
body = markdown.markdown(md, extensions=["tables", "sane_lists"])

TITLES = {0: "Quick Start", 1: "How Renting Works in Japan", 2: "Know Your Costs", 3: "Can a Foreigner Rent?",
          4: "Finding a Place", 5: "Viewing and Applying", 6: "The Contract", 7: "Move-in",
          8: "Living and Moving Out", 9: "FAQ and Red Flags"}
SUMMARY = {
    0: "The 8-step process, how long it takes, and the typical upfront cost.",
    1: "Who is who, how to read floor plans, building types, and the two kinds of leases.",
    2: "Every initial cost, monthly costs, and ways to lower the total.",
    3: "Whether you can rent, the documents you need, and what to do if you are rejected.",
    4: "Where to search, how to set priorities, and how to read a listing sheet.",
    5: "What to check at a viewing, how applying works, and what screening involves.",
    6: "The explanation of important matters and the clauses to read before signing.",
    7: "Utilities, address registration, garbage rules, and the first weeks.",
    8: "Renewal, giving notice, move-out costs, and getting your deposit back.",
    9: "Common questions and the warning signs to watch for.",
}
TILES = {
    0: [("3-6", "weeks", "first inquiry to keys"), ("4-6×", "rent", "typical upfront cost"), ("8", "steps", "from budget to keys")],
    1: [("20-25", "㎡", "a typical 1K"), ("2", "years", "usual lease term"), ("1981", "", "newer quake standard")],
    2: [("4-6×", "rent", "typical upfront cost"), ("1", "month + tax", "agency fee cap"), ("0-2", "months", "key money range")],
    3: [("Yes", "", "foreigners can rent"), ("2-7", "days", "typical screening"), ("1+", "year", "visa left is safer")],
    4: [("80", "m = 1 min", "station walk rule"), ("3", "priorities", "pick your top three"), ("1981", "", "ask building year")],
    5: [("3-4", "properties", "per viewing day"), ("2-7", "days", "screening time"), ("In writing", "", "refund of holding fee")],
    6: [("1", "month", "usual notice (sometimes 2)"), ("2", "years", "usual lease term"), ("Read", "first", "the special terms")],
    7: [("14", "days", "address registration"), ("2+", "weeks", "book gas in busy season"), ("1-4", "weeks", "internet installation")],
    8: [("2-4", "months", "renewal papers arrive"), ("1", "month", "usual notice to leave"), ("明細", "", "ask for an itemized bill")],
    9: [("6", "red flags", "to watch for"), ("5", "FAQs", "answered"), ("7", "days", "refund window")],
}
CALLOUT = {
    2: ("warn", "Ask for a full written breakdown", "Ask what every line is for before you apply. Be careful with vague items such as &quot;support packages&quot; or &quot;cleaning fees&quot;."),
    3: ("tip", "Use the right agency", "Start with agencies that say they accept foreign customers. It saves weeks of rejected inquiries."),
    5: ("warn", "Do not pay large sums at the application stage", "If a small holding fee is requested, ask whether it is refundable and get that in writing."),
    6: ("tip", "Photograph everything on key day", "Take photos of every scratch and stain and email them to the management company. This protects your deposit later."),
    8: ("tip", "Ask for an itemized bill", "If the move-out charge seems too high, ask for a detailed breakdown (明細) and compare it with the official guideline."),
}


TONE = {"#BFD4EA": "#24426F", "#fff": "#CFDBEC", "#FFF": "#CFDBEC", "#1F3A5F": "#0E1D33", "#2E8B8B": "#5C8DB3",
        "#E8B04A": "#D9B26B", "#2D4F7D": "#1B3459", "#C8372D": "#D2452F"}


def tone(svgstr):
    for a, b in TONE.items():
        svgstr = svgstr.replace(f'"{a}"', f'"{b}"').replace(f"'{a}'", f"'{b}'")
    return svgstr


def opener(n):
    tiles = "".join(f"<div class='tile'><div class='tn'>{a}<span>{b}</span></div><div class='tl'>{c}</div></div>" for a, b, c in TILES[n])
    return (f"<section class='opener'><div class='obig'>{n}</div><div class='olabel'>CHAPTER {n}</div>"
            f"<h2 class='otitle'>{TITLES[n]}</h2><div class='osum'>{SUMMARY[n]}</div>"
            f"<div class='oart'>{iso.scene(n)}</div><div class='tiles'>{tiles}</div></section>")


def chapter_block(chunk):
    m = re.match(r"<h2>Chapter (\d+): (.*?)</h2>", chunk)
    if not m:
        return chunk
    n = int(m.group(1))
    rest = chunk[m.end():]
    head = opener(n) + f"<div class='chbar'>CHAPTER {n} <i>/</i> {TITLES[n].upper()}</div>" + FIGS.get(n, "")
    tail = ""
    if n in CALLOUT:
        k, t, x = CALLOUT[n]
        tail = f"<div class='callout {k}'><div class='ctype'>{'CAUTION' if k == 'warn' else 'TIP'}</div><div><b>{t}</b><br>{x}</div></div>"
    return head + rest + tail


body = re.sub(r"<h1>.*?</h3>", "", body, count=1, flags=re.S)
parts = re.split(r"(?=<h2>)", body)
pre, chunks = parts[0], parts[1:]
front = ""
if chunks and not chunks[0].startswith("<h2>Chapter"):
    front = chunks.pop(0)
out_chunks = []
for c in chunks:
    c = chapter_block(c)
    c = re.sub(r"<h2>(Appendix [A-H])", r"<h2 class='ap'>\1", c)
    c = c.replace("<h2>Appendices</h2>", "<h2 class='aps'>Appendices</h2>")
    out_chunks.append(c)

TOC = "".join(f"<li><b>{i}</b> {TITLES[i]}</li>" for i in range(10)) + "<li><b>A-H</b> Appendices: calculator, glossary, email templates, checklists, phrases, resources</li>"
cover = (f"<section class='cover'><div class='ctag'>PRACTICAL GUIDE · 2026</div><h1>Renting an<br>Apartment<br>in Japan</h1>"
         f"<div class='csub'>Costs, contracts, email templates and move-in steps for foreigners</div>"
         f"<div class='cart'>{iso.cover_art()}</div>"
         f"<div class='cbadges'><span>PDF GUIDE</span><span>EXCEL CALCULATOR</span><span>6 EMAIL TEMPLATES</span></div>"
         f"<div class='cfoot'>Japan Living Notes</div></section>")
intro = f"<section class='intro'><h2 class='aps'>Contents</h2><ol class='toc'>{TOC}</ol>{pre}{front}</section>"
body = cover + intro + "".join(out_chunks)

css = """
@page { size: A4; margin: 18mm 18mm 20mm 18mm; @bottom-center { content: 'Japan Living Notes  ·  ' counter(page); font-family: Inter, sans-serif; font-size: 7.5pt; color: #8a8f99; letter-spacing: 1pt; } }
@page full { size: A4; margin: 0; @bottom-center { content: none; } }
* { box-sizing: border-box; }
:root { --navy:#13243C; --red:#C8372D; --paper:#F7F4EE; --ink:#1d2430; --mute:#6b7280; }
body { font-family: 'Inter','Noto Sans JP','Yu Gothic',sans-serif; font-size: 10pt; line-height: 1.62; color:var(--ink); margin:0; }
.serif, h1, h2, h3, .otitle, .tn, .toc li { font-family: 'Fraunces','Noto Serif JP',Georgia,serif; }
section.cover, section.opener { page: full; width:210mm; height:297mm; position:relative; overflow:hidden; background:var(--navy); color:#fff; page-break-after: always; }
.cover { padding:30mm 20mm; }
.ctag { letter-spacing:5pt; color:#D9B26B; font-weight:600; font-size:9.5pt; }
.cover h1 { font-size:62pt; line-height:1.0; margin:14mm 0 9mm; font-weight:600; letter-spacing:-1pt; }
.csub { font-size:13pt; max-width:120mm; color:#b9c8dc; font-weight:300; line-height:1.5; }
.cart { position:absolute; left:30mm; right:30mm; bottom:24mm; }
.cbadges { position:absolute; left:20mm; bottom:28mm; display:flex; gap:0; font-size:8.5pt; letter-spacing:2pt; font-weight:600; color:#D9B26B; }
.cbadges span + span::before { content:'/'; margin:0 10pt; color:#5b6f8c; }
.cfoot { position:absolute; left:20mm; bottom:16mm; font-size:9pt; letter-spacing:2pt; color:#8fa3bf; text-transform:uppercase; }
.obig { position:absolute; right:12mm; top:-6mm; font-family:'Fraunces',serif; font-size:250pt; font-weight:600; color:transparent; -webkit-text-stroke:1.2pt rgba(255,255,255,.16); line-height:1; }
.olabel { position:absolute; left:20mm; top:30mm; letter-spacing:5pt; color:#D9B26B; font-weight:600; font-size:9.5pt; }
.olabel::after { content:''; display:block; width:28pt; height:2pt; background:var(--red); margin-top:9pt; }
.otitle { position:absolute; left:20mm; top:46mm; width:150mm; margin:0; font-size:38pt; line-height:1.08; color:#fff; border:0; padding:0; font-weight:600; letter-spacing:-.5pt; }
.osum { position:absolute; left:20mm; top:96mm; width:120mm; font-size:11.5pt; color:#b9c8dc; font-weight:300; line-height:1.55; }
.oart { position:absolute; left:20mm; right:20mm; top:106mm; }
.oart svg { display:block; }
.tiles { position:absolute; left:20mm; right:20mm; bottom:18mm; display:flex; gap:22pt; }
.tile { flex:1; color:#fff; border-top:1px solid rgba(255,255,255,.35); padding-top:9pt; }
.tn { font-size:26pt; font-weight:600; line-height:1.05; } .tn span { font-family:'Inter',sans-serif; font-size:8.5pt; font-weight:600; margin-left:5pt; color:#D9B26B; letter-spacing:.5pt; }
.tl { font-size:8.5pt; color:#9fb2cc; margin-top:4pt; }
.intro { page-break-after: always; }
.toc { list-style:none; padding:0; margin:10pt 0 18pt; } .toc li { padding:7pt 0; border-bottom:.5pt solid #d8d4ca; font-size:13pt; }
.toc b { display:inline-block; width:34pt; color:var(--red); font-family:'Inter',sans-serif; font-size:9pt; letter-spacing:1pt; }
h2 { font-size: 17pt; color:var(--navy); border-bottom:.75pt solid var(--navy); padding-bottom:4pt; margin-top:20pt; font-weight:600; }
h2.aps { border:0; font-size:26pt; margin-top:4pt; }
h2.ap { background:none; color:var(--navy); border-top:3pt solid var(--red); border-bottom:.75pt solid #cfcabd; padding:8pt 0 5pt; border-radius:0; }
.chbar { font-size:7.5pt; letter-spacing:2.5pt; font-weight:700; color:var(--red); border-bottom:.5pt solid #cfcabd; padding-bottom:5pt; margin-bottom:12pt; } .chbar i { color:#b9b3a4; font-style:normal; margin:0 4pt; } 
h3, h4 { page-break-after: avoid; }
h3 { color:var(--navy); margin:20pt 0 6pt; font-size:14pt; font-weight:600; }
h3::before { content:''; display:block; width:22pt; height:3pt; background:var(--red); margin-bottom:6pt; }
h4 { margin:10pt 0 2pt; color:var(--navy); font-size:10.5pt; }
ul { list-style:none; padding-left:0; } ul li { position:relative; padding-left:15pt; margin:4pt 0; }
ul li::before { content:''; position:absolute; left:1pt; top:8pt; width:7pt; height:1.5pt; background:var(--red); }
ol li::marker { color:var(--red); font-weight:700; }
strong { color:var(--navy); font-weight:600; }
table { border-collapse: collapse; width:100%; margin:10pt 0; font-size:9pt; }
tr { page-break-inside: avoid; }
th { color:var(--navy); text-align:left; font-size:7.5pt; letter-spacing:1.5pt; text-transform:uppercase; border-bottom:1.5pt solid var(--navy); padding:5pt 8pt 5pt 0; }
td { border-bottom:.5pt solid #dcd8ce; padding:5pt 8pt 5pt 0; vertical-align:top; }
blockquote { page-break-inside: avoid; background:var(--paper); border-left:2.5pt solid var(--navy); margin:10pt 0; padding:6pt 14pt; }
hr { border:0; border-top:.5pt solid #cfcabd; margin:14pt 0; }
.ck { margin:4pt 0; padding-left:20pt; }
.fig { margin:14pt 0 16pt; padding:14pt 16pt 10pt; background:var(--paper); border-radius:3pt; page-break-inside:avoid; }
.figt { font-size:7.5pt; letter-spacing:2.5pt; text-transform:uppercase; font-weight:700; color:var(--red); margin-bottom:8pt; }
.cap { font-size:8pt; color:var(--mute); margin-top:6pt; line-height:1.45; }
.callout { display:flex; gap:14pt; padding:12pt 16pt; margin:18pt 0; page-break-inside:avoid; font-size:9.5pt; background:var(--paper); border-left:3pt solid var(--navy); }
.callout.warn { border-left-color:var(--red); }
.callout .ctype { font-size:7pt; letter-spacing:2pt; font-weight:800; color:var(--navy); padding-top:2pt; width:44pt; flex:none; } .callout.warn .ctype { color:var(--red); }
"""
html = f"<!doctype html><html><head><meta charset='utf-8'><link href='https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@300;400;500;600;700;800&family=Noto+Sans+JP:wght@400;500;700&family=Noto+Serif+JP:wght@500;700&display=swap' rel='stylesheet'><style>{css}</style></head><body>{body}</body></html>"
tmp = root / "tools" / "guide.html"
tmp.write_text(html, encoding="utf-8")
out = root / "Renting-an-Apartment-in-Japan.pdf"

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")
    pg = b.new_page()
    pg.goto(tmp.as_uri(), wait_until='networkidle'); pg.evaluate('document.fonts.ready')
    pg.pdf(path=str(out), prefer_css_page_size=True, print_background=True, display_header_footer=False,)
    b.close()
print(out)
