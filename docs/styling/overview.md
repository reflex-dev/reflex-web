```python exec
from pcweb.templates.docpage import docdemo, doclink
from pcweb.base_state import State
import reflex as rx
import inspect
from pcweb.pages.docs.styling import custom_stylesheets
```

# Styling 

Reflex components can be styled using the full power of [CSS]({"https://www.w3schools.com/css/"}).

There are three main ways to add style to your app and they take precedence in the following order:
1. **Inline:** Styles applied to a single component instance.
2. **Component:** Styles applied to components of a specific type.
3. **Global:** Styles applied to all components.

```python eval
rx.alert(
    rx.alert_icon(),
    rx.box(
        rx.alert_title("Style keys can be any valid CSS property name."),
        rx.alert_description(
            "To be consistent with Python standards, you can specify keys in ",
            rx.code("snake_case"),
            ".",
        ),
    ),
    status="success",
)
```

## Global Styles

You can pass a style dictionary to your app to apply base styles to all components.

For example, you can set the default font family and font size for your app here just once rather than having to set it on every component.

```python
style = {
    "font_family": "Comic Sans MS",
    "font_size": "16px",
}

app = rx.App(style=style)
```

## Component Styles

In your style dictionary, you can also specify default styles for specific component types or arbitrary CSS classes and IDs.

```python
accent_color = "#f81ce5"
style = {
    "::selection": {
        "background_color": accent_color,
    },
    ".some-css-class": {
        "text_decoration": "underline",
    },
    "#special-input": \{"width": "20vw"},
    rx.Text: {
        "font_family": styles.SANS,
    },
    rx.Divider: {
        "margin_bottom": "1em",
        "margin_top": "0.5em",
    },
    rx.Heading: {
        "font_weight": "500",
    },
    rx.Code: {
        "color": accent_color,
    },
}

app = rx.App(style=style)
```

Using style dictionaries like this, you can easily create a consistent theme for your app.

```python eval
rx.alert(
    rx.alert_icon(),
    rx.box(
        rx.alert_title("Note the use of the uppercase component names."),
        rx.alert_description(
            "We specify the component classes as keys, rather than their constructors. ",
        ),
    ),
    status="warning",
)
```

```python eval
rx.alert(
    rx.alert_icon(),
    rx.box(
        rx.alert_title("Watch out for underscores in class names and IDs"),
        rx.alert_description(
            "Reflex automatically converts ",
            rx.code("snake_case"),
            " identifiers into ",
            rx.code("camelCase"),
            " format when applying styles. To ensure consistency, it is recommended to use the dash character "
            "or camelCase identifiers in your own class names and IDs. ",
            "To style third-party libraries relying on underscore class names, an external stylesheet should be "
            "used. See ",
            doclink("custom stylesheets", href=custom_stylesheets.path),
            " for how to reference external CSS files.",
        ),
    ),
    status="warning",
)
```

## Inline Styles

