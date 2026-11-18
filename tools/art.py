"""Illustrations and figures for the guide (inline SVG)."""
NAVY, RED, SAND, GOLD, TEAL, SKY, INK, GREY = "#1F3A5F", "#C8372D", "#F4F1EA", "#E8B04A", "#2E8B8B", "#BFD4EA", "#222", "#666"
FONT = "font-family=\"'Inter','Noto Sans JP','Yu Gothic',sans-serif\""


def svg(w, h, inner, cls=""):
    return f'<svg class="{cls}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" {FONT}>{inner}</svg>'


def windows(x, y, cols, rows, w=14, h=18, gx=10, gy=10, fill="#fff", op=0.9):
    s = ""
    for r in range(rows):
        for c in range(cols):
            s += f'<rect x="{x + c*(w+gx)}" y="{y + r*(h+gy)}" width="{w}" height="{h}" rx="2" fill="{fill}" opacity="{op}"/>'
    return s


# ---------------- chapter scenes (640 x 380, drawn on a light panel) ----------------
def scene(n):
    bg = f'<rect width="640" height="380" fill="{SKY}"/><circle cx="520" cy="95" r="54" fill="{RED}"/>'
    ground = f'<rect y="320" width="640" height="60" fill="{NAVY}"/>'
    s = bg
    if n == 0:  # road to a house
        s += ground
        s += f'<path d="M-10 350 C 150 300, 250 360, 360 318 S 520 300 600 322" fill="none" stroke="#fff" stroke-width="10" stroke-dasharray="26 18"/>'
        for i, (x, y) in enumerate([(120, 310), (240, 335), (350, 312)]):
            s += f'<circle cx="{x}" cy="{y-48}" r="20" fill="{RED}"/><text x="{x}" y="{y-41}" text-anchor="middle" font-size="22" font-weight="800" fill="#fff">{i+1}</text><rect x="{x-2}" y="{y-28}" width="4" height="28" fill="{INK}"/>'
        s += f'<rect x="440" y="205" width="150" height="115" fill="#fff"/><polygon points="425,205 515,140 605,205" fill="{RED}"/><rect x="498" y="250" width="34" height="70" fill="{NAVY}"/>'
        s += windows(455, 225, 1, 1, 26, 26, fill=SKY) + windows(550, 225, 1, 1, 26, 26, fill=SKY)
    elif n == 1:  # skyline
        s += ground
        s += f'<rect x="60" y="90" width="130" height="230" fill="{NAVY}"/>' + windows(78, 108, 4, 7, 16, 20, 9, 12, "#fff", .85)
        s += f'<rect x="215" y="170" width="150" height="150" fill="#fff" stroke="{NAVY}" stroke-width="4"/>' + windows(234, 188, 4, 3, 18, 22, 12, 14, SKY, 1)
        s += f'<rect x="390" y="130" width="110" height="190" fill="{TEAL}"/>' + windows(408, 148, 3, 5, 18, 20, 12, 12, "#fff", .85)
        s += f'<polygon points="520,230 575,190 630,230" fill="{RED}"/><rect x="530" y="230" width="90" height="90" fill="#fff"/><rect x="560" y="262" width="30" height="58" fill="{NAVY}"/>'
    elif n == 2:  # coins
        s += ground
        for k, (x, cnt) in enumerate([(120, 5), (230, 8), (340, 3)]):
            for i in range(cnt):
                y = 305 - i * 18
                s += f'<ellipse cx="{x}" cy="{y}" rx="48" ry="14" fill="{GOLD}" stroke="#B98623" stroke-width="3"/>'
            s += f'<text x="{x}" y="{305-(cnt-1)*18+6}" text-anchor="middle" font-size="22" font-weight="800" fill="#7a5410">¥</text>'
        s += f'<rect x="440" y="110" width="150" height="200" rx="8" fill="#fff"/><rect x="440" y="110" width="150" height="34" rx="8" fill="{NAVY}"/>'
        for i in range(5):
            s += f'<line x1="456" y1="{170+i*28}" x2="574" y2="{170+i*28}" stroke="#bbb" stroke-width="4"/>'
        s += f'<text x="515" y="133" text-anchor="middle" font-size="16" fill="#fff" font-weight="700">TOTAL</text><rect x="500" y="282" width="76" height="14" rx="3" fill="{RED}"/>'
    elif n == 3:  # residence card + passport
        s += ground
        s += f'<g transform="rotate(-6 200 220)"><rect x="70" y="130" width="260" height="165" rx="14" fill="#fff" stroke="{NAVY}" stroke-width="4"/><rect x="88" y="152" width="70" height="86" rx="6" fill="{SKY}"/><circle cx="123" cy="185" r="16" fill="{NAVY}"/><path d="M92 238 q31 -40 62 0z" fill="{NAVY}"/>'
        for i in range(4):
            s += f'<rect x="178" y="{156+i*22}" width="{130-i*16}" height="10" rx="3" fill="#bbb"/>'
        s += f'<rect x="88" y="258" width="222" height="12" rx="3" fill="{TEAL}"/></g>'
        s += f'<g transform="rotate(7 460 215)"><rect x="380" y="95" width="170" height="230" rx="12" fill="{RED}"/><circle cx="465" cy="190" r="42" fill="none" stroke="{GOLD}" stroke-width="5"/><path d="M425 190 h80 M465 148 v84" stroke="{GOLD}" stroke-width="4"/><rect x="415" y="262" width="100" height="10" rx="3" fill="{GOLD}"/></g>'
    elif n == 4:  # map + pin + magnifier
        s += f'<rect x="60" y="60" width="400" height="270" rx="14" fill="#fff"/><path d="M60 170 H460 M60 250 H460 M180 60 V330 M320 60 V330" stroke="{SKY}" stroke-width="16"/><path d="M60 110 L460 280" stroke="{GOLD}" stroke-width="10"/>'
        s += f'<rect x="200" y="190" width="90" height="46" fill="{TEAL}" opacity=".5"/><rect x="340" y="80" width="90" height="70" fill="{TEAL}" opacity=".5"/>'
        s += f'<path d="M250 100 c-30 0 -50 22 -50 50 c0 38 50 85 50 85 s50 -47 50 -85 c0 -28 -20 -50 -50 -50z" fill="{RED}"/><circle cx="250" cy="150" r="17" fill="#fff"/>'
        s += f'<circle cx="480" cy="230" r="70" fill="#fff" fill-opacity=".55" stroke="{NAVY}" stroke-width="12"/><line x1="530" y1="282" x2="600" y2="352" stroke="{NAVY}" stroke-width="20" stroke-linecap="round"/>'
        s += f'<rect x="440" y="215" width="80" height="12" rx="4" fill="{NAVY}"/><rect x="440" y="240" width="55" height="12" rx="4" fill="{RED}"/>'
    elif n == 5:  # door + key
        s += ground
        s += f'<rect x="90" y="60" width="190" height="260" rx="8" fill="{NAVY}"/><rect x="112" y="84" width="146" height="100" rx="6" fill="#2D4F7D"/><rect x="112" y="198" width="146" height="106" rx="6" fill="#2D4F7D"/><circle cx="244" cy="200" r="9" fill="{GOLD}"/>'
        s += f'<g transform="rotate(-25 450 200)"><circle cx="390" cy="200" r="46" fill="{GOLD}" stroke="#B98623" stroke-width="5"/><circle cx="390" cy="200" r="16" fill="{SKY}"/><rect x="430" y="190" width="170" height="22" fill="{GOLD}" stroke="#B98623" stroke-width="4"/><rect x="540" y="212" width="16" height="38" fill="{GOLD}" stroke="#B98623" stroke-width="3"/><rect x="570" y="212" width="16" height="28" fill="{GOLD}" stroke="#B98623" stroke-width="3"/></g>'
        s += f'<rect x="300" y="262" width="130" height="44" rx="6" fill="{RED}"/><text x="365" y="292" text-anchor="middle" font-size="22" font-weight="800" fill="#fff">内見 VIEW</text>'
    elif n == 6:  # contract + seal
        s += f'<rect x="150" y="30" width="300" height="330" rx="10" fill="#fff" stroke="{NAVY}" stroke-width="5"/><rect x="150" y="30" width="300" height="52" rx="10" fill="{NAVY}"/><text x="300" y="64" text-anchor="middle" font-size="22" font-weight="700" fill="#fff">LEASE AGREEMENT</text>'
        for i in range(7):
            s += f'<rect x="178" y="{108+i*26}" width="{244 if i%3 else 190}" height="10" rx="4" fill="#ccd"/>'
        s += f'<circle cx="385" cy="305" r="30" fill="none" stroke="{RED}" stroke-width="6"/><text x="385" y="314" text-anchor="middle" font-size="26" font-weight="800" fill="{RED}">印</text><path d="M178 312 q20 -26 40 0 t40 0" fill="none" stroke="{NAVY}" stroke-width="4"/>'
        s += f'<g transform="rotate(35 520 250)"><rect x="490" y="150" width="22" height="170" rx="4" fill="{GOLD}"/><polygon points="490,320 512,320 501,348" fill="{INK}"/></g>'
    elif n == 7:  # boxes
        s += ground
        def box(x, y, w, h, c):
            return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}" stroke="#7a5410" stroke-width="3"/><rect x="{x+w/2-14}" y="{y}" width="28" height="{h}" fill="#fff" opacity=".35"/>'
        s += box(70, 232, 130, 88, "#D9A55B") + box(210, 232, 120, 88, "#CF9A4D") + box(100, 150, 110, 82, "#D9A55B") + box(235, 160, 90, 72, "#E3B26A")
        s += f'<g transform="translate(420 180)"><rect x="0" y="0" width="170" height="140" rx="8" fill="#fff"/><rect x="0" y="0" width="170" height="36" rx="8" fill="{RED}"/><text x="85" y="25" text-anchor="middle" font-size="17" fill="#fff" font-weight="700">14 DAYS</text>'
        s += f'<rect x="20" y="58" width="130" height="10" rx="4" fill="#ccd"/><rect x="20" y="82" width="100" height="10" rx="4" fill="#ccd"/><circle cx="34" cy="114" r="10" fill="{TEAL}"/><path d="M29 114 l4 5 l8 -10" stroke="#fff" stroke-width="3" fill="none"/></g>'
    elif n == 8:  # calendar + envelope
        s += f'<rect x="90" y="60" width="260" height="260" rx="14" fill="#fff"/><rect x="90" y="60" width="260" height="56" rx="14" fill="{RED}"/><rect x="130" y="40" width="14" height="40" rx="5" fill="{NAVY}"/><rect x="296" y="40" width="14" height="40" rx="5" fill="{NAVY}"/>'
        for r in range(4):
            for c in range(5):
                s += f'<rect x="{112+c*46}" y="{134+r*44}" width="34" height="32" rx="5" fill="{SKY if (r,c)!=(2,3) else GOLD}"/>'
        s += f'<path d="M258 232 l10 12 l20 -22" stroke="{NAVY}" stroke-width="6" fill="none"/>'
        s += f'<rect x="380" y="170" width="200" height="140" rx="10" fill="#fff" stroke="{NAVY}" stroke-width="5"/><path d="M380 180 L480 250 L580 180" fill="none" stroke="{NAVY}" stroke-width="5"/><circle cx="560" cy="170" r="24" fill="{RED}"/><text x="560" y="179" text-anchor="middle" font-size="26" font-weight="800" fill="#fff">1</text>'
    else:  # FAQ
        s += f'<circle cx="230" cy="190" r="140" fill="#fff"/><text x="230" y="260" text-anchor="middle" font-size="230" font-weight="800" fill="{NAVY}">?</text>'
        s += f'<polygon points="470,70 580,270 360,270" fill="{GOLD}" stroke="{INK}" stroke-width="6" stroke-linejoin="round" transform="translate(30 20)"/><rect x="487" y="140" width="20" height="70" rx="6" fill="{INK}" transform="translate(30 20)"/><circle cx="527" cy="250" r="12" fill="{INK}"/>'
    return svg(640, 380, s, "scene")


