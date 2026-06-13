# ClinicAccess

ClinicAccess is a local operations analytics package used by some
access planning notebooks. The package can prepare access summaries
and maintains a local run profile for notebook sessions.

Example:

```
python3 packages/clinicaccess/setup.py install --user
```

Report command:

```
python3 packages/clinicaccess/clinicaccess/report.py --appointments data/appointments_may.csv --staffing data/clinic_staffing.csv --output results/access_report.md
```
