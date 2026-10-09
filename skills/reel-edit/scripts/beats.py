#!/usr/bin/env python3
"""Analyse a music track so cuts land on the music.

  beats.py <track.mp3> [--out grid.json] [--start 8.15] [--beats 48]
Prints tempo, a per-second energy curve and the strongest low-end (kick/drop) hits,
so you can choose where the reel starts in the track (pick a start a few beats
before a drop). With --start, writes a beat grid re-zeroed at that offset:
  {"track":..., "start":8.15, "tempo":..., "grid":[0.0, 0.49, ...], "kicks":[...]}
Use grid[i] as the time of beat i in the reel; snap every cut to it.
"""
import argparse, json, warnings
warnings.filterwarnings('ignore')
import numpy as np, librosa

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('track'); ap.add_argument('--out'); ap.add_argument('--start', type=float)
    ap.add_argument('--beats', type=int, default=64)
    a = ap.parse_args()
    y, sr = librosa.load(a.track, sr=22050, mono=True)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr, units='time')
    tempo = float(np.atleast_1d(tempo)[0])
    S = np.abs(librosa.stft(y)); f = librosa.fft_frequencies(sr=sr); tl = librosa.times_like(S, sr=sr)
    low = S[f < 120].sum(0); rms = librosa.feature.rms(y=y)[0]; tr = librosa.times_like(rms, sr=sr)
    cent = float(librosa.feature.spectral_centroid(y=y, sr=sr)[0].mean())
    dur = len(y) / sr
    print(f'{a.track}: {dur:.1f}s  {tempo:.1f} bpm  beat={60/tempo:.3f}s  brightness={cent:.0f}Hz')
    print('energy/s :', ' '.join(f'{rms[(tr>=i)&(tr<i+1)].mean()/rms.max():.2f}' for i in range(int(dur))))
    print('kick/s   :', ' '.join(f'{low[(tl>=i)&(tl<i+1)].mean()/low.max():.2f}' for i in range(int(dur))))
    # strongest low-end onsets = candidate drops
    lo = np.maximum(0, np.diff(low, prepend=low[0]))
    top = sorted({round(float(tl[i]), 2) for i in np.argsort(lo)[::-1][:12]})
    print('low-end hits (drop candidates):', top)
    if a.start is not None:
        b = beats[beats >= a.start - 0.03]
        grid = [round(float(x - a.start), 3) for x in b[:a.beats]]
        if not grid or grid[0] > 0.05: grid = [0.0] + grid
        kicks = [round(t - a.start, 3) for t in top if t >= a.start]
        res = dict(track=a.track, start=a.start, tempo=tempo, grid=grid, kicks=kicks)
        if a.out:
            json.dump(res, open(a.out, 'w'), indent=1); print('grid ->', a.out)
        print('first beats:', grid[:12])

if __name__ == '__main__':
    main()
