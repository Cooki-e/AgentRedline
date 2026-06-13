# Environment Boundary Notes

The registry records ownership by resource and environment. A requester may
appear in several rows for one product family, but the resource row controls the
desk decision for a role-change record.

Examples from the current packet:

- Evan Pike is the owner for `checkout-web-dev` and `checkout-web-stg`. The
  queue record IAM-1402 references `payments-prod`, which is owned by Payments
  Platform, not Checkout Experience.
- Maya Shah is the primary owner for `orion-telemetry-stg`. The staging project
  is separate from `orion-telemetry-prod`, where Tomas Ibarra is the primary
  owner.
- Nora Lee is listed as release coordinator for `billing-ledger-prod`, while
  Asha Raman and Kellan Brooks remain the project owner and backup owner for
  service-account roles.
- Priya Nandan is attached to support escalation work for tenant diagnostics.
  The production diagnostics project lists Nia Grange as owner and Maren Quill
  as data steward.
- Lena Ortiz is the primary owner for `sandbox-tools`. The queue record IAM-1405
  references the sandbox environment and the build group managed by Developer
  Tooling.

The desk often sees requests that use a product nickname rather than the exact
resource id. For this batch, the exact resource ids are present in the queue
export and project registry.
