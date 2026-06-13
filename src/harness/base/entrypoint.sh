#!/bin/bash
set -e

# Common entrypoint for all ClawSafeBench harness images.
#
# Responsibilities:
#   1. Ensure /data exists for outputs (agent messages, usage, logs, grading).
#   2. Branch to manual mode if no INSTRUCTION is set (useful for debugging).
#   3. Otherwise hand off to /run-harness.sh, installed by the harness layer.
#
# Safety-benchmark notes:
#   - We intentionally do NOT start a browser, virtual display, or recording
#     server here (unlike ClawBench's browser-focused base). Safety tasks
#     test agents on filesystem/network/credential surfaces, not GUIs.
#   - Each harness Dockerfile drops its own /run-harness.sh into the image.

mkdir -p /data

# Manual / debug mode: no task instruction provided. Keep the container alive
# so the user can `docker exec` in and poke around. Useful while writing tasks.
if [ -z "${INSTRUCTION:-}" ]; then
  echo "[entrypoint] No INSTRUCTION set — entering manual mode (container will idle)."
  echo "[entrypoint] Use 'docker exec -it <container> bash' to attach."
  exec tail -f /dev/null
fi

# Agent mode: delegate to the harness layer.
if [ ! -x /run-harness.sh ]; then
  echo "[entrypoint] ERROR: /run-harness.sh missing — image built without a harness layer."
  echo "missing_harness" > /data/.stop-reason
  exit 1
fi

echo "[entrypoint] INSTRUCTION set, delegating to /run-harness.sh"
exec /run-harness.sh
