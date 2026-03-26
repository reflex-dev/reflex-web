from typing import TypedDict

import reflex as rx

from pcweb.components.marketing_button import button as marketing_button
from pcweb.constants import REFLEX_ASSETS_CDN


class CustomerCard(TypedDict):
    name: str
    quote: str
    company: str
    logo: str
    url: str


CUSTOMERS: list[CustomerCard] = [
    {
        "name": "Bayesline",
        "header": "Why Bayesline chose Reflex over Plotly Dash",
        "description": "Discover how Bayesline built a robust Python web application aimed at creating scalable risk models and data visualizations.",
        "url": "https://www.bayesline.com",
    },
    {
        "name": "Autodesk",
        "header": "How Autodesk saved 25% of their development time",
        "description": "Learn how Autodesk leveraged Reflex to streamline their internal tools development, cutting build time by 25% while maintaining enterprise-grade reliability.",
        "url": "https://www.autodesk.com",
    },
    {
        "name": "Ansa",
        "header": "How Ansa saved 100 hours of manual work a month with Reflex",
        "description": "See how Ansa automated their fintech workflows with Reflex, eliminating 100 hours of repetitive manual work per month and accelerating their operations.",
        "url": "https://www.ansa.com",
    },
    {
        "name": "SellerX",
        "header": "Why SellerX chose Reflex over Streamlit",
        "description": "Find out why SellerX migrated from Streamlit to Reflex to power their e-commerce analytics platform with greater flexibility and performance.",
        "url": "https://www.sellerx.com",
    },
]


def customer_card(customer: CustomerCard) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.el.div(
                rx.image(
                    src=f"{REFLEX_ASSETS_CDN}case_studies/logos/{rx.color_mode_cond('light', 'dark')}/{customer['name'].lower()}_top.svg",
                    alt=customer["name"],
                    loading="lazy",
                    class_name="mb-2 max-h-6 self-start",
                ),
                rx.el.h3(
                    customer["header"],
                    class_name="text-m-slate-12 dark:text-m-slate-3 text-2xl font-[575]",
                ),
                rx.el.p(
                    customer["description"],
                    class_name="text-m-slate-7 dark:text-m-slate-6 text-sm font-[475]",
                ),
                marketing_button(
                    "Learn more",
                    variant="outline",
                    class_name="w-fit mt-auto z-1",
                    size="sm",
                    native_button=False,
                ),
                class_name="flex flex-col gap-4 max-w-[19rem] lg:pb-8 pb-6 h-full",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        class_name="size-2 shadow-[0_0_0_0.5px_rgba(0,0,0,0.16)_inset] dark:shadow-none dark:border dark:border-m-slate-9 bg-m-slate-4 dark:bg-m-slate-7 rounded-full"
                    ),
                    rx.el.div(
                        class_name="size-2 shadow-[0_0_0_0.5px_rgba(0,0,0,0.16)_inset] dark:shadow-none dark:border dark:border-m-slate-9 bg-m-slate-4 dark:bg-m-slate-7 rounded-full"
                    ),
                    rx.el.div(
                        class_name="size-2 shadow-[0_0_0_0.5px_rgba(0,0,0,0.16)_inset] dark:shadow-none dark:border dark:border-m-slate-9 bg-m-slate-4 dark:bg-m-slate-7 rounded-full"
                    ),
                    class_name="h-8 flex flex-row items-center gap-1 p-3 w-full border-b border-m-slate-4 dark:border-m-slate-9",
                ),
                rx.image(
                    src=f"{REFLEX_ASSETS_CDN}case_studies/apps/case_studies_{customer['name'].lower().replace(' ', '_')}_app.webp",
                    alt=customer["name"],
                    class_name="w-full h-full object-cover object-top-left min-h-[24.125rem]",
                ),
                class_name="flex flex-col border-l border-t border-m-slate-4 dark:border-m-slate-9 rounded-tl-xl w-full bg-white-1 dark:bg-m-slate-11 [box-shadow:0_0_0_1px_rgba(0,_0,_0,_0.06),_0_8px_24px_rgba(0,_0,_0,_0.06),_0_24px_48px_rgba(0,_0,_0,_0.04)] dark:shadow-none",
            ),
            class_name="list-inside flex flex-row gap-12 lg:pl-8 lg:pt-8 pl-6 pt-6 relative rounded-xl bg-white-1 dark:bg-m-slate-11 w-full overflow-hidden h-[25rem] cursor-pointer border border-black/10 dark:border-white/10 [box-shadow:0_6px_12px_0_rgba(0,_0,_0,_0.06),_0_1px_1px_0_rgba(0,_0,_0,_0.01),_0_4px_6px_0_rgba(0,_0,_0,_0.02)] dark:shadow-none after:absolute after:inset-0 after:rounded-xl after:pointer-events-none after:[box-shadow:0_0_0_1px_rgba(0,_0,_0,_0.08)_inset] dark:after:[box-shadow:0_0_0_1px_rgba(255,_255,_255,_0.06)_inset]",
        ),
        to=customer["url"],
        class_name="-m-px",
    )


def customer_cards() -> rx.Component:
    return rx.el.div(
        rx.el.div(class_name="border-b border-m-slate-4 dark:border-m-slate-9 h-12"),
        rx.el.div(
            *[
                rx.fragment(
                    customer_card(customer),
                    rx.el.div(
                        class_name="border-y border-m-slate-4 dark:border-m-slate-9 h-12 last:border-b-transparent last:hidden"
                    ),
                )
                for customer in CUSTOMERS
            ],
            class_name="flex flex-col",
        ),
        rx.el.div(
            class_name="absolute -top-12 -right-px w-px h-12 bg-gradient-to-b from-transparent to-current text-m-slate-4 dark:text-m-slate-10 max-lg:hidden"
        ),
        rx.el.div(
            class_name="absolute -top-12 -left-px w-px h-12 bg-gradient-to-b from-transparent to-current text-m-slate-4 dark:text-m-slate-10 max-lg:hidden"
        ),
        rx.el.div(
            class_name="absolute -bottom-24 -right-px w-px h-24 bg-gradient-to-b from-current to-transparent text-m-slate-4 dark:text-m-slate-10"
        ),
        rx.el.div(
            class_name="absolute -bottom-24 -left-px w-px h-24 bg-gradient-to-b from-current to-transparent text-m-slate-4 dark:text-m-slate-10"
        ),
        class_name="flex flex-col w-full max-w-[42rem] ml-auto border-x border-m-slate-4 dark:border-m-slate-9 mt-12 border-b mb-24 relative",
    )
