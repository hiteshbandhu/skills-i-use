#!/usr/bin/env bash
# Compile the Apple Vision / Core ML CLI tools in this folder into ./bin.
# Needs Xcode command line tools (swiftc). macOS 14+ for fg (subject lift).
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p bin
for src in *.swift; do
  name="${src%.swift}"
  if [ ! -x "bin/$name" ] || [ "$src" -nt "bin/$name" ]; then
    echo "building $name"
    swiftc -O "$src" -o "bin/$name"
  fi
done
echo "tools in $(pwd)/bin: $(ls bin | tr '\n' ' ')"
