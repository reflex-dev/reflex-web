import reflex as rx
from pcweb.components.docpage.navbar import navbar
from pcweb.components.webpage.badge import badge
from pcweb.pages.index.index_colors import index_colors
from pcweb.pages.index.views.footer_index import footer_index
from pcweb.pages.customers.views.hero import hero
from pcweb.pages.customers.views.bento_cards import bento_cards
from pcweb.pages.customers.views.stats import stats
from pcweb.pages.customers.views.customers_list import customers_list
from pcweb.pages.index.views.get_started import get_started


@rx.page(route="/customers", title="Reflex · Customers")
def customers() -> rx.Component:
    """Get the Customers landing page."""
    return rx.box(
        index_colors(),
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
