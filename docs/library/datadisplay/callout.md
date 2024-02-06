---
components:
    - rx.radix.callout
    - rx.radix.callout.root
    - rx.radix.callout.icon
    - rx.radix.callout.text
---


```python exec
import reflex as rx
```

# Callout

A `callout` is a short message to attract user's attention.

```python demo
rx.callout("You will need admin privileges to install and access this application.", icon="info_circled")
```

The `icon` prop allows an icon to be passed to the `callout` component. See the [**icon** component for all icons that are available.](/docs/library/radix/datadisplay/icon)

## As alert

```python demo
rx.callout("Access denied. Please contact the network administrator to view this page.", icon="exclamation_triangle", color_scheme="red", role="alert")
```


## Style


### Size

Use the `size` prop to control the size.

```python demo
rx.flex(
    rx.callout("You will need admin privileges to install and access this application.", icon="info_circled", size="3",),
    rx.callout("You will need admin privileges to install and access this application.", icon="info_circled", size="2",),
    rx.callout("You will need admin privileges to install and access this application.", icon="info_circled", size="1",),
    direction="column",
    gap="3",
    align="start",
)
```

### Variant 

Use the `variant` prop to control the visual style. It is set to `soft` by default.

```python demo
rx.flex(
    rx.callout("You will need admin privileges to install and access this application.", icon="info_circled", variant="soft",),
    rx.callout("You will need admin privileges to install and access this application.", icon="info_circled", variant="surface",),
    rx.callout("You will need admin privileges to install and access this application.", icon="info_circled", variant="outline",),
    direction="column",
    gap="3",
)
```

### Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.


```python demo
rx.flex(
    rx.callout("You will need admin privileges to install and access this application.", icon="info_circled", color_scheme="blue",),
    rx.callout("You will need admin privileges to install and access this application.", icon="info_circled", color_scheme="green",),
    rx.callout("You will need admin privileges to install and access this application.", icon="info_circled", color_scheme="red",),
    direction="column",
    gap="3",
)
```


### High Contrast

Use the `high_contrast` prop to add additional contrast.


```python demo
rx.flex(
    rx.callout("You will need admin privileges to install and access this application.", icon="info_circled",),
    rx.callout("You will need admin privileges to install and access this application.", icon="info_circled", high_contrast=True,),
    direction="column",
    gap="3",
)
```

