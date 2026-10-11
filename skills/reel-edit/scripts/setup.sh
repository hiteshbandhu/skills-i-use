#!/usr/bin/env bash
# Check (and optionally install) what the reel-edit pipeline needs on macOS.
# Usage: scripts/setup.sh            -> report only
#        scripts/setup.sh --install  -> pip install the missing Python packages into the current python3
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
ok(){ echo "PASS|$1"; }; miss(){ echo "MISS|$1"; MISSING=1; }
MISSING=0
command -v ffmpeg >/dev/null && ok "ffmpeg $(ffmpeg -version | head -1 | awk '{print $3}')" || miss "ffmpeg (brew install ffmpeg)"
command -v swiftc >/dev/null && ok "swiftc (Apple Vision tools)" || miss "swiftc (xcode-select --install)"
# Homebrew ffmpeg often has no drawtext/libass -> that's why overlays render through HTML.
ffmpeg -hide_banner -filters 2>/dev/null | grep -q drawtext && ok "ffmpeg drawtext" || echo "INFO|ffmpeg has no drawtext/libass: render text via HTML (render_html.py)"
PKGS="numpy opencv-python pillow librosa playwright faster-whisper"
NEED=""
for p in $PKGS; do
  mod=$p; case $p in opencv-python) mod=cv2;; pillow) mod=PIL;; faster-whisper) mod=faster_whisper;; esac
  python3 -c "import $mod" 2>/dev/null && ok "python: $p" || { miss "python: $p"; NEED="$NEED $p"; }
done
if [ -n "$NEED" ] && [ "${1:-}" = "--install" ]; then
  python3 -m pip install $NEED && python3 -m playwright install chromium
fi
python3 -c "from playwright.sync_api import sync_playwright as s; p=s().start(); b=p.chromium.launch(); b.close(); p.stop()" 2>/dev/null \
  && ok "playwright chromium" || miss "playwright chromium (python3 -m playwright install chromium)"
"$HERE/vision/build.sh" >/dev/null 2>&1 && ok "vision tools built in scripts/vision/bin" || miss "vision tools failed to build"
df -g . | awk 'NR==2{ if ($4<8) print "WARN|only "$4" GB free - 1080x1920 frame dumps need several GB; delete out_* dirs after encoding"; else print "PASS|disk "$4" GB free"}'
echo "INFO|optional ML env (separate venv recommended): mlx mlx-vlm mlx-audio mediapipe torch"
[ $MISSING -eq 0 ] && echo "SUMMARY|ready" || echo "SUMMARY|missing items above"
