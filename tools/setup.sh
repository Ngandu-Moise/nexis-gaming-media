#!/usr/bin/env bash
# Installe le moteur de voix Piper et la voix française (une fois par session).
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
if [ ! -x "$DIR/piper/piper" ]; then
  curl -sSL -m 300 -o /tmp/piper.tgz https://github.com/rhasspy/piper/releases/download/2023.11.14-2/piper_linux_x86_64.tar.gz
  tar xzf /tmp/piper.tgz -C "$DIR"
fi
if [ ! -f "$DIR/voices/fr-siwis-medium.onnx" ]; then
  mkdir -p "$DIR/voices"
  curl -sSL -m 300 -o /tmp/voice.tgz https://github.com/rhasspy/piper/releases/download/v0.0.2/voice-fr-siwis-medium.tar.gz
  tar xzf /tmp/voice.tgz -C "$DIR/voices"
fi
command -v ffmpeg >/dev/null || { echo "ffmpeg manquant"; exit 1; }
python3 -c "import PIL" || pip install --break-system-packages -q pillow
echo "OK : voix et montage prêts"
