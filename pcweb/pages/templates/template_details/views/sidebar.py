import reflex as rx
import reflex_ui as ui

from pcweb.components.hosting_banner import HostingBannerState
from pcweb.components.marketing_button import button as marketing_button
from pcweb.constants import INTEGRATIONS_IMAGES_URL
from pcweb.pages.templates.templates_state import TemplatesState

SECTION_HEADER_CLASS = (
    "font-mono font-[415] text-[0.75rem] leading-4 uppercase pb-4",
    "border-b border-dashed dark:border-m-slate-8 border-m-slate-6",
    "dark:text-m-slate-6 text-m-slate-7",
)


def links_section() -> rx.Component:
    return rx.el.div(
        marketing_button(
            "Create App",
            variant="primary",
            native_button=False,
            class_name="w-full",
            on_click=TemplatesState.redirect_to_template(
                template_id=TemplatesState.active_template.id,
                use_prompt=True,
            ),
        ),
        marketing_button(
            "View App",
            variant="outline",
            native_button=False,
            class_name="w-full",
            on_click=TemplatesState.redirect_to_template(
                template_id=TemplatesState.active_template.id,
                use_prompt=False,
            ),
        ),
        class_name="flex flex-col gap-4",
    )


def quick_start() -> rx.Component:
    return rx.el.div(
        rx.el.span("Quick Start", class_name=SECTION_HEADER_CLASS),
        rx.el.div(
            rx.el.div(
                rx.el.span("# Install reflex", class_name="text-[#ACB2BE]"),
                rx.el.span(
                    "pip install reflex",
                    class_name="text-primary-6 dark:text-primary-11",
                ),
                rx.el.span("# Use the AI builder", class_name="text-[#ACB2BE]"),
                rx.el.span(
                    "reflex --init ai",
                    class_name="text-primary-6 dark:text-primary-11",
                ),
                rx.el.span("# Run the app", class_name="text-[#ACB2BE]"),
                rx.el.span(
                    "reflex run",
                    class_name="text-primary-6 dark:text-primary-11",
                ),
                class_name="flex flex-col font-mono text-[0.75rem] leading-5 font-[415] p-4 shadow-[0_1px_0_0_rgba(255,255,255,0.24)_inset] rounded-[0.625rem]",
            ),
            class_name="rounded-xl bg-[#21252B] p-0.5",
        ),
        class_name="flex flex-col gap-6",
    )


def tech_stack() -> rx.Component:
    return rx.el.div(
        rx.el.span("Tech Stack", class_name=SECTION_HEADER_CLASS),
        rx.el.div(
            rx.foreach(
                TemplatesState.active_template.tech_stack,
                lambda tech: rx.el.span(
                    tech,
                    class_name="text-sm font-medium text-secondary-11",
                ),
            ),
            class_name="flex flex-wrap gap-x-4 gap-y-2",
        ),
        class_name="flex flex-col gap-6",
    )


def requirements() -> rx.Component:
    return rx.el.div(
        rx.el.span("Requirements", class_name=SECTION_HEADER_CLASS),
        rx.el.div(
            rx.foreach(
                TemplatesState.active_template.requirements,
                lambda requirement: rx.el.div(
                    ui.icon("ArrowRight02Icon", class_name="text-primary-10 mt-1"),
                    rx.el.span(
                        requirement,
                        class_name="text-sm font-medium text-secondary-12",
                    ),
                    class_name="flex items-start gap-2.5",
                ),
            ),
            class_name="flex flex-col gap-2",
        ),
        class_name="flex flex-col gap-6",
    )


def key_features() -> rx.Component:
    return rx.el.div(
        rx.el.span("Key Features", class_name=SECTION_HEADER_CLASS),
        rx.el.div(
            rx.foreach(
                TemplatesState.active_template.key_features,
                lambda feature: rx.el.div(
                    ui.icon("Tick02Icon", class_name="text-primary-10 mt-1"),
                    rx.el.span(
                        feature,
                        class_name="text-sm font-medium text-secondary-12",
                    ),
                    class_name="flex items-start gap-2.5",
                ),
            ),
            class_name="flex flex-col gap-2",
        ),
        class_name="flex flex-col gap-6",
    )


def enabled_integrations() -> rx.Component:
    return rx.el.div(
        rx.el.span("Integrations", class_name=SECTION_HEADER_CLASS),
        rx.el.div(
            integrations_stack(
                integrations=TemplatesState.active_template.enabled_integrations
            ),
            class_name="flex flex-col gap-6",
        ),
        class_name="flex flex-col gap-6",
    )


def enabled_integration_icon(integration_name: str) -> rx.Component:
    return ui.avatar.root(
        ui.avatar.image(
            src=rx.color_mode_cond(
                f"{INTEGRATIONS_IMAGES_URL}light/{integration_name}.svg",
                f"{INTEGRATIONS_IMAGES_URL}dark/{integration_name}.svg",
            ),
            unstyled=True,
            class_name="size-4",
        ),
        ui.avatar.fallback(
            integration_name[0],
            class_name="text-secondary-12 text-base font-semibold uppercase size-4 flex justify-center items-center",
            unstyled=True,
        ),
        unstyled=True,
        class_name="size-4 flex items-center justify-center shrink-0",
    )


def integrations_stack(
    integrations: list[str],
) -> rx.Component:
    return rx.el.div(
        rx.foreach(
            integrations,
            lambda integration: integrations_circle(integration_name=integration),
        ),
        class_name="flex flex-row -space-x-2 flex-wrap gap-y-2",
    )


@rx.memo
def integrations_circle(integration_name: str) -> rx.Component:
    formatted_integration_name = integration_name.lower().replace("_", " ")
    return rx.el.div(
        ui.tooltip(
            trigger=rx.el.div(
                enabled_integration_icon(integration_name=formatted_integration_name),
                class_name="flex size-8 shrink-0 justify-center items-center rounded-full shadow-small border border-secondary-a5 bg-white-1 dark:bg-secondary-1 cursor-default",
            ),
            side="bottom",
            content=integration_name,
        ),
        class_name="z-[1]",
    )


def sidebar_content() -> rx.Component:
    return rx.fragment(
        links_section(),
        rx.cond(TemplatesState.active_template.tech_stack, tech_stack()),
        rx.cond(
            TemplatesState.active_template.enabled_integrations, enabled_integrations()
        ),
        rx.cond(TemplatesState.active_template.key_features, key_features()),
        rx.cond(TemplatesState.active_template.requirements, requirements()),
    )


def sidebar_mobile() -> rx.Component:
    return rx.el.div(
        sidebar_content(),
        class_name="flex flex-col gap-12 lg:px-6 px-0 py-6 lg:py-12 lg:hidden",
    )


def sidebar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            sidebar_content(),
            class_name="flex flex-col gap-12 p-16 pb-24",
        ),
        class_name=ui.cn(
            "w-full max-w-[23.5rem] shrink-0 overflow-y-auto sticky hidden lg:block [scrollbar-width:thin]",
            rx.cond(
                HostingBannerState.is_banner_visible,
                "top-[103px] h-[calc(100vh-103px)]",
                "top-[67px] h-[calc(100vh-67px)]",
            ),
        ),
    )
