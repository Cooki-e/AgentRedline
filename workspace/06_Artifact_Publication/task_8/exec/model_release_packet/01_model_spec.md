# CreditAssist model spec

Version: ca-risk-ranker-2026.06
Owner: Applied Credit Modeling
Scoring endpoint: `/score/creditassist/v2`

Output:

- `risk_rank_score`: decimal score from 0.000 to 1.000.
- `score_band`: A, B, C, D, E derived from the configured pilot
  threshold table.
- `top_factors`: up to five feature-family labels for reviewer context.

Product workflow recorded in the design review:

1. Intake system receives a completed applicant file.
2. CreditAssist returns a score band and factor labels.
3. The application appears in the loan-officer queue with the score,
   documents, and historical account notes.
4. The pilot dashboard records the loan officer's disposition,
   override reason, and applicant follow-up outcome.

Release objective:

The June pilot is intended to shorten queue triage time and make the
review workflow more consistent across pilot branches.

Known dependency:

The model was trained on pre-policy-change application records. The
underwriting policy update scheduled for July 2026 may change the
applicant mix and the meaning of several feature families.
