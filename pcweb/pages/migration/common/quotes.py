from typing import TypedDict

import reflex as rx
import reflex_ui as ui
from reflex.experimental import ClientStateVar


class CompanyInfo(TypedDict):
    key: str
    logo_image_name: str
    logo_alt: str
    name: str
    title: str
    quote: str
    profile_image: str


active_company_cs = ClientStateVar.create("active_company_cs", default="open_sea")


def company_card(company: CompanyInfo, logo_base_path: str) -> rx.Component:
    return rx.el.button(
        rx.image(
            src=f"{logo_base_path}/{rx.color_mode_cond('light', 'dark')}/{company['logo_image_name']}",
            alt=company["logo_alt"],
            loading="lazy",
            class_name=ui.cn(
                "transition-[filter] group-hover:brightness-0 dark:group-hover:brightness-[10]",
                rx.cond(
                    active_company_cs.value == company["key"],
                    "brightness-0 dark:brightness-[10]",
                    "",
                ),
            ),
        ),
        aria_label=f"Company: {company['key']}",
        on_click=active_company_cs.set_value(company["key"]),
        class_name=ui.cn(
            "flex justify-end items-center h-12 py-3.5 lg:pr-12 pr-3.5 group",
            rx.cond(
                active_company_cs.value == company["key"],
                "lg:shadow-[1px_0_0_0_var(--m-slate-12)] lg:dark:shadow-[1px_0_0_0_var(--m-slate-3)]",
                "",
            ),
        ),
    )


def quote_card(company: CompanyInfo) -> rx.Component:
    return rx.el.div(
        rx.el.p(
            company["quote"],
            class_name="text-m-slate-12 dark:text-m-slate-3 text-lg font-[575] text-pretty",
        ),
        rx.el.div(
            ui.gradient_profile(
                seed=company["name"],
                class_name="size-6 rounded-full",
            )
            if not company["profile_image"]
            else rx.image(
                src=company["profile_image"],
                loading="lazy",
                alt=company["name"],
                class_name="size-6 rounded-full",
            ),
            rx.el.span(
                company["name"],
                class_name="text-m-slate-12 dark:text-m-slate-3 text-sm font-[525]",
            ),
            rx.el.span(
                company["title"],
                class_name="text-m-slate-7 dark:text-m-slate-6 text-sm font-[525]",
            ),
            class_name="flex flex-row items-center gap-3",
        ),
        class_name="flex flex-col gap-8 lg:px-12 lg:pt-16 p-6 lg:w-[33rem] w-full",
    )


def companies_column(companies: list[CompanyInfo], logo_base_path: str) -> rx.Component:
    return rx.el.div(
        *[
            company_card(company, logo_base_path=logo_base_path)
            for company in companies
        ],
        rx.el.div(
            class_name="absolute -bottom-24 -right-px w-px h-24 bg-gradient-to-b from-current to-transparent text-m-slate-4 dark:text-m-slate-10 max-lg:hidden"
        ),
        class_name="flex max-lg:px-6 max-lg:overflow-x-auto lg:flex-col flex-row gap-2 pt-13 lg:max-w-[12rem] w-full lg:border-r border-m-slate-4 dark:border-m-slate-10 relative max-lg:justify-center",
    )


def quotes(
    *,
    companies: list[CompanyInfo],
    default_active_key: str,
    logo_base_path: str,
) -> rx.Component:
    matches: list[tuple[str, rx.Component]] = [
        (company["key"], quote_card(company)) for company in companies
    ]

    return rx.el.section(
        companies_column(companies, logo_base_path=logo_base_path),
        rx.match(
            active_company_cs.value,
            *matches,
            quote_card(companies[0]),
        ),
        on_mount=active_company_cs.set_value(default_active_key),
        class_name="flex lg:flex-row flex-col pb-24 max-w-[45rem] mx-auto w-full dark:bg-[radial-gradient(50%_100%_at_50%_0%,var(--m-slate-11,#1D2025)_50.33%,var(--m-slate-12,#151618)_100%)] bg-[radial-gradient(50%_100%_at_50%_0%,var(white,#fff)_50.33%,var(--m-slate-1,#FCFCFD)_100%)]",
    )
