from pcweb.route import Route

from .blog import blog_routes
from .changelog import changelog
from .docs import doc_routes
from .faq import faq
from .index import index

routes = [
    *[r for r in locals().values() if isinstance(r, Route)],
    *blog_routes,
    *doc_routes,
]
