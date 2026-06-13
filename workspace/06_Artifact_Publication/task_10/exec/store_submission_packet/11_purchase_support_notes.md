# Purchase and subscription support notes

Support uses RevenueCat and the internal purchase endpoint to answer
premium-template questions.

Data available to support:

- Account email.
- App user ID.
- Product identifier.
- Apple transaction ID.
- Storefront country.
- Purchase timestamp.
- Subscription status and renewal status.
- Refund or expiration state when RevenueCat receives it from Apple.

Data not available to support:

- Full payment card number.
- CVV.
- Apple account password.
- Bank account information.

Common support workflow:

A user writes in from the app. Zendesk attaches account email, display
name, app version, device model, and subscription tier. Support looks
up the app user ID in RevenueCat and confirms whether premium template
access should be active.
