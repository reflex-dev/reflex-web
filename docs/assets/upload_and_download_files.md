```python exec
import reflex as rx
from pcweb.pages.docs import library
from pcweb.pages.docs import api_reference
from pcweb.styles.styles import get_code_style
from pcweb.styles.colors import c_color
```

# Files

In addition to any assets you ship with your app, many web app will often need to receive or send files, whether you want to share media, allow user to import their data, or export some backend data.

In this section, we will cover all you need to know for manipulating files in Reflex.

## Assets vs Upload Directory

Before diving into file uploads and downloads, it's important to understand the difference between assets and the upload directory in Reflex:

```python demo
def assets_vs_upload_comparison():
    # Define styles
    cell_style = {"py": "4", "px": "6"}
    
    # Define comparison data
    features = {
        "Purpose": {
            "assets": "Static files included with your app (images, stylesheets, scripts)",
            "upload": "Dynamic files uploaded by users during runtime"
        },
        "Location": {
            "assets": "`assets/` folder or next to Python files (shared assets)",
            "upload": "`uploaded_files/` directory (configurable)"
        },
        "Access Method": {
            "assets": "`rx.asset()` or direct path reference",
            "upload": "`rx.get_upload_url()`"
        },
        "When to Use": {
            "assets": "For files that are part of your application's codebase",
            "upload": "For files that users upload through your application"
        },
        "Availability": {
            "assets": "Available at compile time",
            "upload": "Available at runtime"
        }
    }
    
    # Function to process text and style code elements
    def process_text(text):
        # Check if the text contains backtick-quoted code
        if "`" in text:
            # Split the text by backticks
            parts = text.split("`")
            components = []
            
            # Process each part
            for i, part in enumerate(parts):
                # Even indices are regular text, odd indices are code
                if i % 2 == 0:
                    if part:  # Only add non-empty text
                        components.append(rx.text(part))
                else:
                    # This is code that was between backticks
                    components.append(rx.code(part, style=get_code_style("violet")))
            
            # Return the components in an hstack
            return rx.hstack(*components, spacing="2", flex_wrap="wrap")
        else:
            # No code to style, just return the text
            return rx.text(text)
    
    # Create table rows
    rows = []
    for feature, values in features.items():
        rows.append(
            rx.table.row(
                rx.table.cell(rx.text(feature, font_weight="bold"), style=cell_style),
                rx.table.cell(process_text(values["assets"]), style=cell_style),
                rx.table.cell(process_text(values["upload"]), style=cell_style),
            )
        )
    
    # Create and return the table
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Feature", style=cell_style),
                rx.table.column_header_cell("Assets", style=cell_style),
                rx.table.column_header_cell("Upload Directory", style=cell_style),
            ),
        ),
        rx.table.body(*rows),
        width="100%",
    )
```

```md alert
# Assets are primarily intended for frontend use

Assets in Reflex are primarily intended for frontend use and are not expected to be read from the backend. When assets are needed in both frontend and backend, they are currently copied to the backend (though this behavior may change in future versions).
```

For more information about assets, see the [Assets Overview](/docs/assets/overview/).

## Download

If you want to let the users of your app download files from your server to their computer, Reflex offer you two way.

### With a regular link

For some basic usage, simply providing the path to your resource in a `rx.link` will work, and clicking the link will download or display the resource.

```python demo
rx.link("Download", href="/reflex_banner.png")
```

### With `rx.download` event

Using the `rx.download` event will always prompt the browser to download the file, even if it could be displayed in the browser.

The `rx.download` event also allows the download to be triggered from another backend event handler.

```python demo
rx.button(
    "Download",
    on_click=rx.download(url="/reflex_banner.png"),
)
```

`rx.download` lets you specify a name for the file that will be downloaded, if you want it to be different from the name on the server side.

```python demo
rx.button(
    "Download and Rename",
    on_click=rx.download(
        url="/reflex_banner.png",
        filename="different_name_logo.png"
    ),
)
```

If the data to download is not already available at a known URL, pass the `data` directly to the `rx.download` event from the backend.

```python demo exec
import random

class DownloadState(rx.State):
    @rx.event
    def download_random_data(self):
        return rx.download(
            data=",".join([str(random.randint(0, 100)) for _ in range(10)]),
            filename="random_numbers.csv"
        )

def download_random_data_button():
    return rx.button(
        "Download random numbers",
        on_click=DownloadState.download_random_data
    )
```

The `data` arg accepts `str` or `bytes` data, a `data:` URI, `PIL.Image`, or any state Var. If the Var is not already a string, it will be converted to a string using `JSON.stringify`. This allows complex state structures to be offered as JSON downloads.

Reference page for `rx.download` [here]({api_reference.special_events.path}#rx.download).

## Upload

Uploading files to your server let your users interact with your app in a different way than just filling forms to provide data.

The component `rx.upload` let your users upload files on the server.

Here is a basic example of how it is used:

```python
def index():
    return rx.fragment(
        rx.upload(rx.text("Upload files"), rx.icon(tag="upload")),
        rx.button(on_submit=State.<your_upload_handler>)
    )
```

For detailed information, see the reference page of the component [here]({library.forms.upload.path}).
