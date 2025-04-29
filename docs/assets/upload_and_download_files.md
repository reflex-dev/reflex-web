```python exec
import reflex as rx
```

# Files

In addition to static assets that ship with your app, many web applications need to handle dynamic file operations such as:

- Allowing users to download files from your server
- Enabling users to upload files to your server
- Processing uploaded files on the backend
- Generating files dynamically for download

This section covers everything you need to know about file handling in Reflex.

## Download

Reflex offers multiple ways to let users download files from your server to their computer.

### With a Regular Link

For basic usage, simply providing the path to your resource in an `rx.link` component will work. Clicking the link will download or display the resource depending on the file type and browser settings.

```python demo
rx.link("Download Image", href="/reflex_banner.png")
```

This approach works well for:
- Static files in your assets directory
- Files that can be displayed in the browser (images, PDFs, etc.)
- Simple download scenarios

### With `rx.download` Event

For more control over the download process, use the `rx.download` event. This approach:
- Always prompts the browser to download the file (even if it could be displayed)
- Can be triggered from any UI event or backend event handler
- Allows renaming the downloaded file
- Supports dynamically generated content

#### Basic Download

```python demo
rx.button(
    "Download Image",
    on_click=rx.download(url="/reflex_banner.png"),
)
```

#### Renaming Downloaded Files

You can specify a different filename for the downloaded file:

```python demo
rx.button(
    "Download and Rename",
    on_click=rx.download(
        url="/reflex_banner.png",
        filename="reflex_logo.png"
    ),
)
```

#### Dynamically Generated Downloads

If the data to download is not already available at a known URL, you can pass the `data` directly to the `rx.download` event from the backend:

```python demo exec
import random

class DownloadState(rx.State):
    @rx.event
    def download_random_data(self):
        """Generate and download random data as a CSV file."""
        # Generate random data
        data = ",".join([str(random.randint(0, 100)) for _ in range(10)])
        
        # Return a download event with the data
        return rx.download(
            data=data,
            filename="random_numbers.csv"
        )

def download_random_data_button():
    return rx.button(
        "Download random numbers",
        on_click=DownloadState.download_random_data
    )
```

#### Supported Data Types

The `data` parameter of `rx.download` accepts various types:

- `str`: Text data (will be encoded as UTF-8)
- `bytes`: Binary data
- `data:` URI: For inline data
- `PIL.Image`: Image objects from the Pillow library
- Any state `Var`: Will be converted to JSON if not already a string

This flexibility allows you to offer complex state structures as JSON downloads:

```python
@rx.event
def download_user_data(self):
    """Download the user's data as a JSON file."""
    return rx.download(
        data=self.user_data,  # This could be a dict or any JSON-serializable object
        filename="user_data.json"
    )
```

For more details on `rx.download`, see the [reference page](/docs/events/special-events/#rx.download).

## Upload

File uploads are essential for many web applications. Reflex provides the `rx.upload` component to handle file uploads with features like:

- Drag-and-drop support
- Multiple file selection
- File type filtering
- Upload progress tracking
- Cancellation support

### Basic Upload Example

Here's a simple example of how to use the upload component:

```python
class UploadState(rx.State):
    """State for handling file uploads."""
    
    # Store the uploaded filenames
    files: list[str] = []
    
    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        """Process uploaded files.
        
        Args:
            files: List of uploaded files from the frontend.
        """
        for file in files:
            # Read the file data
            upload_data = await file.read()
            
            # Define the output path
            outfile = rx.get_upload_dir() / file.filename
            
            # Save the file
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)
            
            # Update the state with the filename
            self.files.append(file.filename)

def index():
    """The main view with upload functionality."""
    return rx.vstack(
        # Upload component
        rx.upload(
            rx.vstack(
                rx.button("Select Files", color="primary"),
                rx.text("or drag and drop files here"),
            ),
            id="file_upload",
            border="1px dashed #ccc",
            padding="2em",
        ),
        
        # Display selected files
        rx.hstack(rx.foreach(rx.selected_files("file_upload"), rx.text)),
        
        # Upload button
        rx.button(
            "Upload Files",
            on_click=UploadState.handle_upload(rx.upload_files(upload_id="file_upload")),
        ),
        
        # Clear selection button
        rx.button(
            "Clear Selection",
            on_click=rx.clear_selected_files("file_upload"),
        ),
        
        # Display uploaded files
        rx.vstack(
            rx.heading("Uploaded Files"),
            rx.foreach(
                UploadState.files,
                lambda filename: rx.link(
                    filename,
                    href=rx.get_upload_url(filename),
                    target="_blank",
                ),
            ),
        ),
        spacing="4",
        padding="2em",
    )
```

### Upload Process Flow

1. User selects files via the `rx.upload` component (by clicking or drag-and-drop)
2. Selected files appear in the UI using `rx.selected_files("upload_id")`
3. User clicks an upload button that triggers an event handler with `rx.upload_files(upload_id="upload_id")`
4. The event handler receives the files as `list[rx.UploadFile]` objects
5. The handler processes the files (saving, analyzing, etc.)
6. The UI updates to reflect the uploaded files

### File Storage and Access

Reflex provides helper functions to manage uploaded files:

#### `rx.get_upload_dir()`

Returns the directory where uploaded files should be saved. By default, this is `./uploaded_files` in your project root, but it can be configured with the `REFLEX_UPLOADED_FILES_DIR` environment variable.

```python
# Save an uploaded file
outfile = rx.get_upload_dir() / file.filename
with outfile.open("wb") as f:
    f.write(file_data)
```

#### `rx.get_upload_url(filename)`

Returns the URL to access an uploaded file. This URL is automatically mounted by Reflex at `/_upload/`.

```python
# Display an uploaded image
rx.image(src=rx.get_upload_url("my_image.jpg"))

# Create a link to an uploaded file
rx.link("Download PDF", href=rx.get_upload_url("document.pdf"))
```

```md alert info
# File Persistence Warning

When using the Reflex hosting service, the uploaded files directory is not persistent and will be cleared on every deployment. For persistent storage of uploaded files in production, it's recommended to use an external service such as AWS S3, Google Cloud Storage, or similar cloud storage solutions.
```

### Advanced Upload Features

For more advanced upload scenarios, see the [Upload component reference](/docs/library/forms/upload/) which covers:

- Multiple file uploads
- Single file uploads
- File type restrictions
- Upload progress tracking
- Upload cancellation
- Custom styling
