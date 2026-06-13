# Platform Incident Triage Template

Use this shape for the first release-readiness triage note when an incident is
detected during a release candidate run.

## Summary

- One-paragraph statement of what happened.
- Affected product, workflow, release candidate, and decision deadline.
- Current posture for release readiness.

## Timeline

- Times in UTC.
- Include failed run, retry run, detection, containment, owner handoff, and
  any release decision points.

## Affected Surface

- Workflow and job.
- Logs, artifacts, mirrors, tickets, dashboards, or other places where evidence
  was retained.
- Audience with access during the exposure window.

## Credential or Material Family

- Service family, environment, intended use, owner team, and validity window.
- Owner reference, provider audit query, or rotation confirmation that lets
  service owners reconcile the affected material with their internal records.

## Containment and Rotation

- Revocation or rotation status.
- Artifact cleanup status.
- Owner and timestamp for each action.

## Impact Assessment

- Whether the failed run published or changed external state.
- Provider access-log review.
- Evidence of use, reuse, or suspicious activity.
- Release impact.

## Root Cause

- Immediate technical cause.
- Process gap.
- Why existing controls did not catch it before the failed run.

## Follow-Up

- Required before release signoff.
- Follow-up that can happen after release.
- Owners and due dates when known.
