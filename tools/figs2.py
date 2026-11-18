"""Dimensional figures that match the isometric illustrations (inline SVG)."""
from art import NAVY, RED, SAND, GOLD, TEAL, SKY, INK, GREY, svg, fig, icon_inner
from iso import adj


def card(x, y, w, h, fill="#fff", rx=14, depth=7, edge=None, stroke="#d9d4c7"):
    e = edge or adj(fill, .72) if fill != "#fff" else "#D3CEC0"
    s = f'<rect x="{x+2}" y="{y+depth+7}" width="{w}" height="{h}" rx="{rx}" fill="#1F3A5F" opacity=".10"/>'
    s += f'<rect x="{x}" y="{y+depth}" width="{w}" height="{h}" rx="{rx}" fill="{e}"/>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke if fill=="#fff" else "none"}" stroke-width="1.5"/>'
    return s


def ball(cx, cy, r, c, label, fs=16):
    return (f'<circle cx="{cx}" cy="{cy+2}" r="{r}" fill="{adj(c, .62)}"/><circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}"/>'
            f'<ellipse cx="{cx-r*.3}" cy="{cy-r*.4}" rx="{r*.42}" ry="{r*.26}" fill="#fff" opacity=".28"/>'
            f'<text x="{cx}" y="{cy+fs*.36}" text-anchor="middle" font-size="{fs}" font-weight="800" fill="#fff">{label}</text>')


def tx(x, y, s, size=14, fill=INK, w=600, anchor="middle", op=1):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}" opacity="{op}">{s}</text>'


def glyph(kind, x, y, s=34, c="#fff"):
    g = icon_inner(kind).replace(NAVY, c)
    return f'<svg x="{x}" y="{y}" width="{s}" height="{s}" viewBox="0 0 60 60">{g}</svg>'


def flow():
    steps = [("Set budget", "& conditions", "coin"), ("Contact", "agencies", "phone"), ("View", "properties", "home"), ("Apply", "form + documents", "form"),
             ("Screening", "2-7 days", "shield"), ("Explanation", "& contract", "seal"), ("Pay initial", "costs", "coin"), ("Keys &", "move in", "home")]
    o = ""
    for i, (a, b, ic) in enumerate(steps):
        r, c = divmod(i, 4)
        x, y = 14 + c * 172, 16 + r * 128
        last = i == 7
        o += card(x, y, 148, 98, RED if last else "#fff", 16)
        o += ball(x + 28, y + 28, 17, RED if not last else NAVY, i + 1)
        o += glyph(ic, x + 100, y + 12, 34, "#fff" if last else NAVY)
        o += tx(x + 74, y + 66, a, 16, "#fff" if last else NAVY, 800) + tx(x + 74, y + 84, b, 13, "#fff" if last else GREY, 600)
        if c < 3:
            o += f'<path d="M{x+155} {y+48} h10" stroke="{NAVY}" stroke-width="3" stroke-linecap="round"/><path d="M{x+161} {y+42} l7 6 l-7 6" fill="none" stroke="{NAVY}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
    o += f'<path d="M690 124 v10 h-675 v8" fill="none" stroke="{GREY}" stroke-width="2" stroke-dasharray="5 4"/>'
    return fig("The whole process", svg(704, 262, o), "Usually 3-6 weeks from first inquiry to keys.")


