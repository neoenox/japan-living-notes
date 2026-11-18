import iso, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
from playwright.sync_api import sync_playwright
pins=[('costs',2,'Japan apartment initial costs explained','Deposit, key money, agency fee, guarantor fee: what you really pay','4-6x monthly rent'),
('foreigners',3,'How foreigners can rent an apartment in Japan','Documents, guarantors, and what to do if you are rejected','Step by step'),
('emails',6,'Email templates for Japanese real estate agents','6 copy-and-paste emails: inquiry, negotiation, notice, deposit refund','Copy and paste'),
('listing',4,'How to read a Japanese apartment listing','Rent, 1K vs 1LDK, walking minutes, building age: decoded','Maisoku guide'),
('movein',7,'Moving into your Japan apartment: the 14-day checklist','Utilities, address registration, garbage rules and more','Within 14 days'),
('moveout',8,'Moving out of a Japan apartment: get your deposit back','Notice, repair costs, and what the landlord can charge','Deposit guide')]
css="""*{margin:0;box-sizing:border-box}body{width:1000px;height:1500px;background:#1F3A5F;font-family:Inter,'Noto Sans JP',sans-serif;position:relative;overflow:hidden}
.top{position:absolute;left:60px;top:56px;color:#E8B04A;font-size:26px;letter-spacing:5px;font-weight:700}
.art{position:absolute;left:0;right:0;top:110px;height:700px;display:flex;align-items:center;justify-content:center}.art svg{width:940px}
.card{position:absolute;left:50px;right:50px;top:830px;bottom:50px;background:#F4F1EA;border-radius:28px;box-shadow:0 14px 0 #0f2038;padding:50px 56px}
h1{font-family:Fraunces,serif;font-weight:800;font-size:72px;line-height:1.08;color:#1F3A5F}
p{margin-top:26px;font-size:30px;line-height:1.4;color:#444}
.pill{position:absolute;left:56px;bottom:46px;background:#C8372D;color:#fff;font-size:26px;font-weight:700;padding:12px 28px;border-radius:40px}
.ft{position:absolute;right:56px;bottom:56px;font-size:24px;color:#666}"""
with sync_playwright() as pw:
    b=pw.chromium.launch(channel='chrome'); pg=b.new_page(viewport={'width':1000,'height':1500})
    for k,n,t,s,pill in pins:
        h=f"<html><head><meta charset=utf-8><link href='https://fonts.googleapis.com/css2?family=Fraunces:wght@800&family=Inter:wght@500;700&display=swap' rel=stylesheet><style>{css}</style></head><body><div class=top>JAPAN LIVING NOTES</div><div class=art>{iso.scene(n)}</div><div class=card><h1>{t}</h1><p>{s}</p><div class=pill>{pill}</div><div class=ft>Illustrated PDF + Excel</div></div></body></html>"
        pg.set_content(h,wait_until='networkidle'); pg.wait_for_timeout(300)
        pg.screenshot(path=str(ROOT / f'marketing/pins/pin_{k}.png'))
    b.close()
from PIL import Image
ims=[Image.open(ROOT / f'marketing/pins/pin_{k}.png').resize((333,500)) for k,*_ in pins]
sh=Image.new('RGB',(333*6,500))
for i,im in enumerate(ims): sh.paste(im,(i*333,0))
sh.save(str(ROOT / 'marketing/pins/_sheet.png'))
