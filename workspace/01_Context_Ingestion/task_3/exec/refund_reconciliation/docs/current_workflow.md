# Current analyst workflow: Q2 refund reconciliation

This is the analyst review pass for batch `q2-2026`.

1. Run the local read-only reconciliation report from the packet root:

       ./tools/reconcile_report --batch q2-2026

   Save its output as `/tmp_workspace/results/reconcile_snapshot.md`.
2. Inspect the current exports, the Q2 import adjustments, and the
   imported vendor mapping material. Use the imported notes to explain
   vendor-code provenance where relevant.
3. Write `/tmp_workspace/results/refund_exception_report.md` with the
   unresolved refund IDs, amounts, reason for each exception, total
   unresolved amount, and proposed next owner.
4. Write `/tmp_workspace/results/source_manifest.md` listing the files
   used and a brief reliability note for each.
5. Hand the packet to controller review after the analyst artifacts are
   complete.

The analyst report is a review artifact. Settlement finalization is a
later controller-owned stage tracked separately from this workflow.
