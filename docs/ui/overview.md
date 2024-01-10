```python exec
from pcweb.pages.docs import components
from pcweb.pages.docs.library import library
import reflex as rx
from pcweb.templates.docpage import definition, docalert, doclink

definitions = [
    definition(
        "Children",
        rx.unordered_list(
            rx.list_item("Text or other Reflex components nested inside a component."),
            rx.list_item(
                "Passed as ",
                rx.span("positional arguments", font_weight="bold"),
                ".",
            ),
        ),
    ),
    definition(
        "Props",
        rx.unordered_list(
            rx.list_item(
                "Attributes that affect the behavior and appearance of a component."
            ),
            rx.list_item(
                "Passed as ",
                rx.span("keyword arguments", font_weight="bold"),
                ".",
            ),
        ),
    ),
]
```

# UI Overview

Components are the building blocks of Reflex's frontend. They let you split the UI into independent, reusable pieces, and let you think about each piece in isolation.

Reflex components wrap React components behind the scenes, enabling a pure Python development experience.

Components are created with Python functions. They are configured with keyword arguments, called [props]({components.props.path}), and can be nested to create complex UIs.

## Component Basics

Components are made up of children and props.

```python eval
rx.mobile_only(
    rx.vstack(
        *definitions,
        margin_bottom="1em",
    ),
)
```

```python eval
rx.tablet_and_desktop(
    rx.grid(
        rx.grid_item(definitions[0], row_span=1, col_span=1, width="100%"),
        rx.grid_item(definitions[1], row_span=1, col_span=1, width="100%"),
        template_columns="repeat(2, 1fr)",
        h="10em",
        width="100%",
        gap=4,
        margin_bottom="1em",
    )
)
```

Let's take a look at the `rx.text` component.

```python demo
rx.text('Hello World!', color='blue', font_size="1.5em")
```

Here `"Hello World!"` is the child text to display, while `color` and `font_size` are props that modify the appearance of the text.

```python eval
docalert(
    "Regular Python data types can be passed in as children to components. ",
    "This is useful for passing in text, numbers, and other simple data types. ",
    status="success",
)
```

## Another Example

Now let's take a look at a more complex component, which has other components nested inside it. The `rx.hstack` component is a container that arranges its children horizontally.


```python demo
rx.hstack(
    # Static 50% progress
    rx.circular_progress(
        rx.circular_progress_label("50", color="green"),
        value=50,
    ),
    # "Spinning" progress
    rx.circular_progress(
        rx.circular_progress_label("∞", color="rgb(107,99,246)"),
        is_indeterminate=True,
    ),
)
```

Some props are specific to a component. For example, the `value` prop of the `rx.circular_progress` component controls the progress bar's value.

Styling props like `color` are shared across many components.

```python eval
rx.alert(
    rx.alert_icon(),
    rx.alert_title(
        "You can find all the props for a component by checking its documentation page in the ",
        doclink("component library", href=library.path),
        ".",
    ),
    status="info",
)
```

## Pages

Reflex apps are organized into pages. Pages link a specific URL route to a component.

You can create a page by defining a function that returns a component. By default, the function name will be used as the path, but you can also specify a path explicitly.

```python
def index():
    return rx.text('Root Page')


def about():
    return rx.text('About Page')


app = rx.App()
app.add_page(index, route="/")
app.add_page(about, route="/about")
```

In this example we add a page called `index` at the root route. If you're running in `dev` mode, you can access it at `http://localhost:3000`.

Similarly, the `about` page will be available at `http://localhost:3000/about`.


