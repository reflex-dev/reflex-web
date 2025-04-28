"""
This file is used to whitelist pages for development.
It should be empty when committed to the repository.
"""

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
    return any(path.startswith(page) for page in WHITELISTED_PAGES)