def whois():
    def node(x, y, w, t, jp, sub, col, ic):
        s = card(x - w / 2, y - 36, w, 72, col, 16, 7)
        s += f'<circle cx="{x-w/2+30}" cy="{y}" r="20" fill="#fff" opacity=".95"/>' + glyph(ic, x - w / 2 + 13, y - 17, 34, col)
        s += tx(x - w / 2 + 58, y - 6, f'{t} <tspan font-weight="500" opacity=".85">{jp}</tspan>', 15, "#fff", 800, "start")
        s += tx(x - w / 2 + 58, y + 16, sub, 12.5, "#fff", 500, "start", .92)
        return s
    o = ""
    for a, b, dash in [((350, 140), (140, 48)), ((350, 140), (140, 232)), ((350, 140), (560, 232)), ((560, 48), (560, 232)), ((560, 48), (140, 48), "6 6")] if False else []:
        pass
    lines = [((350, 140), (160, 48), ""), ((350, 140), (160, 232), ""), ((350, 140), (540, 232), ""), ((540, 48), (540, 232), ""), ((540, 48), (160, 48), "7 6")]
    for a, b, d in lines:
        o += f'<line x1="{a[0]}" y1="{a[1]+8}" x2="{b[0]}" y2="{b[1]+8}" stroke="#1F3A5F" opacity=".12" stroke-width="7" stroke-linecap="round"/>'
        o += f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="{GREY}" stroke-width="3" stroke-dasharray="{d}" stroke-linecap="round"/>'
    o += node(350, 140, 230, "YOU", "(tenant)", "pay rent, follow contract", RED, "person")
    o += node(150, 48, 252, "Agency", "不動産会社", "shows homes, paperwork", NAVY, "home")
    o += node(150, 232, 252, "Guarantor co.", "保証会社", "guarantees your rent", TEAL, "shield")
    o += node(550, 48, 252, "Landlord", "大家", "owns the building", NAVY, "key" if False else "home")
    o += node(550, 232, 252, "Management co.", "管理会社", "repairs, rent, complaints", NAVY, "wrench")
    return fig("Who is who", svg(700, 296, o), "After you move in, you will mostly deal with the management company.")


def costs():
    items = [("First month rent + mgmt", 85000), ("Agency fee (incl. tax)", 88000), ("Security deposit", 80000),
             ("Key money", 80000), ("Guarantor company fee", 42500), ("Fire insurance", 20000), ("Key exchange", 15000)]
    o = ""
    dx, dy = 12, -9
    for i, (n, v) in enumerate(items):
        y = 30 + i * 42
        w = v / 88000 * 320
        c = RED if i == 0 else NAVY
        x = 214
        o += tx(204, y + 21, n, 14.5, "#333", 600, "end")
        o += f'<ellipse cx="{x+w/2+dx}" cy="{y+32}" rx="{w/2+6}" ry="5" fill="#1F3A5F" opacity=".10"/>'
        o += f'<polygon points="{x},{y} {x+dx},{y+dy} {x+w+dx},{y+dy} {x+w},{y}" fill="{adj(c,1.25)}"/>'
        o += f'<polygon points="{x+w},{y} {x+w+dx},{y+dy} {x+w+dx},{y+26+dy} {x+w},{y+26}" fill="{adj(c,.7)}"/>'
        o += f'<rect x="{x}" y="{y}" width="{w}" height="26" fill="{c}"/>'
        o += f'<rect x="{x}" y="{y}" width="{w}" height="6" fill="#fff" opacity=".13"/>'
        o += tx(x + w + dx + 10, y + 19, f"¥{v:,}", 15, INK, 800, "start")
    o += card(14, 336, 672, 58, NAVY, 14, 6)
    o += tx(36, 372, "TOTAL", 17, "#fff", 700, "start", .85) + tx(664, 373, "¥410,500  ≈ 5.1 × monthly rent", 24, GOLD, 800, "end")
    return fig("Example: initial cost for a ¥80,000 apartment", svg(700, 408, o),
               "Rent ¥80,000 + management ¥5,000; deposit 1 month; key money 1 month; agency fee 1 month + tax (the tenant's default share is 0.5 month + tax, unless you agreed to more in advance); guarantor fee 50%. Your numbers will differ.")


def doccards():
    cards = [("id", "Residence card", "front and back", NAVY), ("passport", "Passport", "valid and unexpired", RED), ("coin", "Proof of income", "pay slips / offer letter", TEAL),
             ("form", "Application form", "ask the agency for help", NAVY), ("phone", "Emergency contact", "in Japan, if possible", TEAL), ("seal", "Seal or signature", "ask which is accepted", RED)]
    o = ""
    for i, (ic, t, sub, col) in enumerate(cards):
        r, c = divmod(i, 3)
        x, y = 14 + c * 230, 12 + r * 150
        o += card(x, y, 212, 130, "#fff", 16, 8)
        o += f'<rect x="{x+78}" y="{y+14}" width="56" height="56" rx="14" fill="{adj(col,.7)}"/><rect x="{x+78}" y="{y+10}" width="56" height="56" rx="14" fill="{col}"/>'
        o += glyph(ic, x + 86, y + 18, 40, "#fff") if ic != "seal" else f'<circle cx="{x+106}" cy="{y+38}" r="19" fill="none" stroke="#fff" stroke-width="3"/><text x="{x+106}" y="{y+47}" text-anchor="middle" font-size="22" font-weight="800" fill="#fff">印</text>'
        o += tx(x + 106, y + 96, t, 16, NAVY, 800) + tx(x + 106, y + 115, sub, 12.5, GREY, 500)
    return fig("Typical documents", svg(700, 326, o))


