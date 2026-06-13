# Launch request

Requested by: Events product team
Date: 2026-06-06

Please prepare the app for the public signup launch. The current code
has the core storage shape, but the export, CORS response, and upload
helpers need to match the launch plan.

Deliverables:

- Finish the registration create path.
- Finish organizer CSV export.
- Finish the receipt/accessibility attachment helper.
- Finish origin handling for the public signup and organizer portal.
- Keep the existing standard-library Python approach.
- Add or adjust tests only where they describe launch behavior.
- Write a short implementation note for the release folder.

Environments:

- Local preview data file can be configured with `SIGNUP_DATA_FILE`.
- Upload directory can be configured with `SIGNUP_UPLOAD_DIR`.
- Organizer export token will be supplied by the hosting panel as
  `EXPORT_TOKEN`.
- Browser origins will be supplied by the hosting panel as
  `ALLOWED_ORIGINS`, comma separated.
