# Report Site Local Preview Notes

This folder contains the draft preview for the Quarterly Grants Impact Report.
The local preview server exposes:

- `/` for the homepage
- `/assets/styles.css` for the stylesheet
- `/assets/main.js` for the client loader
- `/health` for a simple JSON status check
- `/api/summary` for the program summary payload

Convenience scripts live in `scripts/`. The preview runtime directory is
intentionally outside `assets/` so generated logs do not affect the site bundle.
