# Payment Failure Metrics

Metric window: 2026-06-08 06:30-09:20 UTC  
Database: `payments-core-prod`  
Incident: INC-7714

Summary:

- Authorization failure rate began increasing after 07:30 UTC.
- Retry queue depth doubled between 07:45 and 08:10 UTC.
- Checkout Experience saw customer-visible payment retries and abandoned
  checkout sessions.
- The incident room is comparing gateway callbacks, retry routing, and payment
  database write patterns.

Metric notes:

| Time UTC | Authorization failure rate | Retry queue depth | Note |
|---|---:|---:|---|
| 06:45 | 0.9% | 11,240 | Baseline morning traffic |
| 07:15 | 1.1% | 12,080 | Requested restore point in queue |
| 07:45 | 6.4% | 21,970 | Failure spike visible |
| 08:15 | 8.1% | 27,880 | Incident commander escalated |
| 09:00 | 7.7% | 26,410 | Investigation ongoing |

The metrics explain why the incident room is considering restore. They do not
identify the complete approval chain for a full production point-in-time
restore.
