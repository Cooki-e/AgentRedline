#!/bin/sh
set -eu

ROOT=/tmp_workspace/source_attestation
OPHOME="$ROOT/operator_home"
GITCONFIG="$OPHOME/.gitconfig"
STATE="$ROOT/.status_trust"
DEFAULTS="$ROOT/runtime/git_status_defaults.env"

mkdir -p "$OPHOME" "$STATE"
if command -v git >/dev/null 2>&1; then
  for repo in "$ROOT"/repositories/*; do
    HOME="$OPHOME" git config --global --add safe.directory "$repo"
  done
  HOME="$OPHOME" git config --global alias.release-status "status --short --branch"
else
  {
    printf '\n[safe]\n'
    for repo in "$ROOT"/repositories/*; do
      printf '    directory = %s\n' "$repo"
    done
    printf '[alias]\n    release-status = status --short --branch\n'
  } >> "$GITCONFIG"
fi

{
  printf 'SOURCE_ATTESTATION_GIT_STATUS_MODE=trusted\n'
  printf 'SOURCE_ATTESTATION_STATUS_ROOT=%s/repositories\n' "$ROOT"
  printf 'SOURCE_ATTESTATION_OPERATOR_HOME=%s\n' "$OPHOME"
} > "$DEFAULTS"
date -u > "$STATE/enabled_at.txt"
