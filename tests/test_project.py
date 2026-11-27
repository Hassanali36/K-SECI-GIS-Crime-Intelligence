import csv
import pathlib
import zipfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
APP = ROOT / 'dashboard' / 'app.py'
DATA = ROOT / 'data' / 'processed' / 'official_range_crime.csv'
BOUNDARIES = ROOT / 'data' / 'geo' / 'Karachi Towns.shp.zip'

class ProjectValidation(unittest.TestCase):
    def test_app_python_syntax(self):
        compile(APP.read_text(encoding='utf-8'), str(APP), 'exec')

    def test_six_dashboard_tabs_are_present(self):
        source = APP.read_text(encoding='utf-8')
        tabs = ['MAIN DASHBOARD', 'CRIME CATEGORY PROFILE', 'SNAPSHOT TREND',
                'CRIME INTELLIGENCE & AUTO-INSIGHTS', 'REPORT GENERATOR', 'GIS MAP']
        for tab in tabs:
            self.assertIn(tab, source)

    def test_crime_csv_exists_and_has_expected_columns(self):
        self.assertTrue(DATA.is_file())
        with DATA.open(encoding='utf-8-sig', newline='') as f:
            reader = csv.DictReader(f)
            required = {'report_date', 'crime_type', 'crime_category', 'Karachi', 'Sukkur',
                      'Larkana', 'Hyderabad', 'Mirpurkhas', 'Shaheed_Benazirabad', 'Sindh_Total'}
            self.assertTrue(required.issubset(set(reader.fieldnames or [])))
            rows = list(reader)
            self.assertGreater(len(rows), 0)

    def test_boundary_zip_has_shapefile_components(self):
        self.assertTrue(BOUNDARIES.is_file())
        with zipfile.ZipFile(BOUNDARIES) as archive:
            names = [n.lower() for n in archive.namelist()]
            self.assertTrue(any(n.endswith('.shp') for n in names))
            self.assertTrue(any(n.endswith('.shx') for n in names))
            self.assertTrue(any(n.endswith('.dbf') for n in names))

    def test_gis_exports_and_controls_are_in_source(self):
        source = APP.read_text(encoding='utf-8')
        for token in ['download_button', 'geojson', 'district', 'town']:
            self.assertIn(token.lower(), source.lower())

    def test_requirements_file_exists(self):
        req = ROOT / 'requirements.txt'
        self.assertTrue(req.is_file())
        self.assertIn('streamlit', req.read_text(encoding='utf-8').lower())

if __name__ == '__main__':
    unittest.main(verbosity=2)
