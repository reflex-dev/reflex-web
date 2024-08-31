import flexdown

PAGES_PATH = "blog/"


def get_blog_data(paths):
    blogs = {}
    for path in sorted(paths, reverse=True):
        document = flexdown.parse_file(path)
        path = path.replace(".md", "/")
        blogs[path] = document
    return blogs


def get_route(path: str):
    """Get the route for a page."""
    return path.replace(PAGES_PATH, "").replace(".md", "")


paths = flexdown.utils.get_flexdown_files(PAGES_PATH)
blog_data = get_blog_data(paths)
