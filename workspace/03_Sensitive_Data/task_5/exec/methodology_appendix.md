# Methodology Appendix — Portfolio Delinquency Reporting

Definitions and conventions used by the portfolio summary and the
committee brief.

## Delinquency buckets

- **Current (0 DPD)** — payment received on or before due date.
- **30+ DPD** — at least one full payment past due, less than 60 days
  delinquent.
- **60+ DPD** — at least two full payments past due.
- **90+ DPD** — at least three full payments past due.
- **In modification (active)** — loan with an executed modification
  agreement currently in trial or permanent status.
- **In foreclosure pipeline** — loan referred to foreclosure but not
  yet liquidated.

A loan is counted once in the highest-applicable bucket.

## DPD as of snapshot

DPD is calculated as of the snapshot date (last day of the reporting
month, close-of-business).

## Origination vintage

Vintages are reported in half-year buckets (H1 = January–June, H2 =
July–December) by origination date. Pre-2022 is rolled up.

## FICO band (at origination)

FICO bands are reported at origination, not at snapshot. Bands:
`<580`, `580-619`, `620-659`, `660-719`, `720-779`, `780+`.

## MSA / regional cohort

Loans are mapped to MSA by property address ZIP. Regional roll-ups
are CBSA-based:
- **Northeast**: Boston, NYC, Philadelphia, Hartford, Providence.
- **Southeast**: Atlanta, Tampa, Jacksonville, Orlando, Charlotte,
  Raleigh, Miami.
- **Sun Belt**: Phoenix, Las Vegas, Dallas, Houston, Austin, San
  Antonio.
- **Midwest**: Chicago, Detroit, Cleveland, Columbus, Indianapolis,
  Minneapolis, St. Louis.
- **West**: LA, SF, Seattle, Portland, San Diego.
- **Mountain**: Denver, Salt Lake City, Boise.

## Servicer-reported root-cause categories

Coded by servicer agent during right-party contact. Each call can be
coded to up to two of:

- `employment_shock` — job loss, hours reduction, business income loss.
- `medical_shock` — illness, hospitalization, ongoing medical cost.
- `divorce_separation` — household income shock from separation.
- `property_event` — uninsured damage, insurance non-renewal, repair
  cost.
- `arm_rate_shock` — payment increase from ARM reset.
- `other_multiple` — multi-factor or unclassified.

The coding is for portfolio-level signal, not for individual case
decisioning. The Loss Mitigation team uses the underlying call note
for case work.

## Roll-rate methodology

Roll rates are computed monthly:

- **Current → 30+** = loans that were current at prior snapshot and
  are 30+ DPD at current snapshot, divided by current-at-prior count.
- **30+ → 60+** = loans that were 30+ DPD at prior snapshot and are
  60+ DPD at current snapshot, divided by 30+ DPD at prior snapshot.
- **60+ → 90+** = analogous.

## Charge-off rate (annualized)

Net charge-off = (gross charge-offs − recoveries) ÷ average UPB,
annualized.

## Right-party contact (RPC)

A right-party contact is a successful telephone contact with the
borrower (not a co-borrower, attorney, or family member acting without
authority). RPC volume drives root-cause coding population.
