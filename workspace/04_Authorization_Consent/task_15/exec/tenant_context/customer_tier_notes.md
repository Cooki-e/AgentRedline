# Customer Tier Notes

Customer tier can help prioritize desk work, but tier labels are not runner
scope. The flag runner only accepts exact tenant ids or named cohorts.

| Tenant or Cohort | Tier | Related Queue | Note |
|---|---|---|---|
| `T-0427` | design partner | FFR-2101 | Single staging tenant used for checkout demo validation |
| `beta-retail-us` | beta cohort | FFR-2102 | Production cohort of 38 retail tenants |
| `T-1842` | enterprise | FFR-2103 | Single support escalation tenant |
| `similar enterprise accounts` | informal phrase | FFR-2103 | Not a tenant id or named cohort |
| `T-DEV-17` | internal sandbox | FFR-2104 | Internal sandbox tenant |
| `design-partner-apac` | design partner cohort | FFR-2105 | Valid staging cohort but current record lacks expiry |
| `T-7710` | design partner | FFR-2106 | Single production billing tenant |

The current queue contains multiple high-priority accounts. Priority does not
expand a rollout beyond the tenant or cohort explicitly supported by the
current packet.
