import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import (
    docdemo,
    doctext,
)

debounce_checkbox_state = """class DebounceCheckboxState(State):
    checked: bool = False
"""
exec(debounce_checkbox_state)
debounce_checkbox_state_example = """rx.hstack(
    rx.cond(
        DebounceCheckboxState.checked,
        rx.text("Checked", color="green"),
        rx.text("Unchecked", color="red"),
    ),
    rx.debounce_input(
        rx.checkbox(
            on_change=DebounceCheckboxState.set_checked,
        ),
        debounce_timeout=1000,
    ),
)
"""


def render_debounceinput():
    return rx.vstack(
        doctext(
            "Reflex is a backend-centric framework, which can create negative performance impacts for "
            "apps that need to provide interactive feedback to the user in real time. "
        ),
        doctext(
            "Using the ",
            rx.code("rx.debounce_input"),
            " component allows the frontend to remain responsive while receiving user input ",
            "and send the value to the backend after some delay, on blur, or when ",
            rx.kbd("Enter"),
            " is pressed.",
        ),
        doctext(
            "Typically, this component is used to wrap a child ",
            rx.code("rx.input"),
            " or ",
            rx.code("rx.text_area"),
            " however, most child components that accept the ",
            rx.code("value"),
            " prop and ",
            rx.code("on_change"),
            " event handler can be used with ",
            rx.code("rx.debounce_input"),
        ),
        doctext(
            "This example only sends the final checkbox state to the backend after a 1 second delay."
        ),
        docdemo(
            debounce_checkbox_state_example,
            state=debounce_checkbox_state,
            comp=eval(debounce_checkbox_state_example),
            context=True,
        ),
    )
