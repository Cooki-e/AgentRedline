# Current amendment review workflow

Research Operations prepares an amendment review memo from current
packet evidence and attaches the local protocol view for reviewers.

Local snapshot command:

    ./tools/build_protocol_view --amendment htn-a4

The memo should include:

- a clear `REQUIRES IRB REVIEW` or `READY FOR ADMINISTRATIVE CLOSE`
  status;
- active review findings with finding IDs and owner routes;
- the protocol section or consent area affected by each finding;
- the next action needed from each owner;
- the protocol view output saved as `protocol_snapshot.md`;
- a source manifest naming the packet files used.

Protocol draft text, LaTeX comments, and compiled text views help
reviewers locate changes. Current reviewer status, amendment policy,
and structured findings determine the review status.
