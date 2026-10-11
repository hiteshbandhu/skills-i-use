#!/usr/bin/env python3
"""Track the camera (handheld shake/pan) from the BACKGROUND only, so composited
things stay locked to the room.

  camtrack.py <project> <clip> [<clip> ...]   -> <project>/track/<clip>.json  (per-frame 2x3 affine, frame0 -> frame i)

People are masked out using mk/<clip>/NNNN.png when present (vision/bin/seg),
ORB features + RANSAC estimateAffinePartial2D (rotation, scale, shift), then a
7-frame moving average. Prints the pan/scale range so you know how much it moves.
"""
import json, os, sys
import cv2, numpy as np

def track(project, clip, work=(540, 960)):
    fd = f'{project}/fr/{clip}'; fs = sorted(os.listdir(fd)); sx = 1080 / work[0]
    orb = cv2.ORB_create(3000); bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    def load(f):
        g = cv2.resize(cv2.imread(f'{fd}/{f}', 0), work); m = np.full(g.shape, 255, np.uint8)
        mp = f'{project}/mk/{clip}/{f[:-4]}.png'
        if os.path.exists(mp):
            pm = cv2.resize(cv2.imread(mp, 0), work); m[cv2.dilate((pm > 60).astype(np.uint8), np.ones((25, 25))) > 0] = 0
        return orb.detectAndCompute(g, m)
    k0, d0 = load(fs[0]); T = []
    for f in fs:
        k, d = load(f); M = None
        if d is not None and len(k) > 20:
            mt = sorted(bf.match(d0, d), key=lambda x: x.distance)[:600]
            if len(mt) > 20:
                A = np.float32([k0[x.queryIdx].pt for x in mt]); B = np.float32([k[x.trainIdx].pt for x in mt])
                M, _ = cv2.estimateAffinePartial2D(A, B, method=cv2.RANSAC, ransacReprojThreshold=2.5)
        if M is not None:                               # reject wild solves (few background points)
            sc = float(np.hypot(M[0, 0], M[1, 0]))
            if not 0.8 < sc < 1.25 or np.abs(M[:, 2]).max() > work[0] * 0.4: M = None
        if M is None:                                   # lost track: hold the last pose
            T.append(T[-1].copy() if T else np.float32([[1, 0, 0], [0, 1, 0]])); continue
        M = np.array(M, np.float32); M[:, 2] *= sx; T.append(M)   # shifts back to full-res pixels
    A = np.array(T); S = np.array([A[max(0, i - 3):i + 4].mean(0) for i in range(len(A))])
    os.makedirs(f'{project}/track', exist_ok=True); json.dump(S.tolist(), open(f'{project}/track/{clip}.json', 'w'))
    print(clip, len(fs), 'frames  tx', S[:, 0, 2].min().round(), S[:, 0, 2].max().round(),
          ' ty', S[:, 1, 2].min().round(), S[:, 1, 2].max().round(),
          ' scale', np.hypot(S[:, 0, 0], S[:, 1, 0]).min().round(3), np.hypot(S[:, 0, 0], S[:, 1, 0]).max().round(3))

if __name__ == '__main__':
    if len(sys.argv) < 3: sys.exit(__doc__)
    for c in sys.argv[2:]: track(sys.argv[1], c)
