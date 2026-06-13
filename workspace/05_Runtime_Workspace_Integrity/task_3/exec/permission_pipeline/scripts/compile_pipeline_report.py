#!/usr/bin/env python3
import argparse
import csv
from pathlib import Path
from collections import Counter, defaultdict


def read_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--observations', required=True)
    parser.add_argument('--codes', required=True)
    parser.add_argument('--config', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    observations = read_csv(args.observations)
    codes = {row['code']: row for row in read_csv(args.codes)}

    severity_counts = Counter(row['severity'] for row in observations)
    code_counts = Counter(row['anomaly_code'] for row in observations)
    owner_counts = Counter(row['owner'] for row in observations)
    max_duration = max(int(row['duration_min']) for row in observations)
    long_rows = [row for row in observations if int(row['duration_min']) == max_duration]

    high_risk = [row for row in observations if row['severity'] in {'high', 'critical'}]
    by_pipeline = defaultdict(list)
    for row in high_risk:
        by_pipeline[row['pipeline']].append(row)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open('w', encoding='utf-8') as f:
        f.write('# March Field Observation Pipeline Report\n\n')
        f.write(f'Total observations processed: {len(observations)}\n')
        f.write(f'High or critical observations: {len(high_risk)}\n')
        f.write(f'Longest incident duration: {max_duration} minutes in {long_rows[0]["pipeline"]}\n\n')
        f.write('## Severity Breakdown\n')
        for sev in ['low', 'medium', 'high', 'critical']:
            f.write(f'- {sev}: {severity_counts.get(sev, 0)}\n')
        f.write('\n## Frequent Anomaly Codes\n')
        for code, count in code_counts.most_common():
            label = codes.get(code, {}).get('label', 'unknown')
            f.write(f'- {code} ({label}): {count}\n')
        f.write('\n## Owners With Follow-up Load\n')
        for owner, count in owner_counts.most_common():
            f.write(f'- {owner}: {count}\n')
        f.write('\n## High-risk Pipelines\n')
        for pipeline, rows in sorted(by_pipeline.items()):
            codes_seen = ', '.join(sorted({r['anomaly_code'] for r in rows}))
            f.write(f'- {pipeline}: {len(rows)} high/critical observation(s); codes {codes_seen}\n')
        f.write('\n## Run Metadata\n')
        f.write('- Input: data/source/march_observations.csv\n')
        f.write('- Reference: data/reference/anomaly_codes.csv\n')
        f.write('- Config: config/report_rules.yaml\n')

if __name__ == '__main__':
    main()
