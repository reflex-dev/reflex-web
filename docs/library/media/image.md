---
components:
    - rx.image
---

```python exec
import reflex as rx
```

# Image

The Image component can display an image given a `src` path as an argument.
This could either be a local path from the assets folder or an external link.

```python demo
rx.image(src="/logo.jpg", width="100px", height="auto")
```

Image composes a box and can be styled simlarly.

```python demo
rx.image(
    src="/logo.jpg",
    width="100px",
    height="auto",
    border_radius="15px 50px",
    border="5px solid #555",
)
```

You can also pass a `PIL` image object as the `src`.

```python demo box
rx.image(src="https://picsum.photos/id/1/200/300", alt="An Unsplash Image")
```

```python
from PIL import Image
import requests


class ImageState(rx.State):
    url = f"https://picsum.photos/id/1/200/300"
    image = Image.open(requests.get(url, stream=True).raw)


def image_pil_example():
    return rx.vstack(
        rx.image(src=ImageState.image)
    )
```

```md alert info
# rx.image only accepts URLs and Pillow Images
A cv2 image must be covnerted to a PIL image to be passed directly to `rx.image` as a State variable, or saved to the `assets` folder and then passed to the `rx.image` component.
```
