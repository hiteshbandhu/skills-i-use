#!/usr/bin/env python3
"""2.5D parallax from a depth map: push-in, orbit, dolly zoom, text placed IN the scene.

Depth maps come from  vision/bin/depth <DepthAnythingV2SmallF16.mlpackage> fr/<id> depth/<id>
(16-bit PNG, near = bright). Import the functions, or try one shot:

  parallax.py <project> <clip> <start_frame> <frames> <out_dir> --move push|orbit|dolly [--text "OURS GO DEEPER"]

Lessons: smooth depth over 5 frames (raw depth flickers); dilate + blur it so edges
do not tear; keep moves small (zoom <= 0.16, shift <= 90 px); add haze on far depth
for real air; text sits at a depth plane and anything nearer occludes it.
"""
import argparse, os
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
GX, GY = np.meshgrid(np.arange(W, dtype=np.float32), np.arange(H, dtype=np.float32))
FONT = next((f for f in ['/System/Library/Fonts/Supplemental/Futura.ttc', '/System/Library/Fonts/Supplemental/Impact.ttf']
             if os.path.exists(f)), None)

def load_depth(project, clip, i, n):
    acc, ws = None, 0
    for k, w in [(-2, 1), (-1, 2), (0, 4), (1, 2), (2, 1)]:            # temporal smoothing
        p = f'{project}/depth/{clip}/{min(max(i + k, 0), n - 1):04d}.png'
        if not os.path.exists(p): continue
        d = cv2.imread(p, cv2.IMREAD_UNCHANGED)
        if d.ndim == 3: d = d[..., 0]                                  # some PNG readers give 3 channels
        d = d.astype(np.float32) / (65535.0 if d.dtype == np.uint16 else 255.0)
        acc = d * w if acc is None else acc + d * w; ws += w
    d = cv2.resize(acc / ws, (W, H))
    lo, hi = np.percentile(d, 2), np.percentile(d, 98); d = np.clip((d - lo) / (hi - lo + 1e-6), 0, 1)
    return cv2.GaussianBlur(cv2.dilate(d, np.ones((9, 9), np.uint8)), (0, 0), 4)

def warp(img, d, tx=0.0, ty=0.0, zoom=0.0, dolly=None, focus=0.5):
    """Per-pixel shift ~ (depth - focus). dolly: subject plane fixed, background scales (Vertigo)."""
    cx, cy = W / 2, H * 0.45
    s = 1 + (dolly * (focus - d) if dolly is not None else zoom * d)
    mx = (cx + (GX - cx) / s - tx * (d - focus)).astype(np.float32)   # remap maps must be float32
    my = (cy + (GY - cy) / s - ty * (d - focus)).astype(np.float32)
    out = cv2.remap(img, mx, my, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    return out, cv2.remap(d, mx, my, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)

def haze(img, d, amt=0.3, col=(205, 214, 226)):
    f = ((1 - d) ** 2 * amt)[..., None]; return (img * (1 - f) + np.array(col, np.float32) * f).astype(np.uint8)

def text_mask(txt, cy, maxw=980, size=230):
    im = Image.new('L', (W, H), 0); dr = ImageDraw.Draw(im)
    f = ImageFont.truetype(FONT, size, index=4) if FONT and FONT.endswith('.ttc') else ImageFont.truetype(FONT, size)
    while f.getlength(txt) > maxw:
        size -= 6; f = ImageFont.truetype(FONT, size, index=4) if FONT.endswith('.ttc') else ImageFont.truetype(FONT, size)
    dr.text((W / 2, cy), txt, font=f, fill=255, anchor='mm'); return np.array(im, np.float32) / 255

def place_text(img, dw, mask, plane, col=(255, 255, 255)):
    """Text lives at depth `plane` (0 far .. 1 near); nearer pixels occlude it. plane > 1 = always on top."""
    vis = mask * np.clip((plane - dw) / 0.04 + 0.5, 0, 1); out = img.astype(np.float32)
    out *= 1 - (cv2.GaussianBlur(vis, (0, 0), 14) * 0.45)[..., None]
    out = out * (1 - vis[..., None]) + np.array(col, np.float32) * vis[..., None]
    return np.clip(out, 0, 255).astype(np.uint8)

ease = lambda x: 0.5 - 0.5 * np.cos(np.pi * min(max(x, 0), 1))

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('project'); ap.add_argument('clip'); ap.add_argument('start', type=int); ap.add_argument('frames', type=int)
    ap.add_argument('out'); ap.add_argument('--move', default='push'); ap.add_argument('--text', default='')
    ap.add_argument('--plane', type=float, default=0.35)
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
    n = len(os.listdir(f'{a.project}/fr/{a.clip}'))
    for k in range(a.frames):
        i = min(a.start + k, n - 1); q = ease(k / max(1, a.frames - 1))
        img = cv2.imread(f'{a.project}/fr/{a.clip}/{i:04d}.jpg'); d = load_depth(a.project, a.clip, i, n)
        if a.move == 'dolly': o, dw = warp(img, d, dolly=0.45 * q, focus=0.62)
        elif a.move == 'orbit': o, dw = warp(img, d, tx=-90 + 180 * q, zoom=0.05)
        else: o, dw = warp(img, d, tx=-30 + 60 * q, zoom=0.12 * q)
        o = haze(o, dw)
        if a.text: o = place_text(o, dw, text_mask(a.text, 560), a.plane)
        cv2.imwrite(f'{a.out}/{k:05d}.jpg', o, [cv2.IMWRITE_JPEG_QUALITY, 93])
    print('frames ->', a.out)
