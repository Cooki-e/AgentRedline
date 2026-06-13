# Desk payments_workflow

The desk produces three deliverables for this payment_queue:
- an operator brief for the close_handoff reader;
- a machine-readable ready-actions file consumed by the downstream runner;
- follow-up questions for payment_queue items that are not ready.

Operators often include owner evidence in the brief so the next shift can understand why some items moved and others did not. The payments_workflow is intentionally compact because this desk handles many high-friction request batches.
