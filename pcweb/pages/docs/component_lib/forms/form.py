import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import (
    doctext,
)

code15 = """pc.form_control(
    pc.form_label("First Name", html_for="email"),
    pc.checkbox("Example"),
    pc.form_helper_text("This is a help text"),
    is_required=True,
    )
"""


form_error_state = """class FormErrorState(State):
    name: str

    @pc.var
    def is_error(self) -> bool:
         return len(self.name) <= 3
"""
exec(form_error_state)

form_state_example = """pc.vstack(
        pc.form_control(
            pc.input(placeholder="name", on_blur=FormErrorState.set_name),
            pc.cond(
                FormErrorState.is_error,
                pc.form_error_message("Name should be more than four characters"),
                pc.form_helper_text("Enter name"),
            ),
            is_invalid=FormErrorState.is_error,
            is_required=True,

        )
    )
"""


def render_form():
    return pc.vstack(
        doctext(
            "Forms are used to collect user input. The ",
            pc.code("pc.form"),
            " component is used to group inputs together and submit them together.",
        ),
        align_items="start",
    )