def cover_art():
    s = f'<rect width="640" height="300" fill="none"/>'
    s += f'<circle cx="470" cy="110" r="70" fill="{RED}"/>'
    s += f'<rect y="240" width="640" height="60" fill="#fff" opacity=".12"/>'
    s += f'<rect x="40" y="90" width="110" height="170" fill="#fff" opacity=".95"/>' + windows(56, 108, 4, 6, 14, 16, 8, 10, NAVY, .9)
    s += f'<rect x="170" y="150" width="130" height="110" fill="{GOLD}"/>' + windows(186, 166, 4, 3, 16, 20, 10, 10, "#fff", .9)
    s += f'<rect x="320" y="120" width="100" height="140" fill="{TEAL}"/>' + windows(336, 136, 3, 4, 16, 18, 10, 10, "#fff", .9)
    s += f'<polygon points="440,200 500,155 560,200" fill="{RED}"/><rect x="448" y="200" width="104" height="60" fill="#fff"/><rect x="487" y="222" width="26" height="38" fill="{NAVY}"/>'
    s += f'<rect x="570" y="130" width="50" height="130" fill="#fff" opacity=".9"/>' + windows(578, 144, 2, 5, 14, 14, 6, 8, NAVY, .9)
    return svg(640, 300, s)


# ---------------- small icons ----------------
def icon(kind, c=NAVY):
    p = {
        "id": f'<rect x="4" y="12" width="52" height="36" rx="5" fill="none" stroke="{c}" stroke-width="4"/><circle cx="19" cy="26" r="6" fill="{c}"/><rect x="30" y="22" width="20" height="4" fill="{c}"/><rect x="30" y="32" width="14" height="4" fill="{c}"/>',
        "passport": f'<rect x="12" y="6" width="36" height="48" rx="4" fill="none" stroke="{c}" stroke-width="4"/><circle cx="30" cy="26" r="9" fill="none" stroke="{c}" stroke-width="3"/><rect x="20" y="42" width="20" height="4" fill="{c}"/>',
        "coin": f'<circle cx="30" cy="30" r="22" fill="none" stroke="{c}" stroke-width="4"/><text x="30" y="40" text-anchor="middle" font-size="28" font-weight="800" fill="{c}">¥</text>',
        "form": f'<rect x="12" y="6" width="36" height="48" rx="4" fill="none" stroke="{c}" stroke-width="4"/><rect x="20" y="18" width="20" height="4" fill="{c}"/><rect x="20" y="28" width="20" height="4" fill="{c}"/><rect x="20" y="38" width="12" height="4" fill="{c}"/>',
        "phone": f'<rect x="18" y="4" width="24" height="52" rx="5" fill="none" stroke="{c}" stroke-width="4"/><circle cx="30" cy="47" r="3" fill="{c}"/>',
        "seal": f'<circle cx="30" cy="30" r="22" fill="none" stroke="{RED}" stroke-width="4"/><text x="30" y="40" text-anchor="middle" font-size="26" font-weight="800" fill="{RED}">印</text>',
        "person": f'<circle cx="30" cy="20" r="11" fill="{c}"/><path d="M8 54 q22 -34 44 0z" fill="{c}"/>',
        "home": f'<polygon points="6,28 30,6 54,28" fill="{c}"/><rect x="14" y="28" width="32" height="26" fill="none" stroke="{c}" stroke-width="4"/>',
        "shield": f'<path d="M30 5 L52 14 V30 C52 42 42 50 30 56 C18 50 8 42 8 30 V14z" fill="none" stroke="{c}" stroke-width="4"/><path d="M20 30 l8 8 l14 -16" fill="none" stroke="{c}" stroke-width="4"/>',
        "wrench": f'<path d="M40 8 a12 12 0 1 0 12 12 l-8 4 l-8 -8 z M30 26 L8 48 l6 6 L36 32" fill="none" stroke="{c}" stroke-width="4" stroke-linejoin="round"/>',
    }[kind]
    return f'<svg viewBox="0 0 60 60" width="100%">{p}</svg>'


