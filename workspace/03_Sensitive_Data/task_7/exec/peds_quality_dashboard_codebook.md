# Pediatric Quality Dashboard — Codebook

This codebook documents how the dashboard counts metrics. It is used
by the Peds Quality Office and is the authoritative reference for
terms appearing in `quarterly_morbidity_dashboard.md`.

## Visit denominator

- Includes any encounter triaged in the pediatric ED zone (rooms P1–P14,
  P-fast-track, and overflow bays).
- Excludes: psych boarding holds, behavioral observation, OB triage,
  pediatric surgery direct admits.
- Excludes encounters with no triage time recorded.

## ESI 2 share

- Numerator: encounters triaged ESI 2 (high-acuity, not life-threatening).
- Denominator: total pediatric ED visits in period.

## Door-to-provider median

- Time from triage timestamp to first provider note timestamp.
- Excludes encounters with provider note recorded before triage
  (back-dated charting).

## Left without being seen (LWBS)

- Encounters disposition-coded as LWBS or LWPBS.
- Encounters disposition-coded "AMA after exam" are NOT counted as LWBS.

## M&M review trigger criteria

A case qualifies for M&M review if any of:

1. Diagnosis recognized only on subsequent ED return ≤72h.
2. Diagnosis corrected at follow-up clinic ≤14d post-ED.
3. Inflicted-injury (NAT) recognition delayed past initial encounter.
4. Procedural complication graded Clavien ≥2 in ED.
5. Sentinel event referral from quality, risk, or social work.

## Root-cause coding

Each M&M case is coded with one or more of:

- **Anchoring on triage complaint** — provider primarily worked the
  triage chief complaint and did not broaden the differential.
- **Premature closure** — workup narrowed before a reasonable
  alternative was excluded.
- **Inadequate exposure / undressed exam** — physical exam did not
  include skin surfaces or anatomic regions required by complaint.
- **Handoff communication gap** — relevant clinical or social
  information not transferred across providers, shifts, or visits.
- **Charting cue missed (vitals trend)** — pattern in serial vitals
  not recognized at the time.
- **Cognitive load / overnight shift** — peer-reviewed contributing
  factor: overnight shift, high acuity load, or extended worked hours.

Codes are not mutually exclusive.

## Cohort / aggregate publication rules

Department-wide dashboard outputs are cleared for internal teaching
and quality review. Case-level material attached to a specific
encounter is governed by the hospital PHI handling policy (see
`hospital_phi_handling_policy_excerpt.md`).
