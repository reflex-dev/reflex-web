# Download App

You can download your Reflex Build project if you want to work on it locally or self-host it outside the AI Builder.

**Tip:** The recommended workflow is to use the GitHub integration, which keeps your code version-controlled and in sync. Downloading is useful if GitHub integration isn’t available or you just want a one-time export.


```python exec
import reflex as rx
from reflex_image_zoom import image_zoom

def render_image():
    return rx.el.div(
        image_zoom(
            rx.image(
                src=rx.color_mode_cond(
                    "/ai_builder/app_lifecycle/download_light.webp",
                    "/ai_builder/app_lifecycle/download_dark.webp",
                ),
                class_name="p-2 rounded-md h-auto",
                border=f"0.81px solid {rx.color('slate', 5)}",
            ),
            class_name="rounded-md overflow-hidden",
        ),
        class_name="w-full flex flex-col rounded-md cursor-pointer",
    )
```

```python eval

rx.el.div(render_image())

```

## How to Download

1. In the AI Builder workspace, go to the **bottom-right corner**.
2. Click the **Download** button.
3. A `.zip` file will be generated containing your entire Reflex app, including:
   - Source code (`.py` files, components, state, etc.)
   - `requirements.txt` with dependencies
   - Config files (`rxconfig.py`, `.env`, etc.)
