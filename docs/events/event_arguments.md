```python exec
import reflex as rx

from pcweb.templates.docpage import docdemo_from
```


# Event Arguments


In some use cases, you want to pass additional arguments to your event handlers. To do this you can bind an event trigger to a lambda, which can call your event handler with the arguments you want.

Try typing a color in an input below and clicking away from it to change the color of the input.


```python exec
class ArgState(rx.State):
    colors: list[str] = ["rgba(222,44,12)", "white", "#007ac2"]

    def change_color(self, color: str, index: int):
        self.colors[index] = color

def event_arguments_example():
    return rx.hstack(
        rx.input(default_value=ArgState.colors[0], on_blur=lambda c: ArgState.change_color(c, 0), bg=ArgState.colors[0]),
        rx.input(default_value=ArgState.colors[1], on_blur=lambda c: ArgState.change_color(c, 1), bg=ArgState.colors[1]),
        rx.input(default_value=ArgState.colors[2], on_blur=lambda c: ArgState.change_color(c, 2), bg=ArgState.colors[2]),
    )

```

```python eval
docdemo_from(ArgState, component=event_arguments_example)
```

In this case, in we want to pass two arguments to the event handler `change_color`, the color and the index of the color to change.

The `on_blur` event trigger passes the text of the input as an argument to the lambda, and the lambda calls the `change_color` event handler with the text and the index of the input.

```python eval
rx.alert(
    rx.alert_icon(),
    rx.box(
        rx.alert_title(
            "Event Handler Parameters should provide type annotations."
        ),
        rx.alert_description(
            "Like state vars, be sure to provide the right type annotations for the prameters in an event "
            "handler."
        ),
    ),
    status="warning",
)
```