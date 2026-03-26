import functools
from dataclasses import dataclass, field
from typing import Callable

import reflex as rx
import reflex_ui as ui
from flexdown.document import Document

from pcweb.components.hosting_banner import HostingBannerState
from pcweb.components.icons.icons import get_icon
from pcweb.components.marketing_button import button as marketing_button
from pcweb.constants import REFLEX_ASSETS_CDN
from pcweb.route import Route
from pcweb.templates.docpage import get_toc, right_sidebar_item_highlight


@dataclass(frozen=True)
class CaseStudy:
    company: str
    description: str
    domain: str
    founded: str
    document: Document
    stats: list[dict[str, str]] = field(default_factory=list)
    meta: list[dict[str, str]] = field(default_factory=list)
    investors: str | None = None
    h1: str | None = None

    @property
    def route(self) -> str:
        return f"/customers/{self.company.lower()}"

    @property
    def title(self) -> str:
        return f"{self.company} Case Study - Reflex Customer Stories"

    @classmethod
    def from_document(cls, document: Document) -> "CaseStudy":
        m = document.metadata
        return cls(
            company=m["company"],
            description=m["description"],
            domain=m["domain"],
            founded=m["founded"],
            document=document,
            stats=m["stats"],
            meta=m.get("meta", []),
            investors=m.get("investors"),
            h1=m.get("h1"),
        )


def hero(study: CaseStudy) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    marketing_button(
                        "Customers",
                        icon="ArrowRight01Icon",
                        native_button=False,
                        variant="ghost",
                        size="xs",
                    ),
                    to="/customers",
                ),
                ui.icon(
                    "ArrowRight01Icon",
                    class_name="text-m-slate-7 dark:text-m-slate-6",
                ),
                rx.el.span(
                    study.company,
                    class_name="text-m-slate-7 dark:text-m-slate-6 text-sm font-[525]",
                ),
                class_name="flex items-center gap-3",
            ),
            rx.el.h1(
                study.h1 or study.company,
                class_name="text-m-slate-12 dark:text-m-slate-3 lg:text-5xl text-3xl font-[575] text-start",
            ),
            rx.el.h2(
                study.description,
                class_name="text-m-slate-7 dark:text-m-slate-6 text-base font-[475]",
            ),
            class_name="flex flex-col gap-6 max-w-[30rem] justify-start",
        ),
        class_name="flex flex-row lg:px-4 max-w-(--docs-layout-max-width) w-full mx-auto py-24 border-b border-m-slate-4 dark:border-m-slate-9",
    )


def stats_cards(study: CaseStudy) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            *[
                rx.el.div(
                    rx.el.span(
                        stat["value"],
                        class_name="text-m-slate-12 dark:text-m-slate-3 lg:text-6xl text-3xl font-[415] font-mono",
                    ),
                    rx.el.span(
                        stat["metric"],
                        class_name="text-m-slate-7 dark:text-m-slate-6 text-xs font-[475]",
                    ),
                    class_name="flex flex-col gap-2",
                )
                for stat in study.stats
            ],
            class_name="grid grid-cols-3 gap-4 lg:gap-12 border-r border-m-slate-4 dark:border-m-slate-9 pt-8 pr-12",
        ),
        rx.el.div(
            rx.box(
                rx.el.span(
                    "Founded",
                    class_name="text-m-slate-7 dark:text-m-slate-6 text-xs font-[415] font-mono uppercase",
                ),
                rx.el.span(
                    study.founded,
                    class_name="text-m-slate-12 dark:text-m-slate-3 lg:text-base text-sm font-[415] uppercase font-mono",
                ),
                class_name="flex flex-col gap-1",
            ),
            rx.cond(
                study.investors,
                rx.el.div(
                    rx.el.span(
                        "Investors",
                        class_name="text-m-slate-7 dark:text-m-slate-6 text-xs font-[415] font-mono uppercase",
                    ),
                    rx.el.span(
                        study.investors,
                        class_name="text-m-slate-12 dark:text-m-slate-3 lg:text-base text-xs font-[415] uppercase font-mono",
                    ),
                    class_name="flex flex-col gap-1",
                ),
            ),
            rx.el.div(
                rx.el.span(
                    "Website",
                    class_name="text-m-slate-7 dark:text-m-slate-6 text-xs font-[415] font-mono uppercase",
                ),
                rx.el.a(
                    rx.el.span(
                        study.domain.split("//")[-1].split("/")[0].replace("www.", ""),
                        class_name="text-xs font-[415] uppercase font-mono",
                    ),
                    rx.icon(
                        tag="arrow-up-right",
                        stroke_width="2.25",
                        class_name="size-3.5",
                    ),
                    to=study.domain,
                    underline="none",
                    target="_blank",
                    class_name="flex flex-row items-center gap-1.5 underline underline-offset-1 text-m-slate-12 dark:text-m-slate-3 ",
                ),
                class_name="flex flex-col gap-1",
            ),
            class_name="flex flex-col gap-4 p-8",
        ),
        class_name="flex flex-row lg:px-4 max-w-(--docs-layout-max-width) w-full mx-auto border-b border-m-slate-4 dark:border-m-slate-9",
    )


