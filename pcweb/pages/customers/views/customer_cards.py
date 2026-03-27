from typing import TypedDict

import reflex as rx

from pcweb.components.marketing_button import button as marketing_button
from pcweb.constants import REFLEX_ASSETS_CDN
from pcweb.pages.customers.data.customers import customer_data


class CustomerCard(TypedDict):
    name: str
    header: str
    description: str
    url: str


CUSTOMERS: list[CustomerCard] = [
    {
        "name": doc.metadata["company"],
        "header": doc.metadata["card_header"],
        "description": doc.metadata["card_description"],
        "url": f"/customers/{doc.metadata['company'].lower().replace(' ', '-')}",
    }
    for doc in customer_data.values()
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
                    class_name="text-m-slate-12 dark:text-m-slate-3 lg:text-2xl text-xl font-[575]",
                ),
                rx.el.p(
                    customer["description"],
                    class_name="text-m-slate-7 dark:text-m-slate-6 lg:text-sm text-xs font-[475]",
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
            class_name="list-inside flex flex-row lg:gap-12 gap-4 lg:pl-8 lg:pt-8 pl-6 pt-6 relative rounded-xl bg-white-1 dark:bg-m-slate-11 w-full overflow-hidden h-[25rem] cursor-pointer border border-black/10 dark:border-white/10 [box-shadow:0_6px_12px_0_rgba(0,_0,_0,_0.06),_0_1px_1px_0_rgba(0,_0,_0,_0.01),_0_4px_6px_0_rgba(0,_0,_0,_0.02)] dark:shadow-none xl:w-[42rem] w-full",
        ),
        to=customer["url"],
        class_name="-m-px h-[25rem] min-w-[42rem]",
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
            class_name="flex flex-col border-x border-m-slate-4 dark:border-m-slate-9",
        ),
        rx.el.div(class_name="border-t border-m-slate-4 dark:border-m-slate-9 h-12"),
        rx.el.div(
            class_name="absolute -top-12 right-0 w-px h-24 bg-gradient-to-b from-transparent to-current text-m-slate-4 dark:text-m-slate-9 max-lg:hidden"
        ),
        rx.el.div(
            class_name="absolute -top-12 left-0 w-px h-24 bg-gradient-to-b from-transparent to-current text-m-slate-4 dark:text-m-slate-9 max-lg:hidden"
        ),
        rx.el.div(
            class_name="absolute bottom-0 right-0 w-px h-24 bg-gradient-to-b from-current to-transparent text-m-slate-4 dark:text-m-slate-9 max-lg:hidden"
        ),
        rx.el.div(
            class_name="absolute bottom-0 left-0 w-px h-24 bg-gradient-to-b from-current to-transparent text-m-slate-4 dark:text-m-slate-9 max-lg:hidden"
        ),
        class_name="flex flex-col w-full xl:max-w-[42rem] xl:ml-auto mt-12 pb-12 relative max-lg:overflow-hidden",
    )
