---
components:
    - rx.radix.themes.CalloutRoot
---



```python exec
import reflex as rx
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
```

# Callout Style

## Size

Use the `size` prop to control the size.

```python demo
flex(
    callout_root(
        callout_icon(icon(tag="info_circled")),
        callout_text("You will need admin privileges to install and access this application."),
        size="3",
    ),
    callout_root(
        callout_icon(icon(tag="info_circled")),
        callout_text("You will need admin privileges to install and access this application."),
        size="2",
    ),
    callout_root(
        callout_icon(icon(tag="info_circled")),
        callout_text("You will need admin privileges to install and access this application."),
        size="1",
    ),
    direction="column",
    gap="3",
    align="start",
)
```

## Variant 

Use the `variant` prop to control the visual style. It is set to `soft` by default.

```python demo
flex(
    callout_root(
        callout_icon(icon(tag="info_circled")),
        callout_text("You will need admin privileges to install and access this application."),
        variant="soft",
    ),
    callout_root(
        callout_icon(icon(tag="info_circled")),
        callout_text("You will need admin privileges to install and access this application."),
        variant="surface",
    ),
    callout_root(
        callout_icon(icon(tag="info_circled")),
        callout_text("You will need admin privileges to install and access this application."),
        variant="outline",
    ),
    direction="column",
    gap="3",
)
```


## Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.


```python demo
flex(
    callout_root(
        callout_icon(icon(tag="info_circled")),
        callout_text("You will need admin privileges to install and access this application."),
        color_scheme="blue",
    ),
    callout_root(
        callout_icon(icon(tag="info_circled")),
        callout_text("You will need admin privileges to install and access this application."),
        color_scheme="green",
    ),
    callout_root(
        callout_icon(icon(tag="info_circled")),
        callout_text("You will need admin privileges to install and access this application."),
        color_scheme="red",
    ),
    direction="column",
    gap="3",
)
```




## High Contrast

Use the `high_contrast` prop to add additional contrast.


```python demo
flex(
    callout_root(
        callout_icon(icon(tag="info_circled")),
        callout_text("You will need admin privileges to install and access this application."),
    ),
    callout_root(
        callout_icon(icon(tag="info_circled")),
        callout_text("You will need admin privileges to install and access this application."),
        high_contrast=True,
    ),
    direction="column",
    gap="3",
)
```