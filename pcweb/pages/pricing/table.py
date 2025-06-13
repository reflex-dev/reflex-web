import reflex as rx
from pcweb.components.button import button
from pcweb.constants import REFLEX_DEV_WEB_LANDING_FORM_URL_GET_DEMO

# Constants for styling - KEEPING ORIGINAL
STYLES = {
    "cell": "text-slate-12 font-medium text-sm",
    "header_cell": "text-slate-12 font-semibold text-lg",
    "header_cell_sub": "text-slate-11 font-semibold text-md",
    "feature_cell": "text-slate-9 font-medium text-sm",
    "button_base": "!text-sm !font-semibold w-full text-nowrap",
}

# KEEPING ORIGINAL TABLE STYLE BUT MODIFIED FOR 2 COLUMNS
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
    word-wrap: break-word;
    hyphens: auto;
}
.rt-TableRow {
    display: grid !important;
    grid-template-columns: minmax(200px, 1fr) minmax(400px, 2fr) !important;
    padding: 1rem 2.5rem;
    gap: 1rem !important;
    min-height: 50px !important;
    align-items: start !important;
}
.rt-ScrollAreaViewport {
    padding-top: 2rem;
}
"""

# NEW DATA STRUCTURE - FEATURE AND DESCRIPTION PAIRS
PRICE_SECTION = [
    ("Per Seat Price", "Flexible pricing tiers from free to custom enterprise solutions"),
    ("Team Size", "Scale from individual developers to unlimited enterprise teams"),
]

AI_TEXT_SECTION = [
    ("Message Limit", "Monthly AI assistance limits ranging from 30 to 250+ messages based on your plan"),
]

AI_BOOLEAN_SECTION = [
    ("Purchase Extra AI Messages", "Buy additional AI messages when you exceed your monthly limit"),
    ("Private Apps", "Keep your applications secure and visible only to authorized team members"),
    ("Image to App", "Transform design mockups into working Reflex applications using AI"),
    ("Web IDE", "Build and edit applications directly in your browser with our integrated development environment"),
    ("Custom User Rules", "Define specific rules and constraints for AI assistance tailored to your project needs"),
    ("One Click Cloud Deploy", "Deploy applications to the cloud instantly without complex configuration"),
    ("Github Integration", "Seamlessly sync your code repositories with GitHub for version control"),
    ("Database Integration", "Connect to PostgreSQL, MySQL, SQLite and other databases with built-in ORM support"),
    ("Secrets Integration", "Securely manage API keys, credentials, and sensitive configuration data"),
    ("Bring your own API Keys", "Use your own third-party service API keys for maximum control and cost management"),
]

REFLEX_ENTERPRISE_BOOLEAN_SECTION = [
    ("AG Grid", "Advanced data grid with sorting, filtering, grouping, and Excel-like functionality"),
    ("AG Charts", "Professional interactive charting and data visualization library"),
    ("Map Component", "Interactive mapping with markers, layers, and geospatial data support"),
    ("Drag and Drop Component", "Intuitive drag-and-drop interface components for enhanced user experience"),
    ("Single Port Deploy", "Simplified deployment architecture running your entire application on one port"),
    ("HTTP Fallback for Websockets", "Automatic fallback ensuring reliability when WebSocket connections fail"),
    ("Custom NPM Registry", "Use private NPM registries for proprietary packages and enhanced security"),
    ("One Click Auth", "Quick authentication setup with Google, GitHub, Auth0 and other providers"),
]

HOSTING_TEXT_SECTION = [
    ("Compute", "Flexible compute resources with credits ranging from 20 hours to custom enterprise allocations"),
    ("Build Logs", "Application build logs retained from 1 day to custom enterprise retention periods"),
    ("Runtime Logs", "Application runtime logs kept from 1 hour to custom enterprise durations"),
]

HOSTING_BOOLEAN_SECTION = [
    ("Multiple Regions", "Deploy across geographic regions for better performance and availability"),
    ("CPU / Memory Metrics", "Monitor application resource usage with detailed performance metrics"),
    ("User Analytics", "Track user behavior and application usage with built-in analytics tools"),
    ("On Premise Deployments", "Deploy on your own infrastructure for maximum control and security"),
    ("Custom Domains", "Use your own domain names instead of default Reflex subdomains"),
]

FEATURES_SECTION = [
    ("Secrets", "Secure storage and management of sensitive configuration data and API keys"),
    ("Custom Alerts", "Set up notifications and alerts based on application metrics and events"),
    ("Rollbacks", "Quickly revert to previous application versions when issues are detected"),
    ("Audit Log", "Comprehensive logging of actions and changes for compliance and security"),
]

SECURITY_SECTION = [
    ("Web App Firewall", "Built-in protection against common web vulnerabilities and attacks"),
    ("HTTP/SSL", "Automatic HTTPS encryption with managed SSL certificates for all applications"),
    ("Automatic CI/CD", "Automated continuous integration and deployment pipelines"),
    ("Security Audit Reports", "Regular security assessments and vulnerability reports"),
    ("SSO", "Single Sign-On integration with enterprise identity providers"),
]

SUPPORT_TEXT_SECTION = [
    ("Support", "Support levels from community forums to dedicated technical assistance")
]

SUPPORT_BOOLEAN_SECTION = [
    ("White Glove Onboarding", "Personalized setup and migration assistance for enterprise customers"),
]

ASTERIX_SECTION_ENTERPRISE = [
    ("* Enterprise components", "Included for Hobby (with `Built with Reflex` badge) and Pro (if self-hosted)."),
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
        class_name="w-full bg-slate-1 z-[2] !h-[50px] hover:bg-slate-2",
    )

def create_table_row_header(name: list, coming_soon: bool = False, anchor: str = None) -> rx.Component:
    # Create row attributes - KEEPING ORIGINAL STYLING
    base_class = "w-full bg-slate-2 border border-slate-3 rounded-2xl z-[6] !h-[3.625rem] relative align-content center"

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
            rx.table.column_header_cell("", class_name=STYLES["header_cell_sub"]),
        ],
        **row_attrs
    )

def create_table_body(*body_content) -> rx.Component:
    return rx.table.body(
        *body_content,
        class_name="w-full divide-y divide-slate-4 border border-slate-4 md:border-t-0 flex flex-col items-center justify-center border-x max-w-[64.19rem] mx-auto border-b-0",
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
            create_table_row_header("Reflex Build", anchor="reflex-build"),
            class_name="relative",
        ),
        create_table_body(
            *[create_table_row(row) for row in AI_TEXT_SECTION],
            *[create_table_row(row) for row in AI_BOOLEAN_SECTION],
        ),
        rx.table.header(
            create_table_row_header("Reflex Enterprise"),
            class_name="relative",
        ),
        create_table_body(
            *[create_table_row(row) for row in REFLEX_ENTERPRISE_BOOLEAN_SECTION],
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
            *[create_table_row(row) for row in SUPPORT_BOOLEAN_SECTION],
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
            *[create_table_row(row) for row in HOSTING_BOOLEAN_SECTION],
        ),
        rx.table.header(
            create_table_row_header("Features"),
            class_name="relative",
        ),
        create_table_body(
            *[create_table_row(row) for row in FEATURES_SECTION],
        ),
        rx.table.header(
            create_table_row_header("Security"),
            class_name="relative",
        ),
        create_table_body(
            *[create_table_row(row) for row in SECURITY_SECTION],
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
