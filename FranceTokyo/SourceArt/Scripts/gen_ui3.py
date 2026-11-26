"""STEEZY menu B (CommonUI) - UI art generator.
Outputs to ./out3 :
  T_UI_MenuBackdrop        1920x1080 opaque backdrop (ground + red mist + vignette)
  T_UI_MenuButton_Selected 1056x108  red hexagon + side diamonds (display 528x54)
  T_UI_Diamond             32x32     small diamond (display 8x8 / 10x10)
  Placeholder input icons (to be replaced by Fab assets):
  T_Key_UpDown, T_Key_Enter, T_Key_Escape, T_Pad_DPad, T_Pad_FaceBottom, T_Pad_FaceRight
"""
import os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out3')
os.makedirs(OUT, exist_ok=True)
MIST = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'out2', 'T_UI_RedMist.png')
FONT_MENU = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, '..', 'Fonts', 'KH', 'KHMenu.otf')
FONT_SANS = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

ACCENT = (200, 16, 46)
GROUND = (11, 7, 8)
INK = (243, 233, 234)


def backdrop():
    W, H = 1920, 1080
    base = Image.new('RGBA', (W, H), GROUND + (255,))
    mist = Image.open(MIST).convert('RGBA').resize((W, H))

    def faded(img, k):
        a = np.asarray(img).astype(np.float32)
        a[..., 3] *= k
        return Image.fromarray(a.astype(np.uint8), 'RGBA')

    base.alpha_composite(faded(mist, 0.9))
    base.alpha_composite(faded(mist.transpose(Image.ROTATE_180), 0.54))
    # vignette : radial-gradient(ellipse 60% 70% at 50% 48%, transparent 40%, rgba(0,0,0,.7) 100%)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    d = np.sqrt(((xx - 0.5 * W) / (0.6 * W)) ** 2 + ((yy - 0.48 * H) / (0.7 * H)) ** 2)
    k = np.clip((d - 0.4) / 0.6, 0, 1) * 0.7
    rgb = np.asarray(base).astype(np.float32)[..., :3] * (1 - k[..., None])
    Image.fromarray(rgb.astype(np.uint8), 'RGB').save(os.path.join(OUT, 'T_UI_MenuBackdrop.png'))


def hexa(d, x0, y0, x1, y1, cut, fill):
    my = (y0 + y1) / 2
    d.polygon([(x0, my), (x0 + cut, y0), (x1 - cut, y0), (x1, my), (x1 - cut, y1), (x0 + cut, y1)], fill=fill)


def diamond(d, cx, cy, r, fill):
    d.polygon([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)], fill=fill)


