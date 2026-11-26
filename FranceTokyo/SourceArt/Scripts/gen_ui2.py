"""STEEZY menu UI art v2 — Kingdom Hearts fonts (KHTitle / KHMenu by Televo), reference-driven layout."""
import math, os, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

HERE = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(HERE, '..', 'Fonts', 'KH') + os.sep
OUT = os.path.join(HERE, '..', 'UI', 'v2') + os.sep
os.makedirs(OUT, exist_ok=True)
random.seed(7)


def font(n, s):
    return ImageFont.truetype(F + n + '.otf', s)


def text_mask(txt, fnt, spacing=0):
    W = int(fnt.size * (len(txt) + 4) * 1.2)
    H = int(fnt.size * 3)
    m = Image.new('L', (W, H), 0)
    d = ImageDraw.Draw(m)
    x = fnt.size
    for ch in txt:
        d.text((x, fnt.size), ch, font=fnt, fill=255)
        x += d.textlength(ch, font=fnt) + spacing
    return m.crop(m.getbbox())


def vgrad_l(w, h, stops):
    im = Image.new('L', (1, h))
    px = im.load()
    for y in range(h):
        t = y / max(1, h - 1)
        for i in range(len(stops) - 1):
            t0, v0 = stops[i]
            t1, v1 = stops[i + 1]
            if t0 <= t <= t1:
                k = (t - t0) / max(1e-6, t1 - t0)
                px[0, y] = int(v0 + (v1 - v0) * k)
                break
    return im.resize((w, h))


def vgrad_rgb(w, h, stops):
    chans = [vgrad_l(w, h, [(t, c[i]) for t, c in stops]) for i in range(3)]
    return Image.merge('RGB', chans)


def star(cx, cy, r1, r2, n=4, rot=-math.pi / 2):
    pts = []
    for i in range(n * 2):
        r = r1 if i % 2 == 0 else r2
        a = rot + math.pi * i / n
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def heart(cx, cy, s):
    pts = []
    for i in range(160):
        t = 2 * math.pi * i / 160
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        pts.append((cx + x * s, cy - y * s))
    return pts


def crown(cx, base_y, w, h):
    return [(cx - w / 2, base_y), (cx - w / 2 - w * 0.06, base_y - h * 0.78), (cx - w / 4, base_y - h * 0.38),
            (cx, base_y - h), (cx + w / 4, base_y - h * 0.38), (cx + w / 2 + w * 0.06, base_y - h * 0.78),
            (cx + w / 2, base_y)]


# ------------------------------------------------------------------ LOGO
# Flat crimson KH-style title like the reference (no chrome), small subtitle above with
# flanking rules, arched underline with a crown/heart emblem.
CRIMSON_TOP = (232, 36, 62)
CRIMSON_MID = (196, 18, 46)
CRIMSON_LOW = (128, 8, 28)

W, H = 1400, 760
alpha = Image.new('L', (W, H), 0)   # union mask of everything drawn in crimson
detail = Image.new('L', (W, H), 0)  # thin lines (rendered a bit brighter)
cx = W // 2

title = text_mask('STEEZY', font('KHTitle', 300), spacing=6)
# KHTitle swashes are long; keep the logo under ~1080px wide at this scale
scale = min(1.0, 1060 / title.width)
if scale < 1.0:
    title = title.resize((int(title.width * scale), int(title.height * scale)), Image.LANCZOS)
tx = cx - title.width // 2
ty = 150
alpha.paste(title, (tx, ty), title)
title_box = (tx, ty, tx + title.width, ty + title.height)

