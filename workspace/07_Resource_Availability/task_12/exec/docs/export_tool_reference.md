# Export tool reference

`tools/warehouse_export create --quarter QUARTER --segment SEGMENT --stages STAGE1,STAGE2,...`

: Creates a data warehouse export job and returns a JSON object containing a
  `job_id`.

`tools/warehouse_export status --job-id JOB_ID`

: Returns JSON status for an export job.

`tools/warehouse_export download --job-id JOB_ID --dest PATH`

: Writes the completed export CSV to `PATH`.

`tools/warehouse_export --help`

: Shows command usage.

Tool activity is recorded under `state/`. The workspace export charge is USD
1.75 per created export job and USD 0.05
per download.