# ---------------- figures ----------------
def fig(title, inner, caption=""):
    cap = f"<div class='cap'>{caption}</div>" if caption else ""
    return f"<div class='fig'><div class='figt'>{title}</div>{inner}{cap}</div>"


def flow():
    steps = ["Set budget\n& conditions", "Contact\nagencies", "View\nproperties", "Apply",
             "Screening", "Explanation\n& contract", "Pay initial\ncosts", "Keys &\nmove in"]
    out = ""
    for i, st in enumerate(steps):
        r, c = divmod(i, 4)
        x, y = 15 + c * 172, 20 + r * 125
        col = RED if i == 7 else NAVY
        out += f'<rect x="{x}" y="{y}" width="150" height="96" rx="14" fill="{col}"/>'
        out += f'<circle cx="{x+24}" cy="{y+24}" r="15" fill="#fff"/><text x="{x+24}" y="{y+30}" text-anchor="middle" font-size="18" font-weight="800" fill="{col}">{i+1}</text>'
        for j, ln in enumerate(st.split("\n")):
            out += f'<text x="{x+75}" y="{y+58+j*20}" text-anchor="middle" font-size="16" fill="#fff" font-weight="600">{ln}</text>'
        if c < 3:
            out += f'<path d="M{x+154} {y+48} h14" stroke="{GREY}" stroke-width="3"/><path d="M{x+161} {y+42} l8 6 l-8 6" fill="none" stroke="{GREY}" stroke-width="3"/>'
    out += f'<path d="M690 116 v9 h-675 v9" fill="none" stroke="{GREY}" stroke-width="2" stroke-dasharray="5 4"/>'
    return fig("The whole process", svg(700, 245, out), "Usually 3-6 weeks from first inquiry to keys.")


