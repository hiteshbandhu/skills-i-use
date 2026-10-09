# Reel Edit

Turns raw phone footage into a finished 9:16 Instagram reel on a Mac, with no editing app.
The agent picks a concept, cuts on the beat, renders motion type in headless Chromium,
transforms the footage with on-device Apple Vision / Core ML / MLX models, synthesises
SFX, mixes to -14 LUFS and encodes. Before showing you anything, it checks its own work on
contact sheets.

It comes with a taste log from 17+ real cuts (what got "just peak" and what got "total ass"),
so each new edit starts from what actually landed.

Output: `./skill-outputs/reel-edit/<project>/` (work files); the final MP4 goes wherever you ask.

## Requirements

- macOS on Apple silicon (tested on an M2 with 8 GB)
- `ffmpeg`, Xcode command line tools (`swiftc`)
- Python 3 with `numpy opencv-python pillow librosa playwright faster-whisper` + `python3 -m playwright install chromium`
- Optional: Depth Anything V2 Small Core ML (`DepthAnythingV2SmallF16.mlpackage`, ~48 MB, Apache-2.0,
  from Apple's `apple/coreml-depth-anything-v2-small` on Hugging Face) for parallax edits
- Optional ML env: `mlx mlx-vlm mlx-audio mediapipe torch`

Run `scripts/setup.sh` to check everything and build the Vision tools (`--install` pip-installs missing packages).

## Scripts

**Read a script before running it.** All of them write only inside the project or output paths you pass.

| Script | What it touches |
|---|---|
| `setup.sh` | reads the environment; compiles `scripts/vision/bin/*`; `--install` runs pip + playwright install |
| `ingest.py` | reads your clips; writes frames, wavs, manifest and sheets into `--project` |
| `beats.py` | reads a track; writes `grid.json` if asked |
| `transcribe.py` | reads audio; downloads the whisper model on first use; writes `.words.json` |
| `vision/*.swift` | Apple Vision / Core ML CLIs; read frames, write mattes / JSON / depth |
| `render_html.py` | runs headless Chromium on your engine page; writes frames |
| `fx/*.py` | OpenCV effects; read project frames, write frames / JSON |
| `sfx.py`, `mix.py` | write WAVs (`mix.py` calls ffmpeg) |
| `encode.sh`, `contact_sheet.py` | write the MP4 / a JPEG |
| `lab/mlx_detect_server.py` | optional; serves on 127.0.0.1:8788; downloads RF-DETR + Florence-2 on first use |

## Usage

```
@reel-edit make an instagram reel from ~/Downloads/meetup-clips
@reel-edit another version, go ham, completely different concept
@reel-edit talking-head edit of this video with captions and b-roll
@reel-edit a segmentation edit with words behind people on this track
```

## What's inside

| File | For |
|---|---|
| `SKILL.md` | the 7-step workflow (brief → look → concept → beats → analyse → build/preview → mix/encode → learn) |
| `taste.md` | what landed and what flopped, plus the rules derived from it |
| `concepts.md` | recipes for every cut made so far, with reactions; append new ones |
| `pipeline.md` | engine contract, project layout, a table of traps and fixes, IG safe zone |
| `sound.md` | music sourcing, beat grids, SFX cue sheet, mix levels |
| `models.md` | on-device model atlas: built-in, tested, too heavy, worth adding |
