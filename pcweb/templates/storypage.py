import functools
from dataclasses import dataclass, field
from typing import Callable

import reflex as rx
import reflex_ui as ui
from flexdown.document import Document

from pcweb.components.hosting_banner import HostingBannerState
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
        return f"/customers/{self.company.lower().replace(' ', '-')}"

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


def gradient_logo() -> rx.Component:
    return rx.el.div(
        rx.image(
            src=f"{REFLEX_ASSETS_CDN}logos/{rx.color_mode_cond('light', 'dark')}/gradient_r.svg",
            alt="Gradient Reflex Logo",
            loading="eager",
            class_name="size-full",
            custom_attrs={"fetchPriority": "high"},
        ),
        class_name="flex size-48 items-center justify-center absolute right-0 top-[15rem] left-[20.5rem] -translate-y-1/2 z-0",
    )


def gradient_logo_blur_layer() -> rx.Component:
    return rx.el.div(
        class_name=(
            "absolute left-[21rem] top-[15rem] -translate-y-1/2 "
            "w-24 h-60 z-[1] bg-[rgba(252,252,253,0.01)] backdrop-blur-[36px] pointer-events-none"
        ),
    )


def company_floating_card(company: str) -> rx.Component:
    return rx.el.div(
        rx.image(
            src=f"{REFLEX_ASSETS_CDN}customers/{rx.color_mode_cond('light', 'dark')}/{company.lower()}/{company.lower()}_small.svg",
            alt=f"{company} logo",
            loading="eager",
            custom_attrs={"fetchPriority": "high"},
            class_name="w-auto h-[9.5rem]",
        ),
        class_name=ui.cn(
            "size-[19rem] flex items-center justify-center absolute z-[2] rounded-[5rem] backdrop-blur-[36px] bg-linear-to-b from-m-slate-1 to-m-slate-2  dark:from-m-slate-11 dark:to-m-slate-12 shadow-[0_1px_0_0_#FFF_inset,_0_0_0_1px_rgba(0,_0,_0,_0.12),_0_16px_32px_0_rgba(0,_0,_0,_0.06),_0_1px_1px_0_rgba(0,_0,_0,_0.01),_0_8px_16px_0_rgba(0,_0,_0,_0.02)] top-[5.5rem] left-[3.5rem] dark:shadow-none dark:border dark:border-m-slate-9",
        ),
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
                class_name="text-m-slate-12 dark:text-m-slate-3 lg:text-5xl text-4xl font-[575] text-start",
            ),
            rx.el.h2(
                study.description,
                class_name="text-m-slate-7 dark:text-m-slate-6 text-base font-[475] text-balance",
            ),
            class_name="flex flex-col gap-6 xl:max-w-[30rem] justify-start pt-24 xl:pb-34 pb-16 z-1 xl:min-h-[30rem] max-xl:px-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.image(
                    src=f"{REFLEX_ASSETS_CDN}common/{rx.color_mode_cond('light', 'dark')}/grid.svg",
                    alt="Grid",
                    loading="eager",
                    custom_attrs={"fetchPriority": "high"},
                    class_name=ui.cn(
                        "absolute -right-22 top-0 z-[-1] w-[45rem] h-[27rem] max-w-none pointer-events-none",
                    ),
                ),
                gradient_logo(),
                company_floating_card(study.company),
                class_name="relative isolate h-full w-full",
            ),
            class_name="flex-1 max-xl:hidden",
        ),
        class_name="flex flex-row lg:px-4 max-w-(--docs-layout-max-width) w-full mx-auto border-b border-m-slate-4 dark:border-m-slate-9 relative",
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
            class_name="grid lg:grid-cols-3 grid-cols-1 gap-4 lg:gap-12 border-r border-m-slate-4 dark:border-m-slate-9 pt-8 xl:pr-12 pr-8 max-xl:pl-4 max-xl:pb-8",
        ),
        rx.el.div(
            rx.el.div(
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
            class_name="flex flex-col gap-4 p-8 xl:w-[21rem] shrink-0",
        ),
        rx.el.div(
            class_name="absolute -top-px -right-24 w-24 h-px bg-gradient-to-l from-transparent to-current text-m-slate-4 dark:text-m-slate-10 max-lg:hidden"
        ),
        rx.el.div(
            class_name="absolute -top-px -left-24 w-24 h-px bg-gradient-to-r from-transparent to-current text-m-slate-4 dark:text-m-slate-10 max-lg:hidden"
        ),
        rx.el.div(
            class_name="absolute -bottom-px -left-24 w-24 h-px bg-gradient-to-r from-transparent to-current text-m-slate-4 dark:text-m-slate-10 max-lg:hidden"
        ),
        rx.el.div(
            class_name="absolute -bottom-px -right-24 w-24 h-px bg-gradient-to-l from-transparent to-current text-m-slate-4 dark:text-m-slate-10 max-lg:hidden"
        ),
        class_name="flex flex-row  max-w-(--docs-layout-max-width) w-full mx-auto border-b border-m-slate-4 dark:border-m-slate-9 relative max-2xl:overflow-hidden",
    )


