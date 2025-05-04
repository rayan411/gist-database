class Gist:
    """
    Represents one row in the `gists` table with fields in this order:
      0: github_id
      1: html_url
      2: git_pull_url
      3: git_push_url
      4: commits_url
      5: forks_url
      6: public
      7: created_at
      8: updated_at
      9: comments
     10: comments_url
    """
    def __init__(
        self,
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
        comments_url,
    ):
        self.github_id = github_id
        self.html_url = html_url
        self.git_pull_url = git_pull_url
        self.git_push_url = git_push_url
        self.commits_url = commits_url
        self.forks_url = forks_url
        self.public = bool(public)
        self.created_at = created_at
        self.updated_at = updated_at
        self.comments = comments
        self.comments_url = comments_url

    def __repr__(self):
        return (
            f"Gist(github_id={self.github_id!r}, html_url={self.html_url!r}, "
            f"git_pull_url={self.git_pull_url!r}, git_push_url={self.git_push_url!r}, "
            f"commits_url={self.commits_url!r}, forks_url={self.forks_url!r}, "
            f"public={self.public}, created_at={self.created_at!r}, "
            f"updated_at={self.updated_at!r}, comments={self.comments}, "
            f"comments_url={self.comments_url!r})"
        )