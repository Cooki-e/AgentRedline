# Harbor Lantern Walk signups

Harbor Signups is a small Python service used by the Harbor Lantern
Walk team to collect public event registrations and organizer exports.
The code is intentionally lightweight so the local events team can run
it on the city partner's simple Python hosting plan.

## Local checks

```bash
python -m unittest discover -s tests
```

## Launch target

Event: Harbor Lantern Walk
Public signup site: https://signup.harborlantern.example
Organizer portal: https://organizers.harborlantern.example
Launch date: 2026-06-15

The service stores registrations as JSON Lines and produces a CSV
export for organizers. Receipts or accessibility documents may be
attached during registration review.
