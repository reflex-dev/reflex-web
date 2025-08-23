# General App Settings

The **General App Settings** section lets you manage key aspects of your app, including its name, ID, and deletion. This is your central place to view and update your app’s core information.


```python exec
import reflex as rx
from reflex_image_zoom import image_zoom

def render_image():
    return rx.el.div(
        image_zoom(
            rx.image(
                src=rx.color_mode_cond(
                    "/ai_builder/app_lifecycle/general_light.png",
                    "/ai_builder/app_lifecycle/general_dark.png",
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


## How to Access Settings

1. In the AI Builder workspace, click the **Settings** icon located at the bottom-left of the screen, inside the chat box area.
2. This will open the **General** tab to see your app’s main settings.

## What You Can Do

- **Change App Name**
  Update the name of your app to reflect its purpose or version.

- **View App ID**
  Find the unique identifier for your app, which can be used for integrations or support.

- **Delete App**
  Permanently remove an app you no longer need. **Warning:** This action cannot be undone.

## Common Use Cases

- **Keep Apps Organized**
  Rename apps to make them easier to find in your workspace.

- **Integration Reference**
  Use the App ID when connecting your app to other tools or APIs.

- **Clean Up Workspace**
  Delete outdated or test apps to keep your workspace tidy.
