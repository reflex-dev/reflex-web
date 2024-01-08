import reflex as rx
from pcweb.templates.docpage import (
    docdemo,
    doctext,
)

code15 = """rx.form_control(
    rx.form_label("First Name", html_for="email"),
    rx.checkbox("Example"),
    rx.form_helper_text("This is a help text"),
    is_required=True,
    )
"""


form_error_state = """class FormErrorState(rx.State):
    name: str

    @rx.var
    def is_error(self) -> bool:
         return len(self.name) <= 3
"""
exec(form_error_state)

form_state_example = """rx.vstack(
        rx.form_control(
            rx.input(placeholder="name", on_blur=FormErrorState.set_name),
            rx.cond(
                FormErrorState.is_error,
                rx.form_error_message("Name should be more than four characters"),
                rx.form_helper_text("Enter name"),
            ),
            is_invalid=FormErrorState.is_error,
            is_required=True,

        )
    )

"""


def render_formcontrol():
    return rx.vstack(
        doctext(
            "Provides context such as filled/focused/error/required for form inputs."
        ),
        docdemo(code15),
        doctext(
            "The example below shows a form error when then name length is 3 or less."
        ),
        docdemo(
            form_state_example,
            state=form_error_state,
            comp=eval(form_state_example),
            context=True,
        ),
        align_items="start",
    )
