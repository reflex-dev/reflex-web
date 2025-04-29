"""Whitelist for pages to compile during development."""

from typing import Callable

# Add pages you're working on to this list to speed up compilation.
WHITELISTED_PAGES = []


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
