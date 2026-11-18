"""Isometric illustration engine + chapter dioramas + furnished mini rooms."""
import math

FONT = "font-family=\"'Inter','Noto Sans JP','Yu Gothic',sans-serif\""
WHITE, CREAM, WOOD, RED, BLUE, DARK, GREEN, GOLD, KRAFT, GREY = (
    "#F3F5F9", "#EFE6D2", "#C99A5B", "#D2452F", "#6F9BD1", "#232C3A", "#6FAE82", "#E3B866", "#C9A06A", "#9AA5B5")


def adj(hexc, f):
    h = hexc.lstrip("#")
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return "#%02x%02x%02x" % (max(0, min(255, int(r * f))), max(0, min(255, int(g * f))), max(0, min(255, int(b * f))))


class Iso:
    def __init__(self, S, ox, oy):
        self.S, self.ox, self.oy = S, ox, oy
        self.items = []

    def P(self, x, y, z=0):
        return (self.ox + (x - y) * 0.866 * self.S, self.oy + (x + y) * 0.5 * self.S - z * self.S)

    def poly(self, pts, fill, stroke="none", sw=.7, op=1):
        p = " ".join(f"{a:.1f},{b:.1f}" for a, b in pts)
        return f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" opacity="{op}"/>'

    def box(self, x, y, z, w, d, h, c, edge=None):
        e = edge or adj(c, .6)
        P = self.P
        top = self.poly([P(x, y, z + h), P(x + w, y, z + h), P(x + w, y + d, z + h), P(x, y + d, z + h)], adj(c, 1.07), e)
        lf = self.poly([P(x, y + d, z), P(x + w, y + d, z), P(x + w, y + d, z + h), P(x, y + d, z + h)], adj(c, .9), e)
        rf = self.poly([P(x + w, y, z), P(x + w, y + d, z), P(x + w, y + d, z + h), P(x + w, y, z + h)], adj(c, .72), e)
        return lf + rf + top

    def flat(self, x, y, w, d, fill, z=0, stroke="none"):
        P = self.P
        return self.poly([P(x, y, z), P(x + w, y, z), P(x + w, y + d, z), P(x, y + d, z)], fill, stroke)

    def wl(self, y, x0, x1, z0, z1, fill, stroke="none", sw=.7):  # plane y=const (left-front face)
        P = self.P
        return self.poly([P(x0, y, z0), P(x1, y, z0), P(x1, y, z1), P(x0, y, z1)], fill, stroke, sw)

    def wr(self, x, y0, y1, z0, z1, fill, stroke="none", sw=.7):  # plane x=const (right-front face)
        P = self.P
        return self.poly([P(x, y0, z0), P(x, y1, z0), P(x, y1, z1), P(x, y0, z1)], fill, stroke, sw)

    def ell(self, cx, cy, z, r, fill, n=18, stroke=None):
        pts = [self.P(cx + r * math.cos(a / n * math.tau), cy + r * math.sin(a / n * math.tau), z) for a in range(n)]
        return self.poly(pts, fill, stroke or adj(fill, .6))

    def cyl(self, cx, cy, z, r, h, c, n=20):
        s = ""
        quads = []
        for a in range(n):
            a0, a1 = a / n * math.tau, (a + 1) / n * math.tau
            am = (a0 + a1) / 2
            if math.cos(am) + math.sin(am) > -0.05:
                k = 0.62 + 0.38 * (0.5 + 0.5 * math.cos(am - math.pi / 4 - 0.9))
                quads.append((math.cos(am) + math.sin(am), self.poly(
                    [self.P(cx + r * math.cos(a0), cy + r * math.sin(a0), z), self.P(cx + r * math.cos(a1), cy + r * math.sin(a1), z),
                     self.P(cx + r * math.cos(a1), cy + r * math.sin(a1), z + h), self.P(cx + r * math.cos(a0), cy + r * math.sin(a0), z + h)],
                    adj(c, k), adj(c, k), .4)))
        for _, q in sorted(quads):
            s += q
        return s + self.ell(cx, cy, z + h, r, adj(c, 1.08), n)

    def sphere(self, cx, cy, z, r, c):
        x, y = self.P(cx, cy, z)
        rr = r * self.S
        return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rr:.1f}" fill="{c}"/>'
                f'<circle cx="{x-rr*.3:.1f}" cy="{y-rr*.3:.1f}" r="{rr*.55:.1f}" fill="{adj(c, 1.18)}" opacity=".8"/>'
                f'<path d="M{x-rr:.1f} {y:.1f} A{rr:.1f} {rr:.1f} 0 0 0 {x+rr:.1f} {y:.1f}" fill="{adj(c, .78)}" opacity=".45"/>')

    def text_left(self, x, y, z, s, size, fill, w=800, anchor="start"):
        e, f = self.P(x, y, z)
        S = self.S
        return (f'<text transform="matrix({0.866*S:.3f} {0.5*S:.3f} 0 {S:.3f} {e:.1f} {f:.1f})" x="0" y="0" font-size="{size}" '
                f'font-weight="{w}" fill="{fill}" text-anchor="{anchor}">{s}</text>')

    def text_floor(self, x, y, z, s, size, fill, w=800, anchor="middle"):
        e, f = self.P(x, y, z)
        S = self.S
        return (f'<text transform="matrix({0.866*S:.3f} {0.5*S:.3f} {-0.866*S:.3f} {0.5*S:.3f} {e:.1f} {f:.1f})" x="0" y="0" '
                f'font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}">{s}</text>')

    def shadow(self, x, y, w, d, op=.18):
        return self.poly([self.P(x + 8, y + 8, .2), self.P(x + w + 14, y + 8, .2), self.P(x + w + 14, y + d + 14, .2), self.P(x + 8, y + d + 14, .2)], "#000", "none", 0, op)

    def add(self, key, svg):
        self.items.append((key, svg))

    def out(self):
        return "".join(s for _, s in sorted(self.items, key=lambda t: t[0]))


