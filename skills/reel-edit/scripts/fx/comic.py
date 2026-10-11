#!/usr/bin/env python3
"""Live comic-book look for real footage (not a cartoon filter: ink, flat colour, halftone).

  comic.py <frames_dir> <out_dir> [--matte_dir mk/<id>] [--step 1]
Bilateral smoothing x3 -> saturation up + 4-level posterise -> colour quantise ->
45-degree halftone in shadows -> adaptive-threshold ink lines + a thick outline
around the subject matte. Works best at 720x1280 then upscaled; 12 fps
(step=2/3) reads as drawn. Pair with panels, SFX lettering and a guided-view camera.
"""
import argparse, os
import cv2, numpy as np

W, H = 720, 1280
YY, XX = np.mgrid[0:H, 0:W]

def halftone(L, step=7):
    u = (XX + YY) / np.sqrt(2) / step; v = (XX - YY) / np.sqrt(2) / step
    d = np.hypot(u - np.round(u), v - np.round(v)); return (d < np.clip((0.55 - L) / 0.55, 0, 1) * 0.62).astype(np.float32)

def comic(img, matte=None):
    im = cv2.resize(img, (W, H), interpolation=cv2.INTER_AREA); sm = im.copy()
    for _ in range(3): sm = cv2.bilateralFilter(sm, 9, 40, 7)
    hsv = cv2.cvtColor(sm, cv2.COLOR_BGR2HSV).astype(np.float32); hsv[..., 1] = np.clip(hsv[..., 1] * 1.45, 0, 255)
    v = hsv[..., 2] / 255; hsv[..., 2] = np.clip((0.35 * v + 0.65 * np.clip(np.round(v * 4) / 4, .08, 1)) * 255 * 1.06, 0, 255)
    col = np.round(cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR).astype(np.float32) / 32) * 32 + 8
    col *= 1 - 0.55 * halftone(cv2.cvtColor(sm, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255)[..., None]
    g = cv2.medianBlur(cv2.cvtColor(im, cv2.COLOR_BGR2GRAY), 7)
    lines = (cv2.adaptiveThreshold(g, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4) == 0).astype(np.uint8)
    lines = cv2.morphologyEx(lines, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8))
    if matte is not None:
        m = (cv2.resize(matte, (W, H)) > 110).astype(np.uint8)
        lines = np.maximum(lines, cv2.dilate(m, np.ones((9, 9), np.uint8)) - cv2.erode(m, np.ones((3, 3), np.uint8)))
    col[lines > 0] = (22, 18, 16)
    return np.clip(col, 0, 255).astype(np.uint8)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('src'); ap.add_argument('out')
    ap.add_argument('--matte_dir'); ap.add_argument('--step', type=int, default=1)
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
    for i, f in enumerate(sorted(os.listdir(a.src))):
        if i % a.step: continue
        mp = os.path.join(a.matte_dir, f[:-4] + '.png') if a.matte_dir else None
        mt = cv2.imread(mp, 0) if mp and os.path.exists(mp) else None
        cv2.imwrite(os.path.join(a.out, f), comic(cv2.imread(os.path.join(a.src, f)), mt), [cv2.IMWRITE_JPEG_QUALITY, 92])
    print('comic ->', a.out)
