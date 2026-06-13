# npm publish failure excerpt

Workflow run: release / publish
Commit: 0b7ad13
Branch: main
Attempt: 2026-06-04 18:22 UTC

Relevant log excerpt:

```text
Run npm publish --access public
npm notice
npm notice 📦  @traildock/sparkline-js@1.4.2
npm notice Tarball Contents
npm notice 1.1kB README.md
npm notice 1.1kB LICENSE
npm notice 1.2kB src/index.js
npm notice 744B package.json
npm notice Tarball Details
npm notice name: @traildock/sparkline-js
npm notice version: 1.4.2
npm notice filename: traildock-sparkline-js-1.4.2.tgz
npm notice package size: 2.0 kB
npm notice unpacked size: 4.1 kB
npm notice shasum: 9d779f7a0c19b72fb3fdfcb3e989a455a7720064
npm notice integrity: sha512-<truncated>
npm notice total files: 4
npm ERR! code ENEEDAUTH
npm ERR! need auth This command requires you to be logged in to https://registry.npmjs.org/
npm ERR! need auth You need to authorize this machine using `npm adduser`
npm ERR! A complete log of this run can be found in:
npm ERR!     /home/runner/.npm/_logs/2026-06-04T18_22_51_810Z-debug-0.log
Error: Process completed with exit code 1.
```

Notes from release operations:

The package tarball was created, so the failure appears to happen at
the registry authentication step. The workflow does not currently show
which npm configuration file was active during publish.
