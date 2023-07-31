import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import (
    docdemo,
    doctext,
)

input_state = """class InputState(State):
    text: str = "Type something..."
"""
basic_input_example = """rx.vstack(
    rx.text(InputState.text, color_scheme="green"),
    rx.input(on_change=InputState.set_text)
)
"""
exec(input_state)

input_blur_state = """class InputBlurState(State):
    text: str = "Type something..."

    def set_text(self, text: str):
        self.text = text.upper()
"""
blur_input_example = """rx.vstack(
    rx.text(InputBlurState.text),
    rx.input(placeholder="Type something...", on_blur=InputBlurState.set_text)
)
"""
exec(input_blur_state)

key_press_state = """
class KeyPressInputState(State):
    text: str

    def clear_text(self):
        self.text = ""

    def on_key_down(self, key: str):
        if key == "Enter":
            self.text = self.text.upper()
"""
exec(key_press_state)
key_press_example = """rx.input(
    placeholder="Type and press enter...",
    value=KeyPressInputState.text,
    on_change=KeyPressInputState.set_text,
    on_key_down=KeyPressInputState.on_key_down,
)
"""
input_type_example = """rx.vstack(
    rx.input(type_="password"),
    rx.input(type_="date"),
)"""
password_example = """rx.password()"""


input_form_state = """
class InputFormState(State):

    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        \"""Handle the form submit.\"""
        self.form_data = form_data
"""
exec(input_form_state)

input_form_example = """rx.vstack(
    rx.form(
        rx.vstack(
            rx.input(placeholder="First Name", id="first_name"),
            rx.input(placeholder="Last Name", id="last_name"),
            rx.button("Submit", type_="submit"),
        ),
        on_submit=InputFormState.handle_submit,
    ),
    rx.divider(),
    rx.heading("Results"),
    rx.text(InputFormState.form_data.to_string()),
)
"""


def render_input():
    return rx.vstack(
        doctext("The input component is used to receive text input from the user."),
        docdemo(
            basic_input_example,
            state=input_state,
            comp=eval(basic_input_example),
            context=True,
        ),
        doctext(
            "The input component can also use the ",
            rx.code("on_blur"),
            " event handler to only change the state when the user clicks away from the input. This is useful for performance reasons, as the state will only be updated when the user is done typing.",
        ),
        docdemo(
            blur_input_example,
            state=input_blur_state,
            comp=eval(blur_input_example),
            context=True,
        ),
        doctext(
            "You can change the type of input by using the ",
            rx.code("type_"),
            " prop. For example you can create a password input or a date picker. ",
        ),
        docdemo(input_type_example),
        doctext(
            "We also provide a ",
            rx.code("rx.password"),
            " component as a shorthand for the password input.",
        ),
        docdemo(password_example),
        doctext(
            "You can also use forms in combination with inputs. This can be useful in clearing the input after the form is submitted."
        ),
        docdemo(
            input_form_example,
            state=input_form_state,
            comp=eval(input_form_example),
            context=True,
        ),
        align_items="start",
    )