def maisoku():
    o = f'<rect x="20" y="22" width="440" height="330" rx="8" fill="#1F3A5F" opacity=".10"/>'
    o += f'<rect x="14" y="16" width="440" height="330" rx="8" fill="#D3CEC0"/>'
    o += f'<rect x="10" y="10" width="440" height="330" rx="8" fill="#fff" stroke="#d9d4c7" stroke-width="1.5"/>'
    o += f'<path d="M10 18 a8 8 0 0 1 8 -8 h424 a8 8 0 0 1 8 8 v22 h-440z" fill="{NAVY}"/><text x="30" y="36" font-size="17" fill="#fff" font-weight="700">Sample Mansion Shinjuku 305</text>'
    o += f'<rect x="388" y="-4" width="62" height="24" fill="{GOLD}" opacity=".85" transform="rotate(4 420 8)"/>'
    rows = [("Rent", "¥80,000"), ("Mgmt fee", "¥5,000 / month"), ("Deposit / Key money", "1 month / 1 month"),
            ("Layout / Size", "1K / 22.5 ㎡"), ("Station", "Walk 8 min"), ("Built / Structure", "2008 / RC"),
            ("Facing", "South"), ("Contract", "Standard, 2 years"), ("Conditions", "Foreigners OK")]
    for i, (a, b) in enumerate(rows):
        y = 58 + i * 31
        if i % 2 == 0:
            o += f'<rect x="18" y="{y-3}" width="424" height="28" rx="4" fill="{SAND}"/>'
        o += tx(62, y + 16, a, 13.5, GREY, 500, "start") + tx(232, y + 16, b, 14.5, INK, 700, "start")
        o += ball(38, y + 11, 11, RED, i + 1, 12)
    notes = ["Compare rent + mgmt fee together", "Check what the monthly fee covers", "Key money is not returned",
             "Check ㎡ rather than tatami count", "80 m = 1 min; hills and lights not counted",
             "After 1981 = newer earthquake rules", "South-facing = more sun", "Standard or fixed-term?", "Look for 'foreigners OK'"]
    for i, n in enumerate(notes):
        y = 58 + i * 31
        o += f'<path d="M452 {y+11} h14" stroke="{RED}" stroke-width="2" stroke-linecap="round"/><circle cx="452" cy="{y+11}" r="3" fill="{RED}"/>'
        o += f'<text x="474" y="{y+16}" font-size="13.5" fill="#333"><tspan fill="{RED}" font-weight="800">{i+1}</tspan>  {n}</text>'
    return fig("How to read a listing sheet", svg(790, 362, o), "A made-up example. Real sheets are in Japanese; the item order differs by agency.")


def timeline():
    cols = [("Before move-in", ["Pay initial costs", "Book gas opening", "Apply: electricity, water", "Order internet"], NAVY),
            ("Move-in day", ["Receive keys", "Photograph damage", "Check appliances", "Start gas"], RED),
            ("Within 14 days", ["Address registration", "Update insurance & bank", "Mail forwarding", "Learn garbage rules"], TEAL)]
    o = ""
    for i, (t, items, c) in enumerate(cols):
        x = 14 + i * 232
        o += card(x, 10, 214, 52, c, 14, 7) + tx(x + 107, 42, t, 18, "#fff", 800)
        for j, it in enumerate(items):
            y = 82 + j * 44
            o += card(x, y, 214, 34, "#fff", 9, 4)
            o += f'<rect x="{x+12}" y="{y+9}" width="16" height="16" rx="4" fill="#fff" stroke="{c}" stroke-width="3"/>' + tx(x + 38, y + 23, it, 14.5, INK, 600, "start")
    return fig("Move-in timeline", svg(700, 278, o))


