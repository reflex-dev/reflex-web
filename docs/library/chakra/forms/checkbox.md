---
components:
    - rx.chakra.Checkbox
---

# Checkbox

A checkbox is a common way to toggle boolean value.
The checkbox component can be used on its own or in a group.

```python exec
import reflex as rx
```

```python demo
rx.checkbox("Check Me!")
```

Checkboxes can range in size and styles.

```python demo
rx.hstack(
    rx.checkbox("Example", color_scheme="green", size="sm"),
    rx.checkbox("Example", color_scheme="blue", size="sm"),
    rx.checkbox("Example", color_scheme="yellow", size="md"),
    rx.checkbox("Example", color_scheme="orange", size="md"),
    rx.checkbox("Example", color_scheme="red", size="lg"),
)
```

Checkboxes can also have different visual states.

```python demo
rx.hstack(
    rx.checkbox(
        "Example", color_scheme="green", size="lg", is_invalid=True
    ),
    rx.checkbox(
        "Example", color_scheme="green", size="lg", is_disabled=True
    ),
)
```

Checkboxes can be hooked up to a state using the `on_change` prop.

```python demo exec
import reflex as rx


class CheckboxState(rx.State):
    checked: bool = False

    def toggle(self):
        self.checked = not self.checked


def checkbox_state_example():
    return rx.hstack(
        rx.cond(
            CheckboxState.checked,
            rx.text("Checked", color="green"),
            rx.text("Unchecked", color="red"),
        ),
        rx.checkbox(
            "Example",
            on_change=CheckboxState.set_checked,
        )
    )
```

## Checkbox Group

You can group checkboxes together using checkbox group.

```python demo
rx.checkbox_group(
    rx.checkbox("Example", color_scheme="green"),
    rx.checkbox("Example", color_scheme="blue"),
    rx.checkbox("Example", color_scheme="yellow"),
    rx.checkbox("Example", color_scheme="orange"),
    rx.checkbox("Example", color_scheme="red"),
    space="1em",
)
```
