# Fork App

The **Fork App** feature lets you take an existing app and create your own version of it. This is perfect for **experimenting, customizing, or building on top of someone else’s work** without affecting the original app.

```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
```

```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src=rx.color_mode_cond(
                "/ai_builder/overview/fork_template_light.png",
                "/ai_builder/overview/fork_template_dark.png",
            ),
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```


## How to Fork an App

1. Browse or open an app you’d like to use as a starting point.
2. Click the **Fork** button in the app’s bottom right corner.
3. The AI Builder will create a **copy of the app** in your workspace.
4. You can now **edit, customize, and expand** your forked app independently of the original.

## What Happens When You Fork

- You get a **full copy** of the original app, including all pages, components, and configurations.
- The forked app is **completely separate**, so changes you make do not affect the original.
- You can **rename, deploy, or share** your forked app like any other app in your workspace.

## Common Use Cases

- **Start From an Example**
  Use a sample or shared app as a foundation to save time and learn best practices.

- **Experiment Safely**
  Try new ideas or features without risking changes to the original app.

- **Collaborate and Customize**
  Fork a teammate’s app to tailor it to your needs while keeping the original intact.
