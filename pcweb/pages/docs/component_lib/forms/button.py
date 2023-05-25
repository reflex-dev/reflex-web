import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import (
    docdemo,
    doctext,
)

# Forms
basic_button = """pc.button("Click Me!")
"""
button_style = """pc.button_group(
    pc.button("Example", bg="lightblue", color="black", size = 'sm'),
    pc.button("Example", bg="orange", color="white", size = 'md'),
    pc.button("Example", color_scheme="red", size = 'lg'),
    space = "1em",
)
"""
button_visual_states = """pc.button_group(
    pc.button("Example", bg="lightgreen", color="black", is_loading = True),
    pc.button("Example", bg="lightgreen", color="black", is_disabled = True),
    pc.button("Example", bg="lightgreen", color="black", is_active = True),
    space = '1em',
)
"""

button_group_example = """pc.button_group(
    pc.button(pc.icon(tag="minus"), color_scheme="red"),
    pc.button(pc.icon(tag="add"), color_scheme="green"),
    is_attached=True,
)
"""

button_state = """class ButtonState(State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1
"""
exec(button_state)
button_state_example = """pc.button_group(
    pc.button(
        "Decrement",
        color_scheme="red",
        variant="outline",
        border_radius="1em",
        on_click=ButtonState.decrement,
    ),
    pc.heading(ButtonState.count, font_size=24),
    pc.button(
        "Increment",
        color_scheme="green",
        variant="outline",
        border_radius="1em",
        on_click=ButtonState.increment,
    ),
    space="1em",
)
"""


def render_button():
    return pc.vstack(
        doctext("A button is a clickable element that is used to trigger an event."),
        docdemo(basic_button),
        doctext(
            "Buttons can range in size and style. You can style it with traditional props or with the color scheme prop for ease of use."
        ),
        docdemo(button_style),
        doctext("Buttons can also have different visual states."),
        docdemo(button_visual_states),
        doctext("You can group buttons together using button group."),
        docdemo(button_group_example),
        doctext(
            "Buttons are use to trigger events using the",
            pc.code("on_click"),
            " event handler. ",
        ),
        docdemo(
            button_state_example,
            state=button_state,
            comp=eval(button_state_example),
            context=True,
        ),
        align_items="start",
    )
