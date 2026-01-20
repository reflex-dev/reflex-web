from pcweb.route import Route

from .blog import blog_routes
from .booked import booked as booked
from .check_your_email_demo import page_thank_you as page_thank_you
from .customers.data.customers import customers_routes
from .customers.landing import customers as customers
from .databricks.databricks import databricks_page as databricks_page
from .demo.book_demo import book_demo as book_demo
from .docs import doc_routes
from .errors import errors as errors
from .faq import faq as faq
from .framework.framework import framework as framework
from .gallery import gallery as gallery
from .gallery.apps import gallery_apps_routes
from .hosting.hosting import hosting_landing as hosting_landing
from .landing.landing import landing as landing
from .meeting_successfully_booked import (
    page_meeting_successfully_booked as page_meeting_successfully_booked,
)
from .page404 import page404 as page404
from .pricing.pricing import pricing as pricing
from .sales import sales as sales
from .security.security import security_page as security_page
from .to_be_booked import to_be_booked as to_be_booked
from .use_cases.consulting import consulting_use_case_page as consulting_use_case_page
from .use_cases.finance import finance_use_case_page as finance_use_case_page
from .use_cases.government import government_use_case_page as government_use_case_page
from .use_cases.healthcare import healthcare_use_case_page as healthcare_use_case_page
from .use_cases.use_cases import use_cases_page as use_cases_page

routes = [
    *[r for r in locals().values() if isinstance(r, Route) and r.add_as_page],
    *blog_routes,
    *doc_routes,
    *customers_routes,
    *gallery_apps_routes,
]