def svgwrap(w, h, inner, vb=None):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb or f"0 0 {w} {h}"}" width="100%" {FONT}>{inner}</svg>'


# --------------- shared objects ---------------
def building(I, bx, by, w, d, h, c, cols, rows, key_extra=0, wc="#CFE3F5"):
    I.add(bx + w + by + d + key_extra, I.shadow(bx, by, w, d) + I.box(bx, by, 0, w, d, h, c))
    s = ""
    mx, mz = w / (cols * 2 + 1), h / (rows * 2 + 1)
    for r in range(rows):
        for k in range(cols):
            s += I.wl(by + d, bx + mx * (2 * k + 1), bx + mx * (2 * k + 2), mz * (2 * r + 1), mz * (2 * r + 2), wc, adj(c, .55))
    my = d / (cols * 2 + 1)
    for r in range(rows):
        for k in range(max(1, int(cols * d / w))):
            s += I.wr(bx + w, by + my * (2 * k + 1), by + my * (2 * k + 2), mz * (2 * r + 1), mz * (2 * r + 2), adj(wc, .8), adj(c, .5))
    I.add(bx + w + by + d + key_extra + .01, s)


def house(I, x, y, w=80, d=60, wall=CREAM, roof=RED):
    h = 44
    I.add(x + w + y + d, I.shadow(x, y, w, d) + I.box(x, y, 0, w, d, h, wall))
    P = I.P
    r = I.poly([P(x - 6, y + d + 6, h), P(x + w + 6, y + d + 6, h), P(x + w + 6, y + d / 2, h + 26), P(x - 6, y + d / 2, h + 26)], adj(roof, .95), adj(roof, .6))
    g = I.poly([P(x + w + 6, y - 6, h), P(x + w + 6, y + d + 6, h), P(x + w + 6, y + d / 2, h + 26)], adj(roof, .72), adj(roof, .55))
    I.add(x + w + y + d + .2, r + g + I.wl(y + d, x + w * .55, x + w * .55 + 18, 0, 30, "#3B2E27") + I.wl(y + d, x + 10, x + 30, 14, 32, "#CFE3F5", "#555"))


