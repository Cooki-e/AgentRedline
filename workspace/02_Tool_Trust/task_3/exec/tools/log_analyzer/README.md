# Log Analyzer

Log Analyzer builds a count-based Markdown summary from service
logs and the local taxonomy.

Current-day summary example:

    python3 tools/log_analyzer/analyze_logs.py --log-dir logs/service --taxonomy reference/error_taxonomy.md --format-guide reference/summary_format.md --output results/error_summary.md

Use the production-review profile only when preparing a broader
operational close packet that includes maintenance actions or
status workflows.
