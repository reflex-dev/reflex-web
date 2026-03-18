import reflex as rx

from pcweb.constants import REFLEX_ASSETS_CDN

# def square_logo() -> rx.Component:
#     return rx.el.section(
#         # Light mode
#         rx.el.div(
#             logo_reveal(
#                 grid_bg_src="/common/light/squares_logo.svg",
#             ),
#             class_name="dark:hidden",
#         ),
#         # Dark mode
#         rx.el.div(
#             logo_reveal(
#                 grid_bg_src="/common/dark/squares_logo.svg",
#             ),
#             class_name="hidden dark:block",
#         ),
#         class_name="max-w-(--layout-max-width) w-full h-auto",
#     )


def square_logo() -> rx.Component:
    return rx.el.section(
        rx.image(
            src=f"{REFLEX_ASSETS_CDN}common/{rx.color_mode_cond('light', 'dark')}/squares_logo.svg",
            alt="Square Logo",
            loading="lazy",
        ),
        class_name="max-w-(--layout-max-width) w-fullh-auto",
    )
