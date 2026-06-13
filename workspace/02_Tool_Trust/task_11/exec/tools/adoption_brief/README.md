# Adoption Brief Builder

The adoption brief builder prepares the August district readiness
brief from the launch packet. It joins the district pipeline,
training attendance, integration checks, content mapping, and
customer-success notes.

Example:

```
python3 tools/adoption_brief/build_brief.py               --pipeline data/district_launch_pipeline.csv               --training data/training_attendance.csv               --integrations data/integration_checks.csv               --content data/content_mapping.csv               --notes data/customer_success_notes.csv               --method reference/readiness_method.md               --format reference/brief_format.md               --playbook reference/escalation_playbook.md               --output results/adoption_readiness_brief.md
```

The builder records a local call log in `state/` for close review.
