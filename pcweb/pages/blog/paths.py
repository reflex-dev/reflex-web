import flexdown
from flexdown.document import Document

from pcweb.constants import REFLEX_ASSETS_CDN

PAGES_PATH = "blog/"


def get_blog_data(paths):
    items = []
    for path in paths:
        document = Document.from_file(path)
        document.metadata["REFLEX_ASSETS_CDN"] = REFLEX_ASSETS_CDN
        path_str = str(path).replace(PAGES_PATH, "").replace(".md", "/")
        items.append((path_str, document))
    items.sort(key=lambda x: str(x[1].metadata.get("date", "")), reverse=True)
    return dict(items)


def get_route(path: str):
    """Get the route for a page."""
    return path.replace(PAGES_PATH, "").replace(".md", "")


paths = flexdown.utils.get_flexdown_files(PAGES_PATH)
blog_data = get_blog_data(paths)


def blog_data_visible() -> list[tuple[str, Document]]:
    """Blog posts with show_in_cards not explicitly False (default True)."""
    return [
        (path, doc)
        for path, doc in blog_data.items()
        if doc.metadata.get("show_in_cards", True)
    ]
