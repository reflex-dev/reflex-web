"""
This file contains a list of paths that should be built for the Reflex application.
If the list is empty, all pages will be built.

Tips:
- Ensure that the path starts with a forward slash '/'.
- Do not include a trailing slash '/' at the end of the path.

Examples:
- Correct: WHITELISTED_PAGES = ["/docs/getting-started/introduction"]
- Incorrect: WHITELISTED_PAGES = ["/docs/getting-started/introduction/"]
"""

WHITELISTED_PAGES = []


def _check_whitelisted_path(path: str) -> bool:
    """Check if a given path is whitelisted.

    Args:
        path: The path to check.

    Returns:
        Whether the path is whitelisted.
    """
    if not WHITELISTED_PAGES:
        return True
    return path in WHITELISTED_PAGES
