import fitz, base64, io
from PIL import Image
from playwright.sync_api import sync_playwright
d=fitz.open('../Renting-an-Apartment-in-Japan.pdf')
spec=[('whois',6,.06,.64,'A typical 1K, drawn as a cutaway','Know what you are renting before you view it'),
('emails',33,.03,.50,'Copy-and-paste email templates','Inquiry, viewing, negotiation, application, notice, refund')]
def b64(im):
    b=io.BytesIO(); im.save(b,'PNG'); return base64.b64encode(b.getvalue()).decode()
css="""*{margin:0;box-sizing:border-box}body{width:1600px;height:1000px;background:#1F3A5F;font-family:Inter,'Noto Sans JP',sans-serif;position:relative;overflow:hidden}
.t{position:absolute;left:80px;top:50px;color:#fff;font-family:Fraunces,serif;font-weight:800;font-size:58px}
.s{position:absolute;left:80px;top:128px;color:#b9c8dc;font-size:28px}
.tag{position:absolute;right:80px;top:60px;color:#E8B04A;font-size:22px;letter-spacing:4px;font-weight:700}
.p{position:absolute;left:80px;right:80px;top:200px;bottom:70px;background:#fff;border-radius:18px;box-shadow:0 14px 0 #0f2038;display:flex;align-items:center;justify-content:center;overflow:hidden}
.p img{max-width:100%;max-height:100%}
.f{position:absolute;left:80px;bottom:22px;color:#8aa0bd;font-size:20px}"""
with sync_playwright() as p:
    br=p.chromium.launch(channel='chrome'); pg=br.new_page(viewport={'width':1600,'height':1000})
    for k,n,a,bb,t,s in spec:
        pm=d[n-1].get_pixmap(dpi=200); im=Image.frombytes('RGB',[pm.width,pm.height],pm.samples)
        w,h=im.size; im=im.crop((int(w*.06),int(h*a),int(w*.94),int(h*bb)))
        html=f"<html><head><meta charset=utf-8><link href='https://fonts.googleapis.com/css2?family=Fraunces:wght@800&family=Inter:wght@500;700&display=swap' rel=stylesheet><style>{css}</style></head><body><div class=t>{t}</div><div class=s>{s}</div><div class=tag>SAMPLE PAGE</div><div class=p><img src='data:image/png;base64,{b64(im)}'></div><div class=f>Japan Living Notes</div></body></html>"
        pg.set_content(html,wait_until='networkidle'); pg.wait_for_timeout(300)
        pg.screenshot(path=f'samples/card_{k}.png')
    br.close()
sh=Image.new('RGB',(1600,500))
for i,k in enumerate(('whois','emails')): sh.paste(Image.open(f'samples/card_{k}.png').resize((800,500)),(i*800,0))
sh.save('samples/_cards2.png')
