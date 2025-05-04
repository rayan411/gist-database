import os
from os.path import dirname as _dirname

BASE_TESTS_PATH    = _dirname(__file__)
BASE_PROJECT_PATH  = _dirname(BASE_TESTS_PATH)
DATABASE_SCHEMA_PATH = os.path.join(BASE_PROJECT_PATH, 'schema.sql')

# Temporary database files
TESTING_DATABASE_PATH   = os.path.join(BASE_TESTS_PATH, 'testing_gists_database.db')
POPULATED_DATABASE_PATH = os.path.join(BASE_TESTS_PATH, 'populated_gists_database.db')

# Gist JSON fixtures
TESTING_GISTS_NAMES = (
    '18bdf248a679155f1381.json',
    '1adb5bee99400ce615a5.json',
    '291bfcfe70d2f9582331.json',
    '4232a4cdad00bd92a7a64cf3e2795820.json',
    '86beaced733b7dbf2d034e56edb8d37e.json',
    'c669398c67386e9fb43e.json',
    'ef201fe313719305c4c7.json',
)
TESTING_GISTS_PATHS = [
    os.path.join(BASE_TESTS_PATH, 'gists_data', name)
    for name in TESTING_GISTS_NAMES
]