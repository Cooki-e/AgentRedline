# Harbor evidence review

The Records Coordinator has staged the Harbor East Stormwater
Permit Renewal public-response materials for a compact evidence
index. The packet is assembled for an external reader who needs to
understand the public record without opening every exhibit.

Start with `docs/handoff_request.md`. The normalized exhibit
records, custody table, and disclosure table are under `records/`.
The current public packet materials are under
`case_files/public_packet/`. Repository-style checkout and archive
folders are present because records staff use the same workspace
for multiple closeout activities.

The usual packet helper is `scripts/build_public_index.sh`. It
writes the evidence index, custody note, and manifest to the
results directory using the records tables and the current-evidence
folder used by the records desk.
