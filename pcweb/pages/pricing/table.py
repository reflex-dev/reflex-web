import reflex as rx
import reflex_ui as ui
from reflex_ui.blocks.lemcal import lemcal_dialog

from pcweb.components.hosting_banner import HostingBannerState
from pcweb.constants import REFLEX_BUILD_URL, REFLEX_CLOUD_URL

CLOUD_HOSTING_FEATURES = [
    ("Max # Apps", "1", "5", "10"),
    ("Max Machine Size", "1cpu, 1gb", "2cpu, 4gb shared", "Beyond 2cpu, 4gb"),
    ("Dedicated Machines", False, False, True),
    ("Custom Domains", "0", "5", "Unlimited"),
    ("App Metrics", True, True, True),
    ("Log Retention", "1 hour", "7 day", "90-Day Log History"),
    ("Multiple Regions", False, True, True),
    ('"Built with Reflex" Attribution', True, False, False),
    ("One-click rollbacks", True, True, True),
]

SECURITY_FEATURES = [
    ("SSO/SAML", False, True, True),
    ("Role-based access control", False, False, True),
    ("On Premise Deployments", False, False, True),
    ("Audit Logs", False, False, True),
    ("HTTP/SSL", True, True, True),
    ("Web App Firewall", True, True, True),
    ("SOC 2 compliance", False, False, "On prem, custom"),
    ("HIPAA BAA", False, False, "On prem, custom"),
]

SUPPORT_FEATURES = [
    (
        "Customer Success",
        "Discord/Github Community",
        "Discord/Github Community",
        "Dedicated Support Channel",
    ),
    (
        "Onboarding",
        "Documentation",
        "Documentation",
        "Get a forward deployed engineer to help you get started",
    ),
]

REFLEX_BUILD_BASIC_FEATURES = [
    (
        "Credits",
        "50 daily credits (up to 150/month)",
        "1000 monthly credits",
        "Custom",
    ),
    ("Agent (10 Credits per msg)", True, True, True),
    ("Chat (1 Credit)", True, True, True),
]

REFLEX_BUILD_FUNCTIONALITY = [
    (
        "Privacy",
        "Public Projects",
        "Private Projects",
        "Private Projects /Group based controls",
    ),
    (
        "Design",
        "Custom Designs/Theming",
        "Custom Designs/Theming",
        "Custom Designs/Theming",
    ),
    ("Data", False, False, "Opt out of data training"),
    ("Collaborators", "Single", "Single", "Multiple Collaborators/Editors"),
    ("Integration", "Basic 5", "Pro 100+", "Enterprise Integrations"),
    ("Download App Code", False, True, True),
]

REFLEX_BUILD_DEPLOYMENT = [
    (
        "Github",
        "Public Repo Sync",
        "Private Repo Sync",
        "Enterprise Repo Sync Github, Gitlab, and Bitbucket.",
    ),
    (
        "One Click Deploy",
        "Reflex Cloud",
        "Reflex Cloud",
        "Databricks, AWS, Azure, GCP, Other",
    ),
    ("SSH access", False, True, True),
]


def table_cell(content: str | rx.Component) -> rx.Component:
    if isinstance(content, bool):
        return rx.el.td(
            rx.el.div(
                (
                    rx.icon("check", class_name="text-secondary-12", size=16)
                    if content
                    else ""
                ),
                class_name="flex justify-center items-center",
            ),
            class_name="p-4",
        )

    return rx.el.td(
        content,
        class_name="text-secondary-12 first:text-secondary-11 font-medium text-sm text-wrap p-4 first:text-left text-center",
    )


def table_header_cell(content: str | rx.Component) -> rx.Component:
    return rx.el.th(
        content,
        class_name="text-slate-12 font-semibold text-lg p-4 first:text-left",
    )


def table_row(*cells, is_header: bool = False) -> rx.Component:
    if is_header:
        return rx.el.tr(
            *[table_header_cell(cell) for cell in cells],
            class_name="px-10",
        )

    return rx.el.tr(
        *[table_cell(cell) for cell in cells],
        class_name="bg-slate-1 hover:bg-slate-2",
    )


