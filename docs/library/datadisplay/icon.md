---
components:
    - rx.radix.themes.Icon
---
# Icon

```python exec
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.components.icons import ICON_LIST
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
```

The Icon component is used to display an icon from a library of icons.

## Basic Example

To create an icon, we specify the `tag` prop from the list of available icons.

```python demo
icon(tag="calendar")
```

## List of Icons

```python eval
flex(
    callout_root(
        callout_icon(icon(tag="check_circled", variant="solid", high_contrast=True, color="green")),
        callout_text("Below is a list of all available icons.", color="black", weight="bold"),
        color="green",
    ),
    separator(size="4"),
    grid(
        *[
            flex(
                icon(tag=icon_tag, alias="Radix" + icon_tag.title()),
                text(icon_tag),
                direction="column",
                align="center",
                bg="white",
                border="1px solid #EAEAEA",
                border_radius="0.5em",
                padding=".75em",
            )
            for icon_tag in ICON_LIST
        ],
        columns="3",
        gap="1",
    ),
    direction="column",
    gap="2",
)
```

## Styling

The icons are based on the Radix primitive component, and it is unstyled. **It does not accept common styling props such as `size` or `color_theme`**. You can still use `width` and `height` together to control the size of the icon, and specify its `color`.

### Width and Height

```python demo
flex(
    icon(tag="magnifying_glass", width=15, height=15),
    icon(tag="magnifying_glass", width=20, height=20),
    icon(tag="magnifying_glass", width=25, height=25),
    icon(tag="magnifying_glass", width=30, height=30),
    align="center",
    gap="2",
)
```

## Color

```python demo
flex(
    icon(tag="magnifying_glass", color="indigo"),
    icon(tag="magnifying_glass", color="cyan"),
    icon(tag="magnifying_glass", color="orange"),
    icon(tag="magnifying_glass", color="crimson"),
    gap="2",
)
```

## Final Example

Icons can be used as child components of many other components. Here is an example of a search bar with a magnifying glass icon.

```python demo
badge(
    flex(
        icon(tag="magnifying_glass", height=18, width=18),
        text("Search documentation...", size="3", weight="medium"),
        direction="row",
        gap="1",
        align="center",
    ),
    size="2",
    radius="full",
    color_scheme="gray",
)
```
