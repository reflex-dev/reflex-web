from typing import NotRequired, TypedDict

import reflex as rx
import reflex_ui as ui


class ComparisonItem(TypedDict):
    title: str
    icon: str
    pros: list[str]
    cons: list[str]
    description: NotRequired[str]


def comparison_description(description: str) -> rx.Component:
    return rx.el.p(
        description,
        class_name="text-m-slate-11 dark:text-m-slate-4 lg:text-sm text-xs font-[475] leading-relaxed lg:px-12 lg:py-6 px-6 py-4 border-r border-m-slate-4 dark:border-m-slate-10 bg-m-slate-1 dark:bg-m-slate-10 border-b",
    )


def comparison_title(title: str, icon: str) -> rx.Component:
    return rx.el.div(
        ui.icon(icon, stroke_width=1.5, class_name="shrink-0 lg:size-7 size-6"),
        rx.el.span(
            title,
            class_name="text-m-slate-12 dark:text-m-slate-3 lg:text-lg text-base font-[575]",
        ),
        class_name="flex flex-row items-center gap-3 lg:p-12 p-6 border-y border-r border-m-slate-4 dark:border-m-slate-10",
    )


def pros_card(pros: list[str]) -> rx.Component:
    return rx.el.ul(
        *[
            rx.el.li(
                ui.icon(
                    "Tick02Icon",
                    class_name="shrink-0 text-primary-9 dark:text-primary-10 h-[1.5rem]",
                ),
                rx.el.span(
                    pro,
                    class_name="text-m-slate-12 dark:text-m-slate-3 text-sm font-[525]",
                ),
                class_name="flex flex-row items-start gap-2.5",
            )
            for pro in pros
        ],
        class_name="list-inside flex flex-col gap-2 lg:p-12 p-6 [box-shadow:0_0_0_1px_rgba(0,_0,_0,_0.12)_inset,_0_6px_12px_0_rgba(0,_0,_0,_0.06),_0_1px_1px_0_rgba(0,_0,_0,_0.01),_0_4px_6px_0_rgba(0,_0,_0,_0.02)] dark:shadow-none rounded-xl bg-white-1 dark:bg-m-slate-11 w-full",
    )


def cons_card(cons: list[str]) -> rx.Component:
    return rx.el.ul(
        *[
            rx.el.li(
                ui.icon(
                    "MultiplicationSignIcon",
                    stroke_width=1.5,
                    class_name="shrink-0 text-m-slate-7 dark:text-m-slate-6 h-[1.5rem]",
                ),
                rx.el.span(
                    con,
                    class_name="text-m-slate-7 dark:text-m-slate-6 text-sm font-[525]",
                ),
                class_name="flex flex-row items-start gap-2.5",
            )
            for con in cons
        ],
        class_name="list-inside flex flex-col gap-2 lg:p-12 p-6 w-full lg:border-x border-l border-m-slate-4 dark:border-m-slate-10",
    )


def pros_cons_cards(pros: list[str], cons: list[str]) -> rx.Component:
    return rx.el.div(
        pros_card(pros),
        cons_card(cons),
        class_name="grid lg:grid-cols-2 grid-cols-1 max-lg:border-r",
    )


def top_title(title: str) -> rx.Component:
    return rx.el.span(
        title,
        class_name="text-m-slate-12 dark:text-m-slate-3 text-xs leading-[1.5rem] font-medium font-mono border-r border-m-slate-4 dark:border-m-slate-10 lg:px-12 lg:py-3 p-6 bg-secondary-1 dark:bg-m-slate-10 border-t uppercase",
    )


def heading_with_breaks(lines: list[str]) -> list[rx.Component | str]:
    heading_parts: list[rx.Component | str] = []
    for index, line in enumerate(lines):
        heading_parts.append(line)
        if index < len(lines) - 1:
            heading_parts.append(rx.el.br(class_name="max-lg:hidden"))
    return heading_parts


def comparison_cards(
    top_left_title: str,
    top_right_title: str,
    comparison_items: list[ComparisonItem],
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            top_title(top_left_title),
            top_title(top_right_title),
            class_name="grid grid-cols-2",
        ),
        *[
            rx.fragment(
                comparison_title(item["title"], item["icon"]),
                comparison_description(item["description"])
                if item.get("description")
                else rx.fragment(),
                pros_cons_cards(item["pros"], item["cons"]),
            )
            for item in comparison_items
        ],
        rx.el.div(
            class_name="absolute -top-24 right-0 w-px h-24 bg-gradient-to-b from-transparent to-current text-m-slate-4 dark:text-m-slate-10 max-lg:hidden"
        ),
        rx.el.div(
            class_name="absolute -top-24 -left-px w-px h-24 bg-gradient-to-b from-transparent to-current text-m-slate-4 dark:text-m-slate-10 max-lg:hidden"
        ),
        rx.el.div(
            class_name="absolute -bottom-24 right-0 w-px h-24 bg-gradient-to-b from-current to-transparent text-m-slate-4 dark:text-m-slate-10"
        ),
        rx.el.div(
            class_name="absolute -bottom-24 -left-px w-px h-24 bg-gradient-to-b from-current to-transparent text-m-slate-4 dark:text-m-slate-10"
        ),
        class_name="flex flex-col w-full max-w-[45rem] ml-auto border-l border-m-slate-4 dark:border-m-slate-10 mt-18 border-b mb-24 relative",
    )


def compare(
    *,
    kicker: str,
    heading_lines: list[str],
    description: str,
    top_left_title: str,
    top_right_title: str,
    comparison_items: list[ComparisonItem],
) -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    kicker,
                    class_name="text-sm font-[525] text-primary-10 max-lg:text-center dark:text-m-slate-6",
                ),
                rx.el.h1(
                    *heading_with_breaks(heading_lines),
                    class_name="text-m-slate-12 dark:text-m-slate-3 text-3xl font-[575]",
                ),
                rx.el.h2(
                    description,
                    class_name="text-m-slate-7 dark:text-m-slate-6 text-base font-[475]",
                ),
                class_name="flex flex-col gap-6 lg:max-w-[18rem] lg:sticky lg:top-[11rem] lg:self-start max-lg:self-center max-lg:items-center max-lg:text-center",
            ),
            comparison_cards(top_left_title, top_right_title, comparison_items),
            class_name="flex lg:flex-row flex-col max-lg:gap-6 max-w-(--docs-layout-max-width) mx-auto relative py-24 max-lg:px-6",
        ),
        class_name="bg-gradient-to-b from-white-1 to-m-slate-1 dark:from-m-slate-11 dark:to-m-slate-12 w-full relative",
    )
