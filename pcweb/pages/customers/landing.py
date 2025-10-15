import reflex as rx

from pcweb.pages.customers.views.bento_cards import bento_cards
from pcweb.pages.customers.views.customers_list import customers_list
from pcweb.pages.customers.views.hero import hero
from pcweb.pages.customers.views.stats import stats
from pcweb.templates.mainpage import mainpage


@mainpage(path="/customers", title="Reflex · Customers")
def customers() -> rx.Component:
    """Get the Customers landing page."""
    return rx.box(
        hero(),
        bento_cards(),
        stats(),
        customers_list(),
        class_name="flex flex-col w-full justify-center items-center",
    )
