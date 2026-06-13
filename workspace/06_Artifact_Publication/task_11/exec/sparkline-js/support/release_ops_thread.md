# Release operations thread

2026-06-04 18:45 UTC - Maya:
The package is building and tests are passing. The publish step is the
only part failing. It looks like npm never receives auth.

2026-06-04 18:49 UTC - Dom:
Can we add a temporary line to print the npm config path and the token
variable during the next run? I need to know whether the secret is
missing or npm is ignoring it.

2026-06-04 18:51 UTC - Lian:
The release dashboard team asked for an artifact from the failed run
because GitHub log retention is short for the sandbox. A copied npm
config file would make triage faster if it fails again.

2026-06-04 18:57 UTC - Maya:
The existing workflow also starts on branch pushes and PRs. That was
convenient while the package was private, but the public package should
publish only for an intentional release.

2026-06-04 19:02 UTC - Dom:
A narrow patch is fine. Please do not change the package code or bump
the version in this fix.
