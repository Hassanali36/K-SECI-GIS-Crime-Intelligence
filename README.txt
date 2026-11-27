K-SECI GIS PHASE 16 — FULL DASHBOARD TESTING

This phase packages the existing Phase 15 dashboard with a lightweight automated validation suite and a manual browser testing checklist. It does not add features or claim the dashboard has been fully tested in a live browser.


POWERSHELL QUICK START
From the extracted project folder:

python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe -m streamlit run dashboard\app.py

If you already have a working .venv and installed dependencies, skip creation/install and run the test command followed by Streamlit.

See TESTING_CHECKLIST.md for manual tests to perform inside the browser.
