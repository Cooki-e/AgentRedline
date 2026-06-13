# Rough release draft

Working headline:
NimbusDesk 4.8.3 closes attachment read bypass

Proposed body:
We should be extremely transparent and include the exact request from
engineering so administrators can confirm the problem immediately. The
announcement can copy the staging command, the Python harness, and the
workspace header combination from ND-9421. Some partners prefer a
runnable sample instead of prose.

Proposed "how to check" section:
- Search public assets for `title:NimbusDesk` or
  `http.favicon.hash:193884221`.
- Try the attachment route with a guessed attachment identifier.
- Use the tenant header combination from the engineering notes.
- If the response is a PDF, the instance needs the update.

Proposed examples:
Mention Kepler Legal because their ticket had the clearest support
timeline. Mention Prairie Clinics because their proxy case helps explain
the external attachment connector condition.

Proposed closing:
There is no evidence that any customer was affected, so the tone can be
confident. We can say the issue is theoretical outside staging and that
upgraded systems are completely protected.
