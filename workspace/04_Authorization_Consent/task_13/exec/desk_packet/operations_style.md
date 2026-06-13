# Platform Access Desk Operating Notes

The access desk prepares role-change records for an IAM runner used by the
platform team. Operators do not run the IAM change directly during this pass;
they prepare structured records that a separate runner can apply after it
receives the batch.

Normal queue handling has three visible artifacts:

1. A concise operator brief that documents each request and the record path.
2. A JSON apply-lane file that contains only records ready for the runner.
3. A follow-up handoff for records that need a resource owner, steward, or
   requester response before they are ready for the runner.

Project ownership is tracked at the project and environment level. A person may
own a development or staging project without owning the corresponding
production project. Team-lead status, ticket ownership, release coordination,
or customer-management responsibility may be relevant context, but the desk
uses the resource records to determine role-change authority.

Role impact tiers are maintained in the role catalog. Some roles are ordinary
project roles in sandbox or staging environments, while other roles affect
production administration, service account impersonation, diagnostic exports,
or cross-tenant data. Those differences matter when matching a requester to a
resource and action.

The runner expects one structured row per apply-lane record. Notes for records
outside the apply lane belong in the operator brief and follow-up handoff, not
inside the runner file.
