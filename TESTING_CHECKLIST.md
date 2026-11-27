# K-SECI Phase 16 — Full Dashboard Test Checklist

## Automated checks in this package
- Python syntax compilation of `dashboard/app.py`
- Presence of the six expected Streamlit dashboard tabs
- Crime CSV existence, expected columns, and non-empty records
- Boundary ZIP contains SHP, SHX, and DBF components
- GIS export controls/tokens present in source
- Requirements file exists and includes Streamlit

Run automated checks from this folder:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```
If you have not created the virtual environment yet:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe -m streamlit run dashboard\app.py
```

## Manual browser checklist (requires running the app)
- [ ] App starts without traceback
- [ ] Main Dashboard loads and KPI values appear
- [ ] Range comparison charts render
- [ ] Hotspot analysis section works with its controls
- [ ] Prediction prototype displays its caveats
- [ ] Data explorer filtering and CSV download work
- [ ] Crime Category Profile tab renders
- [ ] Snapshot Trend tab renders
- [ ] Crime Intelligence & Auto-Insights tab renders
- [ ] Report Generator creates/downloads report
- [ ] GIS map loads bundled boundary ZIP
- [ ] District/town selectors and map interactions respond
- [ ] GIS summary, visible-boundary CSV, and GeoJSON exports download
- [ ] Layout checked at normal desktop window size
- [ ] No missing-file warnings or console errors during tab navigation

## Important data limitation
Crime counts are police-range aggregated, not town-geocoded. Administrative town/district map styling must not be interpreted as crime intensity or town-level crime totals.

## Test status note
Automated source/data/package checks are separate from manual browser testing. Do not mark the manual checklist complete until a local visual run is performed.
