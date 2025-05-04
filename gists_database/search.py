# gists_database/search.py

from gists_database.models import Gist

def search_gists(db_connection, github_id=None, created_at=None):
    """
    Query the `gists` table and return a list of Gist objects.
    
    Optional filters:
      - github_id: exact match on the gist id
      - created_at: exact match on the created_at timestamp
    """
    # 1. Base query
    query = (
        "SELECT "
        "github_id, html_url, git_pull_url, git_push_url, "
        "commits_url, forks_url, public, created_at, updated_at, comments, comments_url "
        "FROM gists WHERE 1=1"
    )
    params = {}

    # 2. Filter by github_id
    if github_id is not None:
        query += " AND github_id = :github_id"
        params["github_id"] = github_id

    # 3. Filter by created_at
    if created_at is not None:
        query += " AND datetime(created_at) = datetime(:created_at)"
        params["created_at"] = created_at

    # 4. Execute and fetch
    cursor = db_connection.execute(query, params)
    rows = cursor.fetchall()

    # 5. Wrap rows in Gist objects
    return [Gist(*row) for row in rows]
