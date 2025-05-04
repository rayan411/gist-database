import os
import sqlite3
import json
import pytest
import responses

from .config import (
    TESTING_DATABASE_PATH,
    POPULATED_DATABASE_PATH,
    DATABASE_SCHEMA_PATH,
    TESTING_GISTS_PATHS,
)

@pytest.fixture()
def clean_gists_database():
    db = sqlite3.connect(TESTING_DATABASE_PATH)
    with open(DATABASE_SCHEMA_PATH) as f:
        db.executescript(f.read())
    yield db
    db.close()
    os.remove(TESTING_DATABASE_PATH)

@pytest.fixture()
def populated_gists_database():
    db = sqlite3.connect(POPULATED_DATABASE_PATH)
    yield db
    db.close()

@pytest.fixture()
def mocked_requests():
    gists = []
    for path in TESTING_GISTS_PATHS:
        with open(path) as f:
            gists.append(json.load(f))

    # Mock successful fetch
    responses.add(
        responses.GET,
        'https://api.github.com/users/gvanrossum/gists',
        json=gists,
        status=200
    )
    # Mock 404 for non-existent user
    responses.add(
        responses.GET,
        'https://api.github.com/users/rmotr-doesnt-exist/gists',
        status=404
    )