# Webhook receiver on-call notes

For a provider delivery regression:

1. Obtain a sanitized failed-delivery sample from support.
2. Compare request headers and raw body bytes with the receiver helper.
3. Keep transport normalization localized to the receiver boundary.
4. Run the focused suite before handing the patch back.
