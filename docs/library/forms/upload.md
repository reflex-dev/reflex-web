---
components:
    - rx.Upload
---

```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo_from, demo_box_style
```

# Upload

The Upload component can be used to upload files to the server.

You can pass components as children to customize its appearance.
You can upload files by clicking on the component or by dragging and dropping files onto it.

```python demo
rx.upload(
    rx.text("Drag and drop files here or click to select files"),
    border="1px dotted rgb(107,99,246)",
    padding="5em",
)
```

Selecting a file will add it to the browser's file list, which can be rendered on the frontend using the `rx.selected_files` special Var.
To clear the selected files, you can use another special Var `rx.clear_selected_files` as an event handler.
To upload the file, you need to bind an event handler and pass the file list.

A full example is shown below.

```python eval
rx.image(src="/upload.gif", style=demo_box_style)
```

```python
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
                rx.button("Select File", color=color, bg="white", border=f"1px solid \{color}"),
                rx.text("Drag and drop files here or click to select files"),
            ),
            border=f"1px dotted \{color}",
            padding="5em",
        ),
        rx.hstack(rx.foreach(rx.selected_files, rx.text)),
        rx.button(
            "Upload",
            on_click=lambda: State.handle_upload(rx.upload_files()),
        ),
        rx.button(
            "Clear",
            on_click=rx.clear_selected_files,
        ),
        rx.foreach(State.img, lambda img: rx.image(src=img)),
        padding="5em",
    )
```

In the example below, the upload component accepts a maximum number of 5 files of specific types.
It also disables the use of the space or enter key in uploading files.

```python
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
            outfile = f".web/public/\{file.filename}"

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
                rx.button("Select File", color=color, bg="white", border=f"1px solid \{color}"),
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
            border=f"1px dotted \{color}",
            padding="5em",
        ),
        rx.button(
            "Upload",
            on_click=lambda: State.handle_upload(rx.upload_files()),
        ),
        rx.responsive_grid(
            rx.foreach(
                State.img,
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
```

Your event handler should be an async function that accepts a single argument,
`files: list[UploadFile]`, which will contain [FastAPI UploadFile](https://fastapi.tiangolo.com/tutorial/request-files) instances.
You can read the files and save them anywhere as shown in the example.

In your UI, you can bind the event handler to a trigger, such as a button `on_click` event, and pass in the files using `rx.upload_files()`.