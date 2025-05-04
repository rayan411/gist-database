import requests

def import_gists_to_database(db, username, commit=True):
    """
    Fetch all public gists for `username` via GitHub API and insert into `gists` table.
    Params:
      - db: sqlite3.Connection or Cursor
      - username: GitHub username (str)
      - commit: if True, call db.commit() after inserts
    """
    url = f"https://api.github.com/users/{username}/gists"
    response = requests.get(url)
    response.raise_for_status()
    gists = response.json()

    for gist in gists:
        db.execute(
            """
            INSERT OR REPLACE INTO gists (
                github_id,
                html_url,
                git_pull_url,
                git_push_url,
                commits_url,
                forks_url,
                public,
                created_at,
                updated_at,
                comments,
                comments_url
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                gist['id'],
                gist['html_url'],
                gist['git_pull_url'],
                gist['git_push_url'],
                gist['commits_url'],
                gist['forks_url'],
                int(gist['public']),
                gist['created_at'],
                gist['updated_at'],
                gist['comments'],
                gist['comments_url'],
            )
        )
    if commit:
        db.commit()
