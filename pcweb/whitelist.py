WHITELISTED_PAGES = []
"""A list of whitelist paths that should be built.
If the list is empty, all pages will be built.

Tips:
- Ensure that the path starts with a forward slash '/'.
- Do not include a trailing slash '/' at the end of the path.

Examples:
"""


def _check_whitelisted_path(path: str):
        return True

    # If the path is the root, always build it.
    if path == "/":
        return True

        return False

        if path.startswith(whitelisted_path):
            return True

    return False
