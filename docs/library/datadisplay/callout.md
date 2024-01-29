---
components:
    - rx.radix.themes.Callout
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
rdxt.callout("You will need admin privileges to install and access this application.", icon="info_circled")
```

The `icon` prop allows an icon to be passed to the `callout` component. See the [**icon** component for all icons that are available.](/docs/library/radix/datadisplay/icon)

## As alert

```python demo
rdxt.callout("Access denied. Please contact the network administrator to view this page.", icon="exclamation_triangle", color_scheme="red", role="alert")
```


## Style


### Size

Use the `size` prop to control the size.

```python demo
rdxt.flex(
    rdxt.callout("You will need admin privileges to install and access this application.", icon="info_circled", size="3",),
    rdxt.callout("You will need admin privileges to install and access this application.", icon="info_circled", size="2",),
    rdxt.callout("You will need admin privileges to install and access this application.", icon="info_circled", size="1",),
    direction="column",
    gap="3",
    align="start",
)
```

### Variant 

Use the `variant` prop to control the visual style. It is set to `soft` by default.

```python demo
rdxt.flex(
    rdxt.callout("You will need admin privileges to install and access this application.", icon="info_circled", variant="soft",),
    rdxt.callout("You will need admin privileges to install and access this application.", icon="info_circled", variant="surface",),
    rdxt.callout("You will need admin privileges to install and access this application.", icon="info_circled", variant="outline",),
    direction="column",
    gap="3",
)
```

### Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.


```python demo
rdxt.flex(
    rdxt.callout("You will need admin privileges to install and access this application.", icon="info_circled", color_scheme="blue",),
    rdxt.callout("You will need admin privileges to install and access this application.", icon="info_circled", color_scheme="green",),
    rdxt.callout("You will need admin privileges to install and access this application.", icon="info_circled", color_scheme="red",),
    direction="column",
    gap="3",
)
```


### High Contrast

Use the `high_contrast` prop to add additional contrast.


```python demo
rdxt.flex(
    rdxt.callout("You will need admin privileges to install and access this application.", icon="info_circled",),
    rdxt.callout("You will need admin privileges to install and access this application.", icon="info_circled", high_contrast=True,),
    direction="column",
    gap="3",
)
```

