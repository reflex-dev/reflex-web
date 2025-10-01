"""Features table section for security page."""

import reflex as rx
from ..data import SECURITY_FEATURES, PAGE_CONTENT
from pcweb.pages.pricing.table import pricing_table, section_header


def security_features_table() -> rx.Component:
    """Complete security features table with separate tables for each category."""
    tables = []

    # Create a separate table for each security category
    for category, features in SECURITY_FEATURES.items():
        table = pricing_table(
            title=category,
            icon="ShieldKeyIcon",
            columns=["", ""],
            features=features,
        )
        tables.append(table)

    return rx.el.div(
        *tables,
        class_name="flex flex-col w-full **:text-start",
    )


def features_table_section() -> rx.Component:
    """Complete features table section with header and table."""
    table_content = PAGE_CONTENT["table"]

    return rx.box(
        section_header(
            table_content["title"],
            table_content["description"],
        ),
        security_features_table(),
        class_name="flex-col w-full max-w-[64.19rem] max-lg:hidden",
    )
