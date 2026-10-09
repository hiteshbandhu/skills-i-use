---
name: reel-edit
description: >
  Edits raw phone footage into a bold, professional-looking 9:16 Instagram reel on a Mac, with no
  editing app: a concept-first workflow, beat-synced cuts, HTML/canvas-rendered motion type,
  on-device Apple Vision / Core ML / MLX models (person mattes, subject lift, depth, hand/body
  pose, optical flow), synthesised SFX and a -14 LUFS mix. Includes scripts for every step and a
  log of what worked and flopped across 17+ real cuts. Triggers on "edit this video", "make a
  reel", "instagram edit", "cut this footage", "make it viral", "another version", "go ham",
  "motion design on this", "beat-synced edit", "segmentation edit", "parallax edit".
---

# Reel Edit — raw footage → finished reel, on a Mac

You are the editor and the motion designer. The user hands over clips and a vibe; you choose
a concept, build it, check it, and deliver an MP4. Everything runs locally.

**Read before starting:**
- [taste.md](taste.md): what lands and what flops. **Read it every time; it overrides your instincts.**
- [concepts.md](concepts.md): 17 cuts already made (recipe, tools, reaction). Do not repeat a
  flop, and do not clone a hit unless asked.
- [pipeline.md](pipeline.md): render engine contract, gotchas, disk/memory limits.
- [sound.md](sound.md): music sourcing, beat grids, SFX, mix levels.
- [models.md](models.md): which on-device model does what, sizes, speeds, what is too heavy.

**Scripts** (read each before running it; they write only inside the project dir you pass):

| Script | Does |
|---|---|
| `scripts/setup.sh` | checks ffmpeg, swiftc, Python packages and Chromium; builds the Vision tools |
| `scripts/ingest.py` | clips → `fr/<id>/` 1080×1920 frames, `au/<id>.wav`, slow-mo variants, manifest, contact sheets |
| `scripts/beats.py` | track → tempo, energy curve, drop candidates, beat grid from a start offset |
| `scripts/transcribe.py` | faster-whisper word timestamps, offline |
| `scripts/vision/*.swift` + `build.sh` | `seg` person matte · `fg` subject lift · `depth` Core ML depth · `hand` · `pose` · `flow` · `contour` |
| `scripts/render_html.py` | renders an HTML engine (`render(t)`) to frames; `--preview` for key moments |
| `scripts/engine_template.html` | starter engine: type with footage inside the letters, full-bleed punch-ins, a word placed behind the person |
| `scripts/fx/` | `parallax.py` (depth 2.5D) · `camtrack.py` (background camera track) · `clone.py` (multiplicity comp) · `comic.py` |
| `scripts/sfx.py` / `scripts/mix.py` | synthesised SFX library / JSON-spec mixer mastered to -14 LUFS |
| `scripts/encode.sh` / `scripts/contact_sheet.py` | IG-ready H.264 + AAC / tiled review sheet |
| `scripts/lab/mlx_detect_server.py` | optional local MLX detector (RF-DETR count, Florence-2 identify/find) |

Output: `{SKILL_OUTPUT_DIR}/reel-edit/<project>/` (see [../OUTPUT.md](../OUTPUT.md)). Work files go
there (`fr/ mk/ depth/ out/ au/`); the final MP4 goes where the user asks, else next to the
source footage. Frame dumps are GBs, so **delete `fr/` and `out*/` after the final encode.**

---

## Step 0 — Brief (do not skip, keep it short)

Infer what you can and ask only what changes the edit:

| Setting | Default |
|---|---|
| Goal | viral IG reel; must look pro-edited, **never AI-made** |
| Length | 15–25 s (music-led) · up to 60 s (talking head) |
| Audio | speech-led if someone talks to camera; otherwise music-led with natural sound under it |
| Music | free-licence track you find (Mixkit-style); **ask before downloading anything** |
| Versions | 1 strong concept. If asked for "versions", make each a *different concept*, not a re-grade |
| Brand text | none permanent on screen; no full stops in on-screen copy |

## Step 1 — Look at the footage

1. `scripts/setup.sh` (first run on a machine).
2. `python3 scripts/ingest.py <clips> --project <out>/<name> [--slow 03,06]`
3. **Open every contact sheet** in `<project>/sheets/`. Log for each clip: subject, motion,
   faces, objects, light, usable seconds, audio (`mean_db` in manifest). Low-res WhatsApp
   footage is fine if the concept is graphic.
