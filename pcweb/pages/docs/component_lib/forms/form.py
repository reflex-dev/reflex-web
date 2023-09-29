import reflex as rx
from pcweb.base_state import State
from pcweb import flexdown

class FormState(State):

    form_data: dict = {}
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def render_form():
    # Get the file.
    front_matter, output = flexdown.read("docs/library/forms/form.md")
    return rx.box(
        *output,
    )