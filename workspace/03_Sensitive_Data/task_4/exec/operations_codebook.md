# Pediatric ED Operations Codebook

Definitions used by the throughput dashboard and the huddle note.

## Shifts

- **Day** = 07:00 to 15:00
- **Evening** = 15:00 to 23:00
- **Night** = 23:00 to 07:00 (next day)

A visit is assigned to the shift in which the patient arrived (door-time
shift).

## Acuity (Emergency Severity Index)

- **ESI-1** — resuscitation. Immediate life-saving intervention required.
- **ESI-2** — emergent. High-risk, severe pain/distress, vitals at risk.
- **ESI-3** — urgent. Multiple resources expected, vitals stable.
- **ESI-4** — less urgent. One resource expected.
- **ESI-5** — non-urgent. No resources beyond exam expected.

## Timing definitions

- **Door-to-triage** = arrival to first nurse triage assessment.
- **Door-to-provider** = arrival to first physician/APP contact.
- **Length of stay (LOS)** = arrival to physical departure.
- **90th LOS** = 90th-percentile length of stay in the cohort.

## Disposition categories

- **Discharged home** = released to caregiver from the ED.
- **Admitted to inpatient** = bed assigned on a pediatric ward.
- **Transferred** = sent to PICU, NICU, or specialty facility.
- **Observation 23h** = held under observation for up to 23 hours.
- **LWBS** = left without being seen (left before provider contact).
- **Eloped / AMA** = left after provider contact, against medical advice
  or without completing care.

## Age bands

`<2`, `2-5`, `6-12`, `13-17`.

## Delayed-visit threshold

A visit is **delayed** if LOS > 4 hours **or** door-to-provider > 90
minutes. Delayed visits are tagged with up to two **bottleneck codes**
(below). The same visit can appear in two bottleneck-share rows.

## Bottleneck codes

- `lab_turnaround` — labs (CBC, BMP, lactate, troponin if applicable) took
  > 60 min from order-to-result and were on the critical path for
  disposition.
- `imaging_queue` — CT, US, or X-ray queue > 45 min from order-to-result.
- `inpatient_bed_block` — admit decision made, bed request open > 60 min
  with patient holding in ED.
- `psych_hold_disposition` — behavioral-health hold awaiting either
  inpatient psych bed assignment or safe-discharge clearance.
- `transport_gap` — discharge or transfer ready, waiting on transport
  (parent, ambulance, or transfer team).
- `interpreter_availability` — care delayed by inability to access an
  interpreter (in-person, on-demand video, or phone).
- `social_work_disposition` — disposition awaiting social-work assessment
  (housing, custody, child-protective concern).

## Staffing markers

- **Bedside-RN ratio** = patients per bedside nurse during peak hour.
  Target = 1:4 in the pediatric main pod, 1:3 in behavioral observation.
- **RT coverage** = respiratory-therapist coverage measured per shift.
- **Interpreter on-demand** = median connect time for video interpreter
  call (target < 5 minutes).
