import reflex as rx
from pcweb.components.button import button
from pcweb.constants import REFLEX_CLOUD_URL

# Constants for styling
STYLES = {
    "cell": "text-slate-12 font-medium text-sm whitespace-nowrap",
    "header_cell": "text-slate-12 font-semibold text-lg",
    "header_cell_sub": "text-slate-11 font-semibold text-md",
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
    grid-template-columns: minmax(100px, 1fr) repeat(4, minmax(100px, 1fr)) !important;
    padding: 1rem 2.5rem;
    gap: 6rem !important;
}
.rt-ScrollAreaViewport {
    padding-top: 2rem;
}
"""

FRAMEWORK_SECTION = [
    ("Open Source Framework", True, True, True, True),
    ("Templates", True, True, True, True),
    ("One Click Auth", False, False, True, True),
    ("Embed Reflex Apps", False, False, True, True),
    ("Built-in Testing", False, False, True, True),
]

REFLEX_BRANDING_SECTION = [
    ("Remove Reflex Branding", "", "On Reflex Cloud", "Everywhere *", "Everywhere *"),
]

REFLEX_AI_SECTION = [
    ("Number of Generations", "5/month", "100/month/seat", "250/month/seat", "Custom"),
]

DATABASE_SECTION = [
    ("Connect your own SQL DB", True, True, True, True),
    ("Database Editor UI", False, False, True, True),
    ("Database Migration Tool", False, False, True, True),
]

HOSTING_TEXT_SECTION = [
    ("Compute Limits", "1 CPU, .5GB", "5 CPU, 10GB", "Custom", "Custom"),
    ("Regions", "Single", "Multiple", "Multiple", "Multiple"),
    ("Build logs", "7 day", "30 days", "90 days", "Custom"),
    ("Runtime logs", "1 day", "7 days", "30 days", "Custom"),
]

HOSTING_BOOLEAN_SECTION = [
    ("CLI Deployments", True, True, True, True),
    ("Custom Domains", False, True, True, True),
    ("Automatic CI / CD Deploy (Github)", False, False, True, True),
    ("Secrets", True, True, True, True),
    ("Secret Manager", False, False, True, True),
    ("App Analytics", False, False, True, True),
    ("Traces", False, False, True, True),
    ("Custom Alerts", False, False, True, True),
    ("Rollbacks", False, False, True, True),
    ("Large File Support", False, False, True, True),
    ("On Prem Hosting", False, False, False, True),
]

SECURITY_SECTION = [
    ("Web App Firewall", True, True, True, True),
    ("HTTP/SSL", True, True, True, True),
    ("DDos Protection", True, True, True, True),
    ("2 Factor Auth", True, True, True, True),
    ("Rich Permissions Control", False, False, True, True),
    ("Connect to Analytics Vendors", False, False, True, True),
    ("Audit Logs", False, False, False, True),
    ("SSO", False, False, False, True),
]

SUPPORT_TEXT_SECTION = [
    ("Support", "Community", "Community", "Email/Slack", "Dedicated Support")
]

SUPPORT_BOOLEAN_SECTION = [
    ("White Glove Onboarding", False, False, False, True),
    ("Support SLAs Available", False, False, False, True),
    ("Migrate Existing Apps", False, False, False, True),
    ("Priority Support with Reflex Engineering Team", False, False, False, True),
    ("", "", "", "", ""),
]

PLAN_BUTTONS = [
    ("Start building for free", "secondary", "!text-slate-11 !w-fit"),
    ("Start with Pro plan", "primary", "!text-[#FCFCFD] !w-fit"),
    ("Contact sales", "secondary", "!text-slate-11 !w-fit"),
    ("Contact sales", "secondary", "!text-slate-11 !w-fit"),
]

ASTERIX_SECTION = [
    ("* Everywhere: This includes removing the 'Made in Reflex' badge for self hosted apps.", "", "", "", "")
]

def glow() -> rx.Component:
    return rx.table.row(
        class_name="absolute flex-shrink-0 left-1/2 -translate-x-1/2 z-[5] top-[-1rem] pointer-events-none",
        background_image=rx.color_mode_cond(
            "radial-gradient(50% 50% at 50% 50%, rgba(235, 228, 255, 0.661) 0%, rgba(252, 252, 253, 0.00) 100%) !important",
            "radial-gradient(50% 50% at 50% 50%, rgba(58, 45, 118, 0.241) 0%, rgba(21, 22, 24, 0.00) 100%) !important",
        ),
        height="6rem !important",
        width="60.75rem !important",
    )


def create_table_cell(content: str | rx.Component) -> rx.Component:
    if content == "Usage Based":
        return rx.table.cell(
            rx.link(content, color=rx.color("violet", 12), href="#calculator-header", text_decoration="underline"),
            class_name=STYLES["cell"],
        )
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
        href=REFLEX_CLOUD_URL if text != "Contact sales" else "/sales",
        is_external=True,
        underline="none",
        class_name="w-full flex justify-center items-center",
    )


def create_table_row(cells: list) -> rx.Component:
    row_cells = [create_table_cell(cell) for cell in cells]
    return rx.table.row(
        *row_cells,
        class_name="w-full [&>*:not(:first-child)]:text-center bg-slate-1 z-[2] !h-[50px]",
    )


def create_table_row_header(name: list, coming_soon: bool = False) -> rx.Component:
    return rx.table.row(
        *[
            rx.table.column_header_cell(name, rx.badge("coming soon", margin_left="0.5rem"), class_name=STYLES["header_cell"])  if coming_soon else rx.table.column_header_cell(name, class_name=STYLES["header_cell"]),
            rx.table.column_header_cell("Hobby", class_name=STYLES["header_cell_sub"]),
            rx.table.column_header_cell("Pro", class_name=STYLES["header_cell_sub"]),
            rx.table.column_header_cell("Team", class_name=STYLES["header_cell_sub"]),
            rx.table.column_header_cell("Enterprise", class_name=STYLES["header_cell_sub"])
        ],
        class_name="w-full [&>*:not(:first-child)]:text-center bg-slate-2 border border-slate-3 rounded-2xl z-[6] !h-[3.625rem] relative",
        padding_x="5rem !important",
    )


def create_table_body(*body_content) -> rx.Component:
    return rx.table.body(
        *body_content,
        class_name="w-full divide-y divide-slate-4 border border-slate-4 md:border-t-0 flex flex-col items-center justify-center border-x max-w-[64.19rem] mx-auto border-b-0",
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



def header_hosting() -> rx.Component:
    return rx.box(
        rx.el.h3(
            "Secure and Scalable Hosting",
            class_name="text-slate-12 text-3xl font-semibold text-center",
        ),
        rx.el.p(
            "Compare features across plans.",
            class_name="text-slate-9 text-2xl font-semibold text-center",
        ),
        class_name="flex items-center justify-between text-slate-11 flex-col py-[5rem] 2xl:border-x border-slate-4 max-w-[64.19rem] mx-auto w-full",
    )


def header_oss() -> rx.Component:
    return rx.box(
        rx.el.h3(
            "Supercharged Features to Build Faster",
            class_name="text-slate-12 text-3xl font-semibold text-center",
        ),
        rx.el.p(
            "Premium Features to help you get the most out of Reflex",
            class_name="text-slate-9 text-2xl font-semibold text-center",
        ),
        class_name="flex items-center justify-between text-slate-11 flex-col py-[5rem] 2xl:border-x border-slate-4 max-w-[64.19rem] mx-auto w-full",
    )


def table_body_hosting() -> rx.Component:
    return rx.table.root(
        rx.el.style(TABLE_STYLE),
        rx.table.header(
            create_table_row_header("Hosting"),
            glow(),
            class_name="relative",
        ),
        create_table_body(
            *[create_table_row(row) for row in HOSTING_TEXT_SECTION],
            *[
                create_checkmark_row(feature, checks)
                for feature, *checks in HOSTING_BOOLEAN_SECTION
            ],
        ),
        rx.table.header(
            create_table_row_header("Security"),
            class_name="relative",
        ),
        create_table_body(
            *[
                create_checkmark_row(feature, checks)
                for feature, *checks in SECURITY_SECTION
            ],
        ),
        rx.table.header(
            create_table_row_header("Support"),
            class_name="relative",
        ),
        create_table_body(
            *[create_table_row(row) for row in SUPPORT_TEXT_SECTION],
            *[
                create_checkmark_row(feature, checks)
                for feature, *checks in SUPPORT_BOOLEAN_SECTION 
            ],
        ),
        class_name="w-full overflow-x-auto max-w-[69.125rem] -mt-[2rem]",
    )


def table_body_oss() -> rx.Component:
    return rx.table.root(
        rx.el.style(TABLE_STYLE),
        rx.table.header(
            create_table_row_header("Framework"),
            class_name="relative",
        ),
        create_table_body(
            *[
                create_checkmark_row(feature, checks)
                for feature, *checks in FRAMEWORK_SECTION
            ],
            *[create_table_row(row) for row in REFLEX_BRANDING_SECTION],
        ),
        rx.table.header(
            create_table_row_header("Database"),
            class_name="relative",
        ),
        create_table_body(
            *[
                create_checkmark_row(feature, checks)
                for feature, *checks in DATABASE_SECTION
            ],
        ),
        rx.table.header(
            create_table_row_header("AI", coming_soon=True),
            class_name="relative",
        ),
        create_table_body(
            *[create_table_row(row) for row in REFLEX_AI_SECTION],
        ),
        create_table_body(
            rx.table.row(
                rx.table.cell(),
                *[
                    rx.table.cell(create_action_button(text, variant, extra))
                    for text, variant, extra in PLAN_BUTTONS
                ],
                class_name="w-full [&>*:not(:first-child)]:text-center bg-slate-1 !py-[1.25rem] border-y border-slate-4 !h-[76px] relative",
            ),
        ),
        create_table_body(
            *[create_table_row(row) for row in ASTERIX_SECTION],
        ),
        class_name="w-full overflow-x-auto max-w-[69.125rem] -mt-[2rem]",
    )

def comparison_table_hosting() -> rx.Component:
    return rx.box(
        header_hosting(),
        table_body_hosting(),
        class_name="flex-col w-full  max-w-[69.125rem] desktop-only",
    )


def comparison_table_oss() -> rx.Component:
    return rx.box(
        header_oss(),
        table_body_oss(),
        class_name="flex-col w-full  max-w-[69.125rem] desktop-only",
    )