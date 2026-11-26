"""STEEZY lecteur de sons de l'ecran Souvenirs, generateur des visuels.
Sorties dans ../UI/v5, en blanc sur fond transparent, la couleur est donnee dans Unreal.
  T_UI_Play        64x64    triangle lecture (affiche en 22x22)
  T_UI_Pause       64x64    deux barres pause (affiche en 22x22)
  T_UI_PlayFrame   128x128  losange creux autour du bouton (affiche en 56x56)
"""
import os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'UI', 'v5')
os.makedirs(OUT, exist_ok=True)
WHITE = (255, 255, 255, 255)
S = 8  # sur-echantillonnage pour des bords propres


def save(im, name, size):
    im.resize((size, size), Image.LANCZOS).save(os.path.join(OUT, name + '.png'))


def play():
    W = 64 * S
    im = Image.new('RGBA', (W, W), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    # triangle un peu decale a droite pour paraitre centre a l'oeil
    left, right, top, bottom = 18 * S, 52 * S, 12 * S, 52 * S
    d.polygon([(left, top), (right, (top + bottom) / 2), (left, bottom)], fill=WHITE)
    save(im, 'T_UI_Play', 64)


def pause():
    W = 64 * S
    im = Image.new('RGBA', (W, W), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for x in (17, 37):
        d.rectangle([x * S, 13 * S, (x + 10) * S, 51 * S], fill=WHITE)
    save(im, 'T_UI_Pause', 64)


def frame():
    W = 128 * S
    im = Image.new('RGBA', (W, W), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    c, r, w = 64 * S, 48 * S, int(4.5 * S)
    pts = [(c, c - r), (c + r, c), (c, c + r), (c - r, c), (c, c - r)]
    d.line(pts, fill=WHITE, width=w, joint='curve')
    # petits traits qui partent des pointes gauche et droite, comme les losanges du menu
    for sx in (-1, 1):
        d.line([(c + sx * (r + 5 * S), c), (c + sx * (r + 14 * S), c)], fill=WHITE, width=int(3 * S))
    save(im, 'T_UI_PlayFrame', 128)


if __name__ == '__main__':
    play()
    pause()
    frame()
