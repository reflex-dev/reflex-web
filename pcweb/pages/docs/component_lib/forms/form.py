import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import (
    doctext,
    docdemo,
)

form_state = """
class FormState(State):

    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        \"""Handle the form submit.\"""
        self.form_data = form_data
"""
exec(form_state)

form_example = """
pc.vstack(
    pc.form(
        pc.vstack(
            pc.input(placeholder="First Name", id="first_name"),
            pc.input(placeholder="Last Name", id="last_name"),
            pc.hstack(
                pc.checkbox("Checked", id="check"),
                pc.switch("Switched", id="switch"),
            ),
            pc.button("Submit", type_="submit"),
        ),
        on_submit=FormState.handle_submit,
    ),
    pc.divider(),
    pc.heading("Results"),
    pc.text(FormState.form_data.to_string()),
)
"""


def render_form():
    return pc.vstack(
        doctext(
            "Forms are used to collect user input. The ",
            pc.code("pc.form"),
            " component is used to group inputs and submit them together.",
        ),
        doctext(
            "The form component's children can be form controls such as ",
            pc.code("pc.input"),
            ", ",
            pc.code("pc.checkbox"),
            ", ",
            " or ",
            pc.code("pc.switch"),
            ".",
            "The controls should have an ",
            pc.code("id"),
            " attribute that is used to identify the control in the form data. ",
            "The ",
            pc.code("on_submit"),
            " event trigger submits the form data as a dictionary to the ",
            pc.code("handle_submit"),
            " event handler.",
        ),
        doctext(
            "The form is submitted when the user clicks the submit button or presses enter on the form controls."
        ),
        docdemo(
            form_example,
            state=form_state,
            comp=eval(form_example),
            context=True,
        ),
        align_items="start",
    )
