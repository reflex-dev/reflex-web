# Share App

The **Share** feature makes it easy to show your app to others without deploying it.
When you share, Reflex Build generates a unique link that points to the current version of your project in the builder.

```python exec
import reflex as rx
from reflex_image_zoom import image_zoom

def render_image():
    return rx.el.div(
        image_zoom(
            rx.image(
                src=rx.color_mode_cond(
                    "/ai_builder/app_lifecycle/share_light.png",
                    "/ai_builder/app_lifecycle/share_dark.png",
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

## How to Share

1. In the AI Builder workspace, click the **Share** button (bottom-right corner).
2. A popup will appear with a **shareable link**.
3. Copy the link and send it to teammates, collaborators, or stakeholders.


## What Others See

- The link opens a **read-only view** of your app generation.
- Recipients can see the app preview but cannot make edits.
- This makes it safe to share work-in-progress versions for quick feedback.


## Common Use Cases

- **Get Feedback Quickly**
  Share a work-in-progress version with your team before deploying.

- **Demo Features**
  Send a link to showcase a new component, layout, or integration.

- **Collaboration**
  Share context with another developer before handing off to GitHub or download.
