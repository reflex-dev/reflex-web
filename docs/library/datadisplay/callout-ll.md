---
components:
    - rx.radix.callout.root
    - rx.radix.callout.icon
    - rx.radix.callout.text
---


```python exec
import reflex as rx
rdx = rx.radix
```

# Callout

A `callout` is a short message to attract user's attention.


```python demo
rdx.callout.root(
    rdx.callout.icon(rdx.icon(tag="info_circled")),
    rdx.callout.text("You will need admin privileges to install and access this application."),
)
```

The `callout` component is made up of a `callout_root`, which groups `callout_icon` and `callout_text` parts. This component is based on the `div` element and supports common margin props.

The `callout_icon` provides width and height for the `icon` associated with the `callout`. This component is based on the `div` element. See the [**icon** component for all icons that are available.](/docs/library/radix/datadisplay/icon)

The `callout_text` renders the callout text. This component is based on the `p` element.


## As alert


```python demo
rdx.callout.root(
    rdx.callout.icon(rdx.icon(tag="exclamation_triangle")),
    rdx.callout.text("Access denied. Please contact the network administrator to view this page."),
    color_scheme="red",
    role="alert",
)
```






## Style



### Size

Use the `size` prop to control the size.

```python demo
rdx.flex(
    rdx.callout.root(
        rdx.callout.icon(rdx.icon(tag="info_circled")),
        rdx.callout.text("You will need admin privileges to install and access this application."),
        size="3",
    ),
    rdx.callout.root(
        rdx.callout.icon(rdx.icon(tag="info_circled")),
        rdx.callout.text("You will need admin privileges to install and access this application."),
        size="2",
    ),
    rdx.callout.root(
        rdx.callout.icon(rdx.icon(tag="info_circled")),
        rdx.callout.text("You will need admin privileges to install and access this application."),
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
rdx.flex(
    rdx.callout.root(
        rdx.callout.icon(rdx.icon(tag="info_circled")),
        rdx.callout.text("You will need admin privileges to install and access this application."),
        variant="soft",
    ),
    rdx.callout.root(
        rdx.callout.icon(rdx.icon(tag="info_circled")),
        rdx.callout.text("You will need admin privileges to install and access this application."),
        variant="surface",
    ),
    rdx.callout.root(
        rdx.callout.icon(rdx.icon(tag="info_circled")),
        rdx.callout.text("You will need admin privileges to install and access this application."),
        variant="outline",
    ),
    direction="column",
    gap="3",
)
```


### Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.


```python demo
rdx.flex(
    rdx.callout.root(
        rdx.callout.icon(rdx.icon(tag="info_circled")),
        rdx.callout.text("You will need admin privileges to install and access this application."),
        color_scheme="blue",
    ),
    rdx.callout.root(
        rdx.callout.icon(rdx.icon(tag="info_circled")),
        rdx.callout.text("You will need admin privileges to install and access this application."),
        color_scheme="green",
    ),
    rdx.callout.root(
        rdx.callout.icon(rdx.icon(tag="info_circled")),
        rdx.callout.text("You will need admin privileges to install and access this application."),
        color_scheme="red",
    ),
    direction="column",
    gap="3",
)
```




### High Contrast

Use the `high_contrast` prop to add additional contrast.


```python demo
rdx.flex(
    rdx.callout.root(
        rdx.callout.icon(rdx.icon(tag="info_circled")),
        rdx.callout.text("You will need admin privileges to install and access this application."),
    ),
    rdx.callout.root(
        rdx.callout.icon(rdx.icon(tag="info_circled")),
        rdx.callout.text("You will need admin privileges to install and access this application."),
        high_contrast=True,
    ),
    direction="column",
    gap="3",
)
```
