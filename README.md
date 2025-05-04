Gist Database 📦🐍

Gist Database is a simple Python project that demonstrates how to:

Fetch data from GitHub Gists API using requests 🛰️

Store and query data in SQLite (via Python’s sqlite3) 🗄️

Write clean, reusable modules (importer, search, models) 🧩

Build and run automated tests with pytest and responses 🧪

📁 Project Structure

./
├── gists_database/       # Python package
│   ├── __init__.py       # Marks package
│   ├── importer.py       # import_gists_to_database()
│   ├── search.py         # search_gists()
│   └── models.py         # Gist class
├── schema.sql            # Database schema
├── main.py               # Demo script
├── requirements.txt      # Dependencies
└── tests/                # Automated tests
    ├── config.py
    ├── fixtures.py
    ├── gists_data/       # JSON fixtures
    ├── populated_gists_database.db
    ├── test_importer.py
    └── test_search.py

🚀 Getting Started

Clone the repo

git clone https://github.com/yourusername/gist-database.git
cd gist-database

Create & activate virtual environment

python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate    # Windows

Install dependencies

pip install -r requirements.txt

Run demo

python main.py

Run tests

pytest -q

⚙️ Key Functions

import_gists_to_database(db, username, commit=True)Fetches a user’s public Gists and inserts them into SQLite.

search_gists(db, github_id=None, created_at=None)Queries the stored Gists, with optional filters for ID or creation date.

📝 License

This project is licensed under the MIT License. See LICENSE for details.

