---
components:
    - rx.radix.themes.CalloutRoot
    - rx.radix.themes.CalloutIcon
    - rx.radix.themes.CalloutText
---


```python exec
import reflex as rx
import reflex.components.radix.themes as rdxt
```

# Callout

A `callout` is a short message to attract user's attention.


```python demo
rdxt.callout_root(
    rdxt.callout_icon(rdxt.icon(tag="info_circled")),
    rdxt.callout_text("You will need admin privileges to install and access this application."),
)
```

The `callout` component is made up of a `callout_root`, which groups `callout_icon` and `callout_text` parts. This component is based on the `div` element and supports common margin props.

The `callout_icon` provides width and height for the `icon` associated with the `callout`. This component is based on the `div` element. See the [**icon** component for all icons that are available.](/docs/library/radix/datadisplay/icon)

The `callout_text` renders the callout text. This component is based on the `p` element.


## As alert


```python demo
rdxt.callout_root(
    rdxt.callout_icon(rdxt.icon(tag="exclamation_triangle")),
    rdxt.callout_text("Access denied. Please contact the network administrator to view this page."),
    color_scheme="red",
    role="alert",
)
```






## Style



### Size

Use the `size` prop to control the size.

```python demo
rdxt.flex(
    rdxt.callout_root(
        rdxt.callout_icon(rdxt.icon(tag="info_circled")),
        rdxt.callout_text("You will need admin privileges to install and access this application."),
        size="3",
    ),
    rdxt.callout_root(
        rdxt.callout_icon(rdxt.icon(tag="info_circled")),
        rdxt.callout_text("You will need admin privileges to install and access this application."),
        size="2",
    ),
    rdxt.callout_root(
        rdxt.callout_icon(rdxt.icon(tag="info_circled")),
        rdxt.callout_text("You will need admin privileges to install and access this application."),
        size="1",
    ),
    direction="column",
    gap="3",
    align="start",
)
```

### Variant 

Use the `variant` prop to control the visual style. It is set to `soft` by default.

```python demo
rdxt.flex(
    rdxt.callout_root(
        rdxt.callout_icon(rdxt.icon(tag="info_circled")),
        rdxt.callout_text("You will need admin privileges to install and access this application."),
        variant="soft",
    ),
    rdxt.callout_root(
        rdxt.callout_icon(rdxt.icon(tag="info_circled")),
        rdxt.callout_text("You will need admin privileges to install and access this application."),
        variant="surface",
    ),
    rdxt.callout_root(
        rdxt.callout_icon(rdxt.icon(tag="info_circled")),
        rdxt.callout_text("You will need admin privileges to install and access this application."),
        variant="outline",
    ),
    direction="column",
    gap="3",
)
```


### Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.


```python demo
rdxt.flex(
    rdxt.callout_root(
        rdxt.callout_icon(rdxt.icon(tag="info_circled")),
        rdxt.callout_text("You will need admin privileges to install and access this application."),
        color_scheme="blue",
    ),
    rdxt.callout_root(
        rdxt.callout_icon(rdxt.icon(tag="info_circled")),
        rdxt.callout_text("You will need admin privileges to install and access this application."),
        color_scheme="green",
    ),
    rdxt.callout_root(
        rdxt.callout_icon(rdxt.icon(tag="info_circled")),
        rdxt.callout_text("You will need admin privileges to install and access this application."),
        color_scheme="red",
    ),
    direction="column",
    gap="3",
)
```




### High Contrast

Use the `high_contrast` prop to add additional contrast.


```python demo
rdxt.flex(
    rdxt.callout_root(
        rdxt.callout_icon(rdxt.icon(tag="info_circled")),
        rdxt.callout_text("You will need admin privileges to install and access this application."),
    ),
    rdxt.callout_root(
        rdxt.callout_icon(rdxt.icon(tag="info_circled")),
        rdxt.callout_text("You will need admin privileges to install and access this application."),
        high_contrast=True,
    ),
    direction="column",
    gap="3",
)
```
