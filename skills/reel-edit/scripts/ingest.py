#!/usr/bin/env python3
"""Normalise raw clips into a 9:16 working project.

  ingest.py <clips_dir_or_files...> --project <dir> [--fps 30] [--size 1080x1920] [--slow 06,10]

Creates, per clip (ids 01, 02, ... in name order):
  <project>/fr/<id>/0000.jpg ...   cover-cropped frames at --size / --fps
  <project>/au/<id>.wav            48 kHz stereo (silent track if the clip has none)
  <project>/fr/<id>s/ ...          optional 2x slow-motion (motion-interpolated) for --slow ids
  <project>/manifest.json          id -> source, duration, frames, original size, loudness
  <project>/sheets/<id>.jpg        8-frame contact sheet, look at these before planning
Frame dumps are big (~0.3 MB/frame). Delete <project>/fr when the reel is done.
"""
import argparse, json, os, subprocess, sys, glob

VID = ('.mp4', '.mov', '.m4v', '.mkv', '.webm', '.avi')

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def probe(path):
    r = run(['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_type,width,height,r_frame_rate:format=duration',
             '-of', 'json', path])
    d = json.loads(r.stdout or '{}')
    v = next((s for s in d.get('streams', []) if s.get('codec_type') == 'video'), {})
    has_audio = any(s.get('codec_type') == 'audio' for s in d.get('streams', []))
    return dict(width=v.get('width'), height=v.get('height'), fps=v.get('r_frame_rate'),
                duration=float(d.get('format', {}).get('duration', 0)), has_audio=has_audio)

def mean_volume(wav):
    r = run(['ffmpeg', '-hide_banner', '-i', wav, '-af', 'volumedetect', '-f', 'null', '-'])
    for line in r.stderr.splitlines():
        if 'mean_volume' in line:
            return float(line.split(':')[1].split()[0])
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('inputs', nargs='+')
    ap.add_argument('--project', required=True)
    ap.add_argument('--fps', type=int, default=30)
    ap.add_argument('--size', default='1080x1920')
    ap.add_argument('--slow', default='', help='comma list of ids to also make 2x slow-mo for')
    ap.add_argument('--quality', type=int, default=3, help='ffmpeg -q:v for jpg frames (2 best)')
    a = ap.parse_args()
    W, H = map(int, a.size.split('x'))
    files = []
    for x in a.inputs:
        files += sorted(f for f in glob.glob(os.path.join(x, '*')) if f.lower().endswith(VID)) if os.path.isdir(x) else [x]
    if not files:
        sys.exit('no video files found')
    P = a.project
    for d in ('fr', 'au', 'sheets'):
        os.makedirs(os.path.join(P, d), exist_ok=True)
    cover = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1'
    slow = set(filter(None, a.slow.split(',')))
    man = {}
    for i, f in enumerate(files, 1):
        cid = f'{i:02d}'
        info = probe(f)
        out = os.path.join(P, 'fr', cid); os.makedirs(out, exist_ok=True)
        run(['ffmpeg', '-v', 'error', '-y', '-i', f, '-vf', f'fps={a.fps},{cover}', '-q:v', str(a.quality),
             '-start_number', '0', os.path.join(out, '%04d.jpg')])
        wav = os.path.join(P, 'au', f'{cid}.wav')
        if info['has_audio']:
            run(['ffmpeg', '-v', 'error', '-y', '-i', f, '-vn', '-ac', '2', '-ar', '48000', wav])
        else:
            run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo', '-t',
                 str(info['duration']), wav])
        if cid in slow:
            so = os.path.join(P, 'fr', cid + 's'); os.makedirs(so, exist_ok=True)
            run(['ffmpeg', '-v', 'error', '-y', '-i', f, '-vf',
                 f'setpts=2*PTS,minterpolate=fps={a.fps}:mi_mode=mci:mc_mode=aobmc,{cover}',
                 '-q:v', str(a.quality), '-start_number', '0', os.path.join(so, '%04d.jpg')])
        n = len(os.listdir(out))
        man[cid] = dict(source=os.path.abspath(f), frames=n, seconds=round(n / a.fps, 2),
                        orig=f"{info['width']}x{info['height']}", has_audio=info['has_audio'],
                        mean_db=mean_volume(wav) if info['has_audio'] else None)
        # contact sheet: 8 evenly spaced frames
        picks = [round(k * (n - 1) / 7) for k in range(8)]
        inputs = sum([['-i', os.path.join(out, f'{p:04d}.jpg')] for p in picks], [])
        run(['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex',
             ''.join(f'[{k}:v]scale=216:384[s{k}];' for k in range(8)) + ''.join(f'[s{k}]' for k in range(8)) + 'hstack=8',
             os.path.join(P, 'sheets', f'{cid}.jpg')])
        print(f"{cid}  {os.path.basename(f)[:40]:40s} {man[cid]['seconds']:6.2f}s  {man[cid]['orig']}  "
              f"audio={man[cid]['mean_db']}")
    json.dump(dict(fps=a.fps, size=[W, H], clips=man), open(os.path.join(P, 'manifest.json'), 'w'), indent=1)
    print('manifest ->', os.path.join(P, 'manifest.json'))

if __name__ == '__main__':
    main()
