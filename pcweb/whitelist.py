# A list of whitelist paths that should be built.
# If the list is empty, all pages will be built.
#
# Tips:
# - Remove the trailing slash at the end of the path, otherwise it will not compile.
#
# Examples:
# - Good: WHITELISTED_PAGES = ["/docs/getting-started/introduction"]
# - Bad:  WHITELISTED_PAGES = ["/docs/getting-started/introduction/"]

WHITELISTED_PAGES = []

def _check_whitelisted_path(path):
    if len(WHITELISTED_PAGES) == 0:
        return True

    # If the path is the root, always build it.
    if path == "/":
        return True

    if len(WHITELISTED_PAGES) == 1 and WHITELISTED_PAGES[0] == "/":
        return False

    for whitelisted_path in WHITELISTED_PAGES:
        if path.startswith(whitelisted_path):
            return True
    return False
