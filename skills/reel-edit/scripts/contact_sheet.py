#!/usr/bin/env python3
"""Tile frames of a finished video (or a frame dir) into one image for review.

  contact_sheet.py <video.mp4|frames_dir> <out.jpg> [--times 0.5,2,4.1] [--n 16] [--cols 8] [--w 216] [--fps 30]
Always look at a sheet of the final encode before showing the user anything:
check text cut-offs, safe zones, misaligned targets, black frames.
"""
import argparse, os, subprocess, tempfile, glob
import cv2, numpy as np

def grab_video(path, times, w):
    cap = cv2.VideoCapture(path); out = []
    for t in times:
        cap.set(cv2.CAP_PROP_POS_MSEC, t * 1000); ok, f = cap.read()
        out.append(f if ok else np.zeros((16, 9, 3), np.uint8))
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('src'); ap.add_argument('out')
    ap.add_argument('--times', default=''); ap.add_argument('--n', type=int, default=16)
    ap.add_argument('--cols', type=int, default=8); ap.add_argument('--w', type=int, default=216)
    ap.add_argument('--fps', type=float, default=30)
    a = ap.parse_args()
    if os.path.isdir(a.src):
        fs = sorted(glob.glob(os.path.join(a.src, '*.jpg')) + glob.glob(os.path.join(a.src, '*.png')))
        dur = len(fs) / a.fps
        times = [float(x) for x in a.times.split(',')] if a.times else [dur * (k + .5) / a.n for k in range(a.n)]
        frames = [cv2.imread(fs[min(len(fs) - 1, int(t * a.fps))]) for t in times]
    else:
        cap = cv2.VideoCapture(a.src); dur = cap.get(cv2.CAP_PROP_FRAME_COUNT) / (cap.get(cv2.CAP_PROP_FPS) or 30)
        times = [float(x) for x in a.times.split(',')] if a.times else [dur * (k + .5) / a.n for k in range(a.n)]
        frames = grab_video(a.src, times, a.w)
    h = int(a.w * frames[0].shape[0] / frames[0].shape[1])
    tiles = []
    for f, t in zip(frames, times):
        f = cv2.resize(f, (a.w, h))
        cv2.putText(f, f'{t:.2f}', (6, 18), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 3)
        cv2.putText(f, f'{t:.2f}', (6, 18), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        tiles.append(f)
    while len(tiles) % a.cols: tiles.append(np.zeros_like(tiles[0]))
    rows = [np.hstack(tiles[i:i + a.cols]) for i in range(0, len(tiles), a.cols)]
    cv2.imwrite(a.out, np.vstack(rows), [cv2.IMWRITE_JPEG_QUALITY, 88])
    print(a.out, f'{len(times)} frames, duration {dur:.2f}s')

if __name__ == '__main__':
    main()