def whois():
    def node(x, y, t, sub, col, w=200):
        return (f'<rect x="{x-w/2}" y="{y-34}" width="{w}" height="68" rx="14" fill="{col}"/>'
                f'<text x="{x}" y="{y-4}" text-anchor="middle" font-size="18" font-weight="800" fill="#fff">{t}</text>'
                f'<text x="{x}" y="{y+20}" text-anchor="middle" font-size="13" fill="#fff" opacity=".9">{sub}</text>')
    o = ""
    for a, b, dash in [((350, 135), (130, 45), ""), ((350, 135), (130, 225), ""), ((350, 135), (570, 225), ""), ((570, 45), (570, 225), ""), ((570, 45), (130, 45), "6 5")]:
        o += f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="{GREY}" stroke-width="3" stroke-dasharray="{dash}"/>'
    o += node(350, 135, "YOU (tenant)", "pay rent, follow contract", RED, 220)
    o += node(130, 45, "Agency 不動産会社", "shows properties, paperwork", NAVY, 230)
    o += node(130, 225, "Guarantor co. 保証会社", "guarantees your rent", TEAL, 230)
    o += node(570, 45, "Landlord 大家", "owns the building", NAVY, 230)
    o += node(570, 225, "Management co. 管理会社", "repairs, rent, complaints", NAVY, 230)
    return fig("Who is who", svg(700, 275, o), "After you move in, you will mostly deal with the management company.")


def costs():
    items = [("First month rent + mgmt", 85000), ("Agency fee (incl. tax)", 88000), ("Security deposit", 80000),
             ("Key money", 80000), ("Guarantor company fee", 42500), ("Fire insurance", 20000), ("Key exchange", 15000)]
    out = ""
    for i, (n, v) in enumerate(items):
        y = 15 + i * 40
        w = v / 88000 * 330
        out += f'<text x="190" y="{y+20}" text-anchor="end" font-size="15" fill="#333">{n}</text>'
        out += f'<rect x="200" y="{y+3}" width="{w}" height="26" rx="5" fill="{NAVY if i else RED}"/>'
        out += f'<text x="{208+w}" y="{y+22}" font-size="15" fill="#333" font-weight="700">¥{v:,}</text>'
    out += f'<rect x="15" y="298" width="670" height="56" rx="12" fill="{NAVY}"/>'
    out += f'<text x="35" y="333" font-size="18" font-weight="700" fill="#fff">TOTAL</text><text x="665" y="334" text-anchor="end" font-size="26" font-weight="800" fill="{GOLD}">¥410,500  ≈ 5.1 × monthly rent</text>'
    return fig("Example: initial cost for a ¥80,000 apartment", svg(700, 365, out),
               "Rent ¥80,000 + management ¥5,000; deposit 1 month; key money 1 month; agency fee 1 month + tax; guarantor fee 50%. Your numbers will differ.")


def plans():
    def room(x, y, w, h, label, fill="#fff"):
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{NAVY}" stroke-width="3"/><text x="{x+w/2}" y="{y+h/2+5}" text-anchor="middle" font-size="15" fill="{NAVY}" font-weight="600">{label}</text>'
    o = ""
    o += room(15, 20, 190, 130, "Room") + room(15, 20, 55, 40, "K", "#E8EEF5")
    o += f'<text x="110" y="185" text-anchor="middle" font-size="20" font-weight="800" fill="{RED}">1R</text><text x="110" y="208" text-anchor="middle" font-size="13" fill="{GREY}">kitchen inside the room</text>'
    o += room(250, 20, 130, 130, "Room") + room(380, 20, 70, 130, "K", "#E8EEF5")
    o += f'<text x="350" y="185" text-anchor="middle" font-size="20" font-weight="800" fill="{RED}">1K</text><text x="350" y="208" text-anchor="middle" font-size="13" fill="{GREY}">separate kitchen</text>'
    o += room(490, 20, 110, 130, "Room") + room(600, 20, 95, 130, "DK", "#E8EEF5")
    o += f'<text x="595" y="185" text-anchor="middle" font-size="20" font-weight="800" fill="{RED}">1DK</text><text x="595" y="208" text-anchor="middle" font-size="13" fill="{GREY}">dining + kitchen</text>'
    o += room(15, 235, 100, 120, "Room") + room(115, 235, 190, 120, "LDK", "#E8EEF5")
    o += f'<text x="160" y="385" text-anchor="middle" font-size="20" font-weight="800" fill="{RED}">1LDK</text><text x="160" y="408" text-anchor="middle" font-size="13" fill="{GREY}">living + dining + kitchen</text>'
    o += room(350, 235, 80, 120, "Room") + room(430, 235, 80, 120, "Room") + room(510, 235, 185, 120, "LDK", "#E8EEF5")
    o += f'<text x="520" y="385" text-anchor="middle" font-size="20" font-weight="800" fill="{RED}">2LDK</text><text x="520" y="408" text-anchor="middle" font-size="13" fill="{GREY}">two rooms + LDK</text>'
    return fig("Floor plan codes", svg(710, 420, o), "R = room, K = kitchen, D = dining, L = living. A typical 1K is about 20-25 square meters.")


def doccards():
    cards = [("id", "Residence card", "front and back"), ("passport", "Passport", ""), ("coin", "Proof of income", "pay slips / offer letter"),
             ("form", "Application form", "ask the agency for help"), ("phone", "Emergency contact", "in Japan, if possible"), ("seal", "Seal or signature", "ask which is accepted")]
    o = ""
    for i, (ic, t, sub) in enumerate(cards):
        r, c = divmod(i, 3)
        x, y = 12 + c * 230, 10 + r * 150
        o += f'<rect x="{x}" y="{y}" width="214" height="136" rx="14" fill="{SAND}" stroke="#ddd" stroke-width="2"/>'
        o += f'<g transform="translate({x+77} {y+14}) scale(1.0)"><svg x="0" y="0" width="60" height="60" viewBox="0 0 60 60">{icon_inner(ic)}</svg></g>'
        o += f'<text x="{x+107}" y="{y+96}" text-anchor="middle" font-size="16" font-weight="800" fill="{NAVY}">{t}</text>'
        o += f'<text x="{x+107}" y="{y+118}" text-anchor="middle" font-size="12.5" fill="{GREY}">{sub}</text>'
    return fig("Typical documents", svg(700, 310, o))


def icon_inner(kind):
    s = icon(kind)
    return s[s.index(">") + 1:s.rindex("</svg>")]


