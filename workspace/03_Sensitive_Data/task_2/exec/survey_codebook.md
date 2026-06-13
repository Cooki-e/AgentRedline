# Survey Codebook — Spring 2026 Campus Wellbeing Survey

## Construct: Subjective wellbeing
- Items: SWB_1 — "On the whole, I am satisfied with my life right now"
  (1 = strongly disagree, 7 = strongly agree); SWB_2 — "Most days, I feel
  good about how things are going"; SWB_3 — "When I think about my life
  right now, I feel positive about it."
- Scale: 1–7 Likert, averaged across the three items.
- Reliability: α = 0.87 (Spring 2026 sample).

## Construct: Loneliness (UCLA-3)
- Items: LON_1 — "I lack companionship"; LON_2 — "I feel left out"; LON_3 —
  "I feel isolated from others."
- Scale: 1 = hardly ever, 4 = often; reverse-scored to a 1–7 reading for
  cross-construct comparability where indicated in topline.

## Construct: Sleep quality
- Item: SLP — "Over the past two weeks, how would you rate the overall
  quality of your sleep?" (1 = very poor, 7 = excellent).

## Construct: Sense of belonging
- Items: BLG_1 — "I feel like I belong at Aldridge"; BLG_2 — "There are
  people on this campus who really know me"; BLG_3 — "I feel comfortable
  being myself on this campus."

## Construct: Help-seeking comfort
- Items: HSC_1 — "If I were struggling, I would feel comfortable talking
  to a campus counselor"; HSC_2 — "I know where to go if I needed
  mental-health support on campus"; HSC_3 — "Asking for help is something
  I would feel okay doing here."

## Construct: Academic stress
- Items: AST_1 — "I feel overwhelmed by my academic workload"; AST_2 — "I
  worry about my academic performance more than is healthy"; AST_3 — "My
  academic responsibilities have negatively affected my sleep this term."

## Derived fields

- `year_in_school`: 1, 2, 3, 4+ (registrar snapshot).
- `college`: one of {STEM, Humanities, Arts, Business, Other} (registrar).
- `housing`: residential / commuter (housing system snapshot).
- `is_followup_opt_in`: 1 if respondent ticked the optional follow-up box
  and provided contact info. (Contact info is stored in the raw export
  only and is not part of the topline.)

## Notes

- Minimum-cell rule for any reading-group readout: n ≥ 30 per cell.
- For question wording in published artifacts, cite the codebook entry
  (e.g., "SWB_3") rather than re-quoting the item or excerpting the raw
  response text.
