import flexdown
from flexdown.document import Document

PAGES_PATH = "blog/"


def get_blog_data(paths):
    blogs = {}
    for path in sorted(paths, reverse=True):
        document = Document.from_file(path)
        path_str = str(path).replace(PAGES_PATH, "").replace(".md", "/")
        blogs[path_str] = document
    return blogs


def get_route(path: str):
    """Get the route for a page."""
    return path.replace(PAGES_PATH, "").replace(".md", "")


paths = flexdown.utils.get_flexdown_files(PAGES_PATH)
blog_data = get_blog_data(paths)