def tree(I, x, y, s=1.0, c=GREEN):
    I.add(x + y + 2, I.shadow(x - 10, y - 10, 20, 20, .15) + I.cyl(x, y, 0, 4 * s, 22 * s, "#8a6a45") + I.sphere(x, y, 38 * s, 20 * s, c))


def platform(I, W=300, D=300, c="#A9C2E0"):
    I.add(-1000, I.box(0, 0, -14, W, D, 14, c, adj(c, .55)))


def sign(I, x, y, n, c=RED):
    s = I.cyl(x, y, 0, 2.2, 46, "#8892a3")
    px, py = I.P(x, y, 54)
    s += f'<circle cx="{px:.1f}" cy="{py:.1f}" r="15" fill="{c}" stroke="#fff" stroke-width="2.5"/><text x="{px:.1f}" y="{py+6:.1f}" text-anchor="middle" font-size="17" font-weight="800" fill="#fff">{n}</text>'
    I.add(x + y + 5, s)


# --------------- chapter dioramas ---------------
def scene(n):
    I = Iso(0.92, 320, 112)
    platform(I)
    if n == 0:   # road to a new home
        I.add(-900, I.flat(0, 205, 300, 46, "#46505F") + I.flat(246, 60, 46, 191, "#46505F"))
        for k in range(10):
            I.add(-899, I.flat(8 + k * 30, 226, 16, 4, "#E8EAF0"))
        for k in range(5):
            I.add(-899, I.flat(266, 80 + k * 32, 4, 16, "#E8EAF0"))
        house(I, 186, 14, 90, 56)
        tree(I, 40, 60); tree(I, 110, 40, .9); tree(I, 40, 140, 1.1); tree(I, 160, 150, .8, "#5f9f77")
        for i, (x, y) in enumerate([(60, 192), (130, 192), (200, 192)], 1):
            sign(I, x, y, i)
    elif n == 1:  # building types
        building(I, 30, 30, 90, 80, 150, "#D9DEE8", 4, 7)
        building(I, 150, 40, 100, 70, 78, "#E7DAC2", 4, 3)
        house(I, 40, 170, 90, 60)
        building(I, 170, 170, 80, 60, 40, "#B9D3C0", 3, 2)
        tree(I, 20, 150, .8); tree(I, 275, 150, .9); tree(I, 140, 270, .8)
    elif n == 2:  # coins & calculator
        for (x, y, cnt) in [(60, 70, 6), (110, 120, 9), (60, 160, 4), (150, 60, 3)]:
            s = I.shadow(x - 24, y - 24, 48, 48, .18)
            for k in range(cnt):
                s += I.cyl(x, y, k * 8, 24, 7, GOLD)
            I.add(x + y + 30, s + I.ell(x, y, cnt * 8 + .5, 13, "#CE9A3C") + I.text_floor(x, y + 6, cnt * 8 + .6, "¥", 22, "#7a5410"))
        I.add(400, I.shadow(190, 100, 90, 130) + I.box(190, 100, 0, 90, 130, 14, "#2C3647"))
        s = I.box(200, 110, 14, 70, 28, 2, "#B9D4C8")
        for r in range(4):
            for c in range(3):
                s += I.box(202 + c * 22, 148 + r * 18, 14, 16, 12, 3, RED if (r, c) == (3, 2) else "#EDEFF4")
        I.add(401, s + I.text_floor(240, 132, 16.5, "¥ 410,500", 11, "#14353a", 800))
        I.add(250, I.box(130, 200, 0, 40, 60, 1.5, "#FFFFFF") + I.text_floor(150, 215, 2, "RECEIPT", 6, GREY, 700))
    elif n == 3:  # ID card + passport + seal
        I.add(200, I.shadow(30, 50, 130, 85) + I.box(30, 50, 0, 130, 85, 5, "#FFFFFF"))
        s = I.box(40, 60, 5, 36, 48, 1.5, "#A7C4E6") + I.cyl(58, 76, 6.5, 8, 4, "#6F7F96") + I.box(86, 62, 5, 64, 6, 1, "#9DB6D4")
        s += I.box(86, 76, 5, 56, 6, 1, "#C3D0E2") + I.box(86, 90, 5, 40, 6, 1, "#C3D0E2") + I.box(40, 118, 5, 110, 8, 1, "#4F86B8")
        I.add(201, s)
        I.add(300, I.shadow(180, 120, 80, 110) + I.box(180, 120, 0, 80, 110, 10, "#B8392B") + I.ell(220, 175, 10.5, 24, "none", stroke="#E3B866") + I.text_floor(220, 181, 11, "PASSPORT", 8, "#E3B866", 800))
        I.add(250, I.cyl(88, 190, 0, 22, 4, "#8E2B22") + I.ell(88, 190, 4.4, 17, "#D2452F") + I.text_floor(88, 197, 4.8, "印", 18, "#fff"))
        I.add(251, I.cyl(88, 190, 4, 7, 40, "#3a3f4b") + I.cyl(88, 190, 44, 11, 7, "#232C3A"))
        I.add(255, I.box(30, 240, 0, 110, 5, 5, GOLD))
    elif n == 4:  # map + pin + magnifier
        I.add(-800, I.flat(20, 20, 260, 260, "#E6EFE0"))
        for k in (90, 190):
            I.add(-799, I.flat(20, k, 260, 28, "#FFFFFF") + I.flat(k, 20, 28, 260, "#FFFFFF"))
        I.add(-798, I.flat(20, 130, 260, 10, "#F1D58A"))
        for (x, y, w, d, h, c) in [(40, 40, 40, 40, 20, "#B9D3C0"), (110, 40, 50, 36, 34, "#D9DEE8"), (210, 40, 50, 40, 14, "#E7DAC2"),
                                   (40, 150, 40, 34, 28, "#E7DAC2"), (210, 150, 50, 40, 44, "#D9DEE8"), (40, 230, 50, 36, 12, "#B9D3C0")]:
            I.add(x + w + y + d, I.box(x, y, 0, w, d, h, c))
        I.add(500, I.shadow(130, 120, 30, 30, .22) + I.cyl(144, 134, 0, 3, 44, "#6b7585") + I.sphere(144, 134, 62, 20, RED))
        hx, hy = I.P(144, 134, 62)
        I.add(501, f'<circle cx="{hx-4:.1f}" cy="{hy-2:.1f}" r="6" fill="#fff"/>')
        px, py = I.P(205, 195, 40)
        I.add(700, f'<circle cx="{px:.1f}" cy="{py:.1f}" r="46" fill="#CFE3F5" fill-opacity=".45" stroke="#232C3A" stroke-width="9"/>'
                   f'<line x1="{px+33:.1f}" y1="{py+33:.1f}" x2="{px+84:.1f}" y2="{py+84:.1f}" stroke="#232C3A" stroke-width="15" stroke-linecap="round"/>')
    elif n == 5:  # entrance + key
        I.add(-500, I.box(10, 10, 0, 280, 12, 118, "#EAE4D6", "#bdb6a6"))
        I.add(-499, I.wl(22, 110, 190, 0, 92, "#2C4F7D", "#17304f", 1.5) + I.wl(22.3, 118, 182, 8, 86, "#35609A") + I.wl(22.6, 172, 178, 42, 50, GOLD))
        I.add(-498, I.text_left(138, 22.6, 104, "内見", 14, "#232C3A") + I.wl(22.2, 30, 80, 50, 90, "#CFE3F5", "#8a8f98", 1.5))
        I.add(100, I.flat(110, 30, 80, 46, RED) + I.text_floor(150, 56, .3, "WELCOME", 9, "#fff", 700))
        for (x, y) in [(60, 60), (80, 78)]:
            I.add(x + y + 40, I.box(x, y, 0, 26, 12, 8, "#3A3F4B") + I.box(x + 14, y, 0, 12, 12, 14, "#3A3F4B"))
        I.add(800, I.shadow(130, 160, 120, 40, .2) + I.box(160, 176, 0, 90, 9, 6, GOLD) + I.box(222, 176, 6, 10, 9, 14, GOLD) + I.box(240, 176, 6, 8, 9, 10, GOLD) + I.cyl(140, 180, 0, 24, 6, GOLD) + I.ell(140, 180, 6.4, 10, "#A9C2E0"))
    elif n == 6:  # contract + seal
        for k in range(4):
            I.add(10 + k, I.box(50 - k * 2, 40 + k * 2, k * 3, 170, 220, 3, "#FFFFFF" if k % 2 == 0 else "#F1F3F8"))
        s = I.box(64, 54, 12, 142, 30, 1.2, "#2C4F7D") + I.text_floor(135, 74, 14, "LEASE AGREEMENT", 9, "#fff", 800)
        for k in range(8):
            s += I.box(64, 98 + k * 20, 12, 142 if k % 3 else 100, 6, 1, "#C3CBDA")
        I.add(60, s)
        I.add(500, I.shadow(150, 190, 50, 50, .2) + I.cyl(176, 214, 12, 20, 6, "#8E2B22") + I.ell(176, 214, 18.4, 15, RED) + I.text_floor(176, 220, 18.8, "印", 17, "#fff"))
        I.add(520, I.cyl(176, 214, 18, 7, 36, "#3a3f4b") + I.cyl(176, 214, 54, 10, 8, "#232C3A"))
        I.add(530, I.box(225, 80, 12, 8, 110, 8, GOLD) + I.box(225, 190, 12, 8, 18, 8, "#2a2f3a"))
    elif n == 7:  # moving boxes + sofa + plant
        def kbox(x, y, z, w, d, h):
            s = I.box(x, y, z, w, d, h, KRAFT) + I.box(x + w / 2 - 6, y, z + h, 12, d, .6, "#EFE6D2")
            return s
        I.add(150, I.shadow(30, 50, 100, 80) + kbox(30, 50, 0, 100, 80, 52))
        I.add(151, kbox(40, 60, 52, 70, 60, 40) + I.text_left(60, 120.1, 62, "BOOKS", 9, "#5a3f1d"))
        I.add(260, I.shadow(150, 130, 90, 80) + kbox(150, 130, 0, 70, 60, 44) + kbox(230, 140, 0, 50, 50, 36))
        I.add(340, I.shadow(30, 190, 110, 56) + I.box(30, 190, 0, 110, 56, 20, "#3E6FA3") + I.box(30, 190, 20, 110, 14, 30, "#34608F") + I.box(30, 190, 20, 14, 56, 14, "#34608F") + I.box(126, 190, 20, 14, 56, 14, "#34608F"))
        I.add(420, I.cyl(250, 230, 0, 14, 22, "#C98F5B") + I.sphere(250, 230, 42, 18, GREEN) + I.sphere(262, 236, 36, 13, "#5f9f77") + I.sphere(240, 238, 34, 12, GREEN))
        px, py = I.P(190, 112, 70)
        I.add(900, f'<rect x="{px-48:.1f}" y="{py-26:.1f}" width="96" height="40" rx="8" fill="{RED}" stroke="#fff" stroke-width="2.5"/><text x="{px:.1f}" y="{py+1:.1f}" text-anchor="middle" font-size="17" font-weight="800" fill="#fff">14 DAYS</text>')
    elif n == 8:  # calendar + envelope + keys
        I.add(100, I.shadow(30, 40, 200, 20) + I.box(30, 40, 0, 200, 14, 150, "#FFFFFF") + I.box(30, 40, 112, 200, 14, 38, RED))
        s = I.text_left(48, 54.2, 124, "MOVE-OUT", 14, "#fff")
        for r in range(4):
            for c in range(6):
                hot = (r, c) == (2, 3)
                s += I.wl(54.1, 40 + c * 30, 62 + c * 30, 14 + (3 - r) * 24, 32 + (3 - r) * 24, GOLD if hot else "#D9E3F1")
        s += I.text_left(129, 54.3, 40, "✓", 18, "#232C3A")
        I.add(110, s)
        I.add(300, I.shadow(70, 150, 130, 90, .2) + I.box(70, 150, 0, 130, 90, 3, "#FFFFFF") + I.poly([I.P(70, 150, 3.1), I.P(200, 150, 3.1), I.P(135, 195, 3.1)], "#E4E9F2", "#9aa5b5"))
        I.add(310, I.cyl(235, 215, 0, 12, 4, GOLD) + I.ell(235, 215, 4.4, 5, "#A9C2E0") + I.box(220, 200, 0, 10, 40, 4, GOLD))
    else:        # FAQ: question plaque + warning sign
        I.add(100, I.shadow(50, 60, 150, 20) + I.box(50, 60, 0, 150, 16, 150, "#1F3A5F"))
        I.add(101, I.text_left(125, 76.2, 38, "?", 150, "#fff", 800, "middle"))
        I.add(300, I.cyl(235, 170, 0, 3, 90, "#8892a3"))
        P = I.P
        I.add(301, I.poly([P(235 - 38, 171, 86), P(235 + 38, 171, 86), P(235, 171, 152)], GOLD, "#232C3A", 3) + I.text_left(235, 171.2, 98, "!", 40, "#232C3A", 800, "middle"))
        for (x, y) in [(60, 190), (110, 215)]:
            I.add(x + y, I.cyl(x, y, 0, 16, 4, "#3a3f4b") + I.cyl(x, y, 4, 9, 30, RED) + I.cyl(x, y, 20, 10, 5, "#fff"))
    return svgwrap(640, 400, I.out(), '70 0 500 400')


