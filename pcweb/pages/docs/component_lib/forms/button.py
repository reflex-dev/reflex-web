import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo, doctext

# Forms
basic_button = """rx.button("Click Me!")
"""
button_style = """rx.button_group(
    rx.button("Example", bg="lightblue", color="black", size = 'sm'),
    rx.button("Example", bg="orange", color="white", size = 'md'),
    rx.button("Example", color_scheme="red", size = 'lg'),
    space = "1em",
)
"""
button_visual_states = """rx.button_group(
    rx.button("Example", bg="lightgreen", color="black", is_loading = True),
    rx.button("Example", bg="lightgreen", color="black", is_disabled = True),
    rx.button("Example", bg="lightgreen", color="black", is_active = True),
    space = '1em',
)
"""

button_group_example = """rx.button_group(
    rx.button(rx.icon(tag="minus"), color_scheme="red"),
    rx.button(rx.icon(tag="add"), color_scheme="green"),
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
button_state_example = """rx.button_group(
    rx.button(
        "Decrement",
        color_scheme="red",
        variant="outline",
        border_radius="1em",
        on_click=ButtonState.decrement,
    ),
    rx.heading(ButtonState.count, font_size=24),
    rx.button(
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
    return rx.vstack(
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
            rx.code("on_click"),
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


iconbutton_example = """rx.icon_button(icon="search")"""


def render_iconbutton():
    return rx.vstack(
        doctext("IconButton display a clickable Icon"),
        docdemo(iconbutton_example),
        doctext(
            "Since IconButton only renders an icon, you must pass the `aria_label` prop, so screen readers can give meaning to the button."
        ),
    )
