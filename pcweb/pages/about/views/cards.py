import reflex as rx
import reflex_ui as ui


def squares_rectangle_small() -> rx.Component:
    return rx.image(
        src=f"/common/{rx.color_mode_cond('light', 'dark')}/squares_rectangle_small.svg",
        alt="Squares Rectangle Small",
        class_name="pointer-events-none",
    )


def card(title: str, description: rx.Component, icon: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            squares_rectangle_small(),
            class_name="absolute top-1 left-4.5",
        ),
        ui.icon(icon, class_name="text-secondary-12 size-10 mb-8", stroke_width=1),
        rx.el.h2(title, class_name="text-secondary-12 text-2xl font-semibold mb-4"),
        description,
        class_name="flex flex-col rounded-xl shadow-[0_0_0_1px_rgba(0,0,0,0.04),0_12px_24px_0_rgba(0,0,0,0.08),0_1px_1px_0_rgba(0,0,0,0.01),0_4px_8px_0_rgba(0,0,0,0.03),0_0_0_1px_#FFF_inset] lg:px-12 lg:pt-16 lg:pb-12 px-10 pt-14 pb-10 relative isolate backdrop-blur-[6px] bg-white/96",
    )


def cards() -> rx.Component:
    return rx.el.section(
        card(
            title="How It Started",
            description=rx.el.p(
                "Reflex began as a simple idea: ",
                rx.el.b(
                    " building web apps in Python should feel effortless. ",
                    class_name="font-semibold text-secondary-12",
                ),
                " What started as an internal experiment quickly grew into a community-driven framework used to ship real products fast.",
                class_name="text-secondary-11 text-base font-medium",
            ),
            icon="Plant04Icon",
        ),
        card(
            title="Core Values",
            description=rx.el.p(
                rx.el.b(
                    "Open source is at the core of Reflex. ",
                    class_name="font-semibold text-secondary-12",
                ),
                " We build in the open, listen to our community, and believe the best developer tools are shaped by the people who use them. ",
                rx.el.b(
                    "Transparency, collaboration, and craft ",
                    class_name="font-semibold text-secondary-12",
                ),
                " come first.",
                class_name="text-secondary-11 text-base font-medium",
            ),
            icon="OpenSourceIcon",
        ),
        class_name="grid grid-cols-1 lg:grid-cols-2 gap-10 max-w-[69rem] w-full mx-auto lg:pb-36 pb-24 max-lg:px-6",
    )
