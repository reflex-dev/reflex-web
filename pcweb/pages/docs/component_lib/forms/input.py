import reflex as rx

from pcweb.templates.docpage import (
    docdemo,
    doclink,
    doctext,
)

input_state = """class InputState(rx.State):
    text: str = "Type something..."
"""
basic_input_example = """rx.vstack(
    rx.text(InputState.text, color_scheme="green"),
    rx.input(value=InputState.text, on_change=InputState.set_text)
)
"""
exec(input_state)

input_blur_state = """class InputBlurState(rx.State):
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
clear_input_state = """
class ClearInputState(rx.State):
    text: str

    def clear_text(self):
        self.text = ""
"""
clear_input_example = """rx.vstack(
    rx.text(ClearInputState.text),
    rx.input(
        on_change=ClearInputState.set_text,
        value=ClearInputState.text,
    ),
    rx.button("Clear", on_click=ClearInputState.clear_text),
)
"""

exec(clear_input_state)
key_press_state = """
class KeyPressInputState(rx.State):
    text: str

    def clear_text(self):
        self.text = ""

    def on_key_down(self, key: str):
        if key == "Enter":
            self.text = self.text.upper()
"""
exec(key_press_state)
key_press_example = """rx.input(
    value=KeyPressInputState.text,
    placeholder="Type and press enter...",
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
class InputFormState(rx.State):

    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        \"""Handle the form submit.\"""
        self.form_data = form_data
        return [rx.set_value(field_id, "") for field_id in form_data]
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
            "Behind the scene, the input component is implemented ",
            "using debounced input to avoid sending individual state ",
            "updates per character to the backend while the user is ",
            "still typing. ",
            "This allows a state var to directly control the ",
            rx.code("value"),
            " prop from the backend without the user experiencing input lag. ",
            "For advanced use cases, you can tune the debounce delay ",
            "by setting the ",
            rx.code("debounce_timeout"),
            " when creating the Input component. ",
            "You can find examples of how it is used in ",
            doclink("DebouncedInput", href="/docs/library/forms/debounceinput"),
            " component.",
        ),
        docdemo(
            clear_input_example,
            state=clear_input_state,
            comp=eval(clear_input_example),
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
        # doctext(
        #     "You can also use the ",
        #     rx.code("on_key_down"),
        #     " and ",
        #     rx.code("on_key_up"),
        #     " event handlers to listen for key presses.",
        # ),
        # docdemo(
        #     key_press_example,
        #     state=key_press_state,
        #     comp=eval(key_press_example),
        #     context=True,
        # ),
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
            "You can also use forms in combination with inputs. This is useful for collecting multiple values with a single ",
            "event handler and automatically supporting ",
            rx.kbd("Enter"),
            " key submit functionality that desktop users expect. ",
        ),
        docdemo(
            input_form_example,
            state=input_form_state,
            comp=eval(input_form_example),
            context=True,
        ),
        align_items="start",
    )
