#!/usr/bin/env sh
# Kokoro v1.0 voice model (Apache-2.0) from the kokoro-onnx releases.
set -e
cd "$(dirname "$0")"; mkdir -p kokoro
base=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
for f in kokoro-v1.0.onnx voices-v1.0.bin; do
  [ -s "kokoro/$f" ] || curl -fL -o "kokoro/$f" "$base/$f"
done
ls -l kokoro
