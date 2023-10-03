import reflex as rx
from pcweb import flexdown


def render_button():
    _, output = flexdown.read("docs/library/forms/button.md")
    return rx.box(
        *output,
    )
