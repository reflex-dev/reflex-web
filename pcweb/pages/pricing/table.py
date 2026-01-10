from dataclasses import dataclass

import reflex as rx
import reflex_ui as ui
from pcweb.components.demo_form import demo_form_dialog

from pcweb.components.hosting_banner import HostingBannerState
from pcweb.constants import REFLEX_BUILD_URL, REFLEX_CLOUD_URL
from pcweb.pages.pricing.enable_tiers_state import EnableTiersState


@dataclass(frozen=True)
class Feature:
    name: str
    free: str | bool
    pro: str | bool = ""
    enterprise: str | bool = ""


CLOUD_HOSTING_FEATURES = [
    Feature(
        name="Max # Apps",
        free="1",
        pro="5",
        enterprise="10",
    ),
    Feature(
        name="Max Machine Size",
        free="1cpu, 1gb",
        pro="2cpu, 4gb shared",
        enterprise="Beyond 2cpu, 4gb",
    ),
    Feature(
        name="Dedicated Machines",
        free=False,
        pro=False,
        enterprise=True,
    ),
    Feature(
        name="Custom Domains",
        free="0",
        pro="5",
        enterprise="Unlimited",
    ),
    Feature(
        name="App Metrics",
        free=True,
        pro=True,
        enterprise=True,
    ),
    Feature(
        name="Log Retention",
        free="1 hour",
        pro="7 day",
        enterprise="90-Day Log History",
    ),
    Feature(
        name="Multiple Regions",
        free=False,
        pro=True,
        enterprise=True,
    ),
    Feature(
        name='"Built with Reflex" Attribution',
        free=True,
        pro=False,
        enterprise=False,
    ),
    Feature(
        name="One-click rollbacks",
        free=True,
        pro=True,
        enterprise=True,
    ),
]

SECURITY_FEATURES = [
    Feature(
        name="SSO/SAML",
        free=False,
        pro=True,
        enterprise=True,
    ),
    Feature(
        name="Role-based access control",
        free=False,
        pro=False,
        enterprise=True,
    ),
    Feature(
        name="On Premise Deployments",
        free=False,
        pro=False,
        enterprise=True,
    ),
    Feature(
        name="Audit Logs",
        free=False,
        pro=False,
        enterprise=True,
    ),
    Feature(
        name="HTTP/SSL",
        free=True,
        pro=True,
        enterprise=True,
    ),
    Feature(
        name="Web App Firewall",
        free=True,
        pro=True,
        enterprise=True,
    ),
    Feature(
        name="SOC 2 compliance",
        free=False,
        pro=False,
        enterprise="On prem, custom",
    ),
    Feature(
        name="HIPAA BAA",
        free=False,
        pro=False,
        enterprise="On prem, custom",
    ),
]

SUPPORT_FEATURES = [
    Feature(
        name="Customer Success",
        free="Discord/Github Community",
        pro="Discord/Github Community",
        enterprise="Dedicated Support Channel",
    ),
    Feature(
        name="Onboarding",
        free="Documentation",
        pro="Documentation",
        enterprise="Get a forward deployed engineer to help you get started",
    ),
]

REFLEX_BUILD_BASIC_FEATURES = [
    Feature(
        name="Credits",
        free="50 daily credits (up to 150/month)",
        pro="1000 monthly credits",
        enterprise="Custom",
    ),
    Feature(
        name="Agent (10 Credits per msg)",
        free=True,
        pro=True,
        enterprise=True,
    ),
    Feature(
        name="Chat (1 Credit)",
        free=True,
        pro=True,
        enterprise=True,
    ),
]

REFLEX_BUILD_FUNCTIONALITY = [
    Feature(
        name="Privacy",
        free="Public Projects",
        pro="Private Projects",
        enterprise="Private Projects /Group based controls",
    ),
    Feature(
        name="Design",
        free="Custom Designs/Theming",
        pro="Custom Designs/Theming",
        enterprise="Custom Designs/Theming",
    ),
    Feature(
        name="Data",
        free=False,
        pro=False,
        enterprise="Opt out of data training",
    ),
    Feature(
        name="Collaborators",
        free="Single",
        pro="Single",
        enterprise="Multiple Collaborators/Editors",
    ),
    Feature(
        name="Integration",
        free="Basic 5",
        pro="Pro 100+",
        enterprise="Enterprise Integrations",
    ),
    Feature(
        name="Download App Code",
        free=False,
        pro=True,
        enterprise=True,
    ),
]

REFLEX_BUILD_DEPLOYMENT = [
    Feature(
        name="Github",
        free="Public Repo Sync",
        pro="Private Repo Sync",
        enterprise="Enterprise Repo Sync Github, Gitlab, and Bitbucket.",
    ),
    Feature(
        name="One Click Deploy",
        free="Reflex Cloud",
        pro="Reflex Cloud",
        enterprise="Databricks, AWS, Azure, GCP, Other",
    ),
    Feature(
        name="SSH access",
        free=False,
        pro=True,
        enterprise=True,
    ),
]


def table_cell(content: str | rx.Component | rx.vars.BooleanVar | bool) -> rx.Component:
    if isinstance(content, bool | rx.vars.BooleanVar):
        return rx.el.td(
            rx.el.div(
                rx.cond(
                    rx.Var.create(content).to(bool),
                    rx.icon("check", class_name="text-secondary-12", size=16),
                    None,
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
    title: str,
    icon: str,
    columns: list[str],
    features: list[Feature],
    show_free_tier: bool = True,
    **kwargs,
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

    is_simple_table = all(
        not feature.pro and not feature.enterprise for feature in features
    )

    if is_simple_table:
        feature_rows = [table_row(feature.name, feature.free) for feature in features]
    else:
        feature_rows = [
            rx.cond(
                EnableTiersState.enable_pro_tier,
                table_row(feature.name, feature.free, feature.pro, feature.enterprise),
                rx.cond(
                    show_free_tier,
                    table_row(
                        feature.name,
                        feature.free,
                        feature.enterprise,
                    ),
                    table_row(
                        feature.name,
                        False,
                        feature.enterprise,
                    ),
                ),
            )
            for feature in features
        ]

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
            rx.cond(
                EnableTiersState.enable_pro_tier,
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
            ),
            # Enterprise column with button
            header_item(
                "Enterprise",
                demo_form_dialog(
                    trigger=ui.button(
                        "Get a demo",
                        variant="primary",
                        class_name="font-semibold w-full",
                    ),
                ),
            ),
            class_name=ui.cn(
                "grid gap-6 p-4",
                rx.cond(EnableTiersState.enable_pro_tier, "grid-cols-4", "grid-cols-3"),
            ),
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
        show_free_tier=EnableTiersState.enable_free_tier,
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
