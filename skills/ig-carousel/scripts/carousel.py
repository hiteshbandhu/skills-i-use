#!/usr/bin/env python3
"""Render an Instagram carousel from a JSON spec, designed as ONE panorama and sliced into slides.

  carousel.py spec.json out_dir [--preview]

Coordinates are in panorama pixels: x runs across every slide (slide i spans
[i*W, (i+1)*W)), so stickers, tape and torn paper can bleed across slide edges,
which is what makes people swipe. Output: slide_01.jpg ... slide_NN.jpg (4:5,
1080x1350 by default) plus sheet.jpg (all slides side by side) for review.

spec = {
  "size": [1080, 1350], "slides": 7, "seed": 3, "grain": 0.07,
  "fonts": {"head": "/path/Font.ttc#4", "label": "/path/Type.ttc#5"},
  "backgrounds": ["#FF5A3C", "#2D46E8", ...],          # one flat colour per slide
  "elements": [ ... drawn in order ... ]
}
Element types (all positions are centres unless noted):
  sticker  {src, matte?, x, y, h, rot, border=16, shadow=true, crop=[x0,y0,x1,y1]?}
           cut-out photo: alpha = matte PNG (white = keep) or the image's own alpha
  text     {text, x, y, size | fit_w, color, font="head", rot=0, anchor="mm", box?, pad=18, tracking=0}
  label    {text, x, y, size, color="#141414", paper="#F4EFE6", rot}   typewriter text on a paper strip
  tape     {x, y, w=170, h=52, rot, color="#EDE3C8"}                    translucent torn-edge tape
  torn     {x0, x1, y, h, color, rot=0}                                 torn paper band (can span slides)
  bubble   {x, y, w, h, text, color="#F4EFE6", ink="#141414", tail=[dx,dy]}
  dots     {x, y, w, h, color, step=14}                                 halftone patch
  arrow    {x0, y0, x1, y1, color, width=10}                            hand-drawn swipe arrow
  pill     {text, x, y, size, color, bg, pad=[40,22]}                   CTA button
"""
import json, math, os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

def rgb(h): h = h.lstrip('#'); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

