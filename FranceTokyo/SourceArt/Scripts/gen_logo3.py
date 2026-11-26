"""STEEZY logo v3. Meme logo que la v2, avec le tas de poudre et la lame a la place du losange au coeur couronne.
Usage  python3 gen_logo3.py chemin/vers/silhouette.png"""
import sys
import math, os, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

HERE = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(HERE, '..', 'Fonts', 'KH') + os.sep
OUT = os.path.join(HERE, '..', 'UI', 'logo') + os.sep
SILHOUETTE = sys.argv[1]
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
# Titre cramoisi a plat, sous-titre au-dessus entre deux filets, soulignement arque et embleme au centre.
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
        x = cx + side * (120 + t * 370)
        y = ey - 4 - 26 * (t ** 1.6)
        pts.append((x, y))
    dl.line(pts, fill=255, width=5, joint='curve')
    pts2 = [(x, y + 14) for x, y in pts[:42]]
    dl.line(pts2, fill=200, width=2, joint='curve')
# embleme : silhouette fournie (tas de poudre + lame), posee entre les deux traits
em = Image.new('L', (W, H), 0)
de = ImageDraw.Draw(em)
src = Image.open(SILHOUETTE).convert('RGBA')
flat = Image.new('RGBA', src.size, (255, 255, 255, 255))   # fond transparent ramene a du blanc
flat.alpha_composite(src)
sil = flat.convert('L')
sil = sil.point(lambda v: 255 if v < 110 else (0 if v > 170 else int(255 * (170 - v) / 60)))  # noir -> plein
sil = sil.crop(sil.getbbox())
EM_W = 196
sil = sil.resize((EM_W, int(sil.height * EM_W / sil.width)), Image.LANCZOS)
em_top = ey - 98
em.paste(sil, (cx - EM_W // 2, em_top), sil)
de.polygon(star(cx, em_top + sil.height + 24, 14, 3, 4), fill=255)
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
json.dump({'size': logo.size, 'sub_top': sy - oy, 'sub_mid': ly - oy, 'title_top': ty - oy, 'title_bot': ty + title.height - oy, 'emblem_y': ey - oy, 'emblem_bot': em_top + sil.height + 38 - oy, 'cx': cx - ox}, open(OUT + 'logo_metrics.json', 'w'))
logo.save(OUT + 'T_UI_Logo.png')
a = logo.split()[3].point(lambda v: 255 if v > 90 else 0)
edge = ImageChops.subtract(a.filter(ImageFilter.MaxFilter(7)), a.filter(ImageFilter.MinFilter(3))).filter(ImageFilter.GaussianBlur(1.4))
Image.merge('RGBA', (edge, edge, edge, edge)).save(OUT + 'T_UI_LogoEdge.png')
print('logo', logo.size)

