#!/usr/bin/env python3
"""Build the reel soundtrack from a JSON spec, then master to -14 LUFS.

  mix.py spec.json out.wav

spec = {
  "duration": 21.3,
  "music": {"file": "track.mp3", "start": 8.15, "gain_db": 0, "fade_in": 0.02, "fade_out": 1.6,
            "duck": [[3.0, 5.2, -9]]},                       # dip music under speech: [from, to, dB]
  "clips": [{"file": "proj/au/05.wav", "in": 2.0, "at": 3.1, "dur": 1.2, "gain_db": -18, "pan": 0.0}],
  "sfx":   [{"type": "riser", "at": 6.2, "dur": 1.8, "gain_db": -12},
            {"type": "thump", "at": 8.0, "gain_db": -8},
            {"file": "my_sound.wav", "at": 10.0, "gain_db": -14}],
  "silence": [[22.6, 23.0]],                                 # hard holes (everything muted, tails too)
  "target_lufs": -14, "ceiling": 0.89
}
Lessons baked in: every clip edge gets a 40 ms fade (no clicks / abrupt cuts);
natural sound sits ~-18 to -25 dB under the music; mastering is a STATIC gain to
the target plus a brickwall limiter. ffmpeg loudnorm squashed the dynamics of
trailer hits, so it is not used.
"""
import json, os, subprocess, sys, tempfile, wave
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sfx as SFX

SR = 48000

def read(path):
    """Any audio file -> float32 stereo 48k (decoded through ffmpeg)."""
    tmp = tempfile.NamedTemporaryFile(suffix='.wav', delete=False).name
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', path, '-ac', '2', '-ar', str(SR), '-sample_fmt', 's16', tmp], check=True)
    with wave.open(tmp) as f:
        a = np.frombuffer(f.readframes(f.getnframes()), np.int16).astype(np.float32) / 32768
    os.unlink(tmp); return a.reshape(-1, 2)

def db(x): return 10 ** (x / 20)

def fade(seg, fi, fo):
    fi, fo = min(int(fi * SR), len(seg) // 2), min(int(fo * SR), len(seg) // 2)
    if fi: seg[:fi] *= np.linspace(0, 1, fi)[:, None]
    if fo: seg[-fo:] *= np.linspace(1, 0, fo)[:, None]
    return seg

def lufs(path):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', path, '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True)
    vals = [l for l in r.stderr.splitlines() if l.strip().startswith('I:')]
    return float(vals[-1].split()[1]) if vals else None

def main():
    spec = json.load(open(sys.argv[1])); out_path = sys.argv[2]
    base = os.path.dirname(os.path.abspath(sys.argv[1]))
    P = lambda p: p if os.path.isabs(p) else os.path.join(base, p)
    N = int(spec['duration'] * SR); out = np.zeros((N, 2), np.float32)
    def add(x, at, g=1.0):
        i = int(at * SR); j = min(N, i + len(x))
        if i < N and j > max(i, 0): out[max(i, 0):j] += x[max(0, -i):j - i] * g
    m = spec.get('music')
    if m:
        a = read(P(m['file']))[int(m.get('start', 0) * SR):][:N].copy()
        a = fade(a, m.get('fade_in', 0.02), m.get('fade_out', 1.6)) * db(m.get('gain_db', 0))
        env = np.ones(len(a), np.float32)
        for t0, t1, g in m.get('duck', []):          # 120 ms ramps in/out of a duck
            i0, i1, r = int(t0 * SR), int(t1 * SR), int(0.12 * SR)
            k = np.ones(len(a)); seg = np.arange(len(a))
            w = np.clip(np.minimum((seg - i0 + r) / r, (i1 + r - seg) / r), 0, 1)
            env *= 1 - (1 - db(g)) * w
        add(a * env[:, None], 0)
    for c in spec.get('clips', []):
        src = read(P(c['file'])); seg = src[int(c.get('in', 0) * SR):][:int(c['dur'] * SR)].copy()
        seg = fade(seg, 0.04, 0.04) * db(c.get('gain_db', -18))
        p = c.get('pan', 0.0); seg[:, 0] *= np.sqrt((1 - p) / 2) * 1.414; seg[:, 1] *= np.sqrt((1 + p) / 2) * 1.414
        add(seg, c['at'])
    for s in spec.get('sfx', []):
        if 'file' in s: x = read(P(s['file']))
        else:
            fn = SFX.ALL[s['type']]; x = fn(s['dur']) if 'dur' in s else fn()
        add(x, s['at'], db(s.get('gain_db', -12)))
    for t0, t1 in spec.get('silence', []):
        i0, i1, f = int(t0 * SR), int(t1 * SR), int(0.03 * SR)
        out[max(0, i0 - f):i0] *= np.linspace(1, 0, min(f, i0))[:, None]; out[i0:i1] = 0
    raw = out_path + '.raw.wav'; SFX.write_wav(raw, out)
    target, ceil = spec.get('target_lufs', -14), spec.get('ceiling', 0.89)
    I = lufs(raw); gain = target - I if I is not None else 0
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', raw, '-af',
                    f'volume={gain:.2f}dB,alimiter=limit={ceil}:attack=3:release=60:level=disabled', '-ar', str(SR), out_path], check=True)
    os.unlink(raw)
    print(f'mix -> {out_path}  pre {I} LUFS, gain {gain:+.1f} dB, final {lufs(out_path)} LUFS')

if __name__ == '__main__':
    main()
