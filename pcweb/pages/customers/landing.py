import reflex as rx
from pcweb.components.icons.patterns import index_patterns
from pcweb.components.docpage.navbar import navbar
from pcweb.components.webpage.badge import badge
from pcweb.pages.index.index_colors import index_colors
from pcweb.pages.index.views.footer_index import footer_index
from pcweb.pages.customers.views.hero import hero
from pcweb.pages.customers.views.bento_cards import bento_cards
from pcweb.pages.customers.views.stats import stats
from pcweb.pages.customers.views.customers_list import customers_list
from pcweb.pages.index.views.get_started import get_started
from pcweb.pages.customers.story_page import story_page


@rx.page(route="/customers", title="Reflex · Customers")
def customers() -> rx.Component:
    """Get the main Reflex landing page."""
    return rx.box(
        index_colors(),
        # *index_patterns(),
        navbar(),
        rx.el.main(
            hero(),
            bento_cards(),
            stats(),
            customers_list(),
            get_started(),
            class_name="flex flex-col w-full justify-center items-center",
        ),
        footer_index(),
        badge(),
        class_name="flex flex-col w-full max-w-[94.5rem] justify-center items-center mx-auto px-4 lg:px-5 relative overflow-hidden",
    )


import flexdown

CUSTOMERS_PATH = "pcweb/pages/customers/stories/"

def get_customer_data(paths):
    customers = {}
    for path in reversed(sorted(paths)):
        document = flexdown.parse_file(path)
        path = path.replace(".md", "/")
        customers[path] = document
    return customers


def get_route(path: str):
    """Get the route for a page."""
    return path.replace(CUSTOMERS_PATH, "").replace(".md", "")


paths = flexdown.utils.get_flexdown_files(CUSTOMERS_PATH)
customer_data = get_customer_data(paths)

customers_routes = []
for path, document in customer_data.items():
    # Get the docpage component.
    route = f"/customers/{document.metadata["company"].lower()}"
    title = rx.utils.format.to_snake_case(path.rsplit("/", 1)[1].replace(".md", ""))
    comp = story_page(
        path=route,
        company=document.metadata["company"],
        description=document.metadata["description"],
        domain=document.metadata["domain"],
        founded=document.metadata["founded"],
        investors=document.metadata["investors"],
        meta=document.metadata["meta"],
    )(lambda doc=document: lambda doc=document: page(doc, route))

    # # Add the route to the list of routes.
    customers_routes.append(comp)