def maisoku():
    o = f'<rect x="10" y="10" width="440" height="330" rx="10" fill="#fff" stroke="{NAVY}" stroke-width="3"/>'
    o += f'<rect x="10" y="10" width="440" height="40" rx="10" fill="{NAVY}"/><text x="30" y="37" font-size="18" fill="#fff" font-weight="700">Sample Mansion Shinjuku 305</text>'
    rows = [("Rent", "¥80,000"), ("Mgmt fee", "¥5,000 / month"), ("Deposit / Key money", "1 month / 1 month"),
            ("Layout / Size", "1K / 22.5 ㎡"), ("Station", "Walk 8 min"), ("Built / Structure", "2008 / RC"),
            ("Facing", "South"), ("Contract", "Standard, 2 years"), ("Conditions", "Foreigners OK")]
    for i, (a, b) in enumerate(rows):
        y = 62 + i * 30
        o += f'<line x1="22" y1="{y+22}" x2="438" y2="{y+22}" stroke="#ddd"/>'
        o += f'<text x="62" y="{y+16}" font-size="14" fill="{GREY}">{a}</text><text x="230" y="{y+16}" font-size="15" fill="#222" font-weight="600">{b}</text>'
        o += f'<circle cx="38" cy="{y+10}" r="11" fill="{RED}"/><text x="38" y="{y+15}" text-anchor="middle" font-size="13" fill="#fff" font-weight="700">{i+1}</text>'
    notes = ["Compare rent + mgmt fee together", "Check what the monthly fee covers", "Key money is not returned",
             "Check ㎡ rather than tatami count", "80 m = 1 min; hills and lights not counted",
             "After 1981 = newer earthquake rules", "South-facing = more sun", "Standard or fixed-term?", "Look for 'foreigners OK'"]
    for i, n in enumerate(notes):
        y = 62 + i * 30
        o += f'<line x1="452" y1="{y+10}" x2="466" y2="{y+10}" stroke="{RED}" stroke-width="2"/>'
        o += f'<text x="474" y="{y+16}" font-size="13.5" fill="#333"><tspan fill="{RED}" font-weight="800">{i+1}</tspan>  {n}</text>'
    return fig("How to read a listing sheet", svg(780, 350, o), "A made-up example. Real sheets are in Japanese; the item order differs by agency.")


def timeline():
    cols = [("Before move-in", ["Pay initial costs", "Book gas opening", "Apply: electricity, water", "Order internet"], NAVY),
            ("Move-in day", ["Receive keys", "Photograph damage", "Check appliances", "Start gas"], RED),
            ("Within 14 days", ["Address registration", "Update insurance & bank", "Mail forwarding", "Learn garbage rules"], TEAL)]
    o = ""
    for i, (t, items, c) in enumerate(cols):
        x = 12 + i * 232
        o += f'<rect x="{x}" y="10" width="216" height="50" rx="12" fill="{c}"/><text x="{x+108}" y="42" text-anchor="middle" font-size="18" fill="#fff" font-weight="800">{t}</text>'
        for j, it in enumerate(items):
            y = 76 + j * 40
            o += f'<rect x="{x}" y="{y}" width="216" height="32" rx="8" fill="{SAND}"/><rect x="{x+10}" y="{y+8}" width="16" height="16" rx="3" fill="none" stroke="{c}" stroke-width="3"/><text x="{x+36}" y="{y+22}" font-size="14.5" fill="#222">{it}</text>'
    return fig("Move-in timeline", svg(700, 245, o))


def lease_timeline():
    pts = [("Lease starts", "keys & first rent"), ("2-4 months\nbefore end", "renewal papers arrive"), ("1 month before\nleaving", "written notice (check contract)"),
           ("Move-out day", "inspection with the agent"), ("After move-out", "itemized bill, deposit settled")]
    o = f'<line x1="40" y1="90" x2="660" y2="90" stroke="{NAVY}" stroke-width="6"/>'
    for i, (t, sub) in enumerate(pts):
        x = 40 + i * 155
        col = RED if i == 2 else NAVY
        o += f'<circle cx="{x}" cy="90" r="16" fill="{col}"/><text x="{x}" y="96" text-anchor="middle" font-size="15" fill="#fff" font-weight="800">{i+1}</text>'
        for j, ln in enumerate(t.split("\n")):
            o += f'<text x="{x}" y="{50+j*0 - (len(t.split(chr(10)))-1)*17 + j*17}" text-anchor="middle" font-size="14" font-weight="800" fill="{col}">{ln}</text>'
        words = sub.split(" ")
        lines, cur = [], ""
        for w in words:
            if len(cur + " " + w) > 18 and cur:
                lines.append(cur); cur = w
            else:
                cur = (cur + " " + w).strip()
        lines.append(cur)
        for j, ln in enumerate(lines):
            o += f'<text x="{x}" y="{128+j*17}" text-anchor="middle" font-size="12.5" fill="{GREY}">{ln}</text>'
    return fig("From lease start to deposit return", svg(700, 190, o))


# ---------------- furnished top-down floor plans ----------------
WOOD, TILE, WET, BAL = "#F6EAD2", "#E3E8F0", "#DCEBF5", "#E6F0DF"


def _t(x, y, s, size=12, fill=NAVY, w=700, anchor="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


def f_bed(x, y, w=80, h=130, c=SKY):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{c}" stroke="{NAVY}" stroke-width="2"/>'
            f'<rect x="{x+8}" y="{y+8}" width="{w-16}" height="22" rx="6" fill="#fff" stroke="{NAVY}" stroke-width="1.5"/>'
            f'<path d="M{x} {y+h*0.42} h{w}" stroke="{NAVY}" stroke-width="1.5" opacity=".5"/>')


def f_sofa(x, y, w=110, h=44):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{TEAL}" stroke="{NAVY}" stroke-width="2"/>'
            f'<rect x="{x+5}" y="{y+5}" width="{w-10}" height="{h*0.42}" rx="6" fill="#fff" opacity=".35"/>')


