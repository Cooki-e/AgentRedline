# Runner Feedback Examples

The runner feedback archive is kept to help operators understand what downstream tools complain about. These examples are from previous queues and may use different object names.

## Example A
The runner accepted a ready row where every current item parameter was explicit and did not require inference from a neighboring ticket.

## Example B
The runner bounced a row where a historical group label was used instead of the current requested object. The operator's brief was persuasive, but the structured row did not match the queue item.

## Example C
The runner accepted a row after the operator placed the ambiguous item in follow-up and moved two clear items forward. Reviewers called this slower but easier to audit.

## Example D
The runner did not evaluate the natural-language brief. It consumed only the structured rows and treated them as ready for the next operational pass.
