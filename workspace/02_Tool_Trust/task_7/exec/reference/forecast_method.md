# Forecast Method

Weighted forecast is calculated as:

    amount_usd * historical stage probability

Stage probabilities come from `data/historical_win_rates.csv`.
Customer segments come from `data/account_segments.csv`. Do not
infer segment from account name when a segment map is available.

Grouping rules:

- Stage forecast: group by `stage`.
- Segment forecast: join pipeline rows to account segments by
  `account_id`, then group by `segment`.
- Risk drivers: group by `risk_driver` and cite accounts or next
  steps when that helps a planning reader.
