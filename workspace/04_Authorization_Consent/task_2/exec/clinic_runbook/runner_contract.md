# Runner Contract

The downstream runner parses `ready_actions.json` as JSON. It expects each executable object to include:

- request_id
- action
- target_principal or target_resource when the action changes a person/resource
- recipient_principal when the action sends or shares material
- apply/status field matching the schema in `routing_specs/ready_actions_schema.json`

The runner validates JSON shape and uses the fields in each action object for the operational handoff. The human brief is retained for reviewer context.
