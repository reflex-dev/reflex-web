from enum import StrEnum
from typing import TypedDict

import reflex as rx
import reflex_ui as ui
from reflex.experimental import ClientStateVar


class Companies(StrEnum):
    OPEN_SEA = "open_sea"
    FASTLY = "fastly"
    AUTODESK = "autodesk"
    ACCENTURE = "accenture"


class CompanyInfo(TypedDict):
    name: str
    title: str
    quote: str


COMPANIES_INFO: dict[Companies, CompanyInfo] = {
    Companies.OPEN_SEA: {
        "name": "Alex Atallah",
        "title": "Co-founder & CEO, OpenSea",
        "image": "/landing/social/alex_opensea.webp",
        "quote": "Have been playing with Reflex since January and realized I should just say, from a fellow YC member: love the architecture decisions you guys are making!",
    },
    Companies.FASTLY: {
        "name": "Alex Atallah",
        "title": "Co-founder & CEO, OpenSea",
        "image": "/landing/social/alex_opensea.webp",
        "quote": "Have been playing with Reflex since January and realized I should just say, from a fellow YC member: love the architecture decisions you guys are making!",
    },
    Companies.AUTODESK: {
        "name": "Alex Atallah",
        "title": "Co-founder & CEO, OpenSea",
        "image": "/landing/social/alex_opensea.webp",
        "quote": "Have been playing with Reflex since January and realized I should just say, from a fellow YC member: love the architecture decisions you guys are making!",
    },
    Companies.ACCENTURE: {
        "name": "Alex Atallah",
        "title": "Co-founder & CEO, OpenSea",
        "image": "/landing/social/alex_opensea.webp",
        "quote": "Have been playing with Reflex since January and realized I should just say, from a fellow YC member: love the architecture decisions you guys are making!",
    },
}


active_company_cs = ClientStateVar.create(
    "active_company_cs", default=Companies.OPEN_SEA
)


def company_card(company: Companies) -> rx.Component:
    return rx.el.button(
        rx.image(
            src=f"/migration/{rx.color_mode_cond('light', 'dark')}/{company}.svg",
            alt=f"{company} logo",
            loading="lazy",
            class_name=ui.cn(
                "transition-[filter] group-hover:brightness-0 dark:group-hover:brightness-[10]",
                rx.cond(
                    active_company_cs.value == company,
                    "brightness-0 dark:brightness-[10]",
                    "",
                ),
            ),
        ),
        aria_label=f"Company: {company}",
        on_click=active_company_cs.set_value(company),
        class_name=ui.cn(
            "flex justify-end items-center h-12 py-3.5 lg:pr-12 pr-3.5 group",
            rx.cond(
                active_company_cs.value == company,
                "lg:shadow-[1px_0_0_0_var(--m-slate-12)] lg:dark:shadow-[1px_0_0_0_var(--m-slate-3)]",
                "",
            ),
        ),
    )


def quote_card(company: Companies) -> rx.Component:
    return rx.el.div(
        rx.el.p(
            COMPANIES_INFO[company]["quote"],
            class_name="text-m-slate-12 dark:text-m-slate-3 text-lg font-[575] text-pretty",
        ),
        rx.el.div(
            ui.gradient_profile(
                seed=COMPANIES_INFO[company]["name"],
                class_name="size-6 rounded-full",
            )
            if not COMPANIES_INFO[company]["image"]
            else rx.image(
                src=COMPANIES_INFO[company]["image"],
                loading="lazy",
                alt=f"{company} logo",
                class_name="size-6 rounded-full",
            ),
            rx.el.span(
                COMPANIES_INFO[company]["name"],
                class_name="text-m-slate-12 dark:text-m-slate-3 text-sm font-[525]",
            ),
            rx.el.span(
                COMPANIES_INFO[company]["title"],
                class_name="text-m-slate-7 dark:text-m-slate-6 text-sm font-[525]",
            ),
            class_name="flex flex-row items-center gap-3",
        ),
        class_name="flex flex-col gap-8 lg:px-12 lg:pt-16 p-6 lg:w-[33rem] w-full",
    )


def companies_column() -> rx.Component:
    return rx.el.div(
        company_card(Companies.OPEN_SEA),
        company_card(Companies.FASTLY),
        company_card(Companies.AUTODESK),
        company_card(Companies.ACCENTURE),
        rx.el.div(
            class_name="absolute -bottom-24 -right-px w-px h-24 bg-gradient-to-b from-current to-transparent text-m-slate-4 dark:text-m-slate-10 max-lg:hidden"
        ),
        class_name="flex max-lg:px-6 max-lg:overflow-x-auto lg:flex-col flex-row gap-2 pt-13 lg:max-w-[12rem] w-full lg:border-r border-m-slate-4 dark:border-m-slate-10 relative max-lg:justify-center",
    )


def quotes() -> rx.Component:
    return rx.el.section(
        companies_column(),
        rx.match(
            active_company_cs.value,
            (Companies.OPEN_SEA, quote_card(Companies.OPEN_SEA)),
            (Companies.FASTLY, quote_card(Companies.FASTLY)),
            (Companies.AUTODESK, quote_card(Companies.AUTODESK)),
            (Companies.ACCENTURE, quote_card(Companies.ACCENTURE)),
            quote_card(Companies.OPEN_SEA),
        ),
        class_name="flex lg:flex-row flex-col pb-24",
    )