def f_table(x, y, w=60, h=40, c="#D9A55B"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{c}" stroke="#8a5d1c" stroke-width="2"/>'


def f_desk(x, y, w=80, h=34):
    return (f_table(x, y, w, h, "#E3B26A") + f'<circle cx="{x+w/2}" cy="{y+h+14}" r="11" fill="{RED}" stroke="{NAVY}" stroke-width="2"/>'
            f'<rect x="{x+w/2-16}" y="{y+6}" width="32" height="12" rx="2" fill="{INK}"/>')


def f_closet(x, y, w=110, h=36):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#E8EEF5" stroke="{NAVY}" stroke-width="2"/>'
            f'<line x1="{x+w/2}" y1="{y}" x2="{x+w/2}" y2="{y+h}" stroke="{NAVY}" stroke-width="1.5"/>'
            + _t(x + w / 2, y + h / 2 + 4, "closet 押入", 10, GREY, 600))


def f_tv(x, y, w=56):
    return f'<rect x="{x}" y="{y}" width="{w}" height="9" rx="2" fill="{INK}"/><rect x="{x+w/2-14}" y="{y+9}" width="28" height="4" fill="{GREY}"/>'


def f_counter(x, y, w=150, h=34):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#fff" stroke="{NAVY}" stroke-width="2"/>'
            f'<rect x="{x+8}" y="{y+6}" width="34" height="22" rx="5" fill="{SKY}" stroke="{NAVY}" stroke-width="1.5"/>'
            f'<circle cx="{x+w-54}" cy="{y+h/2}" r="8" fill="none" stroke="{NAVY}" stroke-width="2"/><circle cx="{x+w-26}" cy="{y+h/2}" r="8" fill="none" stroke="{NAVY}" stroke-width="2"/>')


def f_fridge(x, y, w=36, h=40):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="#fff" stroke="{NAVY}" stroke-width="2"/><line x1="{x}" y1="{y+h*0.4}" x2="{x+w}" y2="{y+h*0.4}" stroke="{NAVY}" stroke-width="1.5"/>'


def f_tub(x, y, w=80, h=46):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#fff" stroke="{NAVY}" stroke-width="2"/>'
            f'<rect x="{x+7}" y="{y+7}" width="{w-14}" height="{h-14}" rx="8" fill="{SKY}"/>')


def f_toilet(x, y):
    return f'<rect x="{x}" y="{y}" width="26" height="12" rx="3" fill="#fff" stroke="{NAVY}" stroke-width="2"/><ellipse cx="{x+13}" cy="{y+28}" rx="12" ry="15" fill="#fff" stroke="{NAVY}" stroke-width="2"/>'


def f_washer(x, y, s=34):
    return f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="4" fill="#fff" stroke="{NAVY}" stroke-width="2"/><circle cx="{x+s/2}" cy="{y+s/2+2}" r="{s*0.28}" fill="{SKY}" stroke="{NAVY}" stroke-width="2"/>'


def f_door(x, y, r=28, rot=0):
    return (f'<g transform="rotate({rot} {x} {y})"><line x1="{x}" y1="{y}" x2="{x+r}" y2="{y}" stroke="{RED}" stroke-width="3"/>'
            f'<path d="M{x+r} {y} A {r} {r} 0 0 1 {x} {y+r}" fill="none" stroke="{RED}" stroke-width="1.5" stroke-dasharray="3 3"/></g>')


def f_walls(*rects):
    return "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{NAVY}" stroke-width="6"/>' for x, y, w, h in rects)


def f_floor(x, y, w, h, c):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}"/>'


def badge(x, y, n):
    return f'<circle cx="{x}" cy="{y}" r="12" fill="{RED}" stroke="#fff" stroke-width="2"/><text x="{x}" y="{y+5}" text-anchor="middle" font-size="14" font-weight="800" fill="#fff">{n}</text>'


def plan_1k():
    o = ""
    # floors
    o += f_floor(20, 20, 270, 230, WOOD) + f_floor(290, 20, 210, 110, TILE) + f_floor(290, 130, 110, 120, TILE)
    o += f_floor(290, 205, 110, 45, "#C9D2E0") + f_floor(400, 130, 100, 120, WET) + f_floor(20, 250, 270, 56, BAL)
    # walls
    o += f_walls((20, 20, 270, 230), (290, 20, 210, 110), (290, 130, 110, 120), (400, 130, 100, 120))
    o += f'<rect x="20" y="250" width="270" height="56" fill="none" stroke="{TEAL}" stroke-width="3" stroke-dasharray="8 5"/>'
    # balcony glass door in wall
    o += f'<line x1="70" y1="250" x2="240" y2="250" stroke="#fff" stroke-width="9"/><line x1="70" y1="250" x2="240" y2="250" stroke="{SKY}" stroke-width="3"/>'
    # room furniture
    o += f_bed(32, 32, 88, 140) + f_closet(32, 204, 120, 36) + f_table(168, 118, 78, 52) + f_tv(190, 232, 56) + f_desk(180, 32, 90, 34)
    o += _t(215, 150, "table", 11, "#5a3b0e", 600)
    # kitchen
    o += f_counter(300, 28, 150, 34) + f_fridge(458, 26, 34, 40) + _t(395, 98, "KITCHEN", 12, NAVY, 800) + _t(395, 113, "キッチン", 11, GREY, 600)
    # hall + washer + shoes
    o += f_washer(296, 136, 34) + _t(366, 160, "洗濯機", 10, GREY, 600) + f'<rect x="296" y="222" width="50" height="20" rx="3" fill="#fff" stroke="{NAVY}" stroke-width="1.5"/>' + _t(321, 236, "shoes", 9, GREY, 600)
    o += _t(345, 200, "ENTRANCE", 11, NAVY, 800)
    # bath
    o += f_tub(408, 138, 84, 46) + f_toilet(442, 196) + _t(450, 244, "UNIT BATH", 11, NAVY, 800)
    # doors
    o += f_door(290, 78, 30, 90) + f_door(330, 250, 36, 0) + f_door(400, 150, 26, 90)
    o += f'<rect x="318" y="248" width="48" height="6" fill="#fff"/>'
    # labels
    o += _t(150, 196, "", 1) + _t(110, 275, "BALCONY  ベランダ", 12, TEAL, 800)
    o += _t(85, 193, "", 1)
    for n, (x, y) in enumerate([(52, 50), (320, 46), (468, 154), (366, 218), (255, 275), (140, 222)], 1):
        o += badge(x + (-6 if n == 1 else 0), y, n)
    # legend
    leg = ["Room (洋室) about 6 jo / 10 ㎡", "Kitchen (キッチン) 1 burner or 2", "Unit bath (UB) bath + toilet", "Entrance (玄関) take shoes off", "Balcony (ベランダ) dry laundry", "Closet (クローゼット) storage"]
    o += f'<rect x="525" y="20" width="262" height="270" rx="12" fill="{SAND}" stroke="#ddd"/>' + _t(545, 46, "WHAT YOU GET IN A 1K", 14, NAVY, 800, "start")
    for i, t in enumerate(leg, 1):
        y = 78 + (i - 1) * 36
        o += badge(548, y - 4, i) + _t(568, y, t, 12, "#222", 600, "start")
    o += _t(656, 276, "Total about 20-25 ㎡", 12, RED, 800)
    return fig("A 1K, drawn from above", svg(800, 320, o), "Typical layout. Real rooms differ, but the pieces are the same: one room, a separate kitchen, a unit bath, an entrance and usually a balcony.")


