import reflex as rx

from pcweb.components.icons.icons import get_icon


@rx.memo
def bottom_logo() -> rx.Component:
    return get_icon("bottom_logo")
