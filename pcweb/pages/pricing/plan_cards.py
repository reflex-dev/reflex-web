from typing import NamedTuple, TypedDict
from urllib.parse import quote_plus

import reflex as rx
import reflex_ui as ui
from reflex.experimental.client_state import ClientStateVar
from reflex_ui.blocks.lemcal import lemcal_dialog

from pcweb.components.hosting_banner import HostingBannerState
from pcweb.components.number_flow import number_flow
from pcweb.constants import PRO_TIERS_TABLE, REFLEX_BUILD_URL, REFLEX_CLOUD_URL

YEARLY_MONTHS_FREE = 2  # 2 months free
YEARLY_DISCOUNT_MULTIPLIER = (12 - YEARLY_MONTHS_FREE) / 12
monthly_yearly_toggle_cs = ClientStateVar.create(
    "monthly_yearly_toggle_value",
    default="monthly",
)


class SelectedTier(TypedDict):
    tier: str
    price: int


class ProTierState(rx.State):
    credits: rx.Field[int] = rx.field(default=1000)

    @rx.event
    def redirect_to_billing(self, yearly: bool = False):
        return rx.redirect(
            f"{REFLEX_CLOUD_URL.rstrip('/')}/?redirect_url={REFLEX_CLOUD_URL.rstrip('/')}/billing/?tier={quote_plus(self.selected_tier['tier'])}{'&yearly=true' if yearly else ''}",
            is_external=True,
        )

    @rx.event
    def update_credits(self, credits: str):
        self.credits = int(credits.replace(",", ""))

    @rx.var
    def selected_tier(self) -> SelectedTier:
        for tier_name, tier_data in PRO_TIERS_TABLE.items():
            if tier_data["credits"] == self.credits:
                return SelectedTier(tier=tier_name, price=tier_data["price"])
        return SelectedTier(tier="Pro", price=PRO_TIERS_TABLE["Pro 50"]["price"])


class Feature(NamedTuple):
    icon: str
    text: str
    component: rx.Component | None = None


def radial_circle(violet: bool = False) -> rx.Component:
    """Create a radial circle background image component.

    Args:
        violet: Whether to use the violet variant. Defaults to False.

    Returns:
        A Reflex image component configured as a radial circle background.

    """
    theme = "violet" if violet else ""
    return rx.image(
        src=rx.color_mode_cond(
            light=f"/logos/light/radial_circle{theme}.svg",
            dark=f"/logos/dark/radial_circle{theme}.svg",
        ),
        alt="Radial circle",
        loading="lazy",
        class_name="top-0 right-0 absolute pointer-events-none z-[-1]",
    )


def card(
    title: str,
    price: str | rx.Component,
    description: str | rx.Component,
    features: list[Feature],
    cta_button: rx.Component,
) -> rx.Component:
    return rx.box(
        rx.el.h3(title, class_name="font-medium text-secondary-12 text-2xl mb-1.5"),
        (
            rx.el.span(
                description,
                class_name="text-sm font-medium text-secondary-11 text-pretty",
            )
            if isinstance(description, str)
            else description
        ),
        (
            rx.el.span(
                price,
                class_name="text-3xl text-secondary-12 font-semibold py-4",
            )
            if isinstance(price, str)
            else price
        ),
        rx.el.ul(
            *[
                rx.el.li(
                    ui.icon(feature.icon, class_name="text-secondary-10", size=16),
                    feature.text,
                    feature.component if feature.component else rx.fragment(),
                    class_name="text-sm font-medium text-secondary-12 flex items-center gap-2",
                )
                for feature in features
            ],
            class_name="flex flex-col gap-2",
        ),
        rx.box(class_name="flex-1"),
        cta_button,
        class_name="flex flex-col p-10 border border-slate-4 rounded-[1.125rem] shadow-small bg-slate-2 w-full h-[30.5rem]",
    )


def popular_card(
    title: str,
    price: str | rx.Component,
    description: str,
    features: list[Feature],
    cta_button: rx.Component,
) -> rx.Component:
    return rx.box(
        radial_circle(),
        rx.box(
            "Most popular",
            class_name="absolute top-[-0.75rem] left-8 rounded-md bg-[#6E56CF] h-[1.5rem] z-[1] text-sm font-medium text-center px-2 flex items-center justify-center text-[#FCFCFD]",
        ),
        rx.el.h3(title, class_name="font-medium text-secondary-12 text-2xl mb-1.5"),
        rx.el.p(description, class_name="text-sm font-medium text-secondary-11"),
        (
            rx.el.span(
                price,
                class_name="text-3xl text-secondary-12 font-semibold py-4",
            )
            if isinstance(price, str)
            else price
        ),
        rx.el.ul(
            *[
                rx.el.li(
                    ui.icon(feature.icon, class_name="text-primary-10", size=16),
                    feature.text,
                    feature.component if feature.component else rx.fragment(),
                    class_name="text-sm font-medium text-secondary-12 flex items-center gap-2",
                )
                for feature in features
            ],
            class_name="flex flex-col gap-2",
        ),
        rx.box(class_name="flex-1"),
        cta_button,
        class_name="flex flex-col p-10 border border-slate-4 rounded-[1.125rem] shadow-small bg-secondary-2 w-full h-[30.5rem] relative z-[1]",
    )


