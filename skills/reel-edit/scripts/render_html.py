#!/usr/bin/env python3
"""Render an HTML "engine" page to video frames with headless Chromium.

  render_html.py <engine.html> --project <dir> --out <frames_dir> [--grid grid.json] [--data extra.json]
                 [--preview 0.5,2,7.9] [--fps 30] [--workers 5] [--size 1080x1920] [--dur 21.3]

The engine page must define  async function render(t)  (t in seconds, deterministic:
same t -> same pixels) and  window.DUR  (reel length). Placeholders substituted
before loading:
  __ROOT__  file:// URL of the project dir (frames at ROOT+'fr/<id>/0000.jpg')
  __CNT__   {"01": 412, ...} frame counts per fr/ subfolder
  __MCNT__  same for mk/ (mattes), __FCNT__ for fg/ (subject lifts)
  __GRID__  the "grid" array from beats.py --out (beat times, reel-relative)
  __DATA__  any JSON you pass with --data (shot lists, copy, positions)
--preview writes pv_<t>.jpg for the listed times plus preview_sheet.jpg. Always
preview 8-16 key moments before a full render; a full render is minutes.
Workers render interleaved frames in parallel; 5 is right for an 8 GB M2.
"""
import argparse, asyncio, json, os, subprocess
from playwright.async_api import async_playwright

def counts(d):
    return {k: len(os.listdir(os.path.join(d, k))) for k in sorted(os.listdir(d))
            if os.path.isdir(os.path.join(d, k))} if os.path.isdir(d) else {}

async def worker(url, size, jobs, out, errs):
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files', '--disable-web-security'])
        pg = await b.new_page(viewport={'width': size[0], 'height': size[1]})
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.on('console', lambda m: m.type == 'error' and errs.append(m.text))
        await pg.goto(url)
        await pg.evaluate('document.fonts.ready')          # fonts must be loaded before layout/measure
        await pg.wait_for_timeout(300)
        for name, t in jobs:
            await pg.evaluate(f'render({t})')
            await pg.screenshot(path=os.path.join(out, name), type='jpeg', quality=93)
        await b.close()

async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('engine'); ap.add_argument('--project', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--grid'); ap.add_argument('--data'); ap.add_argument('--preview')
    ap.add_argument('--fps', type=int, default=30); ap.add_argument('--workers', type=int, default=5)
    ap.add_argument('--size', default='1080x1920'); ap.add_argument('--dur', type=float)
    a = ap.parse_args()
    P = os.path.abspath(a.project) + '/'; size = tuple(map(int, a.size.split('x')))
    html = open(a.engine).read()
    grid = json.load(open(a.grid))['grid'] if a.grid else []
    rep = {'__ROOT__': 'file://' + P, '__CNT__': json.dumps(counts(P + 'fr')), '__MCNT__': json.dumps(counts(P + 'mk')),
           '__FCNT__': json.dumps(counts(P + 'fg')), '__GRID__': json.dumps(grid),
           '__DATA__': open(a.data).read() if a.data else '{}'}
    for k, v in rep.items(): html = html.replace(k, v)
    os.makedirs(a.out, exist_ok=True); errs = []
    built = os.path.join(os.path.abspath(a.out), '_built_' + os.path.basename(a.engine))
    open(built, 'w').write(html)
    url = 'file://' + built
    if a.preview:
        ts = [float(x) for x in a.preview.split(',')]
        await worker(url, size, [(f'pv_{t:06.2f}.jpg', t) for t in ts], a.out, errs)
        fs = [os.path.join(a.out, f'pv_{t:06.2f}.jpg') for t in ts]
        cols = min(8, len(fs)); rows = -(-len(fs) // cols)
        tiles = ''.join(f'[{i}:v]scale=216:384[s{i}];' for i in range(len(fs)))
        pads = ''.join(f'color=black:s=216x384:d=1[p{j}];' for j in range(rows * cols - len(fs)))
        allv = [f's{i}' for i in range(len(fs))] + [f'p{j}' for j in range(rows * cols - len(fs))]
        rowsf = ''.join(''.join(f'[{v}]' for v in allv[r*cols:(r+1)*cols]) + (f'hstack={cols}[r{r}];' if cols > 1 else f'null[r{r}];') for r in range(rows))
        fc = tiles + pads + rowsf + (''.join(f'[r{r}]' for r in range(rows)) + f'vstack={rows}' if rows > 1 else '[r0]null')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', *sum([['-i', f] for f in fs], []), '-filter_complex', fc,
                        '-frames:v', '1', os.path.join(a.out, 'preview_sheet.jpg')])
        print('preview ->', os.path.join(a.out, 'preview_sheet.jpg'))
    else:
        dur = a.dur
        if dur is None:
            async with async_playwright() as p:
                b = await p.chromium.launch(args=['--allow-file-access-from-files']); pg = await b.new_page()
                await pg.goto(url); dur = await pg.evaluate('window.DUR'); await b.close()
        n = int(round(dur * a.fps)); jobs = [(f'{i:05d}.jpg', i / a.fps) for i in range(n)
                                             if not os.path.exists(os.path.join(a.out, f'{i:05d}.jpg'))]
        print(f'rendering {len(jobs)}/{n} frames with {a.workers} workers')
        await asyncio.gather(*[worker(url, size, jobs[k::a.workers], a.out, errs) for k in range(a.workers)])
    if errs: print('PAGE ERRORS:', *sorted(set(errs))[:8], sep='\n  ')

if __name__ == '__main__':
    asyncio.run(main())
