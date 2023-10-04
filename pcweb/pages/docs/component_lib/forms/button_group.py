import reflex as rx
from pcweb import flexdown


def render_buttongroup():
    _, output = flexdown.read("docs/library/forms/button_group.md")
    return rx.box(
        *output,
    )
