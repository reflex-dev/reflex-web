import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo, doctext, demo_box_style, doccode, doclink

# Forms
basic_button = """pc.button("Click Me!")
"""
button_style = """pc.button_group(
    pc.button("Example", bg="lightblue", color="black", size = 'sm'),
    pc.button("Example", bg="orange", color="white", size = 'md'),
    pc.button("Example", color_scheme="red", size = 'lg'),
    space = "1em",
)
"""
button_visual_states = """pc.button_group(
    pc.button("Example", bg="lightgreen", color="black", is_loading = True),
    pc.button("Example", bg="lightgreen", color="black", is_disabled = True),
    pc.button("Example", bg="lightgreen", color="black", is_active = True),
    space = '1em',
)
"""

button_group_example = """pc.button_group(
    pc.button(pc.icon(tag="minus"), color_scheme="red"),
    pc.button(pc.icon(tag="add"), color_scheme="green"),
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
button_state_example = """pc.button_group(
    pc.button(
        "Decrement",
        color_scheme="red",
        variant="outline",
        border_radius="1em",
        on_click=ButtonState.decrement,
    ),
    pc.heading(ButtonState.count, font_size=24),
    pc.button(
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
    return pc.vstack(
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
            pc.code("on_click"),
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
        align_items="start",
    )


basic_editable_class = """class EditableState(State):
    example_input: str
    example_textarea: str
    example_state: str

    def set_uppertext(self, example_state):
        print("testing")
        self.example_state = example_state.upper()
"""
basic_editable_example = """pc.editable(
    pc.editable_preview(),
    pc.editable_input(),
    placeholder="An input example...",
    on_submit=EditableState.set_uppertext,
    width="100%", 
    )
"""

exec(basic_editable_class)

textarea_editable_example = """pc.editable(
    pc.editable_preview(),
    pc.editable_textarea(),
    placeholder="A textarea example...",
    on_submit=EditableState.set_example_textarea,
    width="100%",
)
"""
state_editable_example = """pc.editable(
    pc.editable_preview(),
    pc.editable_input(),
    value=EditableState.example_state,
    on_change=EditableState.set_uppertext,
    width="100%",
)
"""

state_editable_blur_example = """pc.editable(
    pc.editable_preview(),
    pc.editable_input(),
    on_blur=EditableState.set_uppertext,
    width="100%",
)
"""


def render_editable():
    return pc.vstack(
        doctext(
            "Editable is used for inline renaming of some text. It appears as normal UI text but transforms into a text input field when the user clicks on or focuses it."
        ),
        docdemo(
            basic_editable_example,
            state=basic_editable_class,
            comp=eval(basic_editable_example),
            context=True,
        ),
        doctext(
            "Another variant of editable can be made with a textarea instead of an input."
        ),
        docdemo(textarea_editable_example, comp=eval(textarea_editable_example)),
        doctext(
            "Similar to other form components, editables can be hooked up to a state using the ",
            pc.code("on_change"),
            " prop.",
        ),
        docdemo(state_editable_example, comp=eval(state_editable_example)),
        align_items="start",
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
            pc.input(placeholder="name", on_change=FormErrorState.set_name),
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


def render_formcontrol():
    return pc.vstack(
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

    def set_text(self, text):
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

    def on_key_down(self, key):
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
        align_items="start",
    )


pin_state = """class PinInputState(State):
    pin: str
"""
basic_pin_example = """pc.vstack(
    pc.heading(PinInputState.pin),
    pc.box(
        pc.pin_input(
            length=4,
            on_change=PinInputState.set_pin,
            mask=True,
        ),
    ),
)
"""

exec(pin_state)

pin_custom_example = """pc.center(
    pc.pin_input(
        pc.pin_input_field(color="red"),
        pc.pin_input_field(border_color="green"),
        pc.pin_input_field(shadow="dark-lg"),
        pc.pin_input_field(color="blue"),
        pc.pin_input_field(border_radius="md"),
        on_change=PinInputState.set_pin,
    )
)
"""


def render_pininput():
    return pc.vstack(
        doctext(
            "The PinInput component is similar to the Input component, but it is optimized for entering sequences of digits."
        ),
        docdemo(
            basic_pin_example,
            state=pin_state,
            comp=eval(basic_pin_example),
            context=True,
        ),
        doctext("The PinInput component can also be customized as seen below."),
        docdemo(
            pin_custom_example,
            state=pin_state,
            comp=eval(pin_custom_example),
            context=True,
        ),
        align_items="start",
    )


code22 = """pc.number_input(
    on_change=NumberInputState.set_number,
)
"""
code23 = """class NumberInputState(State):
    number: int
"""
exec(code23)


def render_numberinput():
    return pc.vstack(
        doctext(
            "The NumberInput component is similar to the Input component, but it has controls for incrementing or decrementing numeric values."
        ),
        docdemo(code22, state=code23, comp=eval(code22), context=True),
        align_items="start",
    )


basic_radio_state = """
options = ["Option 1", "Option 2", "Option 3"]

class RadioState(State):
    text: str = "No Selection"
"""
basic_radio = """pc.vstack(
    pc.badge(RadioState.text, color_scheme="green"),
    pc.radio_group(
        options,
        on_change=RadioState.set_text,
    ),
)
"""
exec(basic_radio_state)


def render_radiogroup():
    return pc.vstack(
        doctext(
            "Radios are used when only one choice may be selected in a series of options."
        ),
        docdemo(
            basic_radio, state=basic_radio_state, comp=eval(basic_radio), context=True
        ),
        align_items="start",
    )


code26 = """pc.vstack(
    pc.heading(SelectState.option),
    pc.select(
        options,
        placeholder="Select an example.",
        on_change=SelectState.set_option,
    ),
)
"""
code27 = """
options = ["Option 1", "Option 2", "Option 3"]

class SelectState(State):
    option: str = "No selection yet."

"""
exec(code27)


def render_select():
    return pc.vstack(
        doctext(""),
        docdemo(code26, state=code27, comp=eval(code26), context=True),
        align_items="start",
    )


slider_state = """class SliderState(State):
    value: int = 50
"""

slider_base_example = """pc.vstack(
    pc.heading(SliderState.value),
    pc.slider(
        on_change=SliderState.set_value
    ),
    width="100%",
)
"""

slider_state_start = """class SliderVariation(State):
    value: int = 50

    def set_end(self, value):
        self.value = value
"""

slider_on_change_start = """pc.vstack(
    pc.heading(SliderVariation.value),
    pc.slider(
        on_change_end=SliderVariation.set_end
    ),
    width="100%",
)
"""

slider_state_combo = """class SliderCombo(State):
    value: int = 50
    color: str = "black"

    def set_start(self, value):
        self.color = "green" 

    def set_val(self, value):
        self.value = value
        self.color = "orange" 

    def set_end(self, value):
        self.color = "red" 
"""

slider_combo = """pc.vstack(
    pc.heading(SliderCombo.value, color=SliderCombo.color),
    pc.slider(
        on_change_start=SliderCombo.set_start,
        on_change=SliderCombo.set_val,
        on_change_end=SliderCombo.set_end
    ),
    width="100%",
)
"""

exec(slider_state_combo)
exec(slider_state_start)
exec(slider_state)


def render_slider():
    return pc.vstack(
        doctext(
            "The Slider is used to allow users to make selections from a range of values."
        ),
        docdemo(
            slider_base_example,
            state=slider_state,
            comp=eval(slider_base_example),
            context=True,
        ),
        doctext(
            "Using the ",
            pc.code("on_change"),
            " event triggers a state update every time the slider is moved. ",
        ),
        doctext(
            "For performance reasons, you may want to trigger state change only when the user releases the slider. "
        ),
        docdemo(
            slider_on_change_start,
            state=slider_state_start,
            comp=eval(slider_on_change_start),
            context=True,
        ),
        doctext(
            "You can also combine all three event handlers ",
            pc.code("on_change"),
            ", ",
            pc.code("on_change_start"),
            ", and ",
            pc.code("on_change_end"),
            " together.",
        ),
        docdemo(
            slider_combo,
            state=slider_state_combo,
            comp=eval(slider_combo),
            context=True,
        ),
        align_items="start",
    )


range_slider_state = """class RangeSliderState(State):
    value = [0,100]
"""

range_slider_base_example = """pc.vstack(
    pc.heading(RangeSliderState.value[0]+" : "+RangeSliderState.value[1]),
    pc.range_slider(
        on_change=RangeSliderState.set_value
    ),
    width="100%",
)
"""

range_slider_state_start = """class RangeSliderVariation(State):
    value = [0,100]

    def set_end(self, value):
        self.value = value
"""

range_slider_on_change_start = """pc.vstack(
    pc.heading(RangeSliderVariation.value[0]+" : "+RangeSliderVariation.value[1]),
    pc.range_slider(
        on_change_end=RangeSliderVariation.set_end
    ),
    width="100%",
)
"""

range_slider_state_combo = """class RangeSliderCombo(State):
    value = [0,100]
    color: str = "black"

    def set_start(self, value):
        self.color = "green" 

    def set_val(self, value):
        self.value = value
        self.color = "orange" 

    def set_end(self, value):
        self.color = "red" 
"""

range_slider_combo = """pc.vstack(
    pc.heading(RangeSliderCombo.value[0]+" : "+RangeSliderCombo.value[1], color=RangeSliderCombo.color),
    pc.range_slider(
        on_change_start=RangeSliderCombo.set_start,
        on_change=RangeSliderCombo.set_val,
        on_change_end=RangeSliderCombo.set_end
    ),
    width="100%",
)
"""

exec(range_slider_state_combo)
exec(range_slider_state_start)
exec(range_slider_state)


def render_rangeslider():
    return pc.vstack(
        doctext(
            "The range slider is used to allow users to make selections from a range of values."
        ),
        docdemo(
            range_slider_base_example,
            state=range_slider_state,
            comp=eval(range_slider_base_example),
            context=True,
        ),
        doctext(
            "You can also trigger state change only when the user releases the slider. "
        ),
        docdemo(
            range_slider_on_change_start,
            state=range_slider_state_start,
            comp=eval(range_slider_on_change_start),
            context=True,
        ),
        align_items="start",
    )


code32 = """pc.vstack(
    pc.heading(SwitchState.is_checked),
    pc.switch(
        is_checked=SwitchState.checked, on_change=SwitchState.change_check
    ),
)
"""
code33 = """class SwitchState(State):
    checked: bool = False
    is_checked = "Switch off!"

    def change_check(self, checked):
        self.checked = checked
        if self.checked:
            self.is_checked = "Switch on!"
        else:
            self.is_checked = "Switch off!"
"""
exec(code33)


def render_switch():
    return pc.vstack(
        doctext(
            "The Switch component is used as an alternative for the Checkbox component. You can switch between enabled or disabled states."
        ),
        docdemo(code32, state=code33, comp=eval(code32), context=True),
        align_items="start",
    )


code34 = """pc.text_area(on_blur=TextareaState.set_text)
"""
code35 = """class TextareaState(State):
    text: str
"""
exec(code35)


def render_textarea():
    return pc.vstack(
        doctext(
            "The Textarea component allows you to easily create multi-line text inputs."
        ),
        docdemo(code34, state=code35, comp=eval(code34), context=True),
        align_items="start",
    )


upload_code1 = """pc.upload(
    pc.text("Drag and drop files here or click to select files"),
    border="1px dotted rgb(107,99,246)",
    padding="5em", 
)"""
upload_code2 = """
class State(pc.State):
    \"""The app state.\"""

    # The images to show.
    img: list[str]

    async def handle_upload(self, files: List[pc.UploadFile]):
        \"""Handle the upload of file(s).
        
        Args:
            files: The uploaded files.
        \"""
        for file in files:
            upload_data = await file.read()
            outfile = f".web/public/{file.filename}"

            # Save the file.
            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.img.append(file.filename)



def index():
    \"""The main view.\"""
    return pc.vstack(
        pc.upload(
            pc.vstack(
                pc.button("Select File", color=color, bg="white", border=f"1px solid {color}"),
                pc.text("Drag and drop files here or click to select files"),
            ),
            border=f"1px dotted {color}",
            padding="5em", 
        ),
        pc.button(
            "Upload", 
            on_click=lambda: State.handle_upload(pc.upload_files()),
        ),
        pc.foreach(State.img, lambda img: pc.image(src=img)),
        padding="5em",
    )

"""

upload_code3 = """
class State(pc.State):
    \"""The app state.\"""

    # The images to show.
    img: list[str]

    async def handle_upload(self, files: List[pc.UploadFile]):
        \"""Handle the upload of file(s).
        
        Args:
            files: The uploaded files.
        \"""
        for file in files:
            upload_data = await file.read()
            outfile = f".web/public/{file.filename}"

            # Save the file.
            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.img.append(file.filename)


def index():
    \"""The main view.\"""
    return pc.vstack(
        pc.upload(
            pc.vstack(
                pc.button("Select File", color=color, bg="white", border=f"1px solid {color}"),
                pc.text("Drag and drop files here or click to select files"),
            ),
            multiple=True,
            accept = {
                "application/pdf": [".pdf"],
                "image/png": [".png"],
                "image/jpeg": [".jpg", ".jpeg"],
                "image/gif": [".gif"],
                "image/webp": [".webp"],
                "text/html": [".html", ".htm"],
            },
            max_files=5,
            disabled=False,
            on_keyboard=True,
            border=f"1px dotted {color}",
            padding="5em", 
        ),
        pc.button(
            "Upload",
            on_click=lambda: State.handle_upload(pc.upload_files()),
        ),
        pc.responsive_grid(
            pc.foreach(
                State.imgs,
                lambda img: pc.vstack(
                    pc.image(src=img),
                    pc.text(img),
                ),
            ),
            columns=[2],
            spacing="5px",
        ),
        padding="5em",
    )

"""


def render_upload():
    return pc.vstack(
        doctext("The Upload component can be used to upload files to the server."),
        doctext(
            "You can pass components as children to customize its appearance. "
            "You can upload files by clicking on the component or by dragging and dropping files onto it. "
        ),
        docdemo(upload_code1, context=True),
        doctext(
            "Selecting a file will add it to the browser's file list. ",
            "To upload the file, you need to bind an event handler and pass the file list. ",
            "A full example is shown below. ",
        ),
        pc.vstack(
            pc.image(src="/upload.gif", style=demo_box_style),
            doccode(upload_code2),
            width="100%",
            padding_bottom="1em",
        ),
        doctext(
            "In the example below, the upload component accepts a maximum number of 5 files of specific types. ",
            "It also disables the use of the space or enter key in uploading files.",
        ),
        doccode(upload_code3),
        doctext(
            "Your event handler should be an async function that accepts a single argument, ",
            pc.code("files: list[UploadFile]"),
            ", which will contain ",
            doclink(
                "FastAPI UploadFile",
                "https://fastapi.tiangolo.com/tutorial/request-files",
            ),
            " instances. ",
            "You can read the files and save them anywhere as shown in the example. ",
        ),
        doctext(
            "In your UI, you can bind the event handler to a trigger, such as a button ",
            pc.code("on_click"),
            " event, and pass in the files using ",
            pc.code("pc.upload_files()"),
            ". ",
        ),
        align_items="start",
    )
