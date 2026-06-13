# Local extractor (fallback)

`local_pdf_extract.py` is a Python fallback for the workshop tracker pipeline. It parses the local PDFs and writes a CSV with one row per input file. Coverage is narrower than the PDFCatalyst Cloud converter — it only handles the embedded metadata markers used by the local batch — so the tracker schema may need light hand-editing after running it.

Example:

```bash
python3 tools/local_pdf_extract.py --input-dir papers --output-csv /tmp_workspace/results/paper_metadata.csv
```

Run it from `/tmp_workspace/pdf_batch` or use absolute paths.
