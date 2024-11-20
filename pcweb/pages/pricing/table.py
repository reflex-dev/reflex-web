import reflex as rx
from pcweb.components.button import button
from pcweb.constants import HOSTING_URL

# Constants for styling
STYLES = {
    "cell": "text-slate-12 font-medium text-sm whitespace-nowrap",
    "header_cell": "text-slate-12 font-semibold text-lg",
    "feature_cell": "text-slate-9 font-medium text-sm whitespace-nowrap",
    "button_base": "!text-sm !font-semibold w-full text-nowrap",
}

TABLE_STYLE = """
.rt-TableCell {
    background-color: transparent !important;
    box-shadow: none !important;
    vertical-align: 0 !important;
    padding: 0 !important;
    height: 0 !important;
    gap: 0 !important;
    width: 100% !important;
    min-height: max-content !important;
}
.rt-TableRow {
    display: grid !important;
    grid-template-columns: minmax(200px, 1fr) repeat(3, minmax(150px, 1fr)) !important;
    padding: 1rem 2.5rem;
    gap: 6rem !important;
}
.rt-ScrollAreaViewport {
    padding-top: 2rem;
}
"""

# Data configuration
TOP_SECTION = [
    ("Compute", "Up to 5 CPU 10GB", "Usage Based", "Usage Based"),
    ("Regions", "Multiple", "Multiple", "Multiple"),
    ("Team size", "Up to 5", "Up to 25", "Unlimited"),
    ("Build logs", "30 days", "90 days", "Custom"),
    ("Runtime logs", "1 day", "1 week", "Custom"),
    ("Support", "Community support", "Slack, Teams, Email", "Custom"),
]

SECOND_SECTION = [
    ("Web app firewall", True, True, True),
    ("HTTP/SSL", True, True, True),
    ("DDos", True, True, True),
    ("Custom onboarding", False, False, True),
]

THIRD_SECTION = [
    ("Custom onboarding", False, False, True),
    ("Migrate existing apps", False, False, True),
]

PLAN_BUTTONS = [
    ("Start with Pro plan", "primary", "!text-[#FCFCFD]"),
    ("Start with Team plan", "secondary", "!text-slate-11"),
    ("Contact sales", "secondary", "!text-slate-11"),
]


def glow() -> rx.Component:
    return rx.table.row(
        class_name="absolute flex-shrink-0 rounded-[120rem] left-1/2 -translate-x-1/2 z-[5] top-[-1rem] pointer-events-none",
        background_image=rx.color_mode_cond(
            "radial-gradient(50% 50% at 50% 50%, rgba(235, 228, 255, 0.661) 0%, rgba(252, 252, 253, 0.00) 100%) !important",
            "radial-gradient(50% 50% at 50% 50%, rgba(58, 45, 118, 0.241) 0%, rgba(21, 22, 24, 0.00) 100%) !important",
        ),
        height="6rem !important",
        width="60.75rem !important",
    )


def header() -> rx.Component:
    return rx.box(
        rx.el.h3(
            "Compare features across plans.",
            class_name="text-slate-12 text-3xl font-semibold text-center",
        ),
        rx.el.p(
            "Find a perfect fit",
            class_name="text-slate-9 text-3xl font-semibold text-center",
        ),
        class_name="flex items-center justify-between text-slate-11 flex-col py-[5rem] 2xl:border-x border-slate-4 max-w-[64.125rem] mx-auto w-full",
    )


def create_table_cell(content: str | rx.Component) -> rx.Component:
    return rx.table.cell(content, class_name=STYLES["cell"])


def create_action_button(
    text: str, variant: str, extra_styles: str = ""
) -> rx.Component:
    return rx.link(
        button(
            text,
            variant=variant,
            class_name=f"{STYLES['button_base']} {extra_styles}",
        ),
        href=HOSTING_URL if text != "Contact sales" else "mailto:sales@reflex.dev",
        is_external=True,
        underline="none",
        class_name="w-full flex justify-center items-center",
    )


def create_table_row(cells: list) -> rx.Component:
    row_cells = [create_table_cell(cell) for cell in cells]
    return rx.table.row(
        *row_cells,
        class_name="w-full [&>*:not(:first-child)]:text-center bg-slate-1 relative z-[2]",
    )


def create_table_row_header(cells: list) -> rx.Component:
    return rx.table.row(
        *[
            rx.table.column_header_cell(cell, class_name=STYLES["header_cell"])
            for cell in cells
        ],
        class_name="w-full [&>*:not(:first-child)]:text-center relative bg-slate-2 border border-slate-3 rounded-2xl z-[6]",
        padding_x="5rem !important",
    )


def create_table_body(*body_content) -> rx.Component:
    return rx.table.body(
        *body_content,
        class_name="w-full divide-y divide-slate-4 border border-slate-4 md:border-t-0 flex flex-col items-center justify-center border-x max-w-[64.125rem] mx-auto border-b-0",
    )


def create_checkmark_row(feature: str, checks: tuple[bool, ...]) -> rx.Component:
    cells = [
        feature,
        *[
            rx.box(
                rx.icon("check", class_name="text-slate-12", size=16) if c else "",
                class_name="flex justify-center items-center",
            )
            for c in checks
        ],
    ]
    return create_table_row(cells)


def table_body() -> rx.Component:
    return rx.table.root(
        rx.el.style(TABLE_STYLE),
        rx.table.header(
            create_table_row_header(["Features", "Pro", "Team", "Enterprise"]),
            glow(),
            class_name="relative",
        ),
        # Section 1
        create_table_body(
            *[create_table_row(row) for row in TOP_SECTION],
        ),
        # Section 2
        rx.table.header(
            create_table_row_header(["Section 2", "", "", ""]),
            glow(),
            class_name="relative",
        ),
        create_table_body(
            *[
                create_checkmark_row(feature, checks)
                for feature, *checks in SECOND_SECTION
            ],
        ),
        # Section 3
        rx.table.header(
            create_table_row_header(["Section 3", "", "", ""]),
            glow(),
            class_name="relative",
        ),
        create_table_body(
            *[
                create_checkmark_row(feature, checks)
                for feature, *checks in THIRD_SECTION
            ],
        ),
        create_table_body(
            rx.table.row(
                rx.table.cell(),
                *[
                    rx.table.cell(create_action_button(text, variant, extra))
                    for text, variant, extra in PLAN_BUTTONS
                ],
                class_name="w-full [&>*:not(:first-child)]:text-center bg-slate-1 !py-[1.25rem] border-y border-slate-4",
            ),
        ),
        class_name="w-full overflow-x-auto max-w-[69.125rem] -mt-[2rem]",
    )


def comparison_table() -> rx.Component:
    return rx.box(
        header(),
        table_body(),
        class_name="flex flex-col w-full  max-w-[69.125rem]",
    )
