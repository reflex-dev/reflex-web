import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import (
    docdemo,
    doctext,
    demo_box_style,
    doccode,
    doclink,
)

checkbox_example = """pc.vstack(
    pc.heading(SwitchState.is_checked),
    pc.switch(
        is_checked=SwitchState.checked, on_change=SwitchState.change_check
    ),
)
"""
checkbox_example_state = """class SwitchState(State):
    checked: bool = False
    is_checked = "Switch off!"

    def change_check(self, checked):
        self.checked = checked
        if self.checked:
            self.is_checked = "Switch on!"
        else:
            self.is_checked = "Switch off!"
"""
exec(checkbox_example_state)

styled_checkbox = """pc.hstack(
    pc.switch(color_scheme="red"),
    pc.switch(color_scheme="green"),
    pc.switch(color_scheme="yellow"),
    pc.switch(color_scheme="blue"),
    pc.switch(color_scheme="purple"),
)
"""


def render_switch():
    return pc.vstack(
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


code34 = """pc.vstack(
    pc.heading(TextareaState.text),
    pc.text_area(on_blur=TextareaState.set_text)
)
"""
code35 = """class TextareaState(State):
    text: str = "Hello World!"
"""
exec(code35)


def render_textarea():
    return pc.vstack(
        doctext("The Textarea component allows you to easily create multi-line text inputs."),
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
            outfile = pc.get_asset_path(file.filename)

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


copy_to_clipboard_example = """pc.copy_to_clipboard(
                    pc.icon(
                        tag="copy",
                        style=icon_style,
                    ),
                    text=pc.Var.create("Text to copy", is_string=True),
                ),"""


def render_copytoclipboard():
    return pc.vstack(
        doctext("A button that will put some content into the clipboard"),
        # docdemo(copy_to_clipboard_example),
        doctext("TODO: Add example for copy_to_clipboard"),
    )