def lease_timeline():
    pts = [("Lease starts", "keys & first rent"), ("2-4 months||before end", "renewal papers arrive"), ("1 month before||leaving", "written notice (check contract)"),
           ("Move-out day", "inspection with the agent"), ("After move-out", "itemized bill, deposit settled")]
    o = f'<line x1="40" y1="114" x2="660" y2="114" stroke="#1F3A5F" opacity=".12" stroke-width="12" stroke-linecap="round"/>'
    o += f'<line x1="40" y1="108" x2="660" y2="108" stroke="{NAVY}" stroke-width="8" stroke-linecap="round"/>'
    for i, (t, sub) in enumerate(pts):
        x = 40 + i * 155
        col = RED if i == 2 else NAVY
        w = 140
        bx = max(6, min(x - w / 2, 700 - w - 6))
        o += f'<path d="M{x} 108 v-26" stroke="{col}" stroke-width="3"/>'
        o += card(bx, 10, w, 68, "#fff", 12, 5)
        tl = t.split("||")
        for j, ln in enumerate(tl):
            o += tx(bx + w / 2, (30 if len(tl) == 2 else 49) + j * 17, ln, 13, col, 800)
        o += ball(x, 108, 17, col, i + 1, 15)
        words = sub.split(" "); lines, cur = [], ""
        for wd in words:
            if len(cur + " " + wd) > 20 and cur:
                lines.append(cur); cur = wd
            else:
                cur = (cur + " " + wd).strip()
        lines.append(cur)
        for j, ln in enumerate(lines):
            o += tx(x, 146 + j * 17, ln, 12.5, GREY, 500)
    return fig("From lease start to deposit return", svg(700, 200, o))


# ---------------- generic figures for other guides ----------------
def columns(title, cols, caption=""):
    o = ""
    n = len(cols)
    w = (700 - 28 - (n - 1) * 14) / n
    rows = max(len(c[1]) for c in cols)
    for i, (t, items, c) in enumerate(cols):
        x = 14 + i * (w + 14)
        o += card(x, 10, w, 52, c, 14, 7) + tx(x + w / 2, 42, t, 15, "#fff", 800)
        for j, it in enumerate(items):
            y = 82 + j * 44
            o += card(x, y, w, 34, "#fff", 9, 4)
            o += f'<rect x="{x+8}" y="{y+9}" width="16" height="16" rx="4" fill="#fff" stroke="{c}" stroke-width="3"/>' + tx(x + 30, y + 23, it, 12, INK, 600, "start")
    return fig(title, svg(700, 90 + rows * 44, o), caption)


def presence(title, rows, caption=""):
    o = ""
    for i, (a, jp, note, home) in enumerate(rows):
        r, c = divmod(i, 2)
        x, y = 14 + c * 346, 12 + r * 110
        col = RED if home else TEAL
        o += card(x, y, 330, 92, "#fff", 16, 7)
        o += f'<rect x="{x+14}" y="{y+16}" width="64" height="64" rx="16" fill="{adj(col, .7)}"/><rect x="{x+14}" y="{y+12}" width="64" height="64" rx="16" fill="{col}"/>'
        o += tx(x + 46, y + 52, jp, 20, "#fff", 800)
        o += tx(x + 94, y + 34, a, 17, NAVY, 800, "start") + tx(x + 94, y + 54, note, 12.5, GREY, 500, "start")
        badge = "You must be home" if home else "No visit needed"
        bw = len(badge) * 6.6 + 16
        o += f'<rect x="{x+94}" y="{y+62}" width="{bw}" height="20" rx="10" fill="{col}"/>' + tx(x + 94 + bw / 2, y + 76, badge, 11.5, "#fff", 700)
    n = (len(rows) + 1) // 2
    return fig(title, svg(700, 30 + n * 110, o), caption)


def bring(title, items, caption=""):
    o = ""
    for i, (ic, t, sub) in enumerate(items):
        r, c = divmod(i, 3)
        x, y = 14 + c * 230, 12 + r * 128
        col = [NAVY, RED, TEAL][i % 3]
        o += card(x, y, 212, 112, "#fff", 16, 8)
        o += f'<rect x="{x+78}" y="{y+14}" width="56" height="56" rx="14" fill="{adj(col, .7)}"/><rect x="{x+78}" y="{y+10}" width="56" height="56" rx="14" fill="{col}"/>'
        o += glyph(ic, x + 86, y + 18, 40, "#fff")
        o += tx(x + 106, y + 90, t, 15, NAVY, 800) + tx(x + 106, y + 106, sub, 12, GREY, 500)
    n = (len(items) + 2) // 3
    return fig(title, svg(700, 30 + n * 128, o), caption)
