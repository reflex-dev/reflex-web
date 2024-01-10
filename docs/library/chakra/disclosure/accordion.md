---
components:
    - rx.chakra.Accordion
    - rx.chakra.AccordionItem
    - rx.chakra.AccordionButton
    - rx.chakra.AccordionPanel
    - rx.chakra.AccordionIcon
---

```python exec
import reflex as rx
```

# Accordion

Accordions allow you to hide and show content in a container under a header.

Accordion consist of an outer accordion component and inner accordion items.
Each item has a optional button and panel. The button is used to toggle the panel's visibility.

```python demo
rx.accordion(
    rx.accordion_item(
        rx.accordion_button(
            rx.heading("Example"),
            rx.accordion_icon(),
        ),
        rx.accordion_panel(
            rx.text("This is an example of an accordion component.")
        )
    ),
    allow_toggle = True,
    width = "100%"
)
```

An accordion can have multiple items.

```python demo
rx.accordion(
    rx.accordion_item(
        rx.accordion_button(
            rx.heading("Example 1"),
            rx.accordion_icon(),
        ),
        rx.accordion_panel(
            rx.text("This is an example of an accordion component.")
        ),
    ),
    rx.accordion_item(
        rx.accordion_button(
            rx.heading("Example 2"),
            rx.accordion_icon(),
        ),
        rx.accordion_panel(
            rx.text("This is an example of an accordion component.")
        ),
    ),
    allow_multiple = True,
    bg="black",
    color="white",
    width = "100%"
)
```

You can create multilevel accordions by nesting accordions within the outer accordion panel.

```python demo
rx.accordion(
    rx.accordion_item(
        rx.accordion_button(
            rx.accordion_icon(),
            rx.heading("Outer"),
            
        ),
        rx.accordion_panel(
            rx.accordion(
            rx.accordion_item(
                rx.accordion_button(
                    rx.accordion_icon(),
                    rx.heading("Inner"),    
                ),
                rx.accordion_panel(
                    rx.badge("Inner Panel", variant="solid", color_scheme="green"),
                )
            )
            ),
        )  
    ),
    width = "100%"
)
```

You can also create an accordion using the shorthand syntax.
Pass a list of tuples to the `items` prop.
Each tuple should contain a label and a panel.

```python demo
rx.accordion(
   items=[("Label 1", rx.center("Panel 1")), ("Label 2", rx.center("Panel 2"))],
   width="100%"
)
```