# Use Images as a prompt

```python exec
import reflex as rx
```

Uploading an image (screenshot) of a website (web) app of what you are looking to build gives the AI really good context. 

*This is the recommended way to start an app generation.*


Below is a GIF showing how to upload an image to the AI Builder:

```python eval
rx.image(
    src="/ai_builder/image_upload.gif",
    height="auto",
    padding_bottom="2rem",
)
```

The advised prompt to use is:

`Build an app from a reference image`