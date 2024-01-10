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

# Callout

A short message to attract user's attention.

Here is a simple example of using the `callout` component.

```python demo
callout_root(
    callout_icon(icon(tag="info_circled")),
    callout_text("You will need admin privileges to install and access this application."),
)
```

The `callout` component is made up of a `callout_root`, which groups `callout_icon` and `callout_text` parts. This component is based on the `div` element and supports common margin props.

The `callout_icon` provides width and height for the `icon` associated with the `callout`. This component is based on the `div` element. 

!!! Add in a link here to the page where we define all the different icons that can be used !!!

The `callout_text` renders the callout text. This component is based on the `p` element.



## As alert


```python demo
callout_root(
    callout_icon(icon(tag="exclamation_triangle")),
    callout_text("Access denied. Please contact the network administrator to view this page."),
    color_scheme="red",
    role="alert",
)
```
