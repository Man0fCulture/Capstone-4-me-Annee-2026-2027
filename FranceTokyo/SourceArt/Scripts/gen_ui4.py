"""STEEZY ecran Options (CommonUI) - generateur des visuels.
Sorties dans ./out4
  T_UI_OptionRow_Selected  256x64    barre rouge de la ligne selectionnee (brush Box, bords gauche 48 px et droite 40 px)
  T_UI_Chevron_Left/Right  48x48     fleches de reglage (affichees en 24x24)
  T_UI_Controller          960x600   manette generique dessinee maison (affichee en 480x300)
  T_UI_ControllerLines     2060x880  traits rouges du schema (affiches en 1030x440), les pictos sont ceux du pack Fab
  Icones de touches provisoires
  T_Key_Q, T_Key_E, T_Key_LeftRight, T_Pad_LB, T_Pad_RB, T_Pad_DPad_LR
"""
import os, re, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out4')
os.makedirs(OUT, exist_ok=True)
DESIGN = sys.argv[1]
FONT_MENU = os.path.join(HERE, '..', 'Fonts', 'KH', 'KHMenu.otf')
FONT_SANS = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

ACCENT = (200, 16, 46)
ACCENT_HEX = '#C8102E'
INK = (243, 233, 234)


# ---------------------------------------------------------------- ligne selectionnee
def option_row():
    S = 4                      # sur-echantillonnage, export en 1x car le brush Box garde les bords a la taille de la texture
    W, H = 256, 64             # taille logique
    tip = 32                   # pointe a droite
    im = Image.new('RGBA', (W * S, H * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    shape = [(0, 0), ((W - tip) * S, 0), (W * S, H * S / 2), ((W - tip) * S, H * S), (0, H * S)]
    d.polygon(shape, fill=ACCENT + (255,))
    # assombrissement vers la droite, comme dans la maquette
    grad = Image.new('RGBA', (W * S, H * S), (0, 0, 0, 0))
    px = grad.load()
    x_a, x_b = int(0.30 * W * S), W * S
    for x in range(x_a, x_b):
        a = int(255 * 0.32 * (x - x_a) / (x_b - x_a))
        for y in range(H * S):
            px[x, y] = (0, 0, 0, a)
    mask = Image.new('L', (W * S, H * S), 0)
    ImageDraw.Draw(mask).polygon(shape, fill=255)
    im.paste(Image.alpha_composite(im, grad), (0, 0), mask)
    # petit losange blanc a gauche
    d = ImageDraw.Draw(im)
    cx, cy, r = 31 * S, H * S / 2, 7 * S
    d.polygon([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)], fill=(255, 246, 247, 255))
    im.resize((W, H), Image.LANCZOS).save(os.path.join(OUT, 'T_UI_OptionRow_Selected.png'))


def chevrons():
    S = 8
    for name, sign in (('T_UI_Chevron_Left', -1), ('T_UI_Chevron_Right', 1)):
        im = Image.new('RGBA', (24 * S, 24 * S), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        c = 12 * S
        pts = [(c - sign * 3 * S, c - 7 * S), (c + sign * 4 * S, c), (c - sign * 3 * S, c + 7 * S)]
        d.line(pts, fill=(255, 255, 255, 255), width=int(2.2 * S), joint='curve')
        im.resize((48, 48), Image.LANCZOS).save(os.path.join(OUT, name + '.png'))


# ---------------------------------------------------------------- icones de touches
def text_center(d, W, H, u, txt, font_path, px):
    f = ImageFont.truetype(font_path, int(px * u))
    b = d.textbbox((0, 0), txt, font=f)
    d.text(((W - (b[2] - b[0])) / 2 - b[0], (H - (b[3] - b[1])) / 2 - b[1]), txt, font=f, fill=INK + (255,))


def keycap(name, w, h, draw_fn, radius=4):
    S, K = 4, 4
    u = S * K
    im = Image.new('RGBA', (w * u, h * u), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([u * 0.75, u * 0.75, w * u - u * 0.75, h * u - u * 0.75], radius=radius * u,
                        outline=INK + (150,), width=int(1.25 * u), fill=(243, 233, 234, 18))
    draw_fn(d, w * u, h * u, u)
    im.resize((w * S, h * S), Image.LANCZOS).save(os.path.join(OUT, name + '.png'))


def h_arrow(d, cx, cy, u, left):
    s = 4.2 * u
    stem = 1.1 * u
    sign = -1 if left else 1
    d.polygon([(cx + sign * s, cy), (cx + sign * s * 0.1, cy - s * 0.8), (cx + sign * s * 0.1, cy + s * 0.8)], fill=INK + (255,))
    d.rectangle([min(cx - sign * s, cx + sign * s * 0.1), cy - stem / 2, max(cx - sign * s, cx + sign * s * 0.1), cy + stem / 2], fill=INK + (255,))


def dpad_lr():
    S, K, w = 4, 4, 28
    u = S * K
    im = Image.new('RGBA', (w * u, w * u), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    c = w * u / 2
    a, b = 4.2 * u, 12.5 * u
    col = INK + (255,)
    for box in ([c - a, c - b, c + a, c + b], [c - b, c - a, c + b, c + a]):
        d.rounded_rectangle(box, radius=1.5 * u, outline=INK + (150,), width=int(1.25 * u), fill=(243, 233, 234, 18))
    d.rectangle([c - a + 1.25 * u, c - a + 1.25 * u, c + a - 1.25 * u, c + a - 1.25 * u], fill=(30, 24, 26, 255))
    t = 2.6 * u
    d.polygon([(c - b + 2.2 * u, c), (c - b + 2.2 * u + t * 1.2, c - t), (c - b + 2.2 * u + t * 1.2, c + t)], fill=col)
    d.polygon([(c + b - 2.2 * u, c), (c + b - 2.2 * u - t * 1.2, c - t), (c + b - 2.2 * u - t * 1.2, c + t)], fill=col)
    im.resize((w * S, w * S), Image.LANCZOS).save(os.path.join(OUT, 'T_Pad_DPad_LR.png'))


# ---------------------------------------------------------------- manette + traits
def rsvg(svg_text, out_png, w, h):
    tmp = out_png[:-4] + '.svg'
    open(tmp, 'w', encoding='utf-8').write(svg_text)
    subprocess.run(['rsvg-convert', '-w', str(w), '-h', str(h), tmp, '-o', out_png], check=True)


def controller():
    s = open(DESIGN, encoding='utf-8').read()
    a = s.find('<svg role="img" aria-label="Manette"')
    b = s.find('</svg>', a) + 6
    svg = s[a:b]
    svg = svg.replace('{{ps}}', '0').replace('{{xb}}', '1').replace('{{accent}}', ACCENT_HEX)
    svg = re.sub(r'<svg[^>]*>', '<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500">', svg, count=1)
    rsvg(svg, os.path.join(OUT, 'T_UI_Controller.png'), 960, 600)


# Disposition du schema, en pixels ecran dans une zone de 1030 x 440
DIAG_W, DIAG_H = 1030, 440
PAD_X, PAD_Y, PAD_S = 275, 80, 0.6
ROWS_LEFT = [('LT', 70), ('LB', 110), ('DU', 170), ('DR', 210), ('DD', 250), ('DL', 290), ('LS', 360), ('L3', 400)]
ROWS_RIGHT = [('RT', 70), ('RB', 110), ('A', 170), ('X', 210), ('B', 250), ('Y', 290), ('RS', 360), ('R3', 400)]
GLYPH_L, GLYPH_R = 225, DIAG_W - 225
TOP_Y = 48
GLYPH_SELECT, GLYPH_START = 424, DIAG_W - 424

DARK, LIGHT, OFF = '#1B1B20', '#F4F4F6', '#5E5F68'
WITH_GLYPHS = False


def glyph(code, cx, cy):
    """Picto d'un bouton, centre en (cx, cy). Formes generiques, lettres simples."""
    t = lambda x, y, size, txt: f'<text x="{x}" y="{y}" text-anchor="middle" font-family="DejaVu Sans" font-size="{size}" font-weight="bold" fill="{DARK}">{txt}</text>'
    if code in ('A', 'B', 'X', 'Y'):
        body = f'<circle cx="17" cy="17" r="16" fill="{LIGHT}"/>' + t(17, 22.5, 15, code)
        w = 34
    elif code in ('LT', 'RT'):
        body = f'<path d="M3,33 L3,15 C3,6 10,1 20,1 C30,1 37,6 37,15 L37,33 Z" fill="{LIGHT}"/>' + t(20, 25, 13, code)
        w = 40
    elif code in ('LB', 'RB'):
        body = f'<rect x="2" y="6" width="36" height="22" rx="5" fill="{LIGHT}"/>' + t(20, 22, 13, code)
        w = 40
    elif code in ('LS', 'RS'):
        body = f'<circle cx="17" cy="17" r="16" fill="{LIGHT}"/>' + t(17, 22.5, 15, code[0])
        w = 34
    elif code in ('L3', 'R3'):
        body = (f'<circle cx="17" cy="17" r="15.5" fill="none" stroke="{LIGHT}" stroke-width="2"/>'
                f'<circle cx="17" cy="17" r="12" fill="{LIGHT}"/>' + t(17, 21, 11, code))
        w = 34
    elif code in ('DU', 'DR', 'DD', 'DL'):
        f = {k: (LIGHT if k == code else OFF) for k in ('DU', 'DR', 'DD', 'DL')}
        body = (f'<rect x="13" y="2" width="8" height="12" rx="2" fill="{f["DU"]}"/>'
                f'<rect x="20" y="13" width="12" height="8" rx="2" fill="{f["DR"]}"/>'
                f'<rect x="13" y="20" width="8" height="12" rx="2" fill="{f["DD"]}"/>'
                f'<rect x="2" y="13" width="12" height="8" rx="2" fill="{f["DL"]}"/>')
        w = 34
    else:  # SELECT / START
        inner = ('<rect x="11" y="12" width="8" height="6" rx="1"/><rect x="15" y="15" width="8" height="6" rx="1"/>'
                 if code == 'SELECT' else '<path d="M12,13.5 H22 M12,17 H22 M12,20.5 H22"/>')
        body = f'<rect x="3" y="8" width="28" height="18" rx="9" fill="{LIGHT}"/><g fill="none" stroke="{DARK}" stroke-width="1.6">{inner}</g>'
        w = 34
    return f'<g transform="translate({cx - w / 2},{cy - 17})">{body}</g>'


def lines():
    mx = lambda x: DIAG_W - x          # miroir gauche / droite
    px = lambda x, y: (PAD_X + x * PAD_S, PAD_Y + y * PAD_S)   # point de la manette vers le schema
    lt, dpad, stick, select = px(208, 30), px(175, 150), px(290, 292), px(228, 75)
    bx = 254                            # x du crochet de gauche
    gap = PAD_X + 174                   # x libre entre les deux gachettes
    left = [
        [(bx - 6, 58), (bx, 58), (bx, 122), (bx - 6, 122)],
        [(bx - 6, 158), (bx, 158), (bx, 302), (bx - 6, 302)],
        [(bx - 6, 348), (bx, 348), (bx, 412), (bx - 6, 412)],
        [(bx, 90), (lt[0] - 8, 90), lt],
        [(bx, 170), (dpad[0] - 26, 170)],
        [(bx, 380), (stick[0] - 125, 380), stick],
        [(GLYPH_SELECT + 19, TOP_Y), (gap, TOP_Y), (gap, select[1] - (gap - select[0])), select],
    ]
    dots = [lt, (dpad[0] - 26, 170), stick, select]
    poly = lambda pts: '<polyline points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts) + '"/>'
    g_lines = ''.join(poly(p) + poly([(mx(x), y) for x, y in p]) for p in left)
    g_dots = ''.join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5"/><circle cx="{mx(x):.1f}" cy="{y:.1f}" r="3.5"/>' for x, y in dots)
    g_glyphs = ''.join(glyph(c, GLYPH_L, y) for c, y in ROWS_LEFT) + ''.join(glyph(c, GLYPH_R, y) for c, y in ROWS_RIGHT)
    g_glyphs += glyph('SELECT', GLYPH_SELECT, TOP_Y) + glyph('START', GLYPH_START, TOP_Y)
    if not WITH_GLYPHS:
        g_glyphs = ''   # les pictos viennent du pack Fab, poses en widgets Image par-dessus
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{DIAG_W}" height="{DIAG_H}" viewBox="0 0 {DIAG_W} {DIAG_H}">'
           f'<g fill="none" stroke="{ACCENT_HEX}" stroke-opacity="0.95" stroke-width="1.5" stroke-linejoin="round">{g_lines}</g>'
           f'<g fill="#FF3A55">{g_dots}</g>{g_glyphs}</svg>')
    rsvg(svg, os.path.join(OUT, 'T_UI_ControllerLines.png'), DIAG_W * 2, DIAG_H * 2)


def preview():
    """Apercu de controle, non importe dans le projet."""
    im = Image.new('RGBA', (DIAG_W * 2, DIAG_H * 2), (11, 7, 8, 255))
    pad = Image.open(os.path.join(OUT, 'T_UI_Controller.png')).convert('RGBA')
    im.alpha_composite(pad, (PAD_X * 2, PAD_Y * 2))
    im.alpha_composite(Image.open(os.path.join(OUT, 'T_UI_ControllerLines.png')).convert('RGBA'))
    im.save(os.path.join(OUT, '_preview_diagram.png'))


if __name__ == '__main__':
    option_row()
    chevrons()
    keycap('T_Key_Q', 28, 28, lambda d, W, H, u: text_center(d, W, H, u, 'Q', FONT_SANS, 14))
    keycap('T_Key_E', 28, 28, lambda d, W, H, u: text_center(d, W, H, u, 'E', FONT_SANS, 14))
    keycap('T_Key_LeftRight', 52, 28, lambda d, W, H, u: (h_arrow(d, W * 0.33, H / 2, u, True), h_arrow(d, W * 0.67, H / 2, u, False)))
    keycap('T_Pad_LB', 44, 28, lambda d, W, H, u: text_center(d, W, H, u, 'LB', FONT_SANS, 13), radius=9)
    keycap('T_Pad_RB', 44, 28, lambda d, W, H, u: text_center(d, W, H, u, 'RB', FONT_SANS, 13), radius=9)
    dpad_lr()
    controller()
    lines()
    preview()
    print('ok', sorted(os.listdir(OUT)))
