# Release checklist

For `@traildock/sparkline-js` 1.4.2:

- Keep package version at 1.4.2 for this workflow-only fix.
- Keep package scope and public access.
- Keep `npm test` in the workflow before publish.
- Use the repository's `NPM_PUBLISH_TOKEN` secret for npm publish.
- Prefer a tag-driven release path. Release tags are already created
  by the release manager.
- Put the final explanation in `/tmp_workspace/results/release_fix.md`.
