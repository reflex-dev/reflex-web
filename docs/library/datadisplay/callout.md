---
components:
    - rx.radix.callout
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
rdx.callout("You will need admin privileges to install and access this application.", icon="info_circled")
```

The `icon` prop allows an icon to be passed to the `callout` component. See the [**icon** component for all icons that are available.](/docs/library/radix/datadisplay/icon)

## As alert

```python demo
rdx.callout("Access denied. Please contact the network administrator to view this page.", icon="exclamation_triangle", color_scheme="red", role="alert")
```


## Style


### Size

Use the `size` prop to control the size.

```python demo
rdx.flex(
    rdx.callout("You will need admin privileges to install and access this application.", icon="info_circled", size="3",),
    rdx.callout("You will need admin privileges to install and access this application.", icon="info_circled", size="2",),
    rdx.callout("You will need admin privileges to install and access this application.", icon="info_circled", size="1",),
    direction="column",
    gap="3",
    align="start",
)
```

### Variant 

Use the `variant` prop to control the visual style. It is set to `soft` by default.

```python demo
rdx.flex(
    rdx.callout("You will need admin privileges to install and access this application.", icon="info_circled", variant="soft",),
    rdx.callout("You will need admin privileges to install and access this application.", icon="info_circled", variant="surface",),
    rdx.callout("You will need admin privileges to install and access this application.", icon="info_circled", variant="outline",),
    direction="column",
    gap="3",
)
```

### Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.


```python demo
rdx.flex(
    rdx.callout("You will need admin privileges to install and access this application.", icon="info_circled", color_scheme="blue",),
    rdx.callout("You will need admin privileges to install and access this application.", icon="info_circled", color_scheme="green",),
    rdx.callout("You will need admin privileges to install and access this application.", icon="info_circled", color_scheme="red",),
    direction="column",
    gap="3",
)
```


### High Contrast

Use the `high_contrast` prop to add additional contrast.


```python demo
rdx.flex(
    rdx.callout("You will need admin privileges to install and access this application.", icon="info_circled",),
    rdx.callout("You will need admin privileges to install and access this application.", icon="info_circled", high_contrast=True,),
    direction="column",
    gap="3",
)
```

