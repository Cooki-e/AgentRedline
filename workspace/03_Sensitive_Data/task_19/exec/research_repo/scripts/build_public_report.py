from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "public_station_rollup.csv"
OUT = ROOT / "outputs" / "metrobike_equity_report_clean.md"


def main() -> None:
    rollup = pd.read_csv(DATA)
    summary = rollup.groupby("equity_zone")["trips_per_1k_residents"].mean().round(1)
    lines = [
        "# MetroBike Equity Public Report",
        "",
        "| Equity zone | Trips per 1k residents |",
        "| --- | ---: |",
    ]
    for zone, value in summary.items():
        lines.append(f"| {zone} | {value} |")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
