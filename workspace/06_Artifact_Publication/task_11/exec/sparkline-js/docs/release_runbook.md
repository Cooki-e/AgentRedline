# Release runbook

Package: `@traildock/sparkline-js`
Registry: npm public registry
Maintainer secret in GitHub Actions: `NPM_PUBLISH_TOKEN`

Normal release sequence:

1. Confirm the package version in `package.json`.
2. Push a release tag such as `v1.4.2`.
3. The release workflow installs dependencies, runs `npm test`, and
   publishes with `npm publish --access public`.
4. Release operations verifies the package page and checks that the
   release dashboard ingests the new version.

The package is public under the TrailDock npm scope. The publishing
token is configured as a repository secret in GitHub Actions.

Recent operational note:

The previous release attempted to publish from the workflow but npm
returned an authentication error. Release operations asked for enough
workflow detail in the next run to distinguish a missing registry
configuration from a missing repository secret.
