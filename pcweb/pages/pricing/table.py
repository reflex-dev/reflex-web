import reflex as rx
from pcweb.components.button import button
from reflex_ui.blocks.lemcal import lemcal_button

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
    grid-template-columns: minmax(100px, 1fr) repeat(2, minmax(100px, 1fr)) !important;
    padding: 1rem 2.5rem;
    gap: 1rem !important;
}
.rt-ScrollAreaViewport {
    padding-top: 2rem;
}
"""

AI_BUILDER_FEATURES = [
    ("Open Source Framework", "Apache 2.0 License, free forever."),
    ("Enterprise Package", "Advanced features and support for enterprises."),
    ("AI Builder", "Build fullstack Python apps via prompting."),
    (
        "One Click Deploy",
        "Deploy apps with a single click to Reflex Cloud or your own infrastructure.",
    ),
    ("Git Provider", "Connect and deploy from Github, Gitlab, and Bitbucket."),
    ("Integrations", "Connect to Databricks, AWS, GCP, Azure,Snowflake, and more."),
    ("On Premise Deployments", "Deploy on your own infrastructure."),
]

AI_BUILDER_SECURITY_FEATURES = [
    ("SSO/SAML", "Single sign-on and SAML support."),
    ("Granular Access Control", "Fine-grained user and role management."),
    ("Audit Logs", "Track and audit user actions."),
    ("Secret Management Integration", "Integrate with secret management tools."),
]

CLOUD_HOSTING_LIMITS = [
    (
        "Compute",
        "20 hours/month",
        "Custom",
    ),
    ("Build Logs", "1 day", "Custom"),
    ("Runtime Logs", "1 hour", "Custom"),
]

CLOUD_HOSTING_FEATURES = [
    ("Multiple Regions", True, True),
    ("App Metrics", True, True),
    ("Custom Domains", True, True),
    ("On Premise Deployments", False, True),
]

AI_BUILDER_ADDITIONAL_FEATURES = [
    ("Secrets", True, True),
    ("Audit Logs", False, True),
]

CLOUD_SECURITY_FEATURES = [
    ("Web App Firewall", True, True),
    ("HTTP/SSL", True, True),
    ("Security Audit Reports", False, True),
    ("SSO/SAML", False, True),
    ("Audit Logs", False, True),
]

SUPPORT_LEVELS = [
    (
        "Customer Success",
        "Dedicated Customer Success contact to ensure you get the most out of Reflex.",
    ),
    ("Onboarding", "Get a forward deployed engineer to help you get started."),
]

PLAN_BUTTONS = [
    ("Start building for free", "secondary", "!text-slate-11 !w-fit"),
    ("Contact sales", "secondary", "!text-slate-11 !w-fit"),
]

ASTERIX_SECTION = [
    (
        "* AG Grid comes with a 'Built with Reflex' badge for Hobby tier.",
        "",
        "",
    ),
    ("", "", ""),
]

HOSTING_TEXT_SECTION = [
    (
        "Compute",
        "20 hours/month",
        "Custom",
    ),
    ("Build Logs", "1 day", "Custom"),
    ("Runtime Logs", "1 hour", "Custom"),
]

HOSTING_BOOLEAN_SECTION = [
    ("Multiple Regions", True, True),
    ("App Metrics", True, True),
    ("Custom Domains", True, True),
    ("On Premise Deployments", False, True),
]

FEATURES_SECTION = [
    ("Secrets", True, True),
    ("Audit Logs", False, True),
]

BUILDER_SECURITY_SECTION = [
    ("SSO/SAML", True, True),
    ("Granular Access Control", True, True),
    ("Audit Log", True, True),
    ("Secret Management Integration", False, True),
]

SECURITY_SECTION = [
    ("Web App Firewall", True, True),
    ("HTTP/SSL", True, True),
    ("Security Audit Reports", False, True),
    ("SSO/SAML", False, True),
    ("Audit Logs", False, True),
]

SUPPORT_TEXT_SECTION = [
    ("Support", "Community Support", "Dedicated Support"),
]

SUPPORT_BOOLEAN_SECTION = [
    ("White Glove Onboarding", False, True),
    ("", "", ""),
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
    return lemcal_button(
        button(
            text,
            variant=variant,
            class_name=f"{STYLES['button_base']} {extra_styles}",
        ),
        class_name="w-full flex justify-center items-center",
    )


def create_table_row(cells: list) -> rx.Component:
    row_cells = [create_table_cell(cell) for cell in cells]
    return rx.table.row(
        *row_cells,
        class_name="w-full [&>*:not(:first-child)]:text-center bg-slate-1 z-[2] !h-[50px] hover:bg-slate-2",
    )


def create_table_row_header(
    name: str, coming_soon: bool = False, anchor: str = None, badge: str = None
) -> rx.Component:
    # Create row attributes
    base_class = "w-full [&>*:not(:first-child)]:text-center bg-slate-2 border border-slate-3 rounded-2xl z-[6] !h-[3.625rem] relative align-content center"

    # Add scroll margin for anchor positioning
    if anchor:
        base_class += " scroll-mt-24"

    row_attrs = {
        "class_name": base_class,
        "padding_x": "5rem !important",
    }

    # Add id attribute if anchor is provided
    if anchor:
        row_attrs["id"] = anchor

    # Compose the header cell content
    header_content = rx.el.div(
        rx.el.span(name),
        (
            rx.badge(
                badge,
                class_name="ml-2 bg-violet-2 text-violet-11 border border-violet-5",
            )
            if badge
            else None
        ),
        rx.badge("coming soon", margin_left="0.5rem") if coming_soon else None,
        class_name="flex items-center gap-x-2",
    )

    return rx.table.row(
        rx.table.column_header_cell(header_content, class_name=STYLES["header_cell"]),
        rx.table.column_header_cell("Free", class_name=STYLES["header_cell_sub"]),
        rx.table.column_header_cell("Enterprise", class_name=STYLES["header_cell_sub"]),
        **row_attrs,
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


def header_ai() -> rx.Component:
    return rx.box(
        rx.el.h3(
            "The enterprise-grade fullstack AI app building platform.",
            class_name="text-slate-12 text-3xl font-semibold text-center",
        ),
        rx.el.p(
            "Build customized, secure, and scalable apps in seconds",
            class_name="text-slate-9 text-xl font-semibold text-center",
        ),
        class_name="flex items-center justify-between text-slate-11 flex-col py-[4.5rem] 2xl:border-x border-slate-4 max-w-[64.19rem] mx-auto w-full",
    )


def create_feature_row(feature: str, description: str) -> rx.Component:
    return rx.table.row(
        rx.table.cell(feature, class_name=STYLES["cell"]),
        rx.table.cell(description, class_name=STYLES["cell"]),
        class_name="w-full bg-slate-1 z-[2] !h-[50px] hover:bg-slate-2",
    )


def create_feature_table_header(section: str, badge: str = None) -> rx.Component:
    header_content = rx.el.div(
        rx.el.span(section),
        (
            rx.badge(
                badge,
                class_name="ml-2 bg-violet-2 text-violet-11 border border-violet-5",
            )
            if badge
            else None
        ),
        class_name="flex items-center gap-x-2",
    )
    return rx.table.row(
        rx.table.column_header_cell(header_content, class_name=STYLES["header_cell"]),
        rx.table.cell(
            "", class_name=STYLES["header_cell"]
        ),  # Empty cell for alignment, no title
        class_name="w-full bg-slate-2 border border-slate-3 rounded-2xl z-[6] !h-[3.625rem] relative align-content center",
        padding_x="5rem !important",
    )


def table_body_oss() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            create_feature_table_header("Reflex Build"),
            class_name="relative",
        ),
        create_table_body(
            *[
                create_feature_row(feature, desc)
                for feature, desc in AI_BUILDER_FEATURES
            ],
        ),
        rx.table.header(
            create_feature_table_header("Security"),
            class_name="relative",
        ),
        create_table_body(
            *[
                create_feature_row(feature, desc)
                for feature, desc in AI_BUILDER_SECURITY_FEATURES
            ],
        ),
        rx.table.header(
            create_feature_table_header("Support"),
            class_name="relative",
        ),
        create_table_body(
            *[create_feature_row(feature, desc) for feature, desc in SUPPORT_LEVELS],
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
            "Deploy your apps in seconds on cloud, or self-host on your own infra.",
            class_name="text-slate-9 text-xl font-semibold text-center",
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
            *[create_table_row(row) for row in CLOUD_HOSTING_LIMITS],
            *[
                create_checkmark_row(feature, checks)
                for feature, *checks in CLOUD_HOSTING_FEATURES
            ],
        ),
        rx.table.header(
            create_table_row_header("Security"),
            class_name="relative",
        ),
        create_table_body(
            *[
                create_checkmark_row(feature, checks)
                for feature, *checks in CLOUD_SECURITY_FEATURES
            ],
        ),
        class_name="w-full overflow-x-auto max-w-[69.125rem] -mt-[2rem]",
    )


def comparison_table_hosting() -> rx.Component:
    return rx.box(
        header_hosting(),
        table_body_hosting(),
        class_name="flex-col w-full  max-w-[69.125rem] lg:flex hidden",
    )


def comparison_table_ai() -> rx.Component:
    return rx.box(
        header_ai(),
        table_body_oss(),
        class_name="flex-col w-full  max-w-[69.125rem] lg:flex hidden",
    )
