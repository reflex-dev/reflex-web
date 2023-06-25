import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import (
    docdemo,
    doctext,
    subheader,
)

basic_checkbox = """rx.checkbox("Check Me!")
"""
checkbox_style = """rx.hstack(
    rx.checkbox("Example", color_scheme="green", size="sm"),
    rx.checkbox("Example", color_scheme="blue", size="sm"),
    rx.checkbox("Example", color_scheme="yellow", size="md"),
    rx.checkbox("Example", color_scheme="orange", size="md"),
    rx.checkbox("Example", color_scheme="red", size="lg"),
)
"""
checkbox_visual_states = """rx.hstack(
    rx.checkbox(
        "Example", color_scheme="green", size="lg", is_invalid=True
    ),
    rx.checkbox(
        "Example", color_scheme="green", size="lg", is_disabled=True
    ),
)
"""
checkbox_state = """class CheckboxState(State):
    checked: bool = False

    def toggle(self):
        self.checked = not self.checked

"""
exec(checkbox_state)
checkbox_state_example = """rx.hstack(
    rx.cond(
        CheckboxState.checked,
        rx.text("Checked", color="green"),
        rx.text("Unchecked", color="red"),
    ),
    rx.checkbox(
        "Example",
        on_change=CheckboxState.set_checked,
    ),
    rx.box(
        "Example",
        on_blur=CheckboxState.toggle,
    ),
)
"""

checkbox_group_example = """rx.checkbox_group(
    rx.checkbox("Example", color_scheme="green"),
    rx.checkbox("Example", color_scheme="blue"),
    rx.checkbox("Example", color_scheme="yellow"),
    rx.checkbox("Example", color_scheme="orange"),
    rx.checkbox("Example", color_scheme="red"),
    space="1em",
)
"""


def render_checkbox():
    return rx.vstack(
        doctext(
            "A checkbox is a common way to toggle boolean value. The checkbox component can be used on its own or in a group.",
        ),
        docdemo(basic_checkbox),
        doctext("Checkboxes can range in size and styles."),
        docdemo(checkbox_style),
        doctext("Checkboxes can also have different visual states."),
        docdemo(checkbox_visual_states),
        doctext(
            "Checkboxes can be hooked up to a state using the ",
            rx.code("on_change"),
            " prop.",
        ),
        docdemo(
            checkbox_state_example,
            state=checkbox_state,
            comp=eval(checkbox_state_example),
            context=True,
        ),
        subheader("Checkbox Group"),
        doctext("You can group checkboxes together using checkbox group."),
        docdemo(checkbox_group_example),
        align_items="start",
    )
