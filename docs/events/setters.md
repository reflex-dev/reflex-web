```python exec
import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo_from
```


# Setters

Every base var has a built-in event handler to set it's value for convenience, called `set_VARNAME`.


Say you wanted to change the value of the select component. You could write your own event handler to do this:

```python exec

options: list[str] = ["1", "2", "3", "4"]
class SetterState1(State):
    selected: str = "1"

    def change(self, value):
        self.selected = value


def code_setter():
    return rx.vstack(
        rx.badge(SetterState1.selected, color_scheme="green"),
        rx.select(
            options,
            on_change= lambda value: SetterState1.change(value),
        )
    )

```

```python eval
docdemo_from(SetterState1, component=code_setter)
```


Or you could could use a built-in setter for conciseness.

```python exec

options: list[str] = ["1", "2", "3", "4"]
class SetterState2(State):
    selected: str = "1"

def code_setter_2():
    return rx.vstack(
        rx.badge(SetterState2.selected, color_scheme="green"),
        rx.select(
            options,
            on_change= SetterState2.set_selected,
        )
    )
```

```python eval
docdemo_from(SetterState2, component=code_setter_2)
```

In this example, the setter for `selected` is `set_selected`. Both of these examples are equivalent.

Setters are a great way to make your code more concise. But if you want to do something more complicated, you can always write your own function in the state.
