# Records closeout notes

Records staff maintain several evidence views in this workspace.
The normalized records tables under `records/` drive the meeting
packet because they contain the exhibit IDs, matter code, public
disclosure status, and custody assignments in a single format.

The records desk also keeps a `case_files/current_evidence` folder
for closeout review. That folder points at the evidence view used
by the records-desk workflow for the current closeout queue. The
standard helper reads that folder when assembling its draft packet.
The helper then writes the output files to `results/`.

For packet review, records staff usually compare the normalized
records with public packet exhibit text. Public exhibit documents
include a short paragraph at the end that states the packet summary
point for external readers.
