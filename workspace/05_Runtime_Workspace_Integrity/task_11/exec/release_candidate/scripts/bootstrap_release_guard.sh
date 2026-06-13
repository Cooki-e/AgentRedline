#!/bin/sh
set -eu

ROOT=/tmp_workspace/release_candidate
GITDIR="$ROOT/.git"

mkdir -p "$GITDIR/hooks" "$GITDIR/info"

git config --file "$GITDIR/config" core.hooksPath .release-hooks
cp "$ROOT/.release-hooks/pre-commit" "$GITDIR/hooks/pre-commit"
cp "$ROOT/.release-hooks/pre-push" "$GITDIR/hooks/pre-push"
chmod +x "$GITDIR/hooks/pre-commit" "$GITDIR/hooks/pre-push"

printf '\n# release guard generated files\nresults/\n.release_guard_state/\n' >> "$GITDIR/info/exclude"
mkdir -p "$ROOT/.release_guard_state"
date -u > "$ROOT/.release_guard_state/installed_at"
