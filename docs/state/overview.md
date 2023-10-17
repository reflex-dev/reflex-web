```python exec
import reflex as rx
from pcweb.templates.docpage import definition
```

# State

State allows us to create interactive apps that can respond to user input. It defines the variables that can change over time, and the functions that can modify them.

## State Basics

The base state is defined as a class that inherits from `rx.State`.

```python
import reflex as rx


class State(rx.State):
    """Define your app state here."""
```

State is made up of two parts: vars and event handlers.

**Vars** are variables in your app that can change over time. 
**Event handlers** are functions that modify these vars in response to events.

These are the main concepts to understand how state works in Reflex:

```python eval
rx.responsive_grid(
    definition(
        "Base Var",
        rx.unordered_list(
            rx.list_item("Any variable in your app that can change over time."),
            rx.list_item(
                "Defined as a field in the ", rx.code("State"), " class"
            ),
            rx.list_item("Can only be modified by event handlers."),
        ),
    ),
    definition(
        "Computed Var",
        rx.unordered_list(
            rx.list_item("Vars that change automatically based on other vars."),
            rx.list_item(
                "Defined as functions using the ",
                rx.code("@rx.var"),
                " decorator.",
            ),
            rx.list_item(
                "Cannot be set by event handlers, are always recomputed when the state changes."
            ),
        ),
    ),
    definition(
        "Event Trigger",
        rx.unordered_list(
            rx.list_item(
                "A user interaction that triggers an event, such as a button click."
            ),
            rx.list_item(
                "Defined as special component props, such as ",
                rx.code("on_click"),
                ".",
            ),
            rx.list_item("Can be used to trigger event handlers."),
        ),
    ),
    definition(
        "Event Handlers",
        rx.unordered_list(
            rx.list_item(
                "Functions that update the state in response to events."
            ),
            rx.list_item(
                "Defined as methods in the ", rx.code("State"), " class."
            ),
            rx.list_item(
                "Can be called by event triggers, or by other event handlers."
            ),
        ),
    ),
    margin_bottom="1em",
    spacing="1em",
    columns=[1, 1, 2, 2, 2],
)
```




