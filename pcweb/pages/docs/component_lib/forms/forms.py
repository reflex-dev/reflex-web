import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import (
    docdemo,
    doctext,
    demo_box_style,
    doccode,
    doclink,
)

checkbox_example = """rx.vstack(
    rx.heading(SwitchState.is_checked),
    rx.switch(
        is_checked=SwitchState.checked, on_change=SwitchState.change_check
    ),
)
"""
checkbox_example_state = """class SwitchState(State):
    checked: bool = False
    is_checked: bool = "Switch off!"

    def change_check(self, checked: bool):
        self.checked = checked
        if self.checked:
            self.is_checked = "Switch on!"
        else:
            self.is_checked = "Switch off!"
"""
exec(checkbox_example_state)

styled_checkbox = """rx.hstack(
    rx.switch(color_scheme="red"),
    rx.switch(color_scheme="green"),
    rx.switch(color_scheme="yellow"),
    rx.switch(color_scheme="blue"),
    rx.switch(color_scheme="purple"),
)
"""


def render_switch():
    return rx.vstack(
        doctext(
            "The Switch component is used as an alternative for the Checkbox component. You can switch between enabled or disabled states."
        ),
        docdemo(
            checkbox_example,
            state=checkbox_example_state,
            comp=eval(checkbox_example),
            context=True,
        ),
        doctext(
            "You can also change the color scheme of the Switch component by passing the color_scheme argument. The default color scheme is blue."
        ),
        docdemo(styled_checkbox),
        align_items="start",
    )


code34 = """rx.vstack(
    rx.heading(TextareaState.text),
    rx.text_area(value=TextareaState.text, on_change=TextareaState.set_text)
)
"""
code35 = """class TextareaState(State):
    text: str = "Hello World!"
"""
exec(code35)


def render_textarea():
    return rx.vstack(
        doctext(
            "The TextArea component allows you to easily create multi-line text inputs."
        ),
        docdemo(code34, state=code35, comp=eval(code34), context=True),
        doctext(
            "Alternatively, you can use the ",
            rx.code("on_blur"),
            " event handler to only update the state when the user clicks away. ",
            "Similar to the Input component, the TextArea is also implemented using debounced input ",
            "when it is fully controlled. ",
            "You can tune the debounce delay by setting the ",
            rx.code("debounce_timeout"),
            " when creating the TextArea component. ",
            "You can find examples of how it is used in ",
            doclink("DebouncedInput", href="/docs/library/forms/debounceinput"),
            " component.",
        ),
        align_items="start",
    )


upload_code1 = """rx.upload(
    rx.text("Drag and drop files here or click to select files"),
    border="1px dotted rgb(107,99,246)",
    padding="5em",
)"""
upload_code2 = """
class State(rx.State):
    \"""The app state.\"""

    # The images to show.
    img: list[str]

    async def handle_upload(self, files: list[rx.UploadFile]):
        \"""Handle the upload of file(s).

        Args:
            files: The uploaded files.
        \"""
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_asset_path(file.filename)

            # Save the file.
            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.img.append(file.filename)


color = "rgb(107,99,246)"


def index():
    \"""The main view.\"""
    return rx.vstack(
        rx.upload(
            rx.vstack(
                rx.button("Select File", color=color, bg="white", border=f"1px solid {color}"),
                rx.text("Drag and drop files here or click to select files"),
            ),
            border=f"1px dotted {color}",
            padding="5em",
        ),
        rx.hstack(rx.foreach(rx.selected_files, rx.text)),
        rx.button(
            "Upload",
            on_click=lambda: State.handle_upload(rx.upload_files()),
        ),
        rx.foreach(State.img, lambda img: rx.image(src=img)),
        padding="5em",
    )

"""

upload_code3 = """
class State(rx.State):
    \"""The app state.\"""

    # The images to show.
    img: list[str]

    async def handle_upload(self, files: list[rx.UploadFile]):
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


color = "rgb(107,99,246)"


def index():
    \"""The main view.\"""
    return rx.vstack(
        rx.upload(
            rx.vstack(
                rx.button("Select File", color=color, bg="white", border=f"1px solid {color}"),
                rx.text("Drag and drop files here or click to select files"),
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
        rx.button(
            "Upload",
            on_click=lambda: State.handle_upload(rx.upload_files()),
        ),
        rx.responsive_grid(
            rx.foreach(
                State.imgs,
                lambda img: rx.vstack(
                    rx.image(src=img),
                    rx.text(img),
                ),
            ),
            columns=[2],
            spacing="5px",
        ),
        padding="5em",
    )

"""


def render_upload():
    return rx.vstack(
        doctext("The Upload component can be used to upload files to the server."),
        doctext(
            "You can pass components as children to customize its appearance. "
            "You can upload files by clicking on the component or by dragging and dropping files onto it. "
        ),
        docdemo(upload_code1, context=True),
        doctext(
            "Selecting a file will add it to the browser's file list, which can be rendered ",
            "on the frontend using the ",
            rx.code("rx.selected_files"),
            " special Var. "
            "To upload the file, you need to bind an event handler and pass the file list. ",
            "A full example is shown below. ",
        ),
        rx.vstack(
            rx.image(src="/upload.gif", style=demo_box_style),
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
            rx.code("files: list[UploadFile]"),
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
            rx.code("on_click"),
            " event, and pass in the files using ",
            rx.code("rx.upload_files()"),
            ". ",
        ),
        align_items="start",
    )


copy_to_clipboard_example = """rx.copy_to_clipboard(
                    rx.icon(
                        tag="copy",
                        style=icon_style,
                    ),
                    text=rx.Var.create("Text to copy", is_string=True),
                ),"""


# def render_copytoclipboard():
#     return rx.vstack(
#         doctext("A button that will put some content into the clipboard"),
#         docdemo(copy_to_clipboard_example),
#         doctext("TODO: Add example for copy_to_clipboard"),
#     )
