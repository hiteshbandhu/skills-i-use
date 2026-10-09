#!/usr/bin/env python3
"""Synthesised sound design, no downloads, no licences. Import it or render a demo.

  sfx.py demo out.wav          # every sound in a row, to audition
  from sfx import riser, braam, ...   # each returns float32 stereo (N,2) at 48 kHz

Original sounds beat stock "whoosh pack" clichés and avoid licence problems.
Keep SFX under the music (-10 to -16 dB relative), and only on events the
viewer can see (a cut, a stamp, a page turn, a title).
"""
import sys, wave
import numpy as np
from numpy.fft import rfft, irfft

SR = 48000
_rng = np.random.default_rng(7)

def st(y): return np.stack([y, y], 1).astype(np.float32)
def _t(sec): return np.arange(int(sec * SR)) / SR
def norm(y, peak=0.9): return y / (np.abs(y).max() + 1e-9) * peak

def lp(x, fc):
    """One-pole low-pass (fc may be an array for sweeps)."""
    fc = np.broadcast_to(np.asarray(fc, dtype=float), x.shape)
    a = 1 - np.exp(-2 * np.pi * fc / SR); y = np.empty_like(x); s = 0.0
    for i in range(len(x)): s += a[i] * (x[i] - s); y[i] = s
    return y

def reverb(x, decay=2.5, mix=0.4):
    n = int(decay * SR); ir = _rng.standard_normal(n) * np.exp(-np.arange(n) / SR * (6.9 / decay))
    ir = lp(ir, 3500); ir /= np.sqrt((ir ** 2).sum())
    L = len(x) + n; F = 1 << int(np.ceil(np.log2(L))); w = irfft(rfft(x, F) * rfft(ir, F), F)[:L]
    y = np.zeros(L); y[:len(x)] = x; return y * (1 - mix) + w * mix * 2.2

def riser(sec=1.8):
    """Filtered noise + rising tone into a drop or a cut."""
    t = _t(sec); f = 120 * np.exp(np.log(1400 / 120) * (t / sec) ** 1.6)
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.5 + lp(_rng.standard_normal(len(t)), 300 + 4000 * (t / sec) ** 2) * 0.8
    return st(norm(y * (t / sec) ** 2.2))

def swell(sec=1.1):
    t = _t(sec); return st(norm(lp(_rng.standard_normal(len(t)), 1800) * (t / sec) ** 3))

def whoosh(sec=0.45):
    t = _t(sec); env = np.sin(np.pi * t / sec) ** 2
    return st(norm(lp(_rng.standard_normal(len(t)), 400 + 5000 * np.sin(np.pi * t / sec)) * env, 0.8))

def thump():
    """Sub kick for a hard cut or a title slam."""
    t = _t(0.6); return st(norm(np.sin(2 * np.pi * np.cumsum(55 * np.exp(-t * 3) + 30) / SR) * np.exp(-t * 7)))

def braam(sec=3.2):
    """Trailer brass hit: detuned saws + sub + impact, through a long reverb."""
    t = _t(sec); y = np.zeros_like(t)
    for f in [55, 55.4, 110, 110.7, 82.4, 164.8, 54.6]:
        y += 2 * ((f * t) % 1) - 1
    y = lp(y * np.minimum(1, t / 0.02) * np.exp(-t * 0.9), 900)
    sub = np.sin(2 * np.pi * np.cumsum(45 * np.exp(-t * 1.5) + 30) / SR) * np.exp(-t * 1.6)
    imp = lp(_rng.standard_normal(len(t)) * np.exp(-t * 18), 2500)
    return st(norm(reverb(norm(y, .8) + sub * .6 + imp * .5, 3.5, .45)))

def tick():
    t = _t(0.06); return st(norm(lp(_rng.standard_normal(len(t)) * np.exp(-t * 90), 4000), 0.7))

def tok():
    """Wooden card/stamp knock."""
    t = _t(0.25); return st(norm(reverb(lp(_rng.standard_normal(len(t)) * np.exp(-t * 60), 1200), 1.2, .4), 0.7))

def paper(sec=0.35):
    """Paper slap / page flip: crackly band-passed noise bursts."""
    t = _t(sec); n = _rng.standard_normal(len(t)) * (_rng.random(len(t)) < 0.25)
    y = n - lp(n, 900); env = np.exp(-t * 9) * np.minimum(1, t / 0.005)
    return st(norm(lp(y, 6000) * env, 0.7))

def shutter():
    """Camera shutter: two clicks + mechanism."""
    out = np.zeros(int(0.18 * SR))
    for at in (0.0, 0.09):
        c = tick()[:, 0]; i = int(at * SR); out[i:i + len(c)] += c[:len(out) - i]
    return st(norm(out, 0.7))

def tape_stop(x, sec=0.6):
    """Slow a stereo buffer to a halt (pitch drops) - for a power-off / record-scratch ending."""
    n = int(sec * SR); rate = np.linspace(1, 0, n) ** 1.5; pos = np.cumsum(rate)
    pos = pos[pos < len(x) - 1]; return np.stack([np.interp(pos, np.arange(len(x)), x[:, c]) for c in (0, 1)], 1)

def pad(freqs=(220, 277.2, 329.6), sec=2.6):
    t = _t(sec); y = sum(np.sin(2 * np.pi * f * t) * np.exp(-t * .6) for f in freqs) * np.minimum(1, t / .4)
    return st(norm(reverb(y, 2.5, .5), 0.6))

def fanfare(notes=(392, 523.3, 659.3, 784), step=0.14):
    """Short major-arpeggio 'mission passed' sting (original, square-ish synth)."""
    out = []
    for i, f in enumerate(notes):
        t = _t(step if i < len(notes) - 1 else 1.2)
        y = np.sign(np.sin(2 * np.pi * f * t)) * .3 + np.sin(2 * np.pi * f * 2 * t) * .2
        out.append(y * np.exp(-t * (6 if i < len(notes) - 1 else 2.2)))
    return st(norm(reverb(np.concatenate(out), 1.5, .3), 0.8))

ALL = dict(riser=riser, swell=swell, whoosh=whoosh, thump=thump, braam=braam, tick=tick, tok=tok,
           paper=paper, shutter=shutter, pad=pad, fanfare=fanfare)

def write_wav(path, x):
    with wave.open(path, 'w') as f:
        f.setnchannels(2); f.setsampwidth(2); f.setframerate(SR)
        f.writeframes((np.clip(x, -1, 1) * 32767).astype(np.int16).tobytes())

if __name__ == '__main__':
    if len(sys.argv) < 3 or sys.argv[1] != 'demo': sys.exit(__doc__)
    gap = np.zeros((int(.4 * SR), 2), np.float32)
    seq = []
    for name, fn in ALL.items():
        print(name); seq += [fn() * 0.8, gap]
    write_wav(sys.argv[2], np.concatenate(seq)); print('->', sys.argv[2])
