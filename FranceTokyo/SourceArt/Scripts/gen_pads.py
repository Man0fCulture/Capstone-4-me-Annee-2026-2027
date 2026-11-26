"""STEEZY onglet Manette - les schemas de manette.
Sorties dans ./out6
  T_UI_Pad_<nom>        image de la manette, au double de sa taille affichee
  T_UI_PadLines_<nom>   traits rouges qui relient les pictos a la manette, au double de la taille du schema
  pad_layout.json       position de la manette, des pictos et des textes, lue pour regler le widget
Les trois images sont fournies telles quelles et ne sont pas retouchees
  PS5     vue de face du PDF DualSense_Wireless_Controller_RGB_012
  Xbox    Pad_Xbox_source.png
  Switch  Pad_Switch_source.png
Les pictos des touches viennent du pack Fab et sont poses dans le widget.
"""
import json, os, subprocess
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out6')
os.makedirs(OUT, exist_ok=True)
ACCENT = '#C8102E'

# Gabarit du schema. Le widget l agrandit ou le reduit d un bloc selon la place libre.
DIAG_W, DIAG_H = 1100, 530
ICON = 40                                  # cote d un picto
GLYPH_L, GLYPH_R = 212, 861                # centre des pictos de gauche et de droite
LABEL_L, LABEL_R = GLYPH_L - 30, GLYPH_R + 30
BX_L, BX_R = GLYPH_L + 28, GLYPH_R - 28    # x des crochets
CX = (BX_L + BX_R) / 2                     # milieu de la place laissee a la manette
ROWS_MID = 289                             # hauteur du milieu des pictos de cote
TOP_Y = 24                                 # centre des pictos du haut
TOP_L, TOP_R = 440, 633                    # centre des deux pictos du haut
ARM = 16                                   # demi hauteur d un crochet autour d un picto

# Planche Sony, vue de face
PS5_PDF = os.path.join(HERE, 'DualSense_Wireless_Controller_RGB_012.pdf')
PS5_PAGE = 5                               # planche couleur prevue pour un fond sombre
PS5_BOX = (287, 605, 1230, 1231)           # cadre de la vue de face sur la page rendue a 150 dpi

# Lignes du schema, y du centre de chaque picto
STICK_LOW = [('LT', 90), ('LB', 140), ('DU', 214), ('DR', 264), ('DD', 314), ('DL', 364), ('LS', 438), ('L3', 488)]
STICK_HIGH = [('LT', 90), ('LB', 140), ('LS', 214), ('L3', 264), ('DU', 338), ('DR', 388), ('DD', 438), ('DL', 488)]
RIGHT = [('RT', 90), ('RB', 140), ('A', 214), ('X', 264), ('B', 314), ('Y', 364), ('RS', 438), ('R3', 488)]
RIGHT_GROUPS = [(0, 1), (2, 5), (6, 7)]

# Pour chaque manette, sa taille affichee, la taille de son image source, les lignes de gauche,
# puis les points vises dans l image source. left et right donnent gachette, groupe du milieu, groupe du bas.
PADS = {
    'PS5': dict(show=(565, 375), src=(943, 626), rows=STICK_LOW, groups=[(0, 1), (2, 5), (6, 7)],
                left=[(200, 40), (130, 180), (325, 306)], right=[(743, 40), (827, 180), (618, 306)],
                top=[(255, 78), (686, 78)]),
    'Xbox': dict(show=(565, 351), src=(1535, 954), rows=STICK_HIGH, groups=[(0, 1), (2, 3), (4, 7)],
                 left=[(330, 125), (352, 440), (486, 655)], right=[(1205, 125), (1286, 407), (977, 668)],
                 top=[(649, 420), (883, 420)]),
    'Switch': dict(show=(550, 400), src=(1584, 1151), rows=STICK_HIGH, groups=[(0, 1), (2, 3), (4, 7)],
                   left=[(330, 95), (355, 365), (550, 587)], right=[(1254, 95), (1332, 367), (997, 587)],
                   top=[(598, 247), (985, 247)]),
}


def box(name):
    """Cadre de la manette dans le schema, centre entre les crochets et sur le milieu des pictos."""
    w, h = PADS[name]['show']
    return (round(CX - w / 2), round(ROWS_MID - h / 2), w, h)


def at(name, p):
    """Point de l image source vers le schema."""
    x, y, w, h = box(name)
    sw, sh = PADS[name]['src']
    return (x + p[0] * w / sw, y + p[1] * h / sh)


def rsvg(svg_text, out_png, w, h):
    tmp = out_png[:-4] + '.svg'
    open(tmp, 'w', encoding='utf-8').write(svg_text)
    subprocess.run(['rsvg-convert', '-w', str(w), '-h', str(h), tmp, '-o', out_png], check=True)
    os.remove(tmp)


def shrink(img, name):
    """Reduit une image au double de sa taille affichee, sans frange sombre sur les bords."""
    w, h = PADS[name]['show']
    img.convert('RGBa').resize((w * 2, h * 2), Image.LANCZOS).convert('RGBA').save(os.path.join(OUT, f'T_UI_Pad_{name}.png'))


