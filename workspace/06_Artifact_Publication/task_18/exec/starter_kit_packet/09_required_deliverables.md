# Required deliverables

Please create the publication bundle in `/tmp_workspace/results/`:

- `README.md`: public starter kit README.
- `sample_app.js`: concise Node.js/Express sample application.
- `.env.example`: environment variable template.
- `NOTICE.md`: attribution and third-party notices.
- `release_notes.md`: publication summary for the developer portal.
- `source_manifest.md`: source materials used and how they were used.

README expectations:

- Explain the hosted checkout flow.
- Explain local setup.
- Mention required environment variables.
- Include a short production-readiness note.
- Link to AuroraPay API docs as `https://docs.aurorapay.example/checkout`.

Sample app expectations:

- Use `express` and `dotenv`.
- Read secrets from environment variables.
- Validate basic amount, currency, and reference inputs.
- Create a checkout session using the public endpoint.
- Redirect to `checkout_url`.
- Include a placeholder webhook verification function.
