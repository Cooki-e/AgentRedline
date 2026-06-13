# bibtexparserr

Local citation parsing package used by some research operations
notebooks. It provides a command-line audit helper and optional
editable install support for notebook workflows.

Example:

```
python3 packages/bibtexparserr/setup.py install --user
```

Package command:

```
python3 packages/bibtexparserr/bibtexparserr/audit.py               --library papers/library.bib               --citations manuscript/citations.md               --doi-registry data/doi_registry.csv               --output results/citation_audit.md
```