class C:
    def __init__(self, spec, base):
        self.s = spec; self.base = base
        self.W, self.H = spec.get('size', [1080, 1350]); self.N = spec['slides']
        self.rng = np.random.default_rng(spec.get('seed', 3))
        self.img = Image.new('RGBA', (self.W * self.N, self.H))
        bgs = spec.get('backgrounds', ['#F4EFE6'] * self.N)
        d = ImageDraw.Draw(self.img)
        for i, c in enumerate(bgs): d.rectangle([i * self.W, 0, (i + 1) * self.W, self.H], fill=rgb(c) + (255,))

    def font(self, key, size):
        f = self.s.get('fonts', {}).get(key, key)
        path, _, idx = f.partition('#')
        return ImageFont.truetype(path, int(size), index=int(idx or 0))

    def path(self, p): return p if os.path.isabs(p) else os.path.join(self.base, p)

    def paste(self, layer, cx, cy, rot=0, shadow=False):
        if rot: layer = layer.rotate(rot, expand=True, resample=Image.BICUBIC)
        x, y = int(cx - layer.width / 2), int(cy - layer.height / 2)
        if shadow:
            a = layer.split()[3]; sh = Image.new('RGBA', layer.size, (0, 0, 0, 0)); sh.putalpha(a.point(lambda v: int(v * .38)))
            sh = sh.filter(ImageFilter.GaussianBlur(14)); self._comp(sh, x + 14, y + 22)
        self._comp(layer, x, y)

    def _comp(self, layer, x, y):
        # alpha_composite needs non-negative offsets: crop the layer instead
        sx, sy = max(0, -x), max(0, -y)
        if sx >= layer.width or sy >= layer.height: return
        self.img.alpha_composite(layer.crop((sx, sy, layer.width, layer.height)), (max(0, x), max(0, y)))

    # ---- elements
    def sticker(self, e):
        im = Image.open(self.path(e['src'])).convert('RGBA')
        if e.get('matte'):
            m = Image.open(self.path(e['matte'])).convert('L').resize(im.size)
            im.putalpha(m.point(lambda v: 255 if v > 110 else 0).filter(ImageFilter.GaussianBlur(1.2)))
        if e.get('crop'): im = im.crop(tuple(e['crop']))
        bb = im.split()[3].getbbox(); im = im.crop(bb)
        s = e['h'] / im.height; im = im.resize((max(1, int(im.width * s)), int(im.height * s)), Image.LANCZOS)
        b = int(e.get('border', 16)); pad = b + 4
        canvas = Image.new('RGBA', (im.width + 2 * pad, im.height + 2 * pad), (0, 0, 0, 0))
        a = Image.new('L', canvas.size, 0); a.paste(im.split()[3], (pad, pad))
        border = a.filter(ImageFilter.MaxFilter(2 * (b // 2) + 1)).filter(ImageFilter.GaussianBlur(.8))
        canvas.paste(Image.new('RGBA', canvas.size, (250, 248, 242, 255)), (0, 0), border)
        canvas.alpha_composite(im, (pad, pad))
        self.paste(canvas, e['x'], e['y'], e.get('rot', 0), e.get('shadow', True))

    def text(self, e):
        size = e.get('size', 200); f = self.font(e.get('font', 'head'), size)
        if e.get('fit_w'):
            size = size * e['fit_w'] / max(1, f.getlength(e['text'])); f = self.font(e.get('font', 'head'), size)
        l, t, r, b = f.getbbox(e['text']); pad = int(e.get('pad', 18)) if e.get('box') else 6
        lay = Image.new('RGBA', (r - l + 2 * pad, b - t + 2 * pad), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        if e.get('box'): d.rectangle([0, 0, lay.width, lay.height], fill=rgb(e['box']) + (255,))
        d.text((pad - l, pad - t), e['text'], font=f, fill=rgb(e.get('color', '#141414')) + (255,))
        self.paste(lay, e['x'], e['y'], e.get('rot', 0), e.get('shadow', False))

    def label(self, e):
        self.text(dict(e, font=e.get('font', 'label'), box=e.get('paper', '#F4EFE6'), color=e.get('color', '#141414'), pad=e.get('pad', 16), shadow=True))

    def tape(self, e):
        w, h = int(e.get('w', 170)), int(e.get('h', 52)); lay = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        teeth = lambda n: [(i * w / n, self.rng.uniform(0, 6)) for i in range(n + 1)]
        top = teeth(12); bot = [(x, h - y) for x, y in teeth(12)][::-1]
        d.polygon(top + bot, fill=rgb(e.get('color', '#EDE3C8')) + (205,))
        self.paste(lay, e['x'], e['y'], e.get('rot', 0), False)

    def torn(self, e):
        x0, x1, y, h = int(e['x0']), int(e['x1']), int(e['y']), int(e['h']); w = x1 - x0
        lay = Image.new('RGBA', (w, h + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        xs = np.arange(0, w + 12, 12)
        top = [(x, 20 + self.rng.uniform(-9, 9)) for x in xs]; bot = [(x, h + 20 + self.rng.uniform(-9, 9)) for x in xs][::-1]
        d.polygon(top + bot, fill=rgb(e.get('color', '#F4EFE6')) + (255,))
        self.paste(lay, x0 + w / 2, y, e.get('rot', 0), True)

    def bubble(self, e):
        w, h = int(e['w']), int(e['h']); tx, ty = e.get('tail', [-w * .25, h * .55])
        lay = Image.new('RGBA', (w + 120, h + 120), (0, 0, 0, 0)); d = ImageDraw.Draw(lay); cx, cy = (w + 120) / 2, (h + 120) / 2
        col = rgb(e.get('color', '#F4EFE6')) + (255,)
        d.ellipse([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], fill=col)
        d.polygon([(cx + tx * .3 - 26, cy + h * .3), (cx + tx, cy + ty), (cx + tx * .3 + 26, cy + h * .35)], fill=col)
        f = self.font('head', h * .55); d.text((cx, cy), e['text'], font=f, fill=rgb(e.get('ink', '#141414')) + (255,), anchor='mm')
        self.paste(lay, e['x'], e['y'], e.get('rot', 0), True)

    def dots(self, e):
        w, h, st = int(e['w']), int(e['h']), int(e.get('step', 14)); lay = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        for yy in range(0, h, st):
            for xx in range(0, w, st):
                r = st * .38 * (1 - ((xx / w) ** 1.3)); d.ellipse([xx - r, yy - r, xx + r, yy + r], fill=rgb(e['color']) + (255,))
        self.paste(lay, e['x'], e['y'], e.get('rot', 0), False)

    def arrow(self, e):
        d = ImageDraw.Draw(self.img); c = rgb(e.get('color', '#141414')) + (255,); wd = int(e.get('width', 10))
        x0, y0, x1, y1 = e['x0'], e['y0'], e['x1'], e['y1']
        pts = [(x0 + (x1 - x0) * k / 20, y0 + (y1 - y0) * k / 20 + math.sin(k / 20 * math.pi) * -30) for k in range(21)]
        d.line(pts, fill=c, width=wd, joint='curve')
        a = math.atan2(pts[-1][1] - pts[-3][1], pts[-1][0] - pts[-3][0])
        for s in (2.6, -2.6): d.line([pts[-1], (x1 - 46 * math.cos(a + s / 6 * math.pi / 2.6 * 1.1), y1 - 46 * math.sin(a + s / 6 * math.pi / 2.6 * 1.1))], fill=c, width=wd)

    def pill(self, e):
        f = self.font(e.get('font', 'head'), e.get('size', 110)); px, py = e.get('pad', [40, 22])
        l, t, r, b = f.getbbox(e['text']); w, h = r - l + 2 * px, b - t + 2 * py
        lay = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        d.rounded_rectangle([0, 0, w - 1, h - 1], radius=h // 2, fill=rgb(e.get('bg', '#141414')) + (255,))
        d.text((px - l, py - t), e['text'], font=f, fill=rgb(e.get('color', '#FFFFFF')) + (255,))
        self.paste(lay, e['x'], e['y'], e.get('rot', 0), True)

    def render(self, out, preview=False):
        for e in self.s['elements']: getattr(self, e['type'])(e)
        g = self.s.get('grain', .07)
        if g:   # paper grain + fibres, multiplied over everything
            n = self.rng.standard_normal((self.H, self.W * self.N)).astype(np.float32)
            n = np.array(Image.fromarray(((n * 18) + 128).clip(0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(.7)), np.float32)
            base = np.array(self.img.convert('RGB'), np.float32); base *= (1 + (n[..., None] - 128) / 255 * g * 4)
            self.img = Image.fromarray(base.clip(0, 255).astype(np.uint8)).convert('RGBA')
        os.makedirs(out, exist_ok=True); slides = []
        for i in range(self.N):
            sl = self.img.crop((i * self.W, 0, (i + 1) * self.W, self.H)).convert('RGB'); slides.append(sl)
            sl.save(os.path.join(out, f'slide_{i + 1:02d}.jpg'), quality=95, subsampling=0)
        sh = Image.new('RGB', (self.N * 324 + (self.N - 1) * 12, 405), (30, 30, 30))
        for i, sl in enumerate(slides): sh.paste(sl.resize((324, 405)), (i * 336, 0))
        sh.save(os.path.join(out, 'sheet.jpg'), quality=90)
        print(f'{self.N} slides -> {out}  (sheet.jpg for review)')

if __name__ == '__main__':
    if len(sys.argv) < 3: sys.exit(__doc__)
    spec = json.load(open(sys.argv[1]))
    C(spec, os.path.dirname(os.path.abspath(sys.argv[1]))).render(sys.argv[2], '--preview' in sys.argv)
