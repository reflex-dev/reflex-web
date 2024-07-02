```python exec
import reflex as rx
```

# Responsive

Reflex apps can be made responsive to look good on mobile, tablet, and desktop.

You can pass a list of values to any style property to specify its value on different screen sizes.

```python demo
rx.text(
    "Hello World",
    color=["orange", "red", "purple", "blue", "green"],
)
```

The text will change color based on your screen size. If you are on desktop, try changing the size of your browser window to see the color change.

You can also use `rx.breakpoints`. Each size maps to a corresponding key, the value of each will be applied when the screen size is greater than or equal to the named breakpoint.

```python demo
rx.text(
    "Hello World",
    color=rx.breakpoints(
        initial="orange",
        sm="purple",
        lg="green",
    ),
)
```

You can also specify custom values per component using a dictionary instead of named parameters.

```python
rx.text(
    "Hello World",
    color=rx.breakpoints({
        "0px": "orange",
        "48em": "purple",
        "80em": "green",
    }),
)
```

For the Radix UI components' fields that supports responsive value, you can also use `rx.breakpoints` (note that custom breakpoints and list syntax aren't supported).

```python demo
rx.grid(
    rx.foreach(
        list(range(6)),
        lambda _: rx.box(bg_color="#a7db76", height="100px", width="100px")
    ),
    columns=rx.breakpoints(
        initial="2",
        sm="4",
        lg="6"
    ),
    spacing="4"
)
```

## Setting Defaults

The default breakpoints are shown below.

```python eval
rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell("Size"),
            rx.table.column_header_cell("Width"),
        ),
    ),
    rx.table.body(
        rx.table.row(
            rx.table.cell("initial"),
            rx.table.cell("0px"),
        ),
        rx.table.row(
            rx.table.cell("xs"),
            rx.table.cell("30em"),
        ),
        rx.table.row(
            rx.table.cell("sm"),
            rx.table.cell("48em"),
        ),
        rx.table.row(
            rx.table.cell("md"),
            rx.table.cell("62em"),
        ),
        rx.table.row(
            rx.table.cell("lg"),
            rx.table.cell("80em"),
        ),
        rx.table.row(
            rx.table.cell("xl"),
            rx.table.cell("96em"),
        ),
    ),
)
```

You can cusomize them using the style property.

```python
app = rx.App(style=\{"breakpoints": ["520px", "768px", "1024px", "1280px", "1640px"]\})
```

## Showing Components Based on Display

A common use case for responsive is to show different components based on the screen size.

Reflex provides useful helper components for this.

```python demo
rx.vstack(
    rx.desktop_only(
        rx.text("Desktop View"),
    ),
    rx.tablet_only(
        rx.text("Tablet View"),
    ),
    rx.mobile_only(
        rx.text("Mobile View"),
    ),
    rx.mobile_and_tablet(
        rx.text("Visible on Mobile and Tablet"),
    ),
    rx.tablet_and_desktop(
        rx.text("Visible on Desktop and Tablet"),
    ),
)
```

## Specifying Display Breakpoints

You can specify the breakpoints to use for the responsive components by using the `display` style property.

```python demo
rx.vstack(
    rx.text(
        "Hello World",
        color="green",
        display=["none", "none", "none", "none", "flex"],
    ),
    rx.text(
        "Hello World",
        color="blue",
        display=["none", "none", "none", "flex", "flex"],
    ),
    rx.text(
        "Hello World",
        color="red",
        display=["none", "none", "flex", "flex", "flex"],
    ),
    rx.text(
        "Hello World",
        color="orange",
        display=["none", "flex", "flex", "flex", "flex"],
    ),
    rx.text(
        "Hello World",
        color="yellow",
        display=["flex", "flex", "flex", "flex", "flex"],
    ),
)
```
