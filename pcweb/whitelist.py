"""Whitelist for pages to build."""

from typing import List

# Add pages to whitelist here.
# This will significantly improve performance during development.
WHITELISTED_PAGES: List[str] = []


def _check_whitelisted_path(path: str) -> bool:
    """Check if a path is whitelisted.

    Args:
        path: The path to check.

    Returns:
        Whether the path is whitelisted.
    """
    if not WHITELISTED_PAGES:
        return True
    return path in WHITELISTED_PAGES