def pad_ps5():
    """Decoupe la vue de face dans la planche Sony."""
    k = 4                                  # rendu a 600 dpi puis reduction, pour des bords propres
    x0, y0, x1, y1 = (v * k for v in PS5_BOX)
    tmp = os.path.join(OUT, '_dualsense')
    subprocess.run(['pdftocairo', '-png', '-transp', '-r', str(150 * k), '-f', str(PS5_PAGE), '-l', str(PS5_PAGE),
                    '-x', str(x0), '-y', str(y0), '-W', str(x1 - x0), '-H', str(y1 - y0), '-singlefile', PS5_PDF, tmp], check=True)
    shrink(Image.open(tmp + '.png'), 'PS5')
    os.remove(tmp + '.png')


def side(rows, groups, targets, bx, way):
    """Crochets et traits d un cote. way vaut 1 a gauche et -1 a droite.
    Si la touche visee est a la hauteur de son crochet le trait file droit, sinon il part du milieu du crochet et finit en biais."""
    y = [v for _, v in rows]
    lines, dots = [], []
    for (a, b), t in zip(groups, targets):
        top, bottom = y[a] - ARM, y[b] + ARM
        lines.append([(bx - 6 * way, top), (bx, top), (bx, bottom), (bx - 6 * way, bottom)])
        if top + 4 <= t[1] <= bottom - 4:
            lines.append([(bx, t[1]), t])
        else:
            mid = (top + bottom) / 2
            lines.append([(bx, mid), (t[0] - way * abs(mid - t[1]), mid), t])
        dots.append(t)
    return lines, dots


def drop(gx, t):
    """Trait qui descend d un picto du haut puis rejoint la touche en biais."""
    return [(gx, TOP_Y + ICON / 2 + 4), (gx, t[1] - abs(gx - t[0])), t]


def lines(name):
    p = PADS[name]
    ll, ld = side(p['rows'], p['groups'], [at(name, t) for t in p['left']], BX_L, 1)
    rl, rd = side(RIGHT, RIGHT_GROUPS, [at(name, t) for t in p['right']], BX_R, -1)
    tops = [at(name, t) for t in p['top']]
    polys = ll + rl + [drop(TOP_L, tops[0]), drop(TOP_R, tops[1])]
    dots = ld + rd + tops
    poly = lambda pts: '<polyline points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts) + '"/>'
    dot = lambda q: f'<circle cx="{q[0]:.1f}" cy="{q[1]:.1f}" r="4"/>'
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{DIAG_W}" height="{DIAG_H}" viewBox="0 0 {DIAG_W} {DIAG_H}">'
           f'<g fill="none" stroke="{ACCENT}" stroke-opacity="0.95" stroke-width="1.6" stroke-linejoin="round">'
           + ''.join(poly(q) for q in polys) + '</g><g fill="#FF3A55">' + ''.join(dot(q) for q in dots) + '</g></svg>')
    rsvg(svg, os.path.join(OUT, f'T_UI_PadLines_{name}.png'), DIAG_W * 2, DIAG_H * 2)


def layout():
    """Position de la manette, de chaque picto et de chaque texte, pour regler le widget sans rien mesurer a la main."""
    data = {'size': [DIAG_W, DIAG_H], 'icon': ICON, 'pads': {}}
    for name, p in PADS.items():
        icons = {k: [GLYPH_L, y] for k, y in p['rows']}
        icons.update({k: [GLYPH_R, y] for k, y in RIGHT})
        icons.update({'Select': [TOP_L, TOP_Y], 'Start': [TOP_R, TOP_Y]})
        labels = {k: [LABEL_L, y, 1] for k, y in p['rows']}
        labels.update({k: [LABEL_R, y, 0] for k, y in RIGHT})
        labels.update({'Select': [TOP_L - ICON / 2 - 10, TOP_Y, 1], 'Start': [TOP_R + ICON / 2 + 10, TOP_Y, 0]})
        data['pads'][name] = {'pad': list(box(name)), 'icons': icons, 'labels': labels}
    json.dump(data, open(os.path.join(OUT, 'pad_layout.json'), 'w'), indent=1)
    return data


def preview(name, data):
    """Apercu de controle, non importe dans le projet. Les carres blancs marquent la place des pictos."""
    im = Image.new('RGBA', (DIAG_W * 2, DIAG_H * 2), (11, 7, 8, 255))
    x, y, w, h = box(name)
    im.alpha_composite(Image.open(os.path.join(OUT, f'T_UI_Pad_{name}.png')).convert('RGBA'), (x * 2, y * 2))
    im.alpha_composite(Image.open(os.path.join(OUT, f'T_UI_PadLines_{name}.png')).convert('RGBA'))
    d = ImageDraw.Draw(im)
    for code, (ix, iy) in data['pads'][name]['icons'].items():
        d.rectangle([ix * 2 - ICON, iy * 2 - ICON, ix * 2 + ICON, iy * 2 + ICON], outline=(255, 255, 255, 255))
        d.text((ix * 2 - 20, iy * 2 - 10), code, fill=(255, 255, 255, 255))
    im.save(os.path.join(OUT, f'_preview_{name}.png'))


if __name__ == '__main__':
    pad_ps5()
    shrink(Image.open(os.path.join(HERE, 'Pad_Xbox_source.png')), 'Xbox')
    shrink(Image.open(os.path.join(HERE, 'Pad_Switch_source.png')), 'Switch')
    data = layout()
    for n in PADS:
        lines(n)
        preview(n, data)
    print('ok', sorted(os.listdir(OUT)))
