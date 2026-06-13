# Support SLA Policy

The June SLA summary measures resolved tickets where `sla_paused`
is false. Exclude open tickets and paused tickets from the measured
denominator, but mention excluded records in validation notes when
they explain denominator differences.

Targets by priority:

| Priority | First Response Target | Resolution Target |
| --- | ---: | ---: |
| P1 | 30 minutes | 240 minutes |
| P2 | 60 minutes | 480 minutes |
| P3 | 240 minutes | 1440 minutes |
| P4 | 480 minutes | 2880 minutes |

Calculate compliance as tickets meeting the target divided by
measured tickets in the group. A ticket meets the target when the
observed minutes are less than or equal to the target minutes.
