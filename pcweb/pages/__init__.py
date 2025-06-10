from pcweb.route import Route
from .affiliates import affiliates as affiliates
from .databricks import databricks as databricks
from .blog import blog_routes
from .customers.data.customers import customers_routes
from .customers.data.customers import customers_routes
from .customers.landing import customers as customers
from .customers.landing import customers as customers
from .docs import doc_routes
from .errors import errors as errors
from .errors import errors as errors
from .faq import faq as faq
from .framework.framework import framework as framework
from .gallery import gallery as gallery
from .gallery import gallery as gallery
from .gallery.apps import gallery_apps_routes
from .gallery.apps import gallery_apps_routes
from .hosting.hosting import hosting_landing as hosting_landing
from .hosting.hosting import hosting_landing as hosting_landing
from .landing.landing import landing as landing
from .page404 import page404 as page404
from .page404 import page404 as page404
from .pricing.pricing import pricing as pricing

# from .hosting_countdown.hosting_countdown import hosting_countdown as hosting_countdown
from .pricing.pricing import pricing as pricing
from .sales import sales as sales
from .sales import sales as sales

routes = [
    *[r for r in locals().values() if isinstance(r, Route) and r.add_as_page],
    *blog_routes,
    *doc_routes,
    *customers_routes,
    *gallery_apps_routes,
]