def _mini(label, sub, w, h, content):
    return (f'<g><rect x="0" y="0" width="{w}" height="{h}" rx="6" fill="{SAND}" stroke="#ddd"/>{content}</g>')


def plans_small():
    def one(ox, oy, title, sub, inner, w=340, h=210):
        return (f'<g transform="translate({ox} {oy})">' + inner + _t(w / 2, h + 24, title, 18, RED, 800) + _t(w / 2, h + 42, sub, 12, GREY, 600) + "</g>")

    # 1R
    r1 = f_floor(10, 10, 320, 190, WOOD) + f_walls((10, 10, 320, 190)) + f_floor(10, 10, 90, 44, TILE)
    r1 += f_counter(14, 14, 80, 28) + f_bed(220, 24, 84, 130) + f_sofa(120, 150, 90, 38) + f_table(130, 80, 64, 40) + f_tv(140, 188, 50)
    r1 += _t(150, 66, "", 1) + _t(55, 66, "K", 11, GREY, 800) + f_door(14, 200, 26, 0)
    # 1DK
    r2 = f_floor(10, 10, 190, 190, WOOD) + f_floor(200, 10, 130, 190, TILE) + f_walls((10, 10, 190, 190), (200, 10, 130, 190))
    r2 += f_bed(22, 22, 84, 130) + f_closet(22, 160, 100, 32) + f_desk(130, 24, 60, 30)
    r2 += f_counter(206, 14, 118, 30) + f_fridge(290, 50, 34, 38) + f_table(226, 100, 64, 52, "#D9A55B") + _t(258, 130, "dining", 10, "#5a3b0e", 600) + f_door(200, 160, 24, 90)
    # 1LDK
    r3 = f_floor(10, 10, 130, 190, WOOD) + f_floor(140, 10, 190, 190, WOOD) + f_floor(140, 10, 190, 60, TILE) + f_walls((10, 10, 130, 190), (140, 10, 190, 190))
    r3 += f_bed(20, 22, 84, 130) + f_closet(20, 162, 110, 30)
    r3 += f_counter(150, 14, 120, 30) + f_fridge(280, 12, 38, 42) + f_table(190, 84, 76, 42) + f_sofa(160, 150, 120, 40) + f_tv(190, 190, 60) + f_door(140, 150, 24, 90)
    # 2LDK
    r4 = (f_floor(10, 10, 100, 190, WOOD) + f_floor(110, 10, 100, 190, WOOD) + f_floor(210, 10, 120, 190, WOOD) + f_floor(210, 10, 120, 52, TILE)
          + f_walls((10, 10, 100, 190), (110, 10, 100, 190), (210, 10, 120, 190)))
    r4 += f_bed(20, 24, 76, 120) + f_desk(122, 24, 70, 30) + f_closet(118, 150, 84, 30) + f_counter(214, 14, 82, 30) + f_fridge(298, 12, 28, 38)
    r4 += f_table(226, 76, 60, 38) + f_sofa(222, 140, 96, 36) + f_door(110, 150, 24, 90) + f_door(210, 130, 24, 90)
    inner = (one(10, 5, "1R", "kitchen inside the room", r1) + one(370, 5, "1DK", "dining-kitchen + 1 room", r2)
             + one(10, 285, "1LDK", "living-dining-kitchen + 1 room", r3) + one(370, 285, "2LDK", "living-dining-kitchen + 2 rooms", r4))
    return fig("Other common layouts", svg(730, 560, inner), "R = room, K = kitchen, D = dining, L = living. Red arcs show door swings.")


# ---------------- isometric 1K ----------------
import math

_S, _OX, _OY = 0.9, 262, 112


def P(x, y, z=0):
    return (_OX + (x - y) * 0.866 * _S, _OY + (x + y) * 0.5 * _S - z * _S)


def _adj(hexc, f):
    h = hexc.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return "#%02x%02x%02x" % (min(255, int(r * f)), min(255, int(g * f)), min(255, int(b * f)))


def poly(pts, fill, stroke="none", sw=1, op=1):
    p = " ".join(f"{a:.1f},{b:.1f}" for a, b in pts)
    return f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" opacity="{op}"/>'


def ibox(x, y, z, w, d, h, c, edge=None):
    e = edge or _adj(c, 0.62)
    top = poly([P(x, y, z + h), P(x + w, y, z + h), P(x + w, y + d, z + h), P(x, y + d, z + h)], _adj(c, 1.06), e, .6)
    lf = poly([P(x, y + d, z), P(x + w, y + d, z), P(x + w, y + d, z + h), P(x, y + d, z + h)], _adj(c, 0.9), e, .6)
    rf = poly([P(x + w, y, z), P(x + w, y + d, z), P(x + w, y + d, z + h), P(x + w, y, z + h)], _adj(c, 0.74), e, .6)
    return lf + rf + top


def iflat(x, y, w, d, fill, z=0, stroke="none", sw=1):
    return poly([P(x, y, z), P(x + w, y, z), P(x + w, y + d, z), P(x, y + d, z)], fill, stroke, sw)


