import reflex as rx
from pcweb.components.button import button
from pcweb.constants import HOSTING_URL


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
    title: str, description: str, features: list[str], button_text: str
) -> rx.Component:
    return rx.box(
        rx.el.h3(title, class_name="font-semibold text-slate-12 text-2xl mb-2"),
        rx.el.p(
            description, class_name="text-sm font-medium text-slate-9 mb-8 text-pretty"
        ),
        rx.el.ul(
            *[
                rx.el.li(
                    rx.icon("circle-check", class_name="!text-violet-9", size=16),
                    feature,
                    class_name="text-sm font-medium text-slate-11 flex items-center gap-1.5",
                )
                for feature in features
            ],
            class_name="flex flex-col gap-2",
        ),
        rx.box(class_name="flex-1"),
        rx.link(
            button(
                button_text,
                variant="secondary",
                class_name="w-full !text-sm !font-semibold !text-slate-11",
            ),
            href=(
                HOSTING_URL
                if button_text != "Contact sales"
                else "mailto:sales@reflex.dev"
            ),
            is_external=True,
            underline="none",
        ),
        class_name="flex flex-col p-10 border border-slate-4 rounded-[1.125rem] shadow-small bg-slate-2 w-full min-w-[20.375rem] h-[30.5rem]",
    )


def popular_card(
    title: str, description: str, features: list[str], button_text: str
) -> rx.Component:
    return rx.box(
        radial_circle(),
        rx.box(
            "Most popular",
            class_name="absolute top-[-0.75rem] left-8 rounded-md bg-[--violet-9] h-[1.5rem] z-[1] text-sm font-medium text-center px-2 flex items-center justify-center text-[#FCFCFD]",
        ),
        rx.el.h3(title, class_name="font-semibold text-slate-12 text-2xl mb-2"),
        rx.el.p(description, class_name="text-sm font-medium text-slate-9 mb-8"),
        rx.el.ul(
            *[
                rx.el.li(
                    rx.icon("circle-check", class_name="!text-violet-9", size=16),
                    feature,
                    class_name="text-sm font-medium text-slate-11 flex items-center gap-1.5",
                )
                for feature in features
            ],
            class_name="flex flex-col gap-2",
        ),
        rx.box(class_name="flex-1"),
        rx.link(
            button(
                button_text,
                variant="primary",
                class_name="w-full !text-sm !font-semibold",
            ),
            href=HOSTING_URL,
            is_external=True,
            underline="none",
        ),
        class_name="flex flex-col p-10 border border-slate-4 rounded-[1.125rem] shadow-small bg-slate-2 w-full min-w-[20.375rem] h-[30.5rem] relative z-[1]",
    )


def plan_cards() -> rx.Component:
    return rx.box(
        card(
            "Hobby",
            "Everything you need to get started with Reflex.",
            [
                "Community support",
                "1 team member",
                "1 deployed app",
                "1 day log retention",
                "Basic analytics",
            ],
            "Start building for free",
        ),
        popular_card(
            "Pro",
            "For professional projects $19/mo per member. Plus usage.",
            [
                "Community support",
                "Up to 5 team members",
                "Max 5 deployed apps",
                "30 days log retention",
                "Multi-region",
                "Custom domains",
            ],
            "Start with Pro plan",
        ),
        card(
            "Team",
            "Get the most comfort for $249/mo and $29/mo per member. Plus usage.",
            [
                "Email support",
                "Up to 15 team members",
                "Unlimited Apps",
                "90 days log retention",
                "Metrics and analytics",
                "One-click Auth",
                "Everything in Pro",
            ],
            "Start with Team plan",
        ),
        card(
            "Enterprise",
            "Get our priority support and a plan tailored to your needs.",
            [
                "Advanced support",
                "Custom onboarding",
                "On prem deployments",
                "Advanced app analytics",
                "SOC 2 report",
                "Unlimited team members",
                "Customized machine size",
                "Influence Reflex roadmap",
                "Everything in Team",
            ],
            "Contact sales",
        ),
        class_name="grid 2xl:grid-cols-4 xl:grid-cols-2 sm:grid-cols-1 gap-4",
    )