4. Speech? `python3 scripts/transcribe.py <project>/au/<id>.wav`, but only for clips that are
   actually speech. Hinglish or noisy café audio: skip it and go music-led.

## Step 2 — Pick ONE concept (the step that decides everything)

Write a 4-line concept before touching code: **idea · visual language · where the
footage is transformed · the ending**. A concept is an *idea about the subject*
("people made of the words they read", "one founder, four opinions"), not an effect list.

- Start from what landed in [taste.md](taste.md): bold graphic transformation driven by
  segmentation, giant type, flat colour, paper/print textures, energy.
- Every effect must serve the idea. A model showcase (datamosh, x-ray, sketch) without an
  idea reads "forced".
- Use what's actually in the footage: the laptop shot, hands writing, the table of books.
  The user notices when a clip is skipped.
- Check [concepts.md](concepts.md) so you don't repeat a flop.

Tell the user the concept in 2–3 lines and start; do not wait for approval unless the brief
was vague.

## Step 3 — Music and the beat grid

1. Pick a track that matches the energy (see [sound.md](sound.md)).
2. `python3 scripts/beats.py track.mp3` → choose `--start` a few beats before a drop so the
   reel opens with a little tension and lands the drop at 3–8 s.
3. `python3 scripts/beats.py track.mp3 --start <s> --out <project>/grid.json`.
   **All shot boundaries are in beats.** Cuts on beats, hits on kicks, type on off-beats.

## Step 4 — Analyse footage with on-device models (only what the concept needs)

```bash
B=scripts/vision/bin
$B/seg   <p>/fr/05 <p>/mk/05          # person matte (accurate), PNG per frame
$B/fg    <p>/fr/03 <p>/fg/03 2        # subject lift: book, laptop, pen, people
$B/depth DepthAnythingV2SmallF16.mlpackage <p>/fr/06 <p>/depth/06
$B/hand  <p>/fr/10 <p>/hand10.json    # fingertips (1080x1920 px)
$B/pose  <p>/fr/09 <p>/pose09.json    # body joints
python3 scripts/fx/camtrack.py <p> 05 # camera track for anything locked to the room
```
Measure positions (heads, hands, table edge) **from the mattes/JSON**, never by eyeballing.

## Step 5 — Build the engine and preview

1. Copy `scripts/engine_template.html` → `<project>/engine.html`. Give the shot list a JSON
   `--data` file (shots in beats). Restyle freely; keep the `render(t)` / `window.DUR` contract.
   Python/OpenCV renderers (`fx/`) are fine for per-pixel work; composite their frames in.
2. Preview 8–16 key moments:
   `python3 scripts/render_html.py <p>/engine.html --project <p> --grid <p>/grid.json --data <p>/shots.json --out <p>/out --preview 0.4,1.2,...`
3. **Open `preview_sheet.jpg` and the full-size frames.** Check: text inside the IG safe zone,
   nothing clipped, targets aligned (zoom in), type not touching faces, brightness, nothing
   that looks templated/AI. Fix, re-preview. Usually 2–4 rounds.

## Step 6 — Full render, mix, encode

```bash
python3 scripts/render_html.py <p>/engine.html --project <p> --grid <p>/grid.json --data <p>/shots.json --out <p>/out
python3 scripts/mix.py <p>/mix.json <p>/mix.wav          # music + natural sound + SFX → -14 LUFS
scripts/encode.sh <p>/out <p>/mix.wav <final>.mp4
python3 scripts/contact_sheet.py <final>.mp4 <p>/final_sheet.jpg --n 16
```
Look at the final sheet. Then delete `<p>/out` and `<p>/fr` if the disk is tight.

## Step 7 — Deliver and learn

- Send the MP4 with a 3–5 line note: concept, track and licence, what's notable, any asset
  with a rights risk (e.g. game audio).
- When the user reacts, **append the reaction to [concepts.md](concepts.md) and any new
  rule to [taste.md](taste.md)**. That log is what makes the next edit better.
- "Another one" means a new concept and new techniques, not the last cut with a new filter.

## Hard rules

- Never ship without looking at a contact sheet of the actual encode.
- No full stops in on-screen text. No permanent brand header. Keep footage bright.
- Captions/type inside the IG safe zone: x 60–1020, y 220–1500 for anything important.
- Audio edges: 30–60 ms fades always; music fades out at the end; no abrupt cuts.
- Ask before downloading any outside asset (music, fonts, stock, SFX, models); say where it
  came from and its licence.
- 8 GB Macs: ≤5 render workers, one ML model in memory at a time, restart PyTorch MPS workers
  every ~40 frames.
