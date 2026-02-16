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
            class_name="text-m-slate-12 dark:text-m-slate-3 text-xs font-medium bg-m-slate-1 dark:bg-m-slate-11 px-2.5 h-7 absolute top-0 right-0 border-b border-l rounded-bl-lg border-m-slate-4 dark:border-m-slate-9 flex justify-center items-center",
        )
        if enteprise_only
        else None,
        rx.el.div(
            rx.el.span(
                title,
                class_name="text-m-slate-12 dark:text-m-slate-3 text-xl font-[575]",
            ),
            rx.el.span(
                description,
                class_name="text-m-slate-7 dark:text-m-slate-6 text-sm font-[475]",
            ),
            class_name="flex flex-col gap-2 p-8",
        ),
        content,
        rx.el.a(to=href, class_name="absolute inset-0"),
        class_name="flex flex-col bg-white/96 dark:bg-m-slate-11 backdrop-blur-[16px] rounded-xl relative cursor-pointer transition-colors overflow-hidden shadow-[0_0_0_1px_rgba(0,0,0,0.04),0_12px_24px_0_rgba(0,0,0,0.08),0_1px_1px_0_rgba(0,0,0,0.01),0_4px_8px_0_rgba(0,0,0,0.03)] dark:shadow-none dark:border-t  dark:border-m-slate-9",
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
            class_name="text-m-slate-12 dark:text-m-slate-3 text-base font-semibold uppercase size-full",
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
            *[integration_icon_marquee(name) for name in reversed(integration_names)],
            direction="left",
            gradient_color="light-dark(rgba(255, 255, 255, 0.96), var(--m-slate-11))",
            class_name="h-auto w-full overflow-hidden",
            gradient_width=65,
            speed=25,
            pause_on_hover=False,
        ),
        marquee(
            *[integration_icon_marquee(name) for name in integration_names],
            direction="right",
            gradient_color="light-dark(rgba(255, 255, 255, 0.96), var(--m-slate-11))",
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
                    class_name="text-m-slate-12 dark:text-m-slate-3 text-3xl font-[575]",
                ),
                rx.el.p(
                    "Learn how to build applications with Reflex AI.",
                    class_name="text-m-slate-7 dark:text-m-slate-6 text-sm font-[475]",
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
                    content=rx.image(
                        src=f"/docs/{rx.color_mode_cond('light', 'dark')}/mcp.svg",
                        class_name="w-full h-auto dark:hidden",
                    ),
                    href=ai_builder_pages.integrations.mcp_overview.path,
                    enteprise_only=True,
                ),
                class_name="grid grid-cols-1 lg:grid-cols-3 gap-12",
            ),
            class_name="flex flex-col gap-10 max-lg:text-center relative max-w-(--docs-layout-max-width) mx-auto",
        ),
        class_name="bg-gradient-to-b from-white-1 to-m-slate-1 dark:from-m-slate-11 dark:to-m-slate-12 w-full lg:pt-24 lg:pb-24 pb-10 max-xl:px-6 max-lg:pt-10",
    )
