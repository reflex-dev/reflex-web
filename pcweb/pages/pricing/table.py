import reflex as rx
from pcweb.components.button import button
from pcweb.constants import REFLEX_DEV_WEB_LANDING_FORM_URL_GET_DEMO

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
    gap: 1rem !important;
}
.rt-ScrollAreaViewport {
    padding-top: 2rem;
}
"""

PRICE_SECTION = [
    ("Per Seat Price", "FREE", "$20/month", "$49/month", "Custom"),
    ("Team Size", "1", "1", "< 25", "Unlimited"),
]


AI_TEXT_SECTION = [
    (
        "AI App Building",
        "Limited Access",
        "$20 credits/month",
        "$40 credits/user/month",
        "Custom",
    ),
]

AI_BOOLEAN_SECTION = [
    ("Image to App", True, True, True, True),
    ("Web IDE", True, True, True, True),
    ("Custom User Rules", True, True, True, True),
    ("One Click Cloud Deploy", True, True, True, True),
    ("Github Integration", True, True, True, True),
    ("Database Integration", True, True, True, True),
    ("Secrets Integration", True, True, True, True),
    ("Purchase Extra AI Credits", False, True, True, True),
    ("Private Apps", False, True, True, True),
    ("Bring your own API Keys", False, False, False, True),
]

ASTERIX_SECTION_ENTERPRISE = [
    (
        "* Enterprise components included for Hobby (with `Built with Reflex` badge) and Pro (if self-hosted).",
        "",
        "",
        "",
        "",
    ),
]


REFLEX_ENTERPRISE_BOOLEAN_SECTION = [
    ("AG Grid *",True, True, True, True),
    ("AG Charts *",True, True, True, True),
    ("Map Component *",True, True, True, True),
    ("Drag and Drop Component *",True, True, True, True),
    ("Single Port Deploy *",True, True, True, True),
    ("HTTP Fallback for Websockets",False, False, False, True),
    ("Custom NPM Registry",False, False, False, True),
    ("One Click Auth",False, False, True, True),
]

HOSTING_TEXT_SECTION = [
    (
        "Compute",
        "20 hours/month",
        "$10 credits/month",
        "$20 compute credits/user/month",
        "Custom",
    ),
    ("Build Logs", "1 day", "30 days", "90 days", "Custom"),
    ("Runtime Logs", "1 hour", "1 day", "1 week", "Custom"),
]

HOSTING_BOOLEAN_SECTION = [
    ("Multiple Regions", False, True, True, True),
    ("CPU / Memory Metrics", True, True, True, True),
    ("User Analytics", False, False, True, True),
    ("On Premise Deployments", False, False, False, True),
    ("Custom Domains", False, True, True, True),

    # ... the following were not in the notion docs
    # ("CLI Deployments", True, True, True, True),
    # ("CI/CD Deploy Tokens", True, True, True, True),
    # ("Set Billing Limits", True, True, True, True),
]

FEATURES_SECTION = [
    ("Secrets", True, True, True, True),
    ("Custom Alerts", False, False, True, True),
    ("Rollbacks", False, False, True, True),
    ("Audit Log", False, False, True, True),
]

SECURITY_SECTION = [
    ("Web App Firewall", True, True, True, True),
    ("HTTP/SSL", True, True, True, True),
    # ("DDos Protection", True, True, True, True),
    ("Automatic CI/CD", False, True, True, True),
    ("Security Audit Reports", False, False, True, True),
    ("SSO", False, False, False, True),
]

SUPPORT_TEXT_SECTION = [
    ("Support", "Community Support", "Community Support", "Email Support", "Dedicated Support")
]

SUPPORT_BOOLEAN_SECTION = [
    ("White Glove Onboarding", False, False, False, True),
    ("", "", "", "", ""),
    # ... not in the notion docs
    # ("SLAs Available", False, False, False, True),
]

PLAN_BUTTONS = [
    ("Start building for free", "secondary", "!text-slate-11 !w-fit"),
    ("Start with Pro plan", "primary", "!text-[#FCFCFD] !w-fit"),
    ("Contact sales", "secondary", "!text-slate-11 !w-fit"),
    ("Contact sales", "secondary", "!text-slate-11 !w-fit"),
]

ASTERIX_SECTION = [
    (
        "* AG Grid comes with a 'Built with Reflex' badge for Hobby and Pro tier.",
        "",
        "",
        "",
        "",
    ),
    ("", "", "", "", ""),
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
            rx.link(
                content,
                color=rx.color("violet", 12),
                href="#calculator-header",
                text_decoration="underline",
            ),
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
        href=REFLEX_DEV_WEB_LANDING_FORM_URL_GET_DEMO,
        is_external=True,
        underline="none",
        class_name="w-full flex justify-center items-center",
    )


def create_table_row(cells: list) -> rx.Component:
    row_cells = [create_table_cell(cell) for cell in cells]
    return rx.table.row(
        *row_cells,
        class_name="w-full [&>*:not(:first-child)]:text-center bg-slate-1 z-[2] !h-[50px] hover:bg-slate-2",
    )


def create_table_row_header(name: list, coming_soon: bool = False) -> rx.Component:
    return rx.table.row(
        *[
            rx.table.column_header_cell(
                rx.el.div(
                    name,
                    rx.badge("coming soon", margin_left="0.5rem"),
                    class_name="flex items-center gap-2",
                ),
                class_name=STYLES["header_cell"],
            )
            if coming_soon
            else rx.table.column_header_cell(name, class_name=STYLES["header_cell"]),
            rx.table.column_header_cell("Hobby", class_name=STYLES["header_cell_sub"]),
            rx.table.column_header_cell("Pro", class_name=STYLES["header_cell_sub"]),
            rx.table.column_header_cell("Team", class_name=STYLES["header_cell_sub"]),
            rx.table.column_header_cell(
                "Enterprise", class_name=STYLES["header_cell_sub"]
            ),
        ],
        class_name="w-full [&>*:not(:first-child)]:text-center bg-slate-2 border border-slate-3 rounded-2xl z-[6] !h-[3.625rem] relative align-content center",
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


def table_body_oss() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            create_table_row_header("Pricing"),
            class_name="relative",
        ),
        create_table_body(
            *[create_table_row(row) for row in PRICE_SECTION],
        ),
        rx.table.header(
            create_table_row_header("Reflex Build"),
            class_name="relative",
        ),
        create_table_body(
            *[create_table_row(row) for row in AI_TEXT_SECTION],
            *[
                create_checkmark_row(feature, checks)
                for feature, *checks in AI_BOOLEAN_SECTION
            ],
        ),
        #
        rx.table.header(
            create_table_row_header("Reflex Enterprise"),
            class_name="relative",
        ),
        create_table_body(
        *[
            create_checkmark_row(feature, checks)
            for feature, *checks in REFLEX_ENTERPRISE_BOOLEAN_SECTION
        ],
        ),
        create_table_body(
            *[create_table_row(row) for row in ASTERIX_SECTION_ENTERPRISE],
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


def table_body_hosting() -> rx.Component:
    return rx.table.root(
        rx.el.style(TABLE_STYLE),
        rx.table.header(
            create_table_row_header("Reflex Cloud"),
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
            create_table_row_header("Features"),
            class_name="relative",
        ),
        create_table_body(
            *[
                create_checkmark_row(feature, checks)
                for feature, *checks in FEATURES_SECTION
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
        class_name="w-full overflow-x-auto max-w-[69.125rem] -mt-[2rem]",
    )


def comparison_table_hosting() -> rx.Component:
    return rx.box(
        header_hosting(),
        table_body_hosting(),
        class_name="flex-col w-full  max-w-[69.125rem] desktop-only",
    )


def comparison_table_ai_and_oss() -> rx.Component:
    return rx.box(
        header_oss(),
        table_body_oss(),
        class_name="flex-col w-full  max-w-[69.125rem] desktop-only",
    )
