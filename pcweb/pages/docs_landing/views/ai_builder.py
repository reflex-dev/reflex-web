import reflex as rx
import reflex_ui as ui

from pcweb.components.marquee import marquee
from pcweb.constants import INTEGRATIONS_IMAGES_URL
from pcweb.pages.docs import ai_builder as ai_builder_pages
from pcweb.pages.integrations.integration_list import get_integration_path


def card(
    title: str, description: str, content: str, href: str, enteprise_only: bool = False
) -> rx.Component:
    return rx.el.div(
        rx.el.span(
            "Enterprise-only",
            class_name="text-secondary-12 text-xs font-medium bg-secondary-1 px-2.5 h-7 absolute top-0 right-0 border-b border-l rounded-bl-lg border-secondary-4 flex justify-center items-center",
        )
        if enteprise_only
        else None,
        rx.el.div(
            rx.el.span(title, class_name="text-secondary-12 text-xl font-[575]"),
            rx.el.span(description, class_name="text-secondary-11 text-sm font-[475]"),
            class_name="flex flex-col gap-2 p-8",
        ),
        content,
        rx.el.a(to=href, class_name="absolute inset-0"),
        style={
            "box-shadow": "0 0 0 1px rgba(0, 0, 0, 0.04), 0 12px 24px 0 rgba(0, 0, 0, 0.08), 0 1px 1px 0 rgba(0, 0, 0, 0.01), 0 4px 8px 0 rgba(0, 0, 0, 0.03);",
        },
        class_name="flex flex-col bg-white/96 backdrop-blur-[16px] rounded-xl relative cursor-pointer hover:bg-secondary-1 transition-colors overflow-hidden",
    )


def integration_icon_marquee(integration_name: str) -> rx.Component:
    normalized_name = integration_name.lower().replace(" ", "_")
    return ui.avatar.root(
        ui.avatar.image(
            src=rx.color_mode_cond(
                f"{INTEGRATIONS_IMAGES_URL}light/{normalized_name}.svg",
                f"{INTEGRATIONS_IMAGES_URL}dark/{normalized_name}.svg",
            ),
            unstyled=True,
            class_name="size-full",
        ),
        ui.avatar.fallback(
            integration_name[0],
            class_name="text-secondary-12 text-base font-semibold uppercase size-full",
            unstyled=True,
        ),
        unstyled=True,
        class_name="size-6.5 flex items-center justify-center mx-3",
    )


@rx.memo
def integrations_marquee() -> rx.Component:
    integration_names = [
        next(iter(item.values()))["name"] for item in get_integration_path()
    ]
    return rx.el.div(
        marquee(
            *[integration_icon_marquee(name) for name in integration_names],
            direction="left",
            gradient_color="rgba(255, 255, 255, 0.96)",
            class_name="h-auto w-full overflow-hidden",
            gradient_width=65,
            speed=25,
            pause_on_hover=False,
        ),
        marquee(
            *[integration_icon_marquee(name) for name in integration_names],
            direction="right",
            gradient_color="rgba(255, 255, 255, 0.96)",
            class_name="h-auto w-full overflow-hidden",
            gradient_width=65,
            speed=25,
            pause_on_hover=False,
        ),
        class_name="flex flex-col gap-6.5 px-8 max-lg:pb-6",
    )


def ai_builder_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "AI Builder",
                    class_name="text-secondary-12 text-3xl font-[575]",
                ),
                rx.el.p(
                    "Learn how to build applications with Reflex AI.",
                    class_name="text-secondary-11 text-sm font-[475]",
                ),
                class_name="flex flex-col gap-4",
            ),
            rx.el.div(
                card(
                    title="Getting Started",
                    description="A comprehensive guide to working effectively with AI Builder. The key to success is clarity, structure, and iteration.",
                    content=rx.image(
                        src=f"/docs/{rx.color_mode_cond('light', 'dark')}/getting_started.svg",
                        class_name="w-full h-auto pb-8",
                    ),
                    href=ai_builder_pages.overview.best_practices.path,
                ),
                card(
                    title="Integrations",
                    description="Easily connect with the tools your team already uses or extend your app with any Python SDK, library, or API.",
                    content=integrations_marquee(),
                    href=ai_builder_pages.integrations.overview.path,
                ),
                card(
                    title="MCP",
                    description="The Reflex Model Context Protocol (MCP) provides AI assistants and coding tools with structured access to Reflex documentation and component information.",
                    content="WIP",
                    href=ai_builder_pages.integrations.mcp_overview.path,
                    enteprise_only=True,
                ),
                class_name="grid grid-cols-1 lg:grid-cols-3 gap-12",
            ),
            class_name="flex flex-col gap-10 max-lg:text-center relative max-w-(--docs-layout-max-width) mx-auto",
        ),
        class_name="bg-gradient-to-b from-white-1 to-secondary-1 w-full lg:pt-24 lg:mb-24 mb-10 max-lg:px-6 max-lg:pt-10",
    )
