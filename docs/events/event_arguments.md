```python exec
import reflex as rx
```

# Event Arguments

In some use cases, you want to pass additional arguments to your event handlers. To do this you can bind an event trigger to a lambda, which can call your event handler with the arguments you want.

Try typing a color in an input below and clicking away from it to change the color of the input.

```python demo exec
class ArgState(rx.State):
    colors: list[str] = ["rgba(245,168,152)", "MediumSeaGreen", "#DEADE3"]

    def change_color(self, color: str, index: int):
        self.colors[index] = color

def event_arguments_example():
    return rx.hstack(
        rx.input(default_value=ArgState.colors[0], on_blur=lambda c: ArgState.change_color(c, 0), bg=ArgState.colors[0]),
        rx.input(default_value=ArgState.colors[1], on_blur=lambda c: ArgState.change_color(c, 1), bg=ArgState.colors[1]),
        rx.input(default_value=ArgState.colors[2], on_blur=lambda c: ArgState.change_color(c, 2), bg=ArgState.colors[2]),
    )

```

In this case, in we want to pass two arguments to the event handler `change_color`, the color and the index of the color to change.

The `on_blur` event trigger passes the text of the input as an argument to the lambda, and the lambda calls the `change_color` event handler with the text and the index of the input.

```md alert warning
# Event Handler Parameters should provide type annotations.
Like state vars, be sure to provide the right type annotations for the parameters in an event handler.
```

## Events with Partial Arguments

_Added in v0.5.0_

Event arguments in Reflex are passed positionally. Any additional arguments not
passed to an EventHandler will be filled in by the event trigger when it is
fired.

The following two code samples are equivalent:

```python
# Use a lambda to pass event trigger args to the EventHandler.
rx.text(on_blur=lambda v: MyState.handle_update("field1", v))

# Create a partial that passes event trigger args for any args not provided to the EventHandler.
rx.text(on_blur=MyState.handle_update("field1"))
```