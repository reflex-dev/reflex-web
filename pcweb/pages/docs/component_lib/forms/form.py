import reflex as rx

from pcweb.base_state import State
from pcweb import flexdown
from pcweb.templates.docpage import (
    doctext,
    docdemo,
)

# form_state = """
# class FormState(State):

#     form_data: dict = {}

#     def handle_submit(self, form_data: dict):
#         \"""Handle the form submit.\"""
#         self.form_data = form_data
# """
# exec(form_state)

# form_example = """rx.vstack(
#     rx.form(
#         rx.vstack(
#             rx.input(placeholder="First Name", id="first_name"),
#             rx.input(placeholder="Last Name", id="last_name"),
#             rx.hstack(
#                 rx.checkbox("Checked", id="check"),
#                 rx.switch("Switched", id="switch"),
#             ),
#             rx.button("Submit", type_="submit"),
#         ),
#         on_submit=FormState.handle_submit,
#     ),
#     rx.divider(),
#     rx.heading("Results"),
#     rx.text(FormState.form_data.to_string()),
# )
# """


# form_state = """
# class FormState(State):

#     form_data: dict = {}
#     abababab = 0
#     def handle_submit(self, form_data: dict):
#         \"""Handle the form submit.\"""
#         self.form_data = form_data
# """
#exec(form_state)

def render_form():
    # Get the file.

    front_matter, output = flexdown.read("docs/library/forms/form.md")
    return rx.box(
        *output,
    )

    return rx.vstack(
        doctext(
            "Forms are used to collect user input. The ",
            rx.code("rx.form"),
            " component is used to group inputs and submit them together.",
        ),
        doctext(
            "The form component's children can be form controls such as ",
            rx.code("rx.input"),
            ", ",
            rx.code("rx.checkbox"),
            ", ",
            " or ",
            rx.code("rx.switch"),
            ".",
            "The controls should have an ",
            rx.code("id"),
            " attribute that is used to identify the control in the form data. ",
            "The ",
            rx.code("on_submit"),
            " event trigger submits the form data as a dictionary to the ",
            rx.code("handle_submit"),
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
        doctext(
            rx.alert(
                rx.alert_icon(),
                rx.alert_title(
                    "When using the form you must include a button or input with ",
                    rx.code("type_='submit'"),
                    ".",
                ),
                status="warning",
            ),
        ),
        align_items="start",
    )
