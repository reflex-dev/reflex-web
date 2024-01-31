
# Sidebar

Similar to a navigation bar, a sidebar is a common UI element found on the side of a webpage or application.

## Recipe

In this recipe, we will create a sidebar component than can help with navigation in a web app.

In this example we want the sidebar to stick to the left side of the page, so we will use the `position="fixed"` prop to make the sidebar fixed to the left side of the page.
We will also use the `left=0`, `top=0`, and `z_index=5` props to make sure the sidebar is always on top of the screen and above the other components on the page.

```python exec
import reflex as rx
from pcweb.templates.docpage import demo_box_style

# Custom styles for sidebar.
box_style = demo_box_style.copy()
del box_style["padding"]
del box_style["align_items"]
del box_style["justify_content"]
box_style["height"] = "500px"
box_style["position"] = "relative"

def sidebar():
    return rx.vstack(
        rx.image(src="/favicon.ico",width="3em"),
        rx.heading("Sidebar", margin_bottom="1em"),
        position="absolute",
        height="100%",
        # left="0px",
        # top="0px",
        z_index="5",
        padding_x="2em",
        padding_y="1em",
        background_color="lightgray",
        align_items="left",
        width="250px",
    )
```

```python eval
rx.box(
    sidebar(),
    style=box_style,
)
```

```python
def sidebar():
    return rx.vstack(
        rx.image(src="/favicon.ico",width="3em"),
        rx.heading("Sidebar", margin_bottom="1em"),
        position="fixed",
        height="100%",
        left="0px",
        top="0px",
        z_index="5",
        padding_x="2em",
        padding_y="1em",
        background_color="lightgray",
        align_items="left",
        width="250px",
    )
```

## Adding Main Content

Now that we have a sidebar, we can add some content to the main part of the page.

We wrap both the sidebar and content in an `rx.fragment`.
We also make sure the content is aligned to the right of the sidebar by setting the `padding_left` prop to `250px`.

```python exec

def content():
    return rx.box(
        rx.heading("Welcome to My App"),
        rx.text("This is the main content of the page."),
    )


def index():
    return rx.fragment(
        sidebar(),
        rx.container(
            content(),
            max_width="60em",
            margin_left="250px",
            padding="2em"
        ),
    )

```

```python eval
rx.box(
    index(),
    style=box_style,
)
```