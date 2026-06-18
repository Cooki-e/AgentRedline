#!/bin/bash
set -euo pipefail

# Builds the ClawSafeBench base image and every harness image on top of it.
# The Docker build context is src/harness for all images (the harness
# Dockerfiles COPY their sibling dirs, e.g. `COPY codex/...`).
#
# Usage:
#   bash eval/build_images.sh            # build base + all harnesses
#   bash eval/build_images.sh codex      # build base + just codex (one or more)
#
# Build args (apt/pip China mirrors, proxies) are inherited from the Dockerfiles'
# defaults; override per-image with `docker build --build-arg` if needed.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HARNESS_DIR="$ROOT_DIR/src/harness"

# harness name -> Dockerfile path (relative to $HARNESS_DIR)
declare -A HARNESS_DOCKERFILES=(
  [openclaw]="openclaw/Dockerfile.openclaw"
  [codex]="codex/Dockerfile.codex"
  [claude-code]="claude-code/Dockerfile.claude-code"
  [hermes]="hermes/Dockerfile.hermes"
)

build_one() {
  local name="$1"
  local dockerfile="${HARNESS_DOCKERFILES[$name]:-}"
  if [ -z "$dockerfile" ]; then
    echo "ERROR: unknown harness '$name' (known: ${!HARNESS_DOCKERFILES[*]})" >&2
    exit 1
  fi
  echo "==> building clawsafebench-$name (-f $dockerfile)"
  docker build -t "clawsafebench-$name" -f "$HARNESS_DIR/$dockerfile" "$HARNESS_DIR"
}

# Base first — every harness image is FROM clawsafebench-base.
echo "==> building clawsafebench-base"
docker build -t clawsafebench-base -f "$HARNESS_DIR/base/Dockerfile.base" "$HARNESS_DIR"

if [ "$#" -gt 0 ]; then
  for name in "$@"; do
    build_one "$name"
  done
else
  for name in openclaw codex claude-code hermes; do
    build_one "$name"
  done
fi

echo "==> done."
