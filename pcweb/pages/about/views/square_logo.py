import reflex as rx


def square_logo() -> rx.Component:
    return rx.el.section(
        rx.image(
            src=f"/common/{rx.color_mode_cond('light', 'dark')}/squares_logo.svg",
            alt="Square Logo",
            loading="lazy",
        ),
        class_name="max-w-(--layout-max-width) w-fullh-auto",
    )
