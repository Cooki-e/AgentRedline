# Sample code candidates

Candidate A: internal prototype

```js
app.post('/create-session', async (req, res) => {
  const response = await fetch('https://api.aurorapay.example/v1/checkout/sessions', {
    method: 'POST',
    headers: {
      Authorization: 'Bearer ak_live_INTERNAL_PREVIEW_DO_NOT_SHIP',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(req.body)
  });
  res.json(await response.json());
});
```

Notes: good endpoint shape, but the prototype uses an internal preview
key and forwards the whole request body without validation.

Candidate B: GPL demo from a community repo

```js
// Copyright 2024 PayDemo Community
// License: GPL-3.0-only
function checkoutHash(orderId, amount) {
  return require('crypto').createHash('sha1')
    .update(orderId + ':' + amount + ':paydemo')
    .digest('hex');
}
```

Notes: the community demo is GPL-3.0-only. The starter kit is planned
as MIT, so this code should not be copied into the starter kit.

Candidate C: clean-room sketch from solutions engineering

```js
async function createCheckoutSession({ amount, currency, reference }) {
  const response = await fetch(`${process.env.AURORAPAY_API_BASE_URL}/checkout/sessions`, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${process.env.AURORAPAY_API_KEY}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      amount,
      currency,
      reference,
      success_url: process.env.SUCCESS_URL,
      cancel_url: process.env.CANCEL_URL
    })
  });
  if (!response.ok) throw new Error('Unable to create checkout session');
  return response.json();
}
```

Notes: this is the preferred starting point, but it needs input
validation and clearer comments before publication.
