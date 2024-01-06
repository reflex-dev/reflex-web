from pcweb.route import Route
from .docs import doc_routes
from .changelog import changelog
from .blog import blog_routes
from .index import index
from .faq import faq_routes

routes = [r for r in locals().values() if isinstance(r, Route)]
