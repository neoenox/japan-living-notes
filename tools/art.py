"""Illustrations and figures for the guide (inline SVG)."""
NAVY, RED, SAND, GOLD, TEAL, SKY, INK, GREY = "#1F3A5F", "#C8372D", "#F4F1EA", "#E8B04A", "#2E8B8B", "#BFD4EA", "#222", "#666"
FONT = "font-family=\"'Inter','Noto Sans JP','Yu Gothic',sans-serif\""


def svg(w, h, inner, cls=""):
    return f'<svg class="{cls}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" {FONT}>{inner}</svg>'


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


def icon_inner(kind):
    s = icon(kind)
    return s[s.index(">") + 1:s.rindex("</svg>")]


def _t(x, y, s, size=12, fill=NAVY, w=700, anchor="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}">{s}</text>'


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


