"""
Utility helpers for Hermes SDK clients.
"""


from typing import Optional


def normalize_access_token(access_token: str) -> str:
    """Return a token value without an optional Bearer prefix."""
    if not access_token or not isinstance(access_token, str):
        raise ValueError("access_token must be a non-empty string")

    token = access_token.strip()
    parts = token.split(None, 1)
    if parts and parts[0].lower() == "bearer":
        token = parts[1].strip() if len(parts) > 1 else ""

    if not token:
        raise ValueError("access_token must be a non-empty string")

    return token


def build_headers(access_token: str, user_agent: Optional[str] = None) -> dict:
    """Return HTTP headers for Hermes API requests."""
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    if user_agent is not None:
        if not isinstance(user_agent, str) or not user_agent.strip():
            raise ValueError("user_agent must be a non-empty string")
        headers['User-Agent'] = user_agent

    return headers
