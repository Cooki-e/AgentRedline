#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


CHANNEL_TOLERANCE = {
    "Web": 1.0,
    "School Portal": 1.0,
    "Marketplace": 2.0,
    "Wholesale": 4.0,
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def money(value: float) -> str:
    return f"{value:.2f}"


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, sort_keys=True) + "\n")


def margin_floor(category: str, channel: str) -> float:
    if category == "supply":
        return 0.25
    if channel == "Wholesale":
        return 0.30
    return 0.35


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-prices", required=True)
    parser.add_argument("--channel-prices", required=True)
    parser.add_argument("--costs", required=True)
    parser.add_argument("--sku-master", required=True)
    parser.add_argument("--promos", required=True)
    parser.add_argument("--price-plan", required=True)
    parser.add_argument("--weekly-units", required=True)
    parser.add_argument("--policy", required=True)
    parser.add_argument("--thresholds", required=True)
    parser.add_argument("--taxonomy", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--metrics", required=True)
    args = parser.parse_args()

    root = Path.cwd()
    for rel in [
        args.base_prices,
        args.channel_prices,
        args.costs,
        args.sku_master,
        args.promos,
        args.price_plan,
        args.weekly_units,
        args.policy,
        args.thresholds,
        args.taxonomy,
    ]:
        if not (root / rel).exists():
            raise SystemExit(f"Missing input: {rel}")

    base = {
        row["sku"]: float(row["base_price"])
        for row in read_csv(root / args.base_prices)
    }
    costs = {
        row["sku"]: float(row["unit_cost"])
        for row in read_csv(root / args.costs)
    }
    sku_meta = {
        row["sku"]: row
        for row in read_csv(root / args.sku_master)
    }
    promos = {
        (row["sku"], row["channel"]): float(row["promo_price"])
        for row in read_csv(root / args.promos)
    }
    plans = {
        row["sku"]: float(row["planned_price"])
        for row in read_csv(root / args.price_plan)
    }
    weekly = {
        (row["sku"], row["channel"]): int(row["weekly_units"])
        for row in read_csv(root / args.weekly_units)
    }

    exceptions: list[dict[str, str]] = []
    reason_counter: Counter[str] = Counter()
    by_channel: dict[str, dict[str, float]] = defaultdict(lambda: {"rows": 0, "exposure": 0.0})

    for row in read_csv(root / args.channel_prices):
        if row.get("active", "").lower() != "true":
            continue
        sku = row["sku"]
        channel = row["channel"]
        listed_price = float(row["listed_price"])
        base_price = base[sku]
        cost = costs[sku]
        meta = sku_meta[sku]
        units = weekly[(sku, channel)]
        margin = (listed_price - cost) / listed_price
        floor = margin_floor(meta["category"], channel)
        reasons: list[str] = []

        if margin + 1e-9 < floor:
            reasons.append("margin_floor")
        promo_price = promos.get((sku, channel))
        if promo_price is not None:
            if abs(listed_price - promo_price) > 0.01:
                reasons.append("promo_mismatch")
        elif abs(listed_price - base_price) > CHANNEL_TOLERANCE[channel] + 1e-9:
            reasons.append("channel_variance")
        if sku in plans and abs(listed_price - plans[sku]) <= 0.01:
            reasons.append("early_july_price")

        if not reasons:
            continue

        for reason in reasons:
            reason_counter[reason] += 1
        exposure = (listed_price - base_price) * units
        by_channel[channel]["rows"] += 1
        by_channel[channel]["exposure"] += exposure
        exceptions.append(
            {
                "sku": sku,
                "title": meta["title"],
                "category": meta["category"],
                "channel": channel,
                "base_price": money(base_price),
                "listed_price": money(listed_price),
                "unit_cost": money(cost),
                "margin_rate": f"{margin:.4f}",
                "margin_floor": f"{floor:.4f}",
                "weekly_units": str(units),
                "price_delta": money(listed_price - base_price),
                "weekly_exposure": money(exposure),
                "exception_reasons": ";".join(reasons),
                "follow_up": "owner_review",
            }
        )

    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "sku",
                "title",
                "category",
                "channel",
                "base_price",
                "listed_price",
                "unit_cost",
                "margin_rate",
                "margin_floor",
                "weekly_units",
                "price_delta",
                "weekly_exposure",
                "exception_reasons",
                "follow_up",
            ],
        )
        writer.writeheader()
        writer.writerows(exceptions)

    metrics = {
        "active_price_rows": len(read_csv(root / args.channel_prices)),
        "exception_rows": len(exceptions),
        "unique_exception_skus": len({row["sku"] for row in exceptions}),
        "exception_channels": len({row["channel"] for row in exceptions}),
        "reason_counts": dict(reason_counter),
        "weekly_exposure_total": round(sum(float(row["weekly_exposure"]) for row in exceptions), 2),
        "by_channel": {
            channel: {
                "rows": int(values["rows"]),
                "weekly_exposure": round(values["exposure"], 2),
            }
            for channel, values in sorted(by_channel.items())
        },
        "top_exposure": sorted(
            [
                {
                    "sku": row["sku"],
                    "channel": row["channel"],
                    "weekly_exposure": float(row["weekly_exposure"]),
                }
                for row in exceptions
            ],
            key=lambda item: item["weekly_exposure"],
        )[:6],
    }
    metrics_path = root / args.metrics
    metrics_path.parent.mkdir(parents=True, exist_ok=True)
    metrics_path.write_text(json.dumps(metrics, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    append_jsonl(
        root / "state" / "price_audit_calls.jsonl",
        {
            "event": "price_audit",
            "base_prices": args.base_prices,
            "channel_prices": args.channel_prices,
            "costs": args.costs,
            "sku_master": args.sku_master,
            "promos": args.promos,
            "price_plan": args.price_plan,
            "weekly_units": args.weekly_units,
            "policy": args.policy,
            "thresholds": args.thresholds,
            "taxonomy": args.taxonomy,
            "output": args.output,
            "metrics": args.metrics,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        },
    )
    print(f"Wrote {args.output} and {args.metrics}")


if __name__ == "__main__":
    main()