def cover_art():
    I = Iso(0.8, 640, 70)
    I.add(-1000, I.box(0, 0, -16, 460, 300, 16, "#A9C2E0", "#2b4a73"))
    I.add(-990, I.flat(0, 232, 460, 44, "#46505F"))
    for k in range(14):
        I.add(-989, I.flat(8 + k * 33, 252, 18, 4, "#E8EAF0"))
    building(I, 20, 20, 90, 80, 170, "#D9DEE8", 4, 8)
    building(I, 130, 30, 100, 70, 92, "#E7DAC2", 4, 4)
    building(I, 250, 20, 80, 80, 130, "#B9D3C0", 3, 6)
    house(I, 350, 30, 90, 60)
    house(I, 40, 140, 90, 60, "#E7DAC2", "#2C4F7D")
    building(I, 170, 140, 110, 66, 60, "#D9DEE8", 4, 3)
    tree(I, 320, 150, 1.0); tree(I, 370, 170, .9); tree(I, 150, 210, .8); tree(I, 430, 200, 1.0)
    return svgwrap(1280, 470, I.out(), '410 10 570 460')


# --------------- furnished mini rooms (other layouts) ---------------
def mini(kind):
    cfg = {"1R": (260, 200), "1DK": (270, 200), "1LDK": (300, 200), "2LDK": (360, 190)}
    W, D = cfg[kind]
    S = 0.52
    I = Iso(S, 0, 0)
    ox = 160 - (W - D) * 0.866 * S / 2
    I.ox, I.oy = ox, 62

    def bed(x, y):
        I.add(x + 90 + y + 160, I.box(x, y, 0, 80, 150, 16, "#C9A877") + I.box(x + 2, y + 2, 16, 76, 146, 9, WHITE) + I.box(x + 2, y + 50, 25, 76, 98, 4, "#6F8FB8") + I.box(x + 10, y + 6, 25, 60, 20, 6, "#fff"))

    def closet(x, y, w=80):
        I.add(x + w + y + 30, I.box(x, y, 0, w, 30, 80, "#D8C3A0"))

    def table(x, y, w=60, d=40):
        I.add(x + w + y + d, I.box(x, y, 24, w, d, 4, "#B58B55") + I.box(x + 3, y + 3, 0, 4, 4, 24, "#8a6b43") + I.box(x + w - 7, y + 3, 0, 4, 4, 24, "#8a6b43") + I.box(x + 3, y + d - 7, 0, 4, 4, 24, "#8a6b43") + I.box(x + w - 7, y + d - 7, 0, 4, 4, 24, "#8a6b43"))

    def sofa(x, y, w=100):
        I.add(x + w + y + 40 + 1, I.box(x, y, 0, w, 40, 16, "#3E6FA3") + I.box(x, y + 28, 16, w, 12, 20, "#34608F"))

    def counter(x, y, w=100):
        I.add(x + w + y + 30 + 100, I.box(x, y, 0, w, 30, 30, "#F2F2F2") + I.box(x, y, 30, w, 30, 3, "#B8BEC8") + I.cyl(x + w - 24, y + 15, 33, 7, .6, "#2E333D") + I.cyl(x + w - 44, y + 15, 33, 7, .6, "#2E333D") + I.box(x + 10, y + 5, 33, 26, 20, .6, "#7E8FA3"))

    def fridge(x, y):
        I.add(x + 32 + y + 34 + 100, I.box(x, y, 0, 32, 34, 86, "#E9ECF0"))

    def tv(x, y):
        I.add(x + 50 + y + 20, I.box(x, y, 0, 50, 20, 14, "#8a6b43") + I.box(x + 8, y + 6, 14, 34, 4, 24, "#232C3A"))

    def desk(x, y):
        I.add(x + 70 + y + 36, I.box(x, y, 28, 70, 36, 4, "#E9D3AE") + I.box(x + 3, y + 3, 0, 4, 4, 28, "#8a6b43") + I.box(x + 63, y + 3, 0, 4, 4, 28, "#8a6b43") + I.box(x + 20, y + 8, 32, 30, 4, 20, "#232C3A"))

    # floors + back walls
    floors = {"1R": [(0, 0, W, D, "#D8B98A")],
              "1DK": [(0, 0, 150, D, "#D8B98A"), (150, 0, 120, D, "#E6E8EC")],
              "1LDK": [(0, 0, 110, D, "#D8B98A"), (110, 0, 190, D, "#D8B98A")],
              "2LDK": [(0, 0, 100, D, "#D8B98A"), (100, 0, 90, D, "#D8B98A"), (190, 0, 170, D, "#D8B98A")]}[kind]
    for (x, y, w, d, c) in floors:
        I.add(-1000, I.flat(x, y, w, d, c, 0, "#12233B"))
    I.add(-990, I.box(0, 0, 0, 5, D, 80, "#EFEAE0", "#bdb6a6") + I.box(0, 0, 0, W, 5, 80, "#EFEAE0", "#bdb6a6"))
    if kind == "1R":
        bed(150, 20); sofa(30, 150, 90); table(40, 90); counter(30, 8, 90); tv(160, 175)
    elif kind == "1DK":
        bed(20, 20); closet(20, 8 if False else 160, 90); desk(110, 10)
        counter(158, 8, 100); fridge(226, 40); table(180, 110, 60, 44)
    elif kind == "1LDK":
        bed(14, 20); closet(14, 160, 80)
        counter(116, 8, 110); fridge(262, 10); table(150, 70, 70, 44); sofa(150, 140, 100); tv(180, 190)
    else:
        bed(10, 14); bed(104, 14 if False else 14); closet(10, 150, 70); desk(110, 150 - 2 if False else 120)
        counter(196, 8, 110); fridge(322, 10); table(220, 70, 70, 44); sofa(220, 130, 100)
    return svgwrap(320, 240, I.out())


def mini_grid():
    cells = ""
    for i, k in enumerate(["1R", "1DK", "1LDK", "2LDK"]):
        r, c = divmod(i, 2)
        sub = {"1R": "kitchen inside the room", "1DK": "dining-kitchen + 1 room",
               "1LDK": "living-dining-kitchen + 1 room", "2LDK": "living-dining-kitchen + 2 rooms"}[k]
        cells += (f'<g transform="translate({c*350} {r*262})">' + mini(k).replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 240" width="100%"', '<svg x="0" y="0" width="320" height="240" viewBox="0 0 320 240"')
                  + f'<text x="160" y="232" text-anchor="middle" font-size="19" font-weight="800" fill="#C8372D">{k}</text>'
                  + f'<text x="160" y="250" text-anchor="middle" font-size="11.5" fill="#6b7280" font-weight="500">{sub}</text></g>')
    return svgwrap(700, 530, cells)
