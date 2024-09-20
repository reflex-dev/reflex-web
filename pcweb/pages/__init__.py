from pcweb.route import Route

from .blog import blog_routes
from .changelog import changelog
from .docs import doc_routes
from .faq import faq
from .index import index
from .pricing import pricing
from .page404 import page404
from .errors import errors
from .gallery import gallery
from .customers.landing import customers
from .customers.data.customers import customers_routes

routes = [
    *[r for r in locals().values() if isinstance(r, Route) and r.add_as_page],
    *blog_routes,
    *doc_routes,
    *customers_routes,
]
