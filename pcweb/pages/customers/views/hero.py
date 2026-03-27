import reflex as rx

from pcweb.pages.customers.views.customer_cards import customer_cards


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Customers",
                    class_name="text-sm font-[525] text-primary-10 max-lg:text-center dark:text-primary-9",
                ),
                rx.el.h1(
                    "Meet the teams who chose Reflex",
                    class_name="text-m-slate-12 dark:text-m-slate-3 lg:text-5xl text-3xl font-[575]",
                ),
                rx.el.h2(
                    "Companies of all sizes trust Reflex to build internal tools and customer-facing apps",
                    class_name="text-m-slate-7 dark:text-m-slate-6 text-base font-[475]",
                ),
                class_name="flex flex-col gap-6 lg:max-w-[21rem] lg:sticky mt-[5rem] lg:top-[9rem] lg:self-start max-lg:self-center max-lg:items-center max-lg:text-center",
            ),
            customer_cards(),
            class_name="flex lg:flex-row flex-col max-xl:gap-6 max-w-(--docs-layout-max-width) mx-auto relative lg:pb-24 pb-6 max-xl:px-6",
        ),
        class_name="w-full relative",
    )
