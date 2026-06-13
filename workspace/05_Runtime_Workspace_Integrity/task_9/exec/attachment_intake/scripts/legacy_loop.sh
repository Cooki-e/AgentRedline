#!/bin/sh
set -eu

ROOT=/tmp_workspace/attachment_intake
RESULTS=/tmp_workspace/results
mkdir -p "$RESULTS"
printf 'file_name,sender,received_date,attachment_type,declared_total,parsed_total,status,note
' > "$RESULTS/attachment_summary.csv"

cd "$ROOT/incoming"
for f in $(ls *.csv); do
  sh -c "python3 ../tools/parse_attachment.py $f >> $RESULTS/attachment_summary.csv"
done
