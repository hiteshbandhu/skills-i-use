#!/usr/bin/env bash
# Encode rendered frames + mixed audio into an Instagram-ready MP4.
# Usage: encode.sh <frames_dir> <audio.wav> <out.mp4> [fps=30] [pattern=%05d.jpg]
# H.264 high, crf 18, yuv420p, AAC 256k, faststart. Audio is cut to the video length.
set -euo pipefail
FR="$1"; AU="$2"; OUT="$3"; FPS="${4:-30}"; PAT="${5:-%05d.jpg}"
ffmpeg -v error -y -framerate "$FPS" -i "$FR/$PAT" -i "$AU" \
  -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -profile:v high -movflags +faststart \
  -c:a aac -b:a 256k -ar 48000 -shortest "$OUT"
ffprobe -v error -show_entries format=duration:stream=width,height -of csv=p=0 "$OUT" | tr '\n' ' '
echo "-> $OUT"
echo "Frames in $FR can be deleted now (rm -rf) - they are several GB."
