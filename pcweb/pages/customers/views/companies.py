from dataclasses import dataclass
from enum import StrEnum

import reflex as rx
import reflex_ui as ui
from reflex.experimental.client_state import ClientStateVar

from pcweb.constants import REFLEX_ASSETS_CDN


class FilterTab(StrEnum):
    ALL = "All"
    AI = "AI"
    AUTH = "Auth"
    DATA = "Data"
    SAAS = "SaaS"


@dataclass(frozen=True)
class Company:
    name: str
    filters: tuple[FilterTab, ...]


companies_list: list[Company] = [
    Company(name="apple", filters=(FilterTab.SAAS,)),
    Company(name="microsoft", filters=(FilterTab.AI, FilterTab.DATA)),
    Company(name="amazon", filters=(FilterTab.AI, FilterTab.DATA, FilterTab.SAAS)),
    Company(name="fastly", filters=(FilterTab.AUTH, FilterTab.SAAS)),
    Company(name="accenture", filters=(FilterTab.DATA,)),
    Company(name="ibm", filters=(FilterTab.AI, FilterTab.DATA)),
    Company(name="unicef", filters=(FilterTab.DATA,)),
    Company(name="autodesk", filters=(FilterTab.AI,)),
    Company(name="sellerx", filters=(FilterTab.AI, FilterTab.DATA)),
    Company(name="ford", filters=(FilterTab.DATA,)),
    Company(name="paloalto", filters=(FilterTab.AUTH,)),
    Company(name="bosch", filters=(FilterTab.DATA,)),
    Company(name="dell", filters=(FilterTab.DATA, FilterTab.SAAS)),
    Company(name="twilio", filters=(FilterTab.AUTH, FilterTab.SAAS)),
    Company(name="rappi", filters=(FilterTab.DATA,)),
    Company(name="theworldbank", filters=(FilterTab.DATA,)),
    Company(name="redhat", filters=(FilterTab.SAAS,)),
    Company(name="nike", filters=(FilterTab.DATA,)),
]


filter_tab_cs = ClientStateVar.create(
    "filter_tab",
    default=FilterTab.ALL,
)


def tab_item(tab: str) -> rx.Component:
    active_cn = " shadow-[0_-1px_0_0_rgba(0,0,0,0.08)_inset,0_0_0_1px_rgba(0,0,0,0.08)_inset,0_1px_2px_0_rgba(0,0,0,0.02),0_1px_4px_0_rgba(0,0,0,0.02)] dark:shadow-[0_1px_0_0_rgba(255,255,255,0.16)_inset] bg-white dark:bg-m-slate-10 hover:bg-m-slate-2 dark:hover:bg-m-slate-9 text-m-slate-12 dark:text-m-slate-3"
    unactive_cn = " hover:text-m-slate-12 dark:hover:text-m-slate-3 text-m-slate-7 dark:text-m-slate-6"
    return rx.el.button(
        rx.text(tab.value, class_name="text-sm"),
        on_click=filter_tab_cs.set_value(tab),
        class_name=ui.cn(
            "flex items-center cursor-pointer justify-center rounded-lg transition-colors h-7 px-2 outline-none focus:outline-none ",
            rx.cond(filter_tab_cs.value == tab, active_cn, unactive_cn),
        ),
        custom_attrs={"aria-label": f"Toggle {tab} filter"},
    )


def companies_tabs() -> rx.Component:
    return rx.box(
        tab_item(FilterTab.ALL),
        tab_item(FilterTab.AI),
        tab_item(FilterTab.AUTH),
        tab_item(FilterTab.DATA),
        tab_item(FilterTab.SAAS),
        class_name="flex flex-row gap-0.5 items-center p-0.5 [box-shadow:0_1px_0_0_rgba(0,_0,_0,_0.08),_0_0_0_1px_rgba(0,_0,_0,_0.08),_0_1px_2px_0_rgba(0,_0,_0,_0.02),_0_1px_4px_0_rgba(0,_0,_0,_0.02)] w-fit bg-m-slate-1 dark:bg-m-slate-12 rounded-[0.625rem] dark:border dark:border-m-slate-9 border border-transparent mt-2",
    )


