import reflex as rx
from pcweb.components.button import button
from pcweb.pages.docs import getting_started
from pcweb.components.icons.icons import get_icon


def code_block() -> rx.Component:
    return rx.box(
        # Copy button
        rx.el.button(
            get_icon(
                "clipboard",
                class_name="!text-slate-9 hover:!text-slate-11 transition-color",
            ),
            on_click=rx.set_clipboard("pip install reflex\nreflex init\nreflex run"),
            class_name="top-4 right-4 absolute cursor-pointer",
        ),
        rx.box(
            rx.el.p("$ pip install reflex"),
            rx.el.p("$ reflex init"),
            rx.el.p("$ reflex run"),
            class_name="font-['JetBrains_Mono'] !font-medium text-[0.8125rem] text-slate-11 leading-6",
        ),
        rx.box(
            rx.text(
                "Need help? Learn more about using Reflex.",
                class_name="font-small text-slate-9",
            ),
            rx.link(
                button(
                    "Docs",
                ),
                href=getting_started.introduction.path,
            ),
            class_name="flex flex-row justify-between items-center gap-2",
        ),
        class_name="relative flex flex-col gap-4 border-slate-4 bg-slate-2 shadow-large p-4 border rounded-[1.125rem] self-stretch",
    )


def get_started() -> rx.Component:
    return rx.el.section(
        rx.box(
            rx.el.h2(
                "Get started easily",
                class_name="gradient-heading font-x-large",
            ),
            rx.el.h3(
                "Run this code and you should see your first app.",
                class_name="font-base text-slate-9",
            ),
            class_name="flex flex-col gap-4 text-center self-stretch",
        ),
        code_block(),
        id="get-started",
        class_name="flex flex-col justify-center items-center gap-10 pb-2 w-[25rem]",
    )
