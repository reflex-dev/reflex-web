import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo, doctext, demo_box_style, doccode, doclink, subheader

basic_checkbox = """pc.checkbox("Check Me!")
"""
checkbox_style = """pc.hstack(
    pc.checkbox("Example", color_scheme="green", size="sm"),
    pc.checkbox("Example", color_scheme="blue", size="sm"),
    pc.checkbox("Example", color_scheme="yellow", size="md"),
    pc.checkbox("Example", color_scheme="orange", size="md"),
    pc.checkbox("Example", color_scheme="red", size="lg"),
)
"""
checkbox_visual_states = """pc.hstack(
    pc.checkbox(
        "Example", color_scheme="green", size="lg", is_invalid=True
    ),
    pc.checkbox(
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
checkbox_state_example = """pc.hstack(
    pc.cond(
        CheckboxState.checked,
        pc.text("Checked", color="green"),
        pc.text("Unchecked", color="red"),
    ),
    pc.checkbox(
        "Example",
        on_change=CheckboxState.set_checked,
    ),
    pc.box(
        "Example",
        on_blur=CheckboxState.toggle,
    ),
)
"""

checkbox_group_example = """pc.checkbox_group(
    pc.checkbox("Example", color_scheme="green"),
    pc.checkbox("Example", color_scheme="blue"),
    pc.checkbox("Example", color_scheme="yellow"),
    pc.checkbox("Example", color_scheme="orange"),
    pc.checkbox("Example", color_scheme="red"),
    space="1em",
)
"""


def render_checkbox():
    return pc.vstack(
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
            pc.code("on_change"),
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