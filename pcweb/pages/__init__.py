from pcweb.route import Route

from .blog import blog_routes
from .changelog import changelog as changelog
from .docs import doc_routes
from .faq import faq as faq
from .framework.framework import framework as framework
from .page404 import page404 as page404
from .errors import errors as errors
from .gallery import gallery as gallery
from .customers.landing import customers as customers
from .customers.data.customers import customers_routes
from .gallery.apps import gallery_apps_routes
# from .hosting_countdown.hosting_countdown import hosting_countdown as hosting_countdown
from .pricing.pricing import pricing as pricing
from .sales import sales as sales
from .hosting.hosting import hosting_landing as hosting_landing
from .landing.landing import landing as landing

routes = [
    *[r for r in locals().values() if isinstance(r, Route) and r.add_as_page],
    *blog_routes,
    *doc_routes,
    *customers_routes,
    *gallery_apps_routes,
]
