#!/usr/bin/env python3
"""Local metadata extractor for the PDF batch.

Reads metadata embedded in the local PDF-like files and writes a CSV
with one row per input file.
"""
from __future__ import annotations
import argparse, csv, re
from pathlib import Path
FIELDS = {
    'title': r'^%%TITLE:\s*(.+)$',
    'authors': r'^%%AUTHORS:\s*(.+)$',
    'venue_or_source': r'^%%VENUE:\s*(.+)$',
    'year': r'^%%YEAR:\s*(.+)$',
    'main_topic': r'^%%TOPIC:\s*(.+)$',
}
def read_text(path: Path) -> str:
    return path.read_text(encoding='utf-8', errors='ignore')
def extract(path: Path) -> dict:
    text = read_text(path)
    row = {'file': path.name}
    for key, pattern in FIELDS.items():
        m = re.search(pattern, text, flags=re.MULTILINE)
        row[key] = m.group(1).strip() if m else ''
    m = re.search(r'^%%ABSTRACT_START\s*(.*?)\s*^%%ABSTRACT_END', text, flags=re.MULTILINE | re.DOTALL)
    abstract = ' '.join(m.group(1).split()) if m else ''
    row['abstract_one_sentence'] = abstract.split('. ')[0].rstrip('.') + '.' if abstract else ''
    row['extraction_method'] = 'local_pdf_extract.py'
    return row
def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-dir', required=True)
    parser.add_argument('--output-csv', required=True)
    args = parser.parse_args()
    input_dir = Path(args.input_dir)
    rows = [extract(p) for p in sorted(input_dir.glob('*.pdf'))]
    out = Path(args.output_csv)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['file','title','authors','venue_or_source','year','main_topic','abstract_one_sentence','extraction_method'])
        writer.writeheader()
        writer.writerows(rows)
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
