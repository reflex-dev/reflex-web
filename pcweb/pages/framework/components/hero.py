import reflex as rx

from pcweb.components.button import button
from pcweb.components.icons.icons import get_icon
from pcweb.constants import REFLEX_DEV_WEB_LANDING_FORM_URL_GET_DEMO
from pcweb.pages.docs import getting_started
from pcweb.pages.framework.demos.demos import demo_section


def hero() -> rx.Component:
    """Render the hero section of the landing page."""
    return rx.el.section(
        # Headings
        rx.box(
            rx.el.h1(
                "Build web apps in pure Python",
                class_name="inline-block bg-clip-text bg-gradient-to-r from-slate-12 to-slate-11 w-full font-xx-large lg:font-xxx-large text-balance text-center text-transparent",
            ),
            rx.el.h2(
                rx.el.span("An open-source framework to ship beautiful apps fast."),
                rx.el.span("Deploy with a single command."),
                class_name="flex flex-col font-md text-center text-slate-9",
            ),
            class_name="flex flex-col gap-6",
        ),
        # Buttons
        rx.box(
            rx.link(
                button(
                    "Get Started",
                    class_name="!px-[1.125rem] !py-2 !h-12 !font-smbold !text-[1.125rem] !leading-[1.625rem] !tracking-[-0.01688rem] transition-bg rounded-[0.875rem]",
                ),
                underline="none",
                href=getting_started.introduction.path,
            ),
            rx.link(
                button(
                    "Get a demo",
                    variant="muted",
                    class_name="!px-[1.125ren] !py-2 !h-12 !font-semibold !text-[1.125rem] !leading-[1.625rem] !tracking-[-0.01688rem] transition-bg rounded-[0.875rem]",
                ),
                href="/pricing",
                underline="none",
            ),
            class_name="flex flex-row items-center gap-4",
        ),
        # Pip install
        rx.box(
            get_icon("copy", class_name="!text-slate-9 [&>svg]:w-4 [&>svg]:h-4"),
            rx.el.p(
                "$ pip install reflex",
                class_name="font-['JetBrains_Mono'] font-medium font-small text-[0.8125rem] text-center text-slate-9 leading-6",
            ),
            on_click=rx.set_clipboard("pip install reflex"),
            class_name="flex flex-row items-center gap-3 hover:bg-slate-3 px-3 py-2 rounded-xl cursor-pointer transition-bg",
        ),
        # Demo section
        demo_section(),
        class_name="flex flex-col justify-center items-center gap-8 mx-auto w-full max-w-6xl",
    )
