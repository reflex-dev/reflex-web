---
components:
    - rx.chakra.Popover
    - rx.chakra.PopoverTrigger
    - rx.chakra.PopoverContent
    - rx.chakra.PopoverHeader
    - rx.chakra.PopoverBody
    - rx.chakra.PopoverFooter
    - rx.chakra.PopoverArrow
    - rx.chakra.PopoverAnchor
---

```python exec
import reflex as rx
```

# Popover

Popover is a non-modal dialog that floats around a trigger.
It is used to display contextual information to the user, and should be paired with a clickable trigger element.

```python demo
rx.popover(
    rx.popover_trigger(rx.button("Popover Example")),
    rx.popover_content(
        rx.popover_header("Confirm"),
        rx.popover_body("Do you want to confirm example?"),
        rx.popover_footer(rx.text("Footer text.")),
        rx.popover_close_button(),
    ),
)
```