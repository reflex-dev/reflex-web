```python exec
import random

import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo_from, doclink
```

# Var Operations

Var operations transform the placeholder representation of the value on the
frontend and provide a way to perform basic operations on the Var without having
to define a computed var.

Within your frontend components, you cannot use arbitrary Python functions on
the state vars. For example, the following code will **not work.**

```python
class State(rx.State):
    number: int

def index():
    # This will be compiled before runtime, before `State.number` has a known value.
    # Since `float` is not a valid var operation, this will throw an error.
    rx.text(float(State.number))
```
This is because we compile the frontend to Javascript, but the value of `State.number`
is only known at runtime.

```python exec
coins = ["BTC", "ETH", "LTC", "DOGE"]

class VarSelectState(State):
    selected: str = "DOGE"

def var_operations_example():
    return rx.vstack(
        # Using a var operation to concatenate a string with a var.
        rx.heading("I just bought a bunch of " + VarSelectState.selected),
        # Using an f-string to interpolate a var.
        rx.text(f"{VarSelectState.selected} is going to the moon!"),
        rx.select(
            coins,
            value=VarSelectState.selected,
            on_change=VarSelectState.set_selected,
        )
    )
```

```python eval
docdemo_from(VarSelectState, component=var_operations_example, assignments={"coins": coins})
```

```python eval
rx.alert(
    rx.alert_icon(),
    rx.box(
        rx.alert_title("Vars support many common operations."),
        rx.alert_description(
            "They can be used for arithemtic, string concatenation, inequalities, indexing, and more. "
            "See the ",
            doclink(
                "full list of supported operations",
                "/docs/api-reference/var",
            ),
            ".",
        ),
    ),
    status="success",
    margin_bottom="3em",
)
```

You can also combine multiple var operations together, as seen in the next example.

```python exec
import random

class VarNumberState(State):
    number: int

    def update(self):
        self.number = random.randint(0, 100)

def var_number_example():
    return rx.vstack(
        rx.heading(f"The number is {VarNumberState.number}"),
        # Var operations can be composed for more complex expressions.
        rx.cond(
            VarNumberState.number % 2 == 0,
            rx.text("Even", color="green"),
            rx.text("Odd", color="red"),
        ),
        rx.button("Update", on_click=VarNumberState.update),
    )
```

```python eval
docdemo_from(VarNumberState, component=var_number_example, imports=["import random"])
```

We could have made a computed var that returns the parity of `number`, but
it can be simpler just to use a var operation instead.

Var operations may be generally chained to make compound expressions, however
some complex transformations not supported by var operations must use computed vars
to calculate the value on the backend.