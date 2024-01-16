---
components:
    - rx.radix.themes.Button
---


```python exec
import reflex as rx
import reflex.components.radix.themes as rdxt
from pcweb.templates.docpage import style_grid, docdemo_from
```

 
# Button

Buttons are essential elements in your application's user interface that users can click to trigger events. This component uses Radix's [button](https://radix-ui.com/primitives/docs/components/button) component. 

## Basic Example

```python demo
rdxt.button("Click me")
```

### With Icon

```python demo
rdxt.button(
    rdxt.icon(tag="heart"),
    "Like",
    color_scheme="red",
)
```

## Props

### Disabled

The `disabled` prop disables the button, by default it is `False`.

```python demo
rx.hstack(
    rdxt.button("Enabled"),
    rdxt.button("Disabled", disabled=True),
)
```

## Triggers

### On Click

The `on_click` trigger is called when the button is clicked.

```python demo
rdxt.button("Click me", on_click=rx.window_alert("Clicked!"))
```

## Styling

### Variants

The `variant` prop changes the appearance of the button. The default variant is `classic`.

```python eval
style_grid(component_used=rdxt.button, component_used_str="button", variants=["classic", "solid", "soft", "surface", "outline", "ghost"], components_passed="Next", disabled=True)
```

### Radius

The `radius` prop changes the border radius of the button. The default radius is `medium`.

```python demo
rx.hstack(
    rdxt.button("None", radius="none"),
    rdxt.button("Small", radius="small"),
    rdxt.button("Medium", radius="medium"),
    rdxt.button("Large", radius="large"),
    rdxt.button("Full", radius="full"),
)
```

### Size

The `size` prop changes the size of the button. The default size is `2`.

```python demo
rx.hstack(
    rdxt.button("Small", size="1"),
    rdxt.button("Medium", size="2"),
    rdxt.button("Large", size="3"),
    rdxt.button("XLarge", size="4"),
)
```


## Real World Example

```python exec
class CountState(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

def counter():
    return rx.hstack(
        rdxt.button(
            "Decrement",
            color_scheme="red",
            on_click=CountState.decrement,
        ),
        rx.heading(
            CountState.count,
            font_size="2em",
            padding_x="0.5em",
        ),
        rdxt.button(
            "Increment",
            color_scheme="grass",
            on_click=CountState.increment,
        ),
    )

```



```python eval
docdemo_from(
    CountState,
    component=counter,
)
```