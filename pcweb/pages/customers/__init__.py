import reflex as rx

from pcweb.pages.customers.views import book_a_demo, companies, hero
from pcweb.templates.marketing_page import marketing_page


@marketing_page(
    path="/customers",
    title="Reflex Customer Stories - Case Studies",
    description="Case studies: Bayesline, SellerX, and Ansa use Reflex to build production Python web apps. Real success stories.",
)
def customers() -> rx.Component:
    return rx.el.div(
        hero(),
        rx.el.hr(
            class_name="w-full border-t border-m-slate-4 dark:border-m-slate-9",
        ),
        companies(),
        book_a_demo(),
        class_name="flex flex-col w-full justify-center items-center",
    )
