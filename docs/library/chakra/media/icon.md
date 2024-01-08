```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo_from
from reflex.components.media.icon import ICON_LIST
```

# Icon

The Icon component is used to display an icon from a library of icons.

```python demo
rx.icon(tag="calendar")
```

Use the tag prop to specify the icon to display.

```python eval
rx.box(
    rx.alert(
        rx.alert_icon(),
        rx.alert_title("Below is a list of all available icons."),
        status="success",
    ),
    rx.divider(),
    rx.responsive_grid(
        *[
            rx.vstack(
                rx.icon(tag=icon),
                rx.text(icon),
                bg="white",
                border="1px solid #EAEAEA",
                border_radius="0.5em",
                padding=".75em",
            )
            for icon in ICON_LIST
        ],
        columns=[2, 2, 3, 3, 4],
        spacing="1em",
    )
)
```