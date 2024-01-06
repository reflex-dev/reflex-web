import reflex as rx

from pcweb.templates.docpage import (
    docdemo,
    doctext,
)

code22 = """rx.number_input(
    on_change=NumberInputState.set_number,
)
"""
code23 = """class NumberInputState(rx.State):
    number: int
"""
exec(code23)


def render_numberinput():
    return rx.vstack(
        doctext(
            "The NumberInput component is similar to the Input component, but it has controls for incrementing or decrementing numeric values."
        ),
        docdemo(code22, state=code23, comp=eval(code22), context=True),
        align_items="start",
    )