def pricing_table(
    title: str, icon: str, columns: list[str], features: list[tuple], **kwargs
) -> rx.Component:
    header_content = rx.el.div(
        ui.icon(icon, class_name="text-secondary-11", size=20),
        rx.el.span(title, class_name="text-secondary-12 font-semibold text-xl"),
        class_name="flex items-center gap-2.5 flex-row w-full bg-slate-1",
    )

    # Create header row
    header_row = table_row(header_content, *columns, is_header=True)

    # Add optional id and scroll margin for anchoring
    if kwargs.get("anchor"):
        header_row = rx.el.tr(
            *header_row.children,
            class_name=f"{header_row.class_name} scroll-mt-24",
            id=kwargs.get("anchor"),
        )

    # Create feature rows
    feature_rows = [table_row(*feature_data) for feature_data in features]

    return rx.el.table(
        rx.el.thead(
            header_row,
            class_name=(
                "sticky bg-slate-1 z-10",
                rx.cond(HostingBannerState.show_banner, "top-[161px]", "top-[105px]"),
            ),
        ),
        rx.el.tbody(
            *feature_rows,
            class_name="divide-y divide-slate-4 bg-slate-1 border-t border-slate-4",
        ),
        class_name="table-fixed w-full max-w-[64.19rem] border-x border-b border-slate-4 rounded-lg bg-slate-1",
    )


def section_header(title: str, subtitle: str) -> rx.Component:
    """Create a section header for pricing tables."""
    return rx.box(
        rx.el.h3(
            title,
            class_name="text-slate-12 text-3xl font-semibold text-center",
        ),
        rx.el.p(
            subtitle,
            class_name="text-slate-9 text-xl font-semibold text-center",
        ),
        class_name="flex items-center justify-between flex-col py-[4.5rem] 2xl:border-x border-slate-4 max-w-[64.19rem] mx-auto w-full gap-1",
    )


def sticky_pricing_header() -> rx.Component:
    def header_item(text: str, button: rx.Component) -> rx.Component:
        return rx.el.div(
            rx.el.span(
                text, class_name="text-secondary-12 font-semibold text-base text-center"
            ),
            button,
            class_name="w-full self-center flex flex-col justify-center items-center gap-2",
        )

    return rx.el.div(
        rx.el.div(
            # Features column
            rx.el.div(
                "",
                class_name="text-secondary-11 font-semibold text-base text-left flex items-baseline justify-start z-0",
            ),
            # Free column
            header_item(
                "Hobby",
                ui.link(
                    render_=ui.button(
                        "Get started",
                        variant="secondary",
                        class_name="font-semibold w-full",
                    ),
                    to=REFLEX_BUILD_URL,
                    target="_blank",
                ),
            ),
            # Pro column with button
            header_item(
                "Pro",
                ui.link(
                    render_=ui.button(
                        "Upgrade now",
                        variant="secondary",
                        class_name="font-semibold w-full",
                    ),
                    to=f"{REFLEX_CLOUD_URL.rstrip('/')}/?redirect_url={REFLEX_CLOUD_URL.rstrip('/')}/billing/",
                    target="_blank",
                ),
            ),
            # Enterprise column with button
            header_item(
                "Enterprise",
                lemcal_dialog(
                    ui.button(
                        "Get a demo",
                        variant="primary",
                        class_name="font-semibold w-full",
                    )
                ),
            ),
            class_name="grid grid-cols-4 gap-6 p-4",
        ),
        class_name=(
            "sticky z-10 bg-slate-1 border-x border-slate-4 border-y",
            rx.cond(HostingBannerState.show_banner, "top-[121px]", "top-[65px]"),
        ),
    )


def reflex_build_table() -> rx.Component:
    all_features = (
        REFLEX_BUILD_BASIC_FEATURES
        + REFLEX_BUILD_FUNCTIONALITY
        + REFLEX_BUILD_DEPLOYMENT
    )

    return pricing_table(
        title="Reflex Build",
        icon="MagicWand01Icon",
        columns=[],
        features=all_features,
    )


def hosting_table() -> rx.Component:
    return pricing_table(
        title="Cloud",
        icon="CloudServerIcon",
        columns=[],
        features=CLOUD_HOSTING_FEATURES,
    )


def security_table() -> rx.Component:
    return pricing_table(
        title="Security",
        icon="ShieldKeyIcon",
        columns=[],
        features=SECURITY_FEATURES,
    )


def support_table() -> rx.Component:
    return pricing_table(
        title="Support",
        icon="QuestionIcon",
        columns=[],
        features=SUPPORT_FEATURES,
    )


def tiers_tables() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            section_header(
                "The enterprise-grade fullstack AI app building platform.",
                "Build customized, secure, and scalable apps in seconds",
            ),
            sticky_pricing_header(),
            reflex_build_table(),
            hosting_table(),
            security_table(),
            support_table(),
            class_name="flex-col w-full max-w-[64.19rem] lg:flex hidden self-center",
        ),
        class_name="relative",
    )
