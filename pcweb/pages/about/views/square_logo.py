import reflex as rx

from pcweb.components.logo_reveal import logo_reveal


def square_logo() -> rx.Component:
    return rx.el.section(
        # Light mode
        rx.el.div(
            logo_reveal(
                grid_bg_src="/common/light/squares_logo.svg",
            ),
            class_name="dark:hidden",
        ),
        # Dark mode
        rx.el.div(
            logo_reveal(
                grid_bg_src="/common/dark/squares_logo.svg",
            ),
            class_name="hidden dark:block",
        ),
        class_name="max-w-(--layout-max-width) w-full h-auto",
    )
