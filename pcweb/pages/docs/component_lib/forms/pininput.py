import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import (
    docdemo,
    doctext,
)

pin_state = """class PinInputState(State):
    pin: str
"""
basic_pin_example = """rx.vstack(
    rx.heading(PinInputState.pin),
    rx.box(
        rx.pin_input(
            length=4,
            on_change=PinInputState.set_pin,
            mask=True,
        ),
    ),
)
"""

exec(pin_state)

pin_custom_example = """rx.center(
    rx.pin_input(
        rx.pin_input_field(color="red"),
        rx.pin_input_field(border_color="green"),
        rx.pin_input_field(shadow="md"),
        rx.pin_input_field(color="blue"),
        rx.pin_input_field(border_radius="md"),
        on_change=PinInputState.set_pin,
    )
)
"""


def render_pininput():
    return rx.vstack(
        doctext(
            "The PinInput component is similar to the Input component, but it is optimized for entering sequences of digits."
        ),
        docdemo(
            basic_pin_example,
            state=pin_state,
            comp=eval(basic_pin_example),
            context=True,
        ),
        doctext("The PinInput component can also be customized as seen below."),
        docdemo(
            pin_custom_example,
            state=pin_state,
            comp=eval(pin_custom_example),
            context=True,
        ),
        align_items="start",
    )
