import reflex as rx
import reflex_ui as ui

from pcweb.components.icons.icons import get_icon
from pcweb.components.numbers_pattern import numbers_pattern


def header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            ui.icon("DatabaseAddIcon", class_name="shrink-0"),
            rx.el.span("Data", class_name="text-sm font-semibold"),
            class_name="flex flex-row gap-2 items-center text-primary-9",
        ),
        rx.el.h2(
            "Connect to Any Data Source",
            class_name="max-w-full w-full lg:text-3xl text-2xl text-center text-slate-12 font-semibold text-balance word-wrap break-words md:whitespace-pre",
        ),
        rx.el.p(
            "Build powerful data-driven apps with seamless integrations to APIs, databases, Python libraries, and file formats",
            class_name="text-slate-9 text-sm font-medium text-center text-balance word-wrap break-words md:whitespace-pre",
        ),
        class_name="flex flex-col gap-4 items-center mx-auto w-full relative overflow-hidden",
    )


def connect_card(icon: str, title: str, description: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            get_icon(icon, class_name="shrink-0 !text-slate-9 size-5"),
            rx.el.span(title, class_name="text-sm font-medium text-slate-10"),
            class_name="flex flex-row gap-2 items-center",
        ),
        rx.el.p(
            description,
            class_name="text-slate-12 text-base font-medium",
        ),
        class_name="flex flex-col gap-4 p-10 border-r border-slate-3 border-b",
    )


def connect_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            numbers_pattern(side="left", class_name="left-0 top-0"),
            numbers_pattern(side="right", class_name="right-0 top-0"),
            header(),
            class_name="flex flex-col items-center mx-auto w-full relative overflow-hidden py-20 border-b border-slate-3 lg:border-x",
        ),
        rx.el.div(
            connect_card(
                "api",
                "API",
                "Integrate with any REST or GraphQL API to fetch and sync data in real-time",
            ),
            connect_card(
                "python",
                "Python Library/SDK",
                "Import any Python package to extend functionality with data tools and more",
            ),
            connect_card(
                "db",
                "Database",
                "Connect to PostgreSQL, MySQL, MongoDB, or any database to power your app",
            ),
            connect_card(
                "doc",
                "File Types",
                "Process and display CSV, Excel, PDF, images, and other file formats seamlessly",
            ),
            class_name="w-full grid grid-cols-1 lg:grid-cols-2 lg:border-l border-slate-3",
        ),
        class_name="flex flex-col items-center mx-auto w-full max-w-[64.19rem] relative overflow-hidden",
    )