def company_card(company: Company) -> rx.Component:
    is_matching_filter = filter_tab_cs.value == FilterTab.ALL
    for tab in company.filters:
        is_matching_filter = is_matching_filter | (filter_tab_cs.value == tab)

    return rx.box(
        rx.box(
            # Light
            rx.image(
                src=f"{REFLEX_ASSETS_CDN}landing/companies/light/{company.name}.svg",
                class_name="w-[5.5rem] h-auto pointer-events-none group-hover:grayscale-0 grayscale-[1] dark:hidden",
                loading="lazy",
                filter="brightness(0) saturate(100%) invert(44%) sepia(16%) saturate(383%) hue-rotate(178deg) brightness(93%) contrast(85%)",
                alt=f"{company.name} logo",
            ),
            # Dark
            rx.image(
                src=f"{REFLEX_ASSETS_CDN}landing/companies/dark/{company.name}.svg",
                class_name="w-[5.5rem] h-auto pointer-events-none group-hover:grayscale-0 grayscale-[1] dark:block hidden",
                loading="lazy",
                filter="brightness(0) saturate(100%) invert(44%) sepia(16%) saturate(383%) hue-rotate(178deg) brightness(93%) contrast(85%)",
                alt=f"{company.name} logo",
            ),
            class_name=ui.cn(
                "w-full h-[10.75rem] flex justify-center items-center border-box transition-colors group",
                rx.cond(is_matching_filter, "opacity-100", "opacity-30"),
            ),
        ),
        class_name=(
            "relative w-full group border-b border-r border-m-slate-4 dark:border-m-slate-9 transition-opacity",
        ),
    )


def companies() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "All Companies",
                    class_name="text-sm font-[525] text-primary-10 max-lg:text-center dark:text-primary-9",
                ),
                rx.el.h1(
                    "From startups to global enterprises, ambitious builders choose Reflex",
                    class_name="text-m-slate-12 dark:text-m-slate-3 lg:text-4xl text-3xl font-[575] shrink-0 max-w-[42rem] text-center",
                ),
                companies_tabs(),
                class_name="relative flex flex-col gap-6 lg:pt-24 pt-16 justify-center items-center",
            ),
            rx.el.div(
                rx.el.div(
                    class_name="absolute -top-24 left-0 w-px h-24 bg-gradient-to-t from-current to-transparent text-m-slate-4 dark:text-m-slate-10"
                ),
                rx.el.div(
                    class_name="absolute -top-24 right-0 w-px h-24 bg-gradient-to-t from-current to-transparent text-m-slate-4 dark:text-m-slate-10"
                ),
                rx.el.div(
                    class_name="absolute top-0 -right-24 w-24 h-px bg-gradient-to-l from-transparent to-current text-m-slate-4 dark:text-m-slate-10 max-lg:hidden"
                ),
                rx.el.div(
                    class_name="absolute top-0 -left-24 w-24 h-px bg-gradient-to-r from-transparent to-current text-m-slate-4 dark:text-m-slate-10 max-lg:hidden"
                ),
                rx.el.div(
                    class_name="absolute bottom-0 -left-24 w-24 h-px bg-gradient-to-r from-transparent to-current text-m-slate-4 dark:text-m-slate-10 max-lg:hidden"
                ),
                rx.el.div(
                    class_name="absolute bottom-0 -right-24 w-24 h-px bg-gradient-to-l from-transparent to-current text-m-slate-4 dark:text-m-slate-10 max-lg:hidden"
                ),
                rx.el.div(
                    class_name="absolute -bottom-24 left-0 w-px h-24 bg-gradient-to-b from-current to-transparent text-m-slate-4 dark:text-m-slate-10"
                ),
                rx.el.div(
                    class_name="absolute -bottom-24 right-0 w-px h-24 bg-gradient-to-b from-current to-transparent text-m-slate-4 dark:text-m-slate-10"
                ),
                rx.el.div(
                    *[
                        company_card(
                            company=company,
                        )
                        for company in companies_list
                    ],
                    class_name="grid grid-cols-6 w-full relative border-l border-t border-m-slate-4 dark:border-m-slate-9",
                ),
                class_name="relative w-full",
            ),
            class_name="flex flex-col justify-center items-center gap-16 max-w-(--docs-layout-max-width) relative mx-auto",
        ),
        class_name="bg-gradient-to-b from-white-1 to-m-slate-1 dark:from-m-slate-11 dark:to-m-slate-12 w-full lg:mb-24 mb-10 max-lg:hidden",
    )
