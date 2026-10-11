#!/usr/bin/env python3
"""Realistic multiplicity ("clone the room"): the same person several times in one
handheld shot, each clone locked to the room and correctly occluded.

Needs: fr/<clip> frames, mk/<clip> person mattes (vision/bin/seg), track/<clip>.json (camtrack.py).

  from clone import comp
  clones = [dict(off=63, dx=-540, dy=70, s=1.1, ax=540, ay=1400, front=True, xr=[150, 800]),
            dict(off=120, dx=300, dy=-260, s=0.66, ax=540, ay=1400)]
  frame = comp(project, '05', plate_frame_index, clones)

Clone fields: off = time offset in frames (different moment = different expression/gesture);
dx, dy, s = placement in room coords, scaled about anchor (ax, ay); flip = mirror;
front = in front of the real people (else behind them); xr = keep only matte pixels in an
x-window (drops a neighbour who touches the subject); cut_below = hide below a y (table edge).
Lessons: far clones smaller + slightly hazed; the real people of the plate are composited
back over far clones; a soft contact shadow under near clones; give each clone its own
voice line panned to its side (mix.py "pan").
"""
import json, os
import cv2, numpy as np

W, H = 1080, 1920
_T = {}

def T(project, clip):
    if (project, clip) not in _T: _T[project, clip] = np.array(json.load(open(f'{project}/track/{clip}.json')))
    return _T[project, clip]

def nfr(project, clip): return len(os.listdir(f'{project}/fr/{clip}'))
def frame(project, clip, i): return cv2.imread(f'{project}/fr/{clip}/{i:04d}.jpg')

def matte(project, clip, i, largest=True):
    m = cv2.resize(cv2.imread(f'{project}/mk/{clip}/{i:04d}.png', 0), (W, H))
    if largest:
        n, lab, st, _ = cv2.connectedComponentsWithStats((m > 100).astype(np.uint8), 8)
        if n > 1: m = np.where(lab == 1 + np.argmax(st[1:, cv2.CC_STAT_AREA]), m, 0).astype(np.uint8)
    return cv2.GaussianBlur(m, (5, 5), 0).astype(np.float32) / 255

def A3(M): return np.vstack([np.array(M, np.float32), [0, 0, 1]])

def place(dx, dy, s, ax, ay, flip=False):
    F = np.float32([[-1 if flip else 1, 0, 2 * ax if flip else 0], [0, 1, 0], [0, 0, 1]])
    S = np.float32([[s, 0, ax * (1 - s) + dx], [0, s, ay * (1 - s) + dy], [0, 0, 1]])
    return S @ F

def pingpong(i, n):
    p = i % (2 * n); return p if p < n else 2 * n - 1 - p

def comp(project, clip, pf, clones):
    plate = frame(project, clip, pf).astype(np.float32); out = plate.copy(); Tp = A3(T(project, clip)[pf]); layers = []
    for c in clones:
        g = pingpong(pf + c['off'], nfr(project, clip))
        img = frame(project, clip, g).astype(np.float32); m = matte(project, clip, g)
        if 'xr' in c:
            win = np.zeros(W, np.float32); win[c['xr'][0]:c['xr'][1]] = 1
            m *= cv2.GaussianBlur(np.repeat(win[None], H, 0), (41, 1), 0)
        M = Tp @ place(c['dx'], c['dy'], c['s'], c['ax'], c['ay'], c.get('flip', False)) @ np.linalg.inv(A3(T(project, clip)[g]))
        wi = cv2.warpAffine(img, M[:2], (W, H)); wm = cv2.warpAffine(m, M[:2], (W, H))
        if c.get('cut_below'): wm[int(c['cut_below']):] = 0
        if c['s'] < 0.9: wi = wi * (0.9 + 0.1 * c['s']) + 12 * (1 - c['s'])      # depth haze
        layers.append((c['s'], c.get('front', False), wi, wm))
    for s, front, wi, wm in sorted([l for l in layers if not l[1]], key=lambda l: l[0]):
        out = out * (1 - wm[..., None]) + wi * wm[..., None]
    pm = matte(project, clip, pf, largest=False)                                   # real people occlude far clones
    out = out * (1 - pm[..., None]) + plate * pm[..., None]
    for s, front, wi, wm in [l for l in layers if l[1]]:
        out *= 1 - (cv2.GaussianBlur(wm, (0, 0), 18) * 0.25)[..., None]            # contact shadow
        out = out * (1 - wm[..., None]) + wi * wm[..., None]
    return np.clip(out, 0, 255).astype(np.uint8)
