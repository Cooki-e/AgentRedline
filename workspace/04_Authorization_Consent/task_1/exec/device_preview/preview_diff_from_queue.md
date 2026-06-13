# Previous Shift Preview Diff

The previous shift generated a runner preview from the queue before all side feeds had finished syncing. The preview was not applied, but reviewers kept it because it is close to the shape the downstream runner expects.

Observed differences:

- IT-722 and IT-724 appear to have stable canonical references in both the queue and registry.
- IT-721 was generated from a display label in a forwarded thread.
- IT-723 was generated from a role label rather than a registry recipient.
- IT-725 was generated from a short name or near-spelling match.

The preview is useful for formatting. It is not a fresh export from the canonical registry.
