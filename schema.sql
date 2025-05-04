-- Drop existing table
DROP TABLE IF EXISTS gists;

-- Create `gists` table with all required fields
CREATE TABLE gists (
    github_id TEXT PRIMARY KEY,
    html_url TEXT NOT NULL,
    git_pull_url TEXT NOT NULL,
    git_push_url TEXT NOT NULL,
    commits_url TEXT NOT NULL,
    forks_url TEXT NOT NULL,
    public INTEGER NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    comments INTEGER NOT NULL,
    comments_url TEXT NOT NULL
);