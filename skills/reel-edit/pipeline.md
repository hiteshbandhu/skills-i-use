# Pipeline: how the frames get made, and the traps

## Project layout

```
<project>/
  manifest.json     clip ids → source, seconds, original size, mean_db
  sheets/<id>.jpg   contact sheets (look first)
  fr/<id>/0000.jpg  1080×1920 frames @30 fps   (fr/<id>s = 2× slow-mo)
  au/<id>.wav       48 kHz stereo natural sound
  mk/<id>/*.png     person mattes   (vision/bin/seg)
  fg/<id>/*.png     subject lifts   (vision/bin/fg)
  depth/<id>/*.png  16-bit depth    (vision/bin/depth)
  track/<id>.json   camera affine per frame (fx/camtrack.py)
  grid.json         beat grid (beats.py)
  shots.json        shot list for the engine (--data)
  engine.html       the reel, as render(t)
  out/00000.jpg     rendered frames
  mix.json, mix.wav
```

## Why HTML for rendering

Homebrew ffmpeg often ships without `drawtext`/`libass`, and web layout is the best type engine
you have anyway: real fonts, kerning, measurement, blend modes, SVG, canvas. The engine is a
1080×1920 page with `async render(t)`; `render_html.py` screenshots it per frame with 5
parallel Chromium workers. For per-pixel work (depth warps, clones, comic), render frames in
Python with OpenCV and a multiprocessing Pool, then either encode them directly or load them
into the engine as footage.

## Engine contract

- `render(t)` must be **deterministic**: same t → same pixels. Seeded random only (an LCG), never `Math.random()` or `Date.now()`.
- **Await every image.** Cache `Image()` promises, or `el.decode()`, before returning. Otherwise screenshots catch blank frames.
- Time in beats: `bt(beat)` → seconds from the grid. Shots are `{b:[from,to], …}`.
- `window.DUR = bt(lastBeat)` gives the reel length.

## Traps hit (and the fixes)

| Symptom | Cause | Fix |
|---|---|---|
| Footage-inside-letters shows nothing | CSS `clip-path:url(#svgClip)` with `<text>` silently fails in headless Chromium | canvas: draw text, `globalCompositeOperation='source-in'`, draw footage |
| Word-behind-person covers the whole frame | Vision mattes are grayscale PNGs with **no alpha**; `destination-in` needs alpha | copy luminance into alpha once and cache it (`loadMatte` in the template) |
| Type measured wrong or a fallback font in frame 1 | fonts measured before they loaded | `await document.fonts.load('100px HEAD')` in render; `document.fonts.ready` before the first frame |
| Annotation ring or label off-target | coordinates guessed | measure: matte bbox, pose/hand JSON, `getBoundingClientRect` for UI; verify on a zoomed frame |
| Text mirrored ("YMMOT") into a model | sent the mirrored webcam frame | un-mirror before inference, mirror the boxes back |
| `cv2.remap` error | float64 maps | `.astype(np.float32)` |
| Depth PNG has 3 channels | reader default | `cv2.IMREAD_UNCHANGED`, take channel 0 |
| Parallax edges tear and flicker | raw per-frame depth | average depth over 5 frames, dilate 9 px, blur σ4; small moves |
| Camera track jumps to scale 0.1 | bad RANSAC solve, few background points | reject scale outside 0.8–1.25 or huge shifts; hold the last pose |
| faster-whisper hangs at start | HF Hub network check | `HF_HUB_OFFLINE=1` once cached (`transcribe.py` does it) |
| faster-whisper very slow | temperature fallback loop | `temperature=0, condition_on_previous_text=False` |
| faster-whisper `open() … metadata_errors` | PyAV/Python mismatch | decode with ffmpeg to a 16 kHz numpy array (`transcribe.py` does it) |
| Trailer hits flattened | `loudnorm` compresses dynamics | static gain to target + `alimiter` (`mix.py`) |
| Disk full mid-render, shell dead | 1080×1920 JPEG dumps are ~0.3 MB each × 5 cuts | delete `out*/` after each encode; check `df` before full renders |
| PyTorch MPS memory climbs to OOM | MPS leak in long batch loops | restart the worker every ~40 frames + `torch.mps.empty_cache()` |
| SAM3 takes 108 s per frame | too big for 8 GB | use Vision `fg`/`seg`, Florence-2 grounding, or SAM 2 tiny |
| Core ML: `coremlcompiler` missing | no full Xcode | `MLModel.compileModel(at:)` at runtime (the `depth` tool does it and caches `.mlmodelc`) |

## Safe zone (Instagram)

Important type and faces between **x 60–1020, y 220–1500**. Bottom ~420 px sit under the caption
and buttons; the right ~120 px sit under the action rail. Check on a real phone if in doubt.

## Verification loop

1. `--preview` 8–16 times covering every shot type, the drop and the ending.
2. Open the sheet and the 2–3 riskiest frames at full size (type near faces, tracked elements).
3. After the encode, run `contact_sheet.py` on the MP4. Check the duration and that audio is present (`ffprobe`).
4. Listen check: the loudness line printed by `mix.py` should read about -14 LUFS; no clicks at clip edges.
