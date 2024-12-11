```python exec
import reflex as rx
from pcweb.pages.docs import library
from pcweb.pages.docs import api_reference
```

# File Upload and Download

Reflex provides built-in components and events for handling file uploads and downloads in your web applications. Whether you need to share media, allow users to import data, or export backend data, Reflex offers intuitive solutions for file handling.

## File Upload

The `rx.upload` component enables file upload functionality in your application. It supports both click-to-select and drag-and-drop interfaces, making it easy for users to upload files to your server.

### Basic Usage

Here's a simple example of file upload functionality:

```python demo
def index():
    return rx.upload(
        rx.text("Drag and drop files here or click to select files"),
        border="1px dashed",
        padding="2em",
    )
```

### Features
- Click-to-select or drag-and-drop interface
- Multiple file selection
- File type restrictions
- Upload progress tracking
- Upload cancellation
- Custom styling options

For detailed information about advanced features and customization options, see the [Upload Component Documentation]({library.forms.upload.path}).

## File Download

Reflex offers two approaches for implementing file downloads:

### 1. Direct Link Downloads

For simple file downloads, use the `rx.link` component. This is ideal for static files or when you want the browser to handle the file display/download decision:

```python demo
rx.link("Download", href="/reflex_banner.png", download=True)
```

### 2. Programmatic Downloads

For dynamic file downloads or when you need more control over the download process, use the `rx.download` event:

```python demo
rx.button(
    "Download",
    on_click=rx.download(url="/reflex_banner.png"),
)
```

#### Custom Filename

You can specify a custom filename for the downloaded file:

```python demo
rx.button(
    "Download and Rename",
    on_click=rx.download(
        url="/reflex_banner.png",
        filename="different_name_logo.png"
    ),
)
```

#### Dynamic Data Downloads

For downloading dynamically generated data:

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

The `data` parameter accepts various types:
- `str` or `bytes` data
- `data:` URI
- `PIL.Image` objects
- Any state Var (automatically converted to JSON)

For complete details about download options and parameters, see the [`rx.download` reference]({api_reference.special_events.path}#rx.download).