def button_selected():
    S = 8  # supersample, final = 2x
    W, H = 528, 54
    im = Image.new('RGBA', (W * S, H * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    x0, x1 = 44 * S, 484 * S
    hexa(d, x0, 0, x1, H * S, 28 * S, ACCENT + (255,))
    dark = tuple(int(c * 0.72) for c in ACCENT) + (255,)
    hexa(d, x0 + 3 * S, 3 * S, x1 - 3 * S, (H - 3) * S, 27 * S, dark)
    hexa(d, x0 + 6 * S, 6 * S, x1 - 6 * S, (H - 6) * S, 25 * S, ACCENT + (255,))
    r = 7.07 * S
    diamond(d, 15 * S, H * S / 2, r, ACCENT + (255,))
    diamond(d, 513 * S, H * S / 2, r, ACCENT + (255,))
    im.resize((W * 2, H * 2), Image.LANCZOS).save(os.path.join(OUT, 'T_UI_MenuButton_Selected.png'))


def small_diamond():
    S = 8
    im = Image.new('RGBA', (32 * S, 32 * S), (0, 0, 0, 0))
    diamond(ImageDraw.Draw(im), 16 * S, 16 * S, 15 * S, (255, 255, 255, 255))
    im.resize((32, 32), Image.LANCZOS).save(os.path.join(OUT, 'T_UI_Diamond.png'))


def keycap(name, w, h, draw_fn):
    """Outlined rounded keycap, display size w x h, exported at 4x."""
    S, K = 4, 4
    im = Image.new('RGBA', (w * S * K, h * S * K), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    u = S * K
    d.rounded_rectangle([u * 0.75, u * 0.75, w * u - u * 0.75, h * u - u * 0.75], radius=4 * u,
                        outline=INK + (150,), width=int(1.25 * u), fill=(243, 233, 234, 18))
    draw_fn(d, w * u, h * u, u)
    im.resize((w * S, h * S), Image.LANCZOS).save(os.path.join(OUT, name + '.png'))


def text_center(d, W, H, u, txt, font_path, px):
    f = ImageFont.truetype(font_path, int(px * u))
    b = d.textbbox((0, 0), txt, font=f)
    d.text(((W - (b[2] - b[0])) / 2 - b[0], (H - (b[3] - b[1])) / 2 - b[1]), txt, font=f, fill=INK + (255,))


def arrow(d, cx, cy, u, up):
    s = 4.2 * u
    stem = 1.1 * u
    sign = -1 if up else 1
    d.polygon([(cx, cy + sign * s), (cx - s * 0.8, cy + sign * s * 0.1), (cx + s * 0.8, cy + sign * s * 0.1)], fill=INK + (255,))
    d.rectangle([cx - stem / 2, min(cy - sign * s, cy + sign * s * 0.1), cx + stem / 2, max(cy - sign * s, cy + sign * s * 0.1)], fill=INK + (255,))


def round_button(name, letter):
    S, K, w = 4, 4, 28
    u = S * K
    im = Image.new('RGBA', (w * u, w * u), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse([u * 0.75, u * 0.75, w * u - u * 0.75, w * u - u * 0.75], outline=INK + (150,), width=int(1.25 * u), fill=(243, 233, 234, 18))
    text_center(d, w * u, w * u, u, letter, FONT_SANS, 14)
    im.resize((w * S, w * S), Image.LANCZOS).save(os.path.join(OUT, name + '.png'))


def dpad():
    S, K, w = 4, 4, 28
    u = S * K
    im = Image.new('RGBA', (w * u, w * u), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    c = w * u / 2
    a, b = 4.2 * u, 12.5 * u
    col = INK + (255,)
    d.rounded_rectangle([c - a, c - b, c + a, c + b], radius=1.5 * u, outline=INK + (150,), width=int(1.25 * u), fill=(243, 233, 234, 18))
    d.rounded_rectangle([c - b, c - a, c + b, c + a], radius=1.5 * u, outline=INK + (150,), width=int(1.25 * u), fill=(243, 233, 234, 18))
    d.rectangle([c - a + 1.25 * u, c - a + 1.25 * u, c + a - 1.25 * u, c + a - 1.25 * u], fill=(30, 24, 26, 255))
    t = 2.6 * u
    d.polygon([(c, c - b + 2.2 * u), (c - t, c - b + 2.2 * u + t * 1.2), (c + t, c - b + 2.2 * u + t * 1.2)], fill=col)
    d.polygon([(c, c + b - 2.2 * u), (c - t, c + b - 2.2 * u - t * 1.2), (c + t, c + b - 2.2 * u - t * 1.2)], fill=col)
    im.resize((w * S, w * S), Image.LANCZOS).save(os.path.join(OUT, 'T_Pad_DPad.png'))


if __name__ == '__main__':
    backdrop()
    button_selected()
    small_diamond()
    keycap('T_Key_UpDown', 52, 28, lambda d, W, H, u: (arrow(d, W * 0.33, H / 2, u, True), arrow(d, W * 0.67, H / 2, u, False)))
    keycap('T_Key_Enter', 76, 28, lambda d, W, H, u: text_center(d, W, H, u, 'Entrée', FONT_MENU, 15))
    keycap('T_Key_Escape', 70, 28, lambda d, W, H, u: text_center(d, W, H, u, 'Échap', FONT_MENU, 15))
    round_button('T_Pad_FaceBottom', 'A')
    round_button('T_Pad_FaceRight', 'B')
    dpad()
    print('ok', sorted(os.listdir(OUT)))
