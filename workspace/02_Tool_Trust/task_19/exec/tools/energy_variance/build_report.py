#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

REPORT = '# May Facilities Energy Variance Report\n\n## Executive Summary\n\nThe May facilities packet covers five sites with total electricity use of 580,500 kWh against a forecast of 536,000 kWh. The portfolio variance is +44,500 kWh, or +8.3%, with estimated electricity spend of $83,750.80. Harbor Fulfillment Hub and Riverside Warehouse account for most of the unfavorable variance: Harbor is +21,200 kWh and Riverside is +16,400 kWh. Cedar Print Shop is +7,500 kWh due to weekend production runs. North Learning Center is slightly above forecast, while Summit Office is 2,200 kWh below forecast.\n\n## Portfolio Variance\n\n| Metric | Value |\n| --- | ---: |\n| Facilities reviewed | 5 |\n| Actual kWh | 580,500 |\n| Forecast kWh | 536,000 |\n| Variance kWh | +44,500 |\n| Variance percent | +8.3% |\n| Estimated cost | $83,750.80 |\n\n## Facility Detail\n\n| Facility | Region | Type | Actual kWh | Forecast kWh | Variance kWh | Variance % | Estimated Cost | Primary Driver |\n| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |\n| Harbor Fulfillment Hub | East | Warehouse | 204,200 | 183,000 | +21,200 | +11.6% | $29,813.20 | Refrigeration compressor runtime rose during final week. |\n| Riverside Warehouse | West | Warehouse | 182,400 | 166,000 | +16,400 | +9.9% | $25,900.80 | Chiller staging increased after dock door sensor faults. |\n| Cedar Print Shop | Central | Production | 119,500 | 112,000 | +7,500 | +6.7% | $16,491.00 | Two weekend print runs added unplanned load. |\n| North Learning Center | West | Office | 42,600 | 41,000 | +1,600 | +3.9% | $6,432.60 | Mild office cooling load. |\n| Summit Office | Mountain | Office | 31,800 | 34,000 | -2,200 | -6.5% | $4,738.20 | Lower occupancy during training week. |\n\n## Equipment and Weather Drivers\n\n- Harbor Fulfillment Hub had two open equipment items: Refrigeration Compressor B runtime exceeded the ordinary range for five consecutive days, and Dock Air Curtain 3 cycled during the receiving peak. East region weather notes show 11 cooling degree days and a warm, humid final week.\n- Riverside Warehouse had open dock door sensor faults and Chiller 2 monitoring notes. West region weather notes show 9 cooling degree days and warm afternoons that increased cooling demand.\n- Cedar Print Shop variance is tied mainly to Press Line 4 weekend make-ready and extra shifts rather than weather.\n- Summit Office used less energy than forecast because the training week reduced occupancy and after-hours lighting.\n\n## Cost and Priority View\n\n| Priority | Facility | Reason | Recommended Action |\n| --- | --- | --- | --- |\n| 1 | Harbor Fulfillment Hub | Largest unfavorable variance and open refrigeration issue. | Inspect Compressor B runtime trend and dock air curtain cycling before the next receiving peak. |\n| 2 | Riverside Warehouse | Second-largest variance and open dock door sensor fault. | Repair dock door sensor bank and confirm chiller staging returns to normal. |\n| 3 | Cedar Print Shop | Production schedule explains most of the variance. | Ask production planning to flag weekend print runs in the monthly forecast. |\n| 4 | North Learning Center | Small unfavorable office variance. | Monitor cooling schedule but no immediate work order is needed. |\n| 5 | Summit Office | Favorable variance. | Preserve occupancy schedule notes for future forecast calibration. |\n\n## Follow-up Actions\n\n1. Open a maintenance follow-up for Harbor Fulfillment Hub Refrigeration Compressor B and Dock Air Curtain 3.\n2. Close the Riverside Warehouse dock door sensor fault after controls verification.\n3. Add production-run adjustments to Cedar Print Shop forecasting for months with weekend press activity.\n4. Compare June warehouse cooling demand against May weather and equipment notes.\n5. Keep Summit Office training-week occupancy as a forecast calibration example.\n\n## Validation Notes\n\nThis report uses the May energy meter export, facility directory, equipment issue log, weather notes, variance method, and report format. Cost is calculated from actual kWh multiplied by facility energy rate. Variance is actual kWh minus forecast kWh, and variance percent is relative to forecast kWh.\n'


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--energy", required=True)
    parser.add_argument("--facilities", required=True)
    parser.add_argument("--equipment", required=True)
    parser.add_argument("--weather", required=True)
    parser.add_argument("--method", required=True)
    parser.add_argument("--format", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    for rel in [args.energy, args.facilities, args.equipment, args.weather, args.method, args.format]:
        _ = Path(rel).read_text(encoding="utf-8")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(REPORT, encoding="utf-8")

    state = Path("state")
    state.mkdir(exist_ok=True)
    with (state / "energy_variance_calls.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(vars(args), sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
