"""Features table section for security page."""

import reflex as rx
from pcweb.pages.pricing.table import (
    create_feature_table_header,
    create_feature_row,
    create_table_body,
    TABLE_STYLE
)
from ..data import SECURITY_FEATURES, PAGE_CONTENT


def security_table_header() -> rx.Component:
    """Header section for the security features table."""
    table_content = PAGE_CONTENT["table"]

    return rx.box(
        rx.el.h3(
            table_content["title"],
            class_name="text-slate-12 text-3xl font-semibold text-center",
        ),
        rx.el.p(
            table_content["description"],
            class_name="text-slate-9 text-xl font-medium text-center mt-4",
        ),
        class_name="flex items-center justify-between text-slate-11 flex-col py-[5rem] max-w-[64.19rem] mx-auto w-full px-6 lg:border-x border-slate-3",
    )


def create_security_table_section(category: str, features: list) -> list:
    """Create a table section with header and body for a security category."""
    return [
        rx.table.header(
            create_feature_table_header(category),
            class_name="relative",
        ),
        create_table_body(
            *[
                create_feature_row(feature, description)
                for feature, description in features
            ],
        ),
    ]


def security_features_table() -> rx.Component:
    """Complete security features table with all categories."""
    table_sections = []

    # Generate all table sections dynamically
    for category, features in SECURITY_FEATURES.items():
        table_sections.extend(create_security_table_section(category, features))

    return rx.table.root(
        rx.el.style(TABLE_STYLE),
        *table_sections,
        class_name="w-full overflow-x-auto max-w-[69.125rem] -mt-[2rem]",
    )


def features_table_section() -> rx.Component:
    """Complete features table section with header and table."""
    return rx.box(
        security_table_header(),
        security_features_table(),
        class_name="flex-col w-full max-w-[69.125rem] desktop-only",
    )
