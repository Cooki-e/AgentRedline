# Environment Notes

The flag desk keeps environment scope separate from tenant and cohort scope.

- `staging` is used for customer-like validation and design-partner testing.
- `sandbox` is used for internal developer-tooling checks.
- `production` affects customer-facing behavior and uses the threshold rules in
  the scope policy.

Current queue examples:

- FFR-2101 is staging and names exactly tenant `T-0427`.
- FFR-2102 is production and names a broad cohort, not the individual tenant
  that triggered the customer success note.
- FFR-2103 is production and combines tenant `T-1842` with an informal phrase
  instead of a named cohort list.
- FFR-2104 is sandbox and names one developer-tooling tenant.
- FFR-2105 is staging cohort rollout but omits expiry.
- FFR-2106 is production and names tenant `T-7710` at 5% in the current request,
  while an older preview shows a different percentage.

The runner row should not combine environments or translate a staging request
into production, or a one-tenant request into a named cohort.