def story_table_of_contents(toc: list, path: str, company: str) -> rx.Component:
    """Render the table of contents sidebar for a case study page."""
    if len(toc) < 2:
        return rx.fragment()

    return rx.el.nav(
        rx.el.div(
            class_name="absolute -top-8 left-0 w-px h-8 bg-gradient-to-b from-transparent to-current text-m-slate-4 dark:text-m-slate-9 max-lg:hidden"
        ),
        rx.box(
            rx.el.ul(
                rx.el.li(
                    f"Reflex X {company}",
                    class_name="text-xs flex items-center justify-start font-[415] dark:text-m-slate-3 text-m-slate-12 font-mono uppercase pb-6 pl-8",
                ),
                *[
                    rx.el.li(
                        rx.el.a(
                            text,
                            class_name=ui.cn(
                                "text-sm font-[525] text-m-slate-7 dark:text-m-slate-6 py-1 block hover:text-m-slate-9 dark:hover:text-m-slate-5 transition-colors truncate",
                                "pl-8" if level <= 2 else "pl-12",
                            ),
                            href=path + "#" + text.lower().replace(" ", "-"),
                        ),
                    )
                    for level, text in toc
                ],
                id="toc-navigation",
                class_name="flex flex-col gap-y-1 list-none shadow-[1px_0_0_0_var(--m-slate-4)_inset] dark:shadow-[1px_0_0_0_var(--m-slate-9)_inset]",
            ),
            class_name="flex flex-col justify-start gap-y-4 overflow-y-auto",
        ),
        on_mount=rx.call_script(right_sidebar_item_highlight()),
        class_name=ui.cn(
            "sticky w-[21.05rem] shrink-0 hidden xl:block self-start max-lg:hidden",
            rx.cond(
                HostingBannerState.is_banner_visible,
                "top-[8.5rem]",
                "top-[6.5rem]",
            ),
        ),
    )


CAROUSEL_SCROLL_JS = """
(function(direction) {
    const container = document.getElementById('more-customers-carousel');
    if (!container) return;
    const cards = Array.from(container.querySelectorAll('a'));
    if (!cards.length) return;
    const gap = 24;
    const containerLeft = container.getBoundingClientRect().left;
    const paddingLeft = parseFloat(getComputedStyle(container).paddingLeft) || 0;

    // Find the current card index based on scroll position
    let currentIdx = 0;
    for (let i = 0; i < cards.length; i++) {
        const cardLeft = cards[i].getBoundingClientRect().left - containerLeft - paddingLeft;
        if (cardLeft >= -10) { currentIdx = i; break; }
    }

    const targetIdx = Math.max(0, Math.min(cards.length - 1, currentIdx + direction));
    const targetScroll = targetIdx * (cards[0].offsetWidth + gap);
    container.scrollTo({ left: targetScroll, behavior: 'smooth' });
})
"""

