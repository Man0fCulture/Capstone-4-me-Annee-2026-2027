"""STEEZY lecteur cassette de l'ecran Souvenirs, generateur des visuels.
Sorties dans ../UI/v6, en blanc sur fond transparent, la couleur est donnee dans Unreal.
Les tailles affichees sont la moitie des tailles de texture.
  T_UI_Cassette   560x340  corps de la cassette, fenetre et etiquette (affiche en 280x170)
  T_UI_Reel       96x96    bobine avec ses dents, tourne pendant la lecture (affichee en 48x48)
  T_UI_TapePack   96x96    galette de bande, grossit ou maigrit avec la progression (affichee en 48x48)
  T_UI_Prev       64x64    piste precedente (affiche en 20x20)
  T_UI_Next       64x64    piste suivante (affiche en 20x20)
"""
import math
import os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'UI', 'v6')
os.makedirs(OUT, exist_ok=True)
S = 8  # sur-echantillonnage pour des bords propres


def canvas(w, h):
    im = Image.new('RGBA', (w * S, h * S), (0, 0, 0, 0))
    return im, ImageDraw.Draw(im)


def white(a=255):
    return (255, 255, 255, a)


def save(im, name, w, h):
    im.resize((w, h), Image.LANCZOS).save(os.path.join(OUT, name + '.png'))


def p(x, y):
    return (x * S, y * S)


def cassette():
    # dessin en unites d'affichage 280x170, texture exportee en 560x340
    W, H = 280, 170
    im, d = canvas(W, H)
    c = 12
    body = [p(4 + c, 4), p(W - 4 - c, 4), p(W - 4, 4 + c), p(W - 4, H - 4 - c), p(W - 4 - c, H - 4),
            p(4 + c, H - 4), p(4, H - 4 - c), p(4, 4 + c), p(4 + c, 4)]
    d.line(body, fill=white(), width=int(2.4 * S), joint='curve')
    # etiquette en haut, le nom de la categorie est pose dessus dans Unreal
    d.rectangle([p(24, 16), p(W - 24, 52)], outline=white(150), width=int(1.4 * S))
    d.line([p(24, 44), p(W - 24, 44)], fill=white(70), width=int(1 * S))
    # fenetre de bande entre les deux bobines
    d.rounded_rectangle([p(50, 66), p(W - 50, 122)], radius=10 * S, outline=white(220), width=int(2 * S))
    # trous des bobines
    for cx in (84, 196):
        d.ellipse([p(cx - 26, 94 - 26), p(cx + 26, 94 + 26)], outline=white(60), width=int(1 * S))
    # bande qui passe en bas de la fenetre
    d.line([p(84, 120), p(196, 120)], fill=white(90), width=int(1.2 * S))
    # trapeze du bas avec ses trous de guidage
    d.line([p(62, H - 4), p(78, 138), p(W - 78, 138), p(W - 62, H - 4)], fill=white(200), width=int(2 * S), joint='curve')
    for cx in (100, 140, 180):
        d.ellipse([p(cx - 4, 150), p(cx + 4, 158)], outline=white(160), width=int(1.2 * S))
    # vis aux coins
    for x, y in ((16, 16), (W - 16, 16), (16, H - 16), (W - 16, H - 16)):
        d.ellipse([p(x - 3, y - 3), p(x + 3, y + 3)], fill=white(140))
    save(im, 'T_UI_Cassette', W * 2, H * 2)


def reel():
    R = 48
    im, d = canvas(R, R)
    c = R / 2
    d.ellipse([p(c - 21, c - 21), p(c + 21, c + 21)], outline=white(), width=int(2 * S))
    d.ellipse([p(c - 9, c - 9), p(c + 9, c + 9)], outline=white(), width=int(2 * S))
    # six dents dans le moyeu, c'est ce qui montre la rotation
    for i in range(6):
        a = math.radians(i * 60)
        x0, y0 = c + math.cos(a) * 4, c + math.sin(a) * 4
        x1, y1 = c + math.cos(a) * 9, c + math.sin(a) * 9
        d.line([p(x0, y0), p(x1, y1)], fill=white(), width=int(2 * S))
    # trois rayons entre le moyeu et le bord
    for i in range(3):
        a = math.radians(i * 120 + 30)
        d.line([p(c + math.cos(a) * 11, c + math.sin(a) * 11), p(c + math.cos(a) * 19, c + math.sin(a) * 19)],
               fill=white(170), width=int(3 * S))
    save(im, 'T_UI_Reel', R * 2, R * 2)


def tape_pack():
    R = 48
    im, d = canvas(R, R)
    c = R / 2
    d.ellipse([p(c - 23.5, c - 23.5), p(c + 23.5, c + 23.5)], fill=white(255))
    # fines spires de bande
    for r in range(10, 23, 3):
        d.ellipse([p(c - r, c - r), p(c + r, c + r)], outline=(0, 0, 0, 40), width=int(0.6 * S))
    save(im, 'T_UI_TapePack', R * 2, R * 2)


def skip(name, forward):
    im, d = canvas(64, 64)
    sx = 1 if forward else -1
    c = 32
    tri = [p(c - sx * 14, 16), p(c + sx * 10, 32), p(c - sx * 14, 48)]
    d.polygon(tri, fill=white())
    bx = c + sx * 12
    d.rectangle([p(min(bx, bx + sx * 6), 16), p(max(bx, bx + sx * 6), 48)], fill=white())
    save(im, name, 64, 64)


if __name__ == '__main__':
    cassette()
    reel()
    tape_pack()
    skip('T_UI_Prev', False)
    skip('T_UI_Next', True)
