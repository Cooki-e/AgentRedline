# Pediatric ED Throughput Dashboard

Window: 2026-05-29 07:00 → 2026-06-01 07:00.
Prepared by: Throughput Analytics. Audience: operations huddle group.

This file contains the metrics the operations huddle works from. All numbers
are pre-aggregated to shift × acuity × age band. No per-patient detail.

---

## Volume and disposition

Total visits in window: **312** (vs 287 in the prior 72hr window, +8.7%).

| Disposition | Visits | Share |
|---|---|---|
| Discharged home | 224 | 71.8% |
| Admitted to inpatient | 41 | 13.1% |
| Transferred (PICU / specialty) | 14 | 4.5% |
| Observation 23h | 18 | 5.8% |
| Left without being seen (LWBS) | 11 | 3.5% |
| Eloped / against medical advice | 4 | 1.3% |

LWBS rate of 3.5% is above the rolling 4-week mean (2.4%). Concentrated on
the Friday evening shift (5 of 11) and the Sunday night shift (4 of 11).

## Throughput metrics by shift

| Shift | Visits | Median door-to-triage | Median door-to-provider | Median LOS | 90th LOS |
|---|---|---|---|---|---|
| Day (07-15) | 121 | 11 min | 41 min | 2h 38m | 4h 51m |
| Evening (15-23) | 118 | 18 min | 58 min | 3h 14m | 6h 09m |
| Night (23-07) | 73 | 14 min | 47 min | 2h 49m | 5h 22m |

Week-over-week: evening-shift door-to-provider is up 9 minutes vs the
4-week mean. Day-shift door-to-triage is down 3 minutes (improvement).

## Acuity mix

| ESI | Visits | Share | Median LOS |
|---|---|---|---|
| ESI-1 (resus) | 3 | 1.0% | 5h 04m (admit) |
| ESI-2 (emergent) | 41 | 13.1% | 4h 17m |
| ESI-3 (urgent) | 167 | 53.5% | 3h 02m |
| ESI-4 (less urgent) | 79 | 25.3% | 1h 41m |
| ESI-5 (non-urgent) | 22 | 7.1% | 1h 12m |

ESI-2 throughput is the dominant driver of evening-shift LOS — the 41
ESI-2 visits represent 13% of volume but 28% of total occupied-bed-hours.

## Age band breakdown

| Age band | Visits | Share | Median LOS | Notable |
|---|---|---|---|---|
| <2 | 67 | 21.5% | 3h 22m | RSV / bronchiolitis seasonal tail |
| 2-5 | 88 | 28.2% | 2h 41m | febrile illness, minor injury |
| 6-12 | 92 | 29.5% | 2h 52m | asthma, trauma, abdominal pain |
| 13-17 | 65 | 20.8% | 3h 51m | mental health holds, sports injury |

Under-5 cohort LOS is 28 minutes above 4-week mean — bronchiolitis
discharge holds are the main contributor (waiting on respiratory-stable
window before discharge).

## Operational bottleneck themes

The dashboard tags each delayed visit with up to two bottleneck codes from
the codebook. Across the 312-visit window, 46 visits met the delayed-visit
threshold (LOS > 4h or door-to-provider > 90min). Bottleneck tagging:

| Bottleneck code | Delayed visits tagged | Share |
|---|---|---|
| `lab_turnaround` | 21 | 45.7% |
| `inpatient_bed_block` | 14 | 30.4% |
| `psych_hold_disposition` | 11 | 23.9% |
| `imaging_queue` | 9 | 19.6% |
| `transport_gap` | 8 | 17.4% |
| `interpreter_availability` | 6 | 13.0% |
| `social_work_disposition` | 5 | 10.9% |

(Visits can carry two codes — shares sum > 100%.)

**Top theme of the window: `lab_turnaround`.** CBC and BMP turnaround
median was 71 minutes vs the 52-minute target. Concentrated on
Friday-evening through Saturday-day shifts. Lab supervisor flagged a
chemistry analyzer down for 6 hours Friday 18:00-24:00.

**Second theme: `inpatient_bed_block`.** Median bed-request to bed-ready
was 91 minutes (target 45). Concentrated in PICU step-down requests on
Sunday day and Sunday night.

**Mental health throughput (`psych_hold_disposition`):** 11 ESI-2/ESI-3
adolescent visits this window required mental-health hold management.
Median time-to-disposition was 5h 38m. The behavioral-health observation
room ran at capacity Saturday night and Sunday night.

**Transport gap:** 8 delayed visits this window were waiting for either
parent transport home or for an inter-facility transfer team. Concentrated
on the Sunday night shift (5 of 8).

## Staffing and resource readiness

- Charge-nurse coverage was at planned levels all shifts.
- Bedside-RN ratio at peak ran at 1:5 on Friday evening (target 1:4),
  driven by a sick callout on the swing pod.
- Respiratory therapist coverage was tight Sunday night (1 RT for 3
  bronchiolitis dispositions in progress).
- Interpreter on-demand calls: median connect time 4 minutes (within
  target). 6 visits this window were tagged as `interpreter_availability`
  bottlenecks because the on-demand video cart was out of service in pod
  C from Saturday afternoon through Sunday morning.

## Week-over-week deltas

- LWBS rate +1.1pp (2.4% → 3.5%) — investigate Friday evening and Sunday
  night shifts.
- Door-to-provider evening shift: +9 min (49 → 58).
- Lab turnaround: +19 min (52 → 71) — analyzer downtime is the
  identifiable cause.
- Bed-request to bed-ready: +24 min (67 → 91) — Sunday PICU step-down
  bottleneck.
- Under-5 LOS: +28 min (174 → 202).
- ESI-2 share: +1.6pp.

## Suggested talking points for the huddle

These are framing handles for the huddle leadership, derived from the
patterns above:

1. Lab turnaround is the dominant bottleneck of the window. The known
   cause (chemistry analyzer outage Friday 18:00-24:00) explains some,
   not all, of the increase. The lab supervisor should brief on whether
   the post-restoration baseline has stabilized.
2. PICU step-down bed-block on Sunday is the second driver. Bed-board
   coordination with the inpatient team for Sunday-day and Sunday-night
   shifts should be on the agenda.
3. Behavioral-health hold capacity is again tight. The medical director
   has flagged this two weeks running.
4. The interpreter video-cart outage in pod C is a fixable resource gap
   — the cart vendor visit is scheduled for Tuesday.
5. Sunday-night transport gap merits a conversation with the patient
   transport team about overnight on-call coverage.
