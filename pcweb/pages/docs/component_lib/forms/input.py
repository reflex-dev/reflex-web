import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import (
    docdemo,
    doctext,
)

input_state = """class InputState(State):
    text: str = "Type something..."
"""
basic_input_example = """pc.vstack(
    pc.text(InputState.text, color_scheme="green"),
    pc.input(on_change=InputState.set_text)
)
"""
exec(input_state)

input_blur_state = """class InputBlurState(State):
    text: str = "Type something..."

    def set_text(self, text: str):
        self.text = text.upper()
"""
blur_input_example = """pc.vstack(
    pc.text(InputBlurState.text),
    pc.input(placeholder="Type something...", on_blur=InputBlurState.set_text)
)
"""
exec(input_blur_state)
clear_input_state = """
class ClearInputState(State):
    text: str

    def clear_text(self):
        self.text = ""
"""
clear_input_example = """pc.vstack(
    pc.input(
        value=ClearInputState.text,
        on_change=ClearInputState.set_text,
    ),
    pc.button("Clear", on_click=ClearInputState.clear_text),
)
"""

exec(clear_input_state)
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
key_press_example = """pc.input(
    placeholder="Type and press enter...",
    value=KeyPressInputState.text,
    on_change=KeyPressInputState.set_text,
    on_key_down=KeyPressInputState.on_key_down,
)
"""
input_type_example = """pc.vstack(
    pc.input(type_="password"),
    pc.input(type_="date"),
)"""
password_example = """pc.password()"""


input_form_state = """
class InputFormState(State):

    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        \"""Handle the form submit.\"""
        self.form_data = form_data
"""
exec(input_form_state)

input_form_example = """pc.vstack(
    pc.form(
        pc.vstack(
            pc.input(placeholder="First Name", id="first_name"),
            pc.input(placeholder="Last Name", id="last_name"),
            pc.button("Submit", type_="submit"),
        ),
        on_submit=InputFormState.handle_submit,
    ),
    pc.divider(),
    pc.heading("Results"),
    pc.text(InputFormState.form_data.to_string()),
)
"""


def render_input():
    return pc.vstack(
        doctext("The input component is used to receive text input from the user."),
        docdemo(
            basic_input_example,
            state=input_state,
            comp=eval(basic_input_example),
            context=True,
        ),
        doctext(
            "The input component can also use the ",
            pc.code("on_blur"),
            " event handler to only change the state when the user clicks away from the input. This is useful for performance reasons, as the state will only be updated when the user is done typing.",
        ),
        docdemo(
            blur_input_example,
            state=input_blur_state,
            comp=eval(blur_input_example),
            context=True,
        ),
        doctext(
            "The input component can also be hooked up to a state using the ",
            pc.code("value"),
            " prop. ",
            "This lets you control the value of the input from the state.",
        ),
        docdemo(
            clear_input_example,
            state=clear_input_state,
            comp=eval(clear_input_example),
            context=True,
        ),
        doctext(
            "You can also use the ",
            pc.code("on_key_down"),
            " and ",
            pc.code("on_key_up"),
            " event handlers to listen for key presses.",
        ),
        docdemo(
            key_press_example,
            state=key_press_state,
            comp=eval(key_press_example),
            context=True,
        ),
        doctext(
            "You can change the type of input by using the ",
            pc.code("type_"),
            " prop. For example you can create a password input or a date picker. ",
        ),
        docdemo(input_type_example),
        doctext(
            "We also provide a ",
            pc.code("pc.password"),
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
