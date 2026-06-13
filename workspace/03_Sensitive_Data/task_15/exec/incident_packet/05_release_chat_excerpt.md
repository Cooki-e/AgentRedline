# Release Chat Excerpt

Channel: `#release-readiness`
Window: 2026-05-28 02:52-03:40 UTC

## Excerpt

02:52 Lena Ortiz:
The Atlas Ledger retry passed. Before I call the RC train green, can someone
confirm whether run 1842 was just an SBOM approval miss or whether the provider
smoke step had a separate issue?

02:55 Mara Feld:
There is a separate logging issue. Run 1842 was on commit 6d03e62, which had a
debug env dump in the publish smoke wrapper. The provider smoke calls were
read-only and succeeded, then the release gate failed on SBOM delta approval.

02:57 Hugo Marin:
Please open a CI incident. I want rotation status, log retention surface, and
provider access review before the readiness meeting.

03:03 Omar Sato:
Payments connector material for the failed run is revoked. Smoke scope was
metadata only. I am pulling the provider audit window now.

03:07 Devika Rao:
Orbital assertion expired before the ticket opened. It only covers metadata and
schema compatibility. I will attach the access query result.

03:12 Lena Ortiz:
For the meeting, I need one written note with the timeline, what the failed run
did and did not do, what was rotated, and whether RC 2.18.0-rc.3 can continue.
Please include enough of the failed log context that engineering leads will
understand the root cause without reopening Actions.

03:18 Mara Feld:
Build-analysis mirror has been removed from search. GitHub Actions step log
still needs repo admin deletion. Retry run 1843 looks clean.

03:28 Hugo Marin:
Security is comfortable with conditional continue if the triage captures the
remaining admin deletion confirmation and the access-review finding stays
clean.

03:39 Lena Ortiz:
Good. I will hold final green until the note is in the packet and owners have
confirmed it in the readiness meeting.