def story_table_of_contents(toc: list, path: str, company: str) -> rx.Component:
    """Render the table of contents sidebar for a case study page."""
    if len(toc) < 2:
        return rx.fragment()

    return rx.el.nav(
        rx.box(
            rx.el.p(
                f"Reflex X {company}",
                class_name="text-xs h-8 flex items-center justify-start font-[415] dark:text-m-slate-3 text-m-slate-12 font-mono uppercase",
            ),
            rx.el.ul(
                *[
                    rx.el.li(
                        rx.el.a(
                            text,
                            class_name=ui.cn(
                                "text-sm font-[525] text-m-slate-7 dark:text-m-slate-6 py-1 block hover:text-m-slate-9 dark:hover:text-m-slate-5 transition-colors truncate",
                                "pl-4" if level <= 2 else "pl-8",
                            ),
                            href=path + "#" + text.lower().replace(" ", "-"),
                        ),
                    )
                    for level, text in toc
                ],
                id="toc-navigation",
                class_name="flex flex-col gap-y-1 list-none shadow-[1.5px_0_0_0_var(--m-slate-4)_inset] dark:shadow-[1.5px_0_0_0_var(--m-slate-9)_inset]",
            ),
            class_name="flex flex-col justify-start gap-y-4 overflow-y-auto",
        ),
        on_mount=rx.call_script(right_sidebar_item_highlight()),
        class_name=ui.cn(
            "sticky w-[17.5rem] shrink-0 hidden xl:block self-start max-lg:hidden",
            rx.cond(
                HostingBannerState.is_banner_visible,
                "top-[8.5rem]",
                "top-[6.5rem]",
            ),
        ),
    )


