from dataclasses import dataclass
from datetime import datetime

@dataclass
class UsarioGit:
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: str
    name: str
    company: str
    blog: str
    location: str
    email: str or None
    hireable: str or None
    bio: str
    twitter_username: str or None
    public_repos: int
    public_gists: int
    followers: int
    following: int
    created_at: datetime
    updated_at: datetime