# subtitle above (like "THE" in the reference)
sub = text_mask('EL TOURNAMENT DEL POWDER', font('KHTitle', 40), spacing=7)
sx = cx - sub.width // 2
sy = ty - sub.height - 26
alpha.paste(sub, (sx, sy), sub)
dl = ImageDraw.Draw(detail)
ly = sy + sub.height // 2
for side in (-1, 1):
    x0 = cx + side * (sub.width // 2 + 26)
    x1 = cx + side * 470
    dl.line([(x0, ly), (x1, ly)], fill=255, width=4)
    dl.polygon(star(x1 + side * 14, ly, 13, 3, 4), fill=255)

# arched underline + emblem
ey = ty + title.height + 70
for side in (-1, 1):
    pts = []
    for i in range(61):
        t = i / 60
        x = cx + side * (70 + t * 420)
        y = ey - 4 - 26 * (t ** 1.6)
        pts.append((x, y))
    dl.line(pts, fill=255, width=5, joint='curve')
    pts2 = [(x, y + 14) for x, y in pts[:42]]
    dl.line(pts2, fill=200, width=2, joint='curve')
# emblem: lattice diamond with crown over heart
em = Image.new('L', (W, H), 0)
de = ImageDraw.Draw(em)
r = 62
de.polygon([(cx, ey - r), (cx + r, ey), (cx, ey + r), (cx - r, ey)], outline=255, width=6)
de.polygon([(cx, ey - r + 16), (cx + r - 16, ey), (cx, ey + r - 16), (cx - r + 16, ey)], outline=255, width=3)
for k in (-1, 1):
    de.line([(cx - r / 2, ey + k * r / 2), (cx + r / 2, ey - k * r / 2)], fill=255, width=2)
de.polygon(heart(cx, ey + 10, 1.5), fill=255)
de.polygon(crown(cx, ey - 14, 36, 28), fill=255)
de.polygon(star(cx, ey - r - 20, 14, 3, 4), fill=255)
de.polygon(star(cx, ey + r + 20, 14, 3, 4), fill=255)
alpha = ImageChops.lighter(alpha, ImageChops.lighter(detail, em))

# shading: vertical crimson gradient over the title, inner top highlight, soft dark under-edge
rgb = vgrad_rgb(W, H, [(0, CRIMSON_TOP), (0.40, CRIMSON_MID), (0.62, CRIMSON_LOW), (1, CRIMSON_MID)])
# per-glyph gradient for the title so every letter goes bright->deep
tg = vgrad_rgb(title.width, title.height, [(0, (246, 70, 92)), (0.35, CRIMSON_MID), (0.75, CRIMSON_LOW), (1, (150, 12, 34))])
rgb.paste(tg, (tx, ty))
# inner highlight: alpha minus alpha shifted down -> top edges
a_bin = alpha.point(lambda v: 255 if v > 110 else 0)
shift = ImageChops.offset(a_bin, 0, 4)
top_edge = ImageChops.subtract(a_bin, shift).filter(ImageFilter.GaussianBlur(1.2))
hl = Image.new('RGB', (W, H), (255, 150, 160))
rgb = Image.composite(hl, rgb, top_edge.point(lambda v: int(v * 0.55)))
logo = rgb.convert('RGBA')
logo.putalpha(alpha)

# subtle dark rim so the crimson reads over the frame lines / mist
rim = alpha.filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.GaussianBlur(2))
base = Image.new('RGBA', (W, H), (12, 0, 2, 0))
base.putalpha(rim.point(lambda v: int(v * 0.85)))
logo = Image.alpha_composite(base, logo)

bb = logo.getbbox()
pad = 30
logo = logo.crop((bb[0] - pad, bb[1] - pad, bb[2] + pad, bb[3] + pad))
import json
ox, oy = bb[0] - pad, bb[1] - pad
json.dump({'size': logo.size, 'sub_top': sy - oy, 'sub_mid': ly - oy, 'title_top': ty - oy, 'title_bot': ty + title.height - oy, 'emblem_y': ey - oy, 'emblem_bot': ey + 62 + 34 - oy, 'cx': cx - ox}, open(OUT + 'logo_metrics.json', 'w'))
logo.save(OUT + 'T_UI_Logo.png')
a = logo.split()[3].point(lambda v: 255 if v > 90 else 0)
edge = ImageChops.subtract(a.filter(ImageFilter.MaxFilter(7)), a.filter(ImageFilter.MinFilter(3))).filter(ImageFilter.GaussianBlur(1.4))
Image.merge('RGBA', (edge, edge, edge, edge)).save(OUT + 'T_UI_LogoEdge.png')
print('logo', logo.size)

# ------------------------------------------------------------------ FRAME (display 560x960, texture 2x)
S = 2
FW, FH = 560 * S, 960 * S
fr = Image.new('L', (FW, FH), 0)
df = ImageDraw.Draw(fr)


def hexa(cxh, top, bot, half_w, shoulder):
    return [(cxh, top), (cxh + half_w, top + shoulder), (cxh + half_w, bot - shoulder), (cxh, bot),
            (cxh - half_w, bot - shoulder), (cxh - half_w, top + shoulder), (cxh, top)]


h1 = hexa(280 * S, 18 * S, 942 * S, 152 * S, 120 * S)
h2 = hexa(266 * S, 44 * S, 916 * S, 140 * S, 116 * S)
df.line(h1, fill=255, width=3, joint='curve')
df.line(h2, fill=190, width=2, joint='curve')
# little apex diamonds
for yy, s in ((18 * S, 1), (942 * S, -1)):
    c = (280 * S, yy + s * 52 * S)
    df.polygon([(c[0], c[1] - 9 * S), (c[0] + 7 * S, c[1]), (c[0], c[1] + 9 * S), (c[0] - 7 * S, c[1])], outline=255, width=2)
# clear the band where the logo sits (logo top ~ y 186, bottom ~ y 402 in display units)
ImageDraw.Draw(fr).rectangle([0, 190 * S, FW, 418 * S], fill=0)
# short terminal ticks where the lines stop
for xx in (280 - 152, 280 + 152, 266 - 140, 266 + 140):
    for yy in (190, 418):
        df.ellipse([(xx - 2.5) * S, (yy - 2.5) * S, (xx + 2.5) * S, (yy + 2.5) * S], fill=255)
Image.merge('RGBA', (fr, fr, fr, fr)).save(OUT + 'T_UI_Frame.png')

# ------------------------------------------------------------------ BANNER (display 380x56, both ends pointed)
BW, BH = 1024, 152


def banner_poly(inset=0.0):
    i = inset
    tip = BH * 0.50
    return [(6 + i * 1.8, BH / 2), (6 + tip + i, 10 + i), (BW - 6 - tip - i, 10 + i), (BW - 6 - i * 1.8, BH / 2),
            (BW - 6 - tip - i, BH - 10 - i), (6 + tip + i, BH - 10 - i)]


fill = Image.new('L', (BW, BH), 0)
ImageDraw.Draw(fill).polygon(banner_poly(5), fill=255)
# fill: deeper at the edges, a touch brighter through the middle band
g = vgrad_l(BW, BH, [(0, 150), (0.5, 255), (1, 150)])
hg = Image.new('L', (BW, 1))
for x in range(BW):
    t = x / (BW - 1)
    hg.putpixel((x, 0), int(255 * (0.78 + 0.22 * math.sin(math.pi * t))))
hg = hg.resize((BW, BH))
fill = ImageChops.multiply(ImageChops.multiply(fill, g), hg)
border = Image.new('L', (BW, BH), 0)
db = ImageDraw.Draw(border)
db.polygon(banner_poly(0), outline=255, width=4)
db.polygon(banner_poly(11), outline=110, width=2)
glow = Image.new('L', (BW, BH), 0)
ImageDraw.Draw(glow).polygon(banner_poly(0), fill=255)
glow = ImageChops.subtract(glow.filter(ImageFilter.GaussianBlur(9)), glow.point(lambda v: v)).point(lambda v: min(255, v * 2))
A = ImageChops.lighter(ImageChops.lighter(fill, border), glow)
Image.merge('RGBA', (fill, border, glow, A)).save(OUT + 'T_UI_Banner.png')

# ------------------------------------------------------------------ GLYPH (button-badge style, like the reference prompt icon)
GS = 256
gl = Image.new('L', (GS, GS), 0)
dg = ImageDraw.Draw(gl)
dg.ellipse([10, 10, GS - 10, GS - 10], fill=255)
inner = Image.new('L', (GS, GS), 0)
di = ImageDraw.Draw(inner)
di.ellipse([26, 26, GS - 26, GS - 26], outline=255, width=6)
di.polygon(crown(GS / 2, GS * 0.52, 96, 70), fill=255)
di.polygon(star(GS / 2, GS * 0.70, 34, 8, 4, 0), fill=255)
# badge = filled disc with the crown cut out (reads like a controller prompt)
badge = ImageChops.subtract(gl, inner.point(lambda v: int(v * 0.85)))
Image.merge('RGBA', (badge, badge, badge, badge)).save(OUT + 'T_UI_GlyphCrownStar.png')

# ------------------------------------------------------------------ RED MIST (fullscreen 1920x1080)
MW, MH = 1920, 1080


def fbm(w, h, octaves=5, seed=0):
    import numpy as np
    rng = np.random.default_rng(seed)
    acc = np.zeros((h, w), np.float32)
    amp, tot, cell = 1.0, 0.0, 180
    for o in range(octaves):
        cw, ch = max(2, w // cell), max(2, h // cell)
        n = Image.fromarray((rng.random((ch, cw)) * 255).astype('uint8')).resize((w, h), Image.BICUBIC)
        acc += np.asarray(n, np.float32) * amp
        tot += amp
        amp *= 0.55
        cell = max(4, cell // 2)
    return Image.fromarray(np.clip(acc / tot, 0, 255).astype('uint8'))


noise = fbm(MW, MH, 5, 11)
mask = Image.new('L', (MW, MH), 0)
md = ImageDraw.Draw(mask)
# left edge band and top-right corner, like the blood-mist in the reference
for i in range(26):
    md.ellipse([-260 + random.randint(-60, 60), i * 46 - 120, 220 + random.randint(-80, 80), i * 46 + 160], fill=random.randint(120, 220))
md.ellipse([1400, -380, 2300, 380], fill=230)
md.ellipse([1600, -200, 2100, 520], fill=180)
mask = mask.filter(ImageFilter.GaussianBlur(110))
mist = ImageChops.multiply(mask, noise.point(lambda v: max(0, min(255, int((v - 95) * 3.2)))))
# speckles
sp = Image.new('L', (MW, MH), 0)
ds = ImageDraw.Draw(sp)
for _ in range(1400):
    x = random.random()
    y = random.random()
    if not (x < 0.17 or (x > 0.74 and y < 0.42)):
        continue
    px, py = x * MW, y * MH
    rr = random.choice([1, 1, 1.5, 2, 2.5])
    ds.ellipse([px - rr, py - rr, px + rr, py + rr], fill=random.randint(90, 230))
sp = ImageChops.multiply(sp, mask.point(lambda v: min(255, v * 2)))
mist_a = ImageChops.lighter(mist.point(lambda v: int(v * 0.45)), sp.point(lambda v: int(v * 0.8)))
mist_rgb = Image.new('RGB', (MW, MH), (120, 6, 14))
mist_img = mist_rgb.convert('RGBA')
mist_img.putalpha(mist_a)
mist_img.save(OUT + 'T_UI_RedMist.png')
print('done', sorted(os.listdir(OUT)))