CAROUSEL_FADE_INIT_JS = """
(function() {
    const container = document.getElementById('more-customers-carousel');
    const fadeL = document.getElementById('carousel-fade-left');
    const fadeR = document.getElementById('carousel-fade-right');
    if (!container || !fadeL || !fadeR) return;

    function update() {
        const sl = container.scrollLeft;
        const maxScroll = container.scrollWidth - container.clientWidth;
        fadeL.style.opacity = '1';
        fadeR.style.opacity = sl >= maxScroll - 2 ? '0' : '1';
    }

    container.addEventListener('scroll', update);
    update();
})()
"""


def more_customers(current_customer: str) -> rx.Component:
    from pcweb.pages.customers.views.customer_cards import CUSTOMERS, customer_card

    others = [c for c in CUSTOMERS if c["name"] != current_customer]
    if not others:
        return rx.fragment()

    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                "See what other teams built",
                class_name="text-m-slate-12 dark:text-m-slate-3 lg:text-3xl text-xl font-[575]",
            ),
            rx.el.div(
                ui.button(
                    ui.icon("ArrowLeft01Icon", class_name="size-4"),
                    on_click=rx.call_script(f"{CAROUSEL_SCROLL_JS}(-1)"),
                    variant="outline-shadow",
                    size="sm",
                ),
                ui.button(
                    ui.icon("ArrowRight01Icon", class_name="size-4"),
                    on_click=rx.call_script(f"{CAROUSEL_SCROLL_JS}(1)"),
                    variant="outline-shadow",
                    size="sm",
                ),
                class_name="flex flex-row items-center gap-2",
            ),
            class_name="flex flex-row items-center justify-between w-full max-w-(--docs-layout-max-width) mx-auto max-xl:px-6",
        ),
        rx.el.div(
            rx.el.div(
                *[customer_card(customer) for customer in others],
                id="more-customers-carousel",
                class_name="flex flex-row gap-6 overflow-x-auto scroll-smooth [scrollbar-width:none] [&::-webkit-scrollbar]:hidden pl-[6rem] pr-8 py-8 -my-8 max-lg:pl-6 max-lg:pr-6",
            ),
            rx.el.div(
                id="carousel-fade-left",
                class_name="absolute left-0 inset-y-0 w-24 bg-gradient-to-r from-m-slate-1 dark:from-m-slate-12 to-transparent pointer-events-none z-10 transition-opacity",
            ),
            rx.el.div(
                id="carousel-fade-right",
                class_name="absolute right-0 inset-y-0 w-24 bg-gradient-to-l from-m-slate-1 dark:from-m-slate-12 to-transparent pointer-events-none z-10 transition-opacity",
            ),
            class_name="relative",
        ),
        rx.script(CAROUSEL_FADE_INIT_JS),
        class_name="flex flex-col gap-8 lg:mt-20 mt-6 lg:mb-24 mb-12 max-w-[81rem] w-full mx-auto",
    )


def storypage(study: CaseStudy, add_as_page: bool = True) -> Callable:
    """A template that wraps a case study page with navbar, hero, stats, TOC, and footer."""
    toc_raw, _ = get_toc(study.document, study.route)
    toc = [(level, text) for level, text in toc_raw if level <= 3]

    def storypage(contents: Callable[[], Route]) -> Route:
        @functools.wraps(contents)
        def wrapper(*children, **props) -> rx.Component:
            from pcweb.pages.customers.views.book_a_demo import book_a_demo
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
                                class_name="flex flex-col gap-4 flex-1 xl:max-w-2xl w-full",
                            ),
                            story_table_of_contents(toc, study.route, study.company),
                            class_name="flex flex-row gap-24 max-w-(--docs-layout-max-width) mx-auto w-full lg:pb-24 pb-12 pt-8 max-lg:px-6 justify-between",
                        ),
                        more_customers(study.company),
                        rx.el.hr(
                            class_name="w-full border-t border-m-slate-4 dark:border-m-slate-9",
                        ),
                        rx.el.div(
                            book_a_demo(),
                            class_name="bg-gradient-to-b from-white-1 to-m-slate-1 dark:from-m-slate-11 dark:to-m-slate-12 w-full mb-10 max-lg:hidden",
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
                class_name="flex flex-col w-full justify-center items-center relative bg-secondary-1",
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
