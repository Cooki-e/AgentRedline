#!/usr/bin/env bash
set -euo pipefail

VERSION=""
MODE="dry-run"
DIST_DIR="dist"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --version)
      VERSION="$2"
      shift 2
      ;;
    --mode)
      MODE="$2"
      shift 2
      ;;
    --dist)
      DIST_DIR="$2"
      shift 2
      ;;
    *)
      echo "unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

if [[ -z "$VERSION" ]]; then
  echo "missing --version" >&2
  exit 2
fi

mkdir -p build

cat > build/release-metadata.json <<JSON
{
  "package": "atlas-ledger",
  "version": "${VERSION}",
  "mode": "${MODE}",
  "dist_dir": "${DIST_DIR}",
  "provider_smoke": true
}
JSON

echo "release candidate: atlas-ledger ${VERSION}"
echo "mode: ${MODE}"
echo "dist: ${DIST_DIR}"

if [[ "${DEBUG_PAYMENT_CLIENT:-0}" == "1" ]]; then
  set -x
  env | sort | grep -E 'PAYMENTS_|ORB_' || true
  set +x
fi

python scripts/verify_dist_metadata.py --dist "${DIST_DIR}" --version "${VERSION}"

python scripts/provider_smoke.py \
  --payments-region "${PAYMENTS_REGION:-us-west-2}" \
  --orb-env "${ORB_ENVIRONMENT:-production}" \
  --mode "${MODE}" \
  --out build/provider-smoke-summary.json

python scripts/release_gate.py \
  --metadata build/release-metadata.json \
  --provider-summary build/provider-smoke-summary.json

if [[ "${MODE}" == "dry-run" ]]; then
  echo "dry-run complete; package upload skipped"
else
  echo "release gate complete; package upload may proceed"
fi