def more_customers(current_customer: str) -> rx.Component:
    from pcweb.pages.customers.data.customers import customer_data

    customer_items = list(customer_data.items())

    # Filter out the current company
    other_customers = [
        c for c in customer_items if c[1].metadata.get("company") != current_customer
    ]
    if not other_customers:
        return rx.box()

    current_index = next(
        (
            i
            for i, (_, doc) in enumerate(customer_items)
            if doc.metadata.get("company") == current_customer
        ),
        0,
    )

    prev_index = (current_index - 1) % len(customer_items)
    next_index = (current_index + 1) % len(customer_items)

    prev_customer = customer_items[prev_index]
    next_customer = customer_items[next_index]

    while prev_customer[1].metadata.get("company") == current_customer:
        prev_index = (prev_index - 1) % len(customer_items)
        prev_customer = customer_items[prev_index]

    while next_customer[1].metadata.get("company") == current_customer:
        next_index = (next_index + 1) % len(customer_items)
        next_customer = customer_items[next_index]

    customers = [
        rx.box(
            rx.link(
                rx.box(
                    "Previous",
                    get_icon(icon="arrow_right", class_name="rotate-180"),
                    class_name="flex flex-row-reverse justify-center lg:justify-start items-center gap-2 rounded-lg w-full self-end",
                ),
                underline="none",
                href=f"/customers/{prev_customer[1].metadata['company'].lower()}",
                class_name="py-0.5 lg:py-0 rounded-lg lg:w-auto font-small text-slate-9 hover:!text-slate-11 transition-color",
            ),
            rx.box(
                rx.image(
                    src=rx.color_mode_cond(
                        light=f"{REFLEX_ASSETS_CDN}customers/light/{prev_customer[1].metadata['company'].lower()}/{prev_customer[1].metadata['company'].lower()}_small.svg",
                        dark=f"{REFLEX_ASSETS_CDN}customers/dark/{prev_customer[1].metadata['company'].lower()}/{prev_customer[1].metadata['company'].lower()}_small.svg",
                    ),
                    alt=f"{next_customer[1].metadata['company']} logo",
                    loading="lazy",
                    class_name="h-[1.25rem] w-auto",
                ),
                rx.text(
                    prev_customer[1].metadata["company"],
                    class_name="font-smbold text-slate-12",
                ),
                class_name="flex flex-row justify-start gap-2.5 items-center",
            ),
            class_name="flex flex-col justify-start gap-1 items-start",
        ),
        rx.box(
            rx.link(
                rx.box(
                    "Next",
                    get_icon(icon="arrow_right"),
                    class_name="flex flex-row justify-center lg:justify-start items-center gap-2 rounded-lg w-full self-end",
                ),
                underline="none",
                href=f"/customers/{next_customer[1].metadata['company'].lower()}",
                class_name="py-0.5 lg:py-0 rounded-lg lg:w-auto font-small text-slate-9 hover:!text-slate-11 transition-color",
            ),
            rx.box(
                rx.text(
                    next_customer[1].metadata["company"],
                    class_name="font-smbold text-slate-12",
                ),
                rx.image(
                    src=rx.color_mode_cond(
                        light=f"{REFLEX_ASSETS_CDN}customers/light/{next_customer[1].metadata['company'].lower()}/{next_customer[1].metadata['company'].lower()}_small.svg",
                        dark=f"{REFLEX_ASSETS_CDN}customers/dark/{next_customer[1].metadata['company'].lower()}/{next_customer[1].metadata['company'].lower()}_small.svg",
                    ),
                    alt=f"{next_customer[1].metadata['company']} logo",
                    loading="lazy",
                    class_name="h-[1.25rem] w-auto",
                ),
                class_name="flex flex-row justify-start gap-2.5 items-center",
            ),
            class_name="flex flex-col justify-start gap-1 items-end",
        ),
    ]

    return rx.box(
        rx.box(
            *customers,
            class_name="flex flex-row gap-4 justify-between items-center",
        ),
        class_name="flex flex-col gap-6 mt-20",
    )


def storypage(study: CaseStudy, add_as_page: bool = True) -> Callable:
    """A template that wraps a case study page with navbar, hero, stats, TOC, and footer."""
    toc_raw, _ = get_toc(study.document, study.route)
    toc = [(level, text) for level, text in toc_raw if level <= 3]

    def storypage(contents: Callable[[], Route]) -> Route:
        @functools.wraps(contents)
        def wrapper(*children, **props) -> rx.Component:
            from pcweb.pages.framework.views.footer_index import footer_index
            from pcweb.views.marketing_navbar import marketing_navbar

            return rx.el.div(
                marketing_navbar(),
                rx.el.main(
                    rx.el.div(
                        hero(study),
                        stats_cards(study),
                        rx.el.div(
                            rx.el.div(
                                contents(*children, **props),
                                class_name="flex flex-col gap-4 flex-1 max-w-2xl",
                            ),
                            story_table_of_contents(toc, study.route, study.company),
                            class_name="flex flex-row gap-24 max-w-(--docs-layout-max-width) mx-auto w-full lg:py-24 py-12 max-lg:px-6 justify-between",
                        ),
                        footer_index(),
                        class_name="flex flex-col relative justify-center items-center w-full",
                    ),
                    class_name=ui.cn(
                        "flex flex-col w-full relative h-full justify-center items-center",
                        rx.cond(
                            HostingBannerState.is_banner_visible,
                            "mt-28",
                            "mt-16",
                        ),
                    ),
                ),
                class_name="flex flex-col w-full justify-center items-center relative dark:bg-m-slate-12 bg-m-slate-1",
            )

        return Route(
            path=study.route,
            title=study.title,
            description=study.description,
            meta=study.meta,
            component=wrapper,
            add_as_page=add_as_page,
        )

    return storypage
