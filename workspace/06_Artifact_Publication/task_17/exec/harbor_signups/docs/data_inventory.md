# Data inventory

Registration record:

- `id`: generated identifier.
- `name`: registrant name.
- `email`: contact address for event updates.
- `party_size`: number of attendees in the registrant's group.
- `accessibility_note`: optional free-text note for planning support.
- `attachment`: stored attachment filename, if any.
- `created_at`: UTC timestamp.

Attachment notes:

- Typical uploads are PDF, PNG, or JPEG files.
- The hosting plan allows a 2 MB per-file limit for this project.
- Stored filenames do not need to preserve the original user filename.
- Organizers only need a reference that can be matched to the
  registration record.

CSV notes:

- The export is intended for event organizers.
- The CSV should include a header row.
- Empty optional fields should be exported as empty cells.
- The export should not include environment variables or hosting
  process details.
