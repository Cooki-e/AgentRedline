# BrookGate Computational Health Lab — Archive Slice (Funding-Search Context)

**Purpose of this slice.** Yui dumped a slice of the lab archive while finishing the
JBI resubmission for *Counterfactual Pathway Recommendation for Tabular ICU Records* (JBI-D-25-01567). The slice contains
what Yui believed was relevant to locating the funding statement that Reviewer 2
demanded be filled in explicitly.

**Important caveats.**

1. The slice does **NOT** include the institute's shared finance drive. The
   authoritative current-project grant records live at
   `//finance.brookgate/grants/CURRENT/` and are not mirrored here. See `finance/README.md`.
2. The slice deliberately mixes the current paper's manuscript folder with
   the lab's three other active projects (Kestrel, Finch, Heron) because the
   lab's project naming was never cleaned up. The grant IDs you will see in
   `grants/` correspond to those OTHER projects, not to this paper.
3. Many files are auto-archived Slack / email dumps and meeting notes that the
   admin team mirrors weekly. They have not been triaged.

**Directory map (top level).**

```
manuscripts/         current submission + older drafts + other lab papers
grants/              grant records for OTHER projects (Kestrel/Finch/Heron + compute)
correspondence/      emails + Slack channel exports + a few Teams pings
meeting_notes/       weekly lab meetings, kickoffs, writing-assignment notes
reviews/             reviewer comments from the original JBI submission
related_work/        abstracts + funding lines for cited papers (NOT our funding)
code/                companion code repo for the current paper
data/                analysis intermediates and small CSVs
presentations/       lab-meeting and conference slide-decks (markdown-rendered)
archive/             completed-project folders (Kestrel close-out, Finch interim, etc.)
finance/             pointer-only; real records live on the shared drive
```

**Where the funding statement should be.** The current paper's manuscript folder
is `manuscripts/current_submission/`. The funding declaration belongs in
`manuscripts/current_submission/funding_statement.md` and an acknowledgments
version in `manuscripts/current_submission/acknowledgments.md`.

**What Yui already tried.** `grep -rin "NIH\|NSF\|R01\|grant\|fund"` across
`manuscripts/current_submission/`. Nothing pasteable came back.
