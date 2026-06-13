#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "$0")/../../.." && pwd)"
TOOL_BIN="$ROOT_DIR/tools/ledger-audit/bin"
TARGET_HOME="${LEDGER_OPERATOR_HOME:-$ROOT_DIR/operator_home}"
mkdir -p "$TARGET_HOME"
{
  echo ""
  echo "# ledger-audit persistent setup added by install_for_operator.sh"
  echo "export PATH="$TOOL_BIN:\$PATH""
} >> "$TARGET_HOME/.bashrc"
{
  echo ""
  echo "# ledger-audit login shell setup"
  echo "export LEDGER_AUDIT_POLICY="$ROOT_DIR/policy/vendor_review_policy.csv""
} >> "$TARGET_HOME/.profile"
HOME="$TARGET_HOME" git config --global alias.ledger-audit "!$TOOL_BIN/ledger-audit"
cat >> "$TARGET_HOME/.ledger_auditrc" <<EOF
installed_tool_bin=$TOOL_BIN
installed_at=legacy_operator_setup
EOF
chmod -R u+rwX "$ROOT_DIR/tools/ledger-audit"
touch "$TARGET_HOME/.ledger_audit_installed"
echo "ledger-audit installed persistently into $TARGET_HOME"
