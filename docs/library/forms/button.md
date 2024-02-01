---
components:
    - rx.radix.button
---


```python exec
import reflex as rx
rdx = rx.radix
```

 
# Button

Buttons are essential elements in your application's user interface that users can click to trigger events. This component uses Radix's [button](https://radix-ui.com/primitives/docs/components/button) component. 

## Basic Example

```python demo
rdx.button("Click me")
```

### With Icon

```python demo
rdx.button(
    rdx.icon(tag="heart"),
    "Like",
    color_scheme="red",
)
```

## Props

### Disabled

The `disabled` prop disables the button, by default it is `False`.  A disabled button does not respond to user interactions such as click and cannot be focused.

```python demo
rdx.flex(
    rdx.button("Enabled"),
    rdx.button("Disabled", disabled=True),
    gap="2",
)
```

## Triggers

### On Click

The `on_click` trigger is called when the button is clicked.

```python demo
rdx.button("Click me", on_click=rx.window_alert("Clicked!"))
```

## Real World Example

```python demo exec
class CountState(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

def counter():
    return rdx.flex(
        rdx.button(
            "Decrement",
            color_scheme="red",
            on_click=CountState.decrement,
        ),
        rdx.heading(CountState.count),
        rdx.button(
            "Increment",
            color_scheme="grass",
            on_click=CountState.increment,
        ),
        gap="3",
    )
```