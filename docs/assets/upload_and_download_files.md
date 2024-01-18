```python exec
import reflex as rx
from pcweb.pages.docs import library
from pcweb.pages.docs import api_reference
```


# Files

In addition to any assets you ship with your app, many web app will often need to receive or send files, whether you want to share medias, allow user to import their data, or export some backend data.

In this section, we will cover all you need to know for manipulating files in Reflex.

## Download

If you want to let the users of your app download files from your server to their computer, Reflex offer you two way.

### With a regular link

For some basic usage, simply providing the path to your resource in a `rx.link` will work, and clicking the link will download the resource.

```python demo
rx.link("Download", href="/reflex_logo.png")
```

### With `rx.download` event

In case a simple link is not enough, or if you want to trigger downloads from the backend, you can use `rx.download` event.

```python demo
rx.button(
    "Download", 
    on_click=rx.download(url="/reflex_logo.png"),
)
```

`rx.download` also let you specify a name for the file that will be downloaded, if you want it to be different from the name on the server side.

```python demo
rx.button(
    "Download and Rename", 
    on_click=rx.download(
        url="/reflex_logo.png", 
        filename="different_name_logo.png"
    ),
)
```

Reference page for `rx.download` [here]({api_reference.special_events.path}).

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

For detailed informations, see the reference page of the component [here]({library.forms.upload.path}).