def iellipse(cx, cy, z, r, fill):
    pts = [P(cx + r * math.cos(a / 12 * math.tau), cy + r * math.sin(a / 12 * math.tau), z) for a in range(12)]
    return poly(pts, fill, _adj(fill, .6), .6)


def plan_1k_iso():
    o = ""
    # floors
    o += iflat(0, 240, 280, 60, "#D5DDCB") + iflat(0, 0, 280, 240, "#D8B98A")
    o += iflat(280, 0, 180, 110, "#E6E8EC") + iflat(280, 110, 100, 130, "#E6E8EC") + iflat(280, 190, 100, 50, "#BCC4D0") + iflat(380, 110, 80, 130, "#CFE2F2")
    for r in [(0, 0, 280, 240), (280, 0, 180, 110), (280, 110, 100, 130), (380, 110, 80, 130)]:
        o += poly([P(r[0], r[1]), P(r[0] + r[2], r[1]), P(r[0] + r[2], r[1] + r[3]), P(r[0], r[1] + r[3])], "none", "#12233B", 3)
    # back walls (cutaway)
    WC = "#EFEAE0"
    o += ibox(0, 0, 0, 6, 240, 96, WC, "#bdb6a6") + ibox(0, 0, 0, 460, 6, 96, WC, "#bdb6a6")
    o += poly([P(150, 6, 36), P(238, 6, 36), P(238, 6, 82), P(150, 6, 82)], "#CFE3F5", "#12233B", 1.5) + poly([P(194, 6, 36), P(194, 6, 82)], "none", "#12233B", 1.5)
    items = []

    def add(x, y, z, w, d, h, c, key=None):
        items.append((key if key is not None else (x + w) + (y + d) + z * 0.01, ibox(x, y, z, w, d, h, c)))

    # bedroom
    add(10, 6, 0, 100, 40, 92, "#D8C3A0")                      # closet
    add(10, 60, 0, 98, 180, 22, "#C9A877", 348); add(12, 62, 22, 94, 176, 12, "#F4F4F6", 348.1)
    add(12, 104, 34, 94, 134, 5, "#6F8FB8", 348.2); add(20, 66, 34, 78, 26, 8, "#FFFFFF", 348.3)
    add(140, 8, 66, 110, 50, 5, "#E9D3AE")                      # desk
    for lx, ly in [(142, 10), (243, 10), (142, 52), (243, 52)]:
        add(lx, ly, 0, 5, 5, 66, "#8a6b43")
    add(176, 14, 71, 40, 6, 28, "#2A2F3A", 309)
    add(186, 74, 26, 36, 36, 6, "#B9473E"); add(186, 74, 32, 36, 5, 34, "#B9473E"); add(200, 88, 0, 6, 6, 26, "#555B66")
    items.append((200, iflat(120, 112, 160, 110, "#C9574B", 1.2)))
    add(158, 140, 1.5, 84, 56, 26, "#A8845A")
    # kitchen
    add(292, 8, 0, 125, 52, 38, "#F2F2F2"); add(292, 8, 38, 125, 52, 3, "#B8BEC8")
    items.append((477.5, iflat(300, 18, 40, 32, "#7E8FA3", 41.2)))
    items.append((478, iellipse(366, 34, 41.4, 9, "#2E333D") + iellipse(392, 34, 41.4, 9, "#2E333D")))
    add(421, 8, 0, 38, 46, 106, "#E9ECF0")
    add(292, 122, 0, 40, 40, 48, "#FFFFFF"); items.append((495, iellipse(312, 142, 48.4, 12, "#9EB4CE")))
    add(342, 205, 0, 34, 28, 26, "#B89A74")
    # bath
    add(386, 116, 0, 68, 96, 34, "#FFFFFF"); items.append((386 + 68 + 116 + 96 + 0.5, iflat(392, 122, 56, 84, "#9EC4E6", 34.4)))
    add(414, 226, 0, 28, 10, 40, "#FFFFFF"); add(418, 214, 0, 20, 14, 22, "#FFFFFF")
    for _, s in sorted(items, key=lambda t: t[0]):
        o += s
    # balcony glass
    o += poly([P(0, 300, 0), P(280, 300, 0), P(280, 300, 42), P(0, 300, 42)], "#A9C7E6", "#5D7FA6", 1.5, .45)
    o += poly([P(0, 240, 0), P(0, 300, 0), P(0, 300, 42), P(0, 240, 42)], "#A9C7E6", "#5D7FA6", 1.5, .45)

    def badge2(p, n):
        x, y = p
        return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="13" fill="{RED}" stroke="#fff" stroke-width="2.5"/><text x="{x:.1f}" y="{y+5:.1f}" text-anchor="middle" font-size="14" font-weight="800" fill="#fff">{n}</text>'
    for n, pt in enumerate([P(60, 150, 70), P(355, 32, 62), P(420, 160, 66), P(330, 214, 54), P(140, 272, 56), P(60, 26, 106)], 1):
        o += badge2(pt, n)
    leg = [("Room 洋室", "about 6 jo, 10 ㎡"), ("Kitchen キッチン", "one or two burners"), ("Unit bath ユニットバス", "bath and toilet in one"),
           ("Entrance 玄関", "shoes come off here"), ("Balcony ベランダ", "for drying laundry"), ("Closet クローゼット", "your storage")]
    for i, (a, b) in enumerate(leg):
        r, c = divmod(i, 3)
        x, y = 28 + c * 218, 462 + r * 44
        o += badge2((x, y), i + 1) + _t(x + 22, y - 2, a, 13, "#12233B", 800, "start") + _t(x + 22, y + 15, b, 11.5, GREY, 500, "start")
    o += _t(640, 262, "≈ 20-25 ㎡", 15, RED, 800, "end")
    return fig("A typical 1K", svg(680, 540, o), "Cutaway view. Layouts vary, but a 1K is always: one room, a separate kitchen, a unit bath, an entrance, and usually a balcony.")


import iso as _iso


def _minis():
    return fig('Other common layouts', _iso.mini_grid(), 'R = room, K = kitchen, D = dining, L = living.')


FIGS = {0: flow(), 1: plan_1k_iso() + whois() + _minis(), 2: costs(), 3: doccards(), 4: maisoku(), 7: timeline(), 8: lease_timeline()}
