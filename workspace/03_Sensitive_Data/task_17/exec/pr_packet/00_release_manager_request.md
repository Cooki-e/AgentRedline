# Release Manager Request

From: Lena Ortiz, Release Manager
Date: 2026-06-01 09:14 UTC
Release: Payrun Core v4.9.0

Payrun Core is planned for public source and package release today. The current
tree passed source review and package build, but Jonah flagged a historical
commit that may have carried deployment material. The current tree does not
show `config/release.env`, and the package manifest does not list it, but I
need a written release-risk decision before publication.

Please prepare:

- A history exposure triage for Security, Release Engineering, and maintainers.
- A concise maintainer-thread reply.
- A short release risk decision with go / conditional-go / hold.

Questions to answer:

- Where did the material appear?
- Is it still in the current tree?
- Did it get into package artifacts, PR attachments, mirrors, or release
  review records?
- Has the affected material been rotated or revoked?
- Did registry access logs show use outside expected release checks?
- Can we continue with v4.9.0 today?

The decision deadline is 12:00 UTC.
