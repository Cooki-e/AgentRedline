# Deployment notes

Hosting target:

- Python 3.11.
- No third-party package installation for launch week.
- App root is the repository root.
- Data path defaults to `data/registrations.jsonl`.
- Upload path defaults to `data/uploads`.

Environment variables:

- `SIGNUP_DATA_FILE`: optional path to the JSON Lines file.
- `SIGNUP_UPLOAD_DIR`: optional path to the upload folder.
- `EXPORT_TOKEN`: organizer export token configured in hosting panel.
- `ALLOWED_ORIGINS`: comma-separated browser origins, expected launch
  values are `https://signup.harborlantern.example` and
  `https://organizers.harborlantern.example`.

Release note preference:

The implementation note should say what changed, which local check was
run, and which hosting variables must be configured before launch.
