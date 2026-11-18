import iso, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
from playwright.sync_api import sync_playwright
art = iso.cover_art().replace('410 10 570 460','410 -40 570 510',1)
html = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@600;800&family=Inter:wght@500;600;700&display=swap" rel="stylesheet">
<style>*{{box-sizing:border-box;margin:0}}
body{{width:1600px;height:1000px;background:#F4F1EA;position:relative;overflow:hidden;font-family:Inter,sans-serif}}
.band{{position:absolute;left:0;top:0;width:100%;height:18px;background:#1F3A5F}}
.art{{position:absolute;right:20px;top:60px;width:800px}}
.wrap{{position:absolute;left:100px;top:170px;width:720px}}
.tag{{font-size:26px;letter-spacing:5px;color:#C8372D;font-weight:700;margin-bottom:26px}}
h1{{font-family:Fraunces,serif;font-size:98px;line-height:1.05;color:#1F3A5F;font-weight:800}}
.sub{{font-size:32px;color:#444;margin-top:30px;line-height:1.4}}
.chips{{position:absolute;left:100px;bottom:120px;display:flex;gap:16px}}
.chip{{background:#1F3A5F;color:#fff;font-size:28px;padding:14px 26px;border-radius:40px;font-weight:600}}
.chip.o{{background:#fff;color:#1F3A5F;border:3px solid #1F3A5F}}
.foot{{position:absolute;left:100px;bottom:48px;font-size:24px;color:#666}}
</style></head><body><div class="band"></div>
<div class="art">{art}</div>
<div class="wrap"><div class="tag">PRACTICAL GUIDE 2026</div>
<h1>Renting an Apartment in Japan</h1>
<div class="sub">Costs, contracts, email templates and move-in steps for foreigners</div></div>
<div class="chips"><div class="chip">Illustrated PDF</div><div class="chip">Excel calculator</div><div class="chip o">Instant download</div></div>
<div class="foot">Japan Living Notes</div></body></html>"""
open(HERE / 'cover2.html','w',encoding='utf-8').write(html)
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome"); pg = b.new_page(viewport={'width':1600,'height':1000})
    pg.goto((HERE / 'cover2.html').as_uri(), wait_until='networkidle'); pg.wait_for_timeout(500)
    pg.screenshot(path=str(ROOT / 'cover.png')); b.close()