def pro_tiers_select() -> rx.Component:
    return rx.el.div(
        ui.select(
            items=[f"{int(tier['credits']):,}" for tier in PRO_TIERS_TABLE.values()],
            value=f"{ProTierState.credits:,}",
            on_value_change=ProTierState.update_credits,
            size="xs",
        ),
        rx.el.span(
            "monthly credits",
            class_name="text-sm font-medium text-secondary-12",
        ),
        class_name="flex flex-row gap-2 items-center **:data-[slot=select-trigger]:min-w-22",
    )


def pricing_cards() -> rx.Component:
    return rx.el.div(
        card(
            "Hobby",
            "Free",
            "Perfect for getting started and trying out Reflex.",
            [
                Feature(
                    "TokenCircleIcon",
                    "50 daily credits (up to 150/month)",
                ),
                Feature("EarthIcon", "Public apps only"),
                Feature("CheckmarkBadge02Icon", "Built with Reflex Attribution"),
                Feature("PlugSocketIcon", "Integrations"),
            ],
            ui.link(
                render_=ui.button(
                    "Start building for free",
                    variant="secondary",
                    size="lg",
                    class_name="w-full font-semibold",
                ),
                to=REFLEX_BUILD_URL,
                target="_blank",
            ),
        ),
        card(
            "Pro",
            number_flow(
                value=rx.cond(
                    monthly_yearly_toggle_cs.value == "monthly",
                    ProTierState.selected_tier["price"],
                    round(
                        ProTierState.selected_tier["price"]
                        * YEARLY_DISCOUNT_MULTIPLIER,
                        1,
                    ),
                ),
                trend="0",
                prefix="$",
                suffix=" /monthly",
                class_name="text-3xl text-secondary-12 font-semibold py-4",
            ),
            "Build, deploy and scale your apps.",
            [
                Feature("TokenCircleIcon", "", pro_tiers_select()),
                Feature("SquareLock02Icon", "Private Projects"),
                Feature("CursorInWindowIcon", "Full-Fledged Browser IDE"),
                Feature("PlugSocketIcon", "Integrations"),
                Feature("GithubIcon", "Connect to Github"),
                Feature("Globe02Icon", "Custom Domains"),
                Feature("CpuIcon", "Up to 8 GB RAM / 4 vCPU per deployed app"),
            ],
            ui.button(
                "Start with Pro plan",
                variant="secondary",
                size="lg",
                class_name="w-full font-semibold",
                on_click=ProTierState.redirect_to_billing(
                    monthly_yearly_toggle_cs.value == "yearly"
                ),
            ),
        ),
        popular_card(
            "Enterprise",
            "Custom",
            "Tailored solutions for enterprise needs.",
            [
                Feature(
                    "UserMultipleIcon",
                    "Role based access: Collaborators/Editors/Viewers",
                ),
                Feature("PlugSocketIcon", "Enterprise Integrations"),
                Feature("GithubIcon", "Enterprise Repo Sync"),
                Feature(
                    "AiCloud01Icon", "Deploy to Databricks, AWS, Azure, GCP, Other"
                ),
                Feature("ShieldKeyIcon", "SOC 2, HIPAA BAA compliance"),
                Feature("QuestionIcon", "Dedicated Support Channel"),
                Feature("CustomerSupportIcon", "Onboarding support"),
            ],
            lemcal_dialog(
                ui.button(
                    "Contact sales",
                    variant="primary",
                    size="lg",
                    class_name="w-full font-semibold",
                ),
            ),
        ),
        class_name="grid xl:grid-cols-3 grid-cols-1 gap-4 w-full",
    )


def header():
    return rx.box(
        rx.el.h3(
            "Choose the perfect plan for your needs",
            class_name="text-slate-12 text-3xl font-semibold text-center",
        ),
        rx.el.p(
            "Start free, scale as you grow, or go enterprise for maximum power",
            class_name="text-slate-9 text-xl font-semibold text-center",
        ),
        class_name="flex items-center justify-between text-slate-11 flex-col lg:pt-[4.5rem] pt-[2.5rem] pb-[3.5rem] 2xl:border-x border-slate-4 max-w-[64.19rem] mx-auto w-full gap-1",
    )


def monthly_yearly_toggle():
    return rx.el.div(
        ui.tabs(
            ui.tabs.list(
                ui.tabs.tab(
                    "Monthly", value="monthly", class_name="text-base h-9 px-4"
                ),
                ui.tabs.tab(
                    "Yearly (2 months free)",
                    value="yearly",
                    class_name="text-base h-9 px-4",
                ),
                ui.tabs.indicator(class_name="h-9"),
            ),
            default_value="monthly",
            value=monthly_yearly_toggle_cs.value,
            on_value_change=monthly_yearly_toggle_cs.set_value,
            class_name="flex items-center justify-center pb-10",
        ),
        class_name="2xl:border-x border-slate-4 w-full mx-auto max-w-[64.19rem]",
    )


def plan_cards():
    return rx.box(
        header(),
        # monthly_yearly_toggle(),
        rx.el.style(
            """
            number-flow-react::part(suffix) {
                color: var(--secondary-10);
                font-weight: 450;
                font-size: large;
                letter-spacing: -0.00875em;
            }
            """
        ),
        pricing_cards(),
        class_name=(
            "flex flex-col w-full justify-center items-center max-w-[85rem] mx-auto",
            rx.cond(
                HostingBannerState.show_banner,
                "pt-[8rem] lg:pt-[7rem]",
                "pt-[8rem] lg:pt-[4rem]",
            ),
        ),
    )
