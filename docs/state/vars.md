```python exec
import inspect
import random
import time

import numpy as np

import reflex as rx

from pcweb.base_state import State
from pcweb.pages.docs.advanced_guide.custom_vars import custom_vars
from pcweb.templates.docpage import (
    doccode,
    docdemo_from,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader,
)
```

# Vars

Vars are any fields in your app that may change over time. A Var is directly
rendered into the frontend of the app.

## Base Vars

Base vars are defined as fields in your State class.

They can have a preset default value. If you don't provide a default value, you
must provide a type annotation.

```python eval
rx.alert(
    rx.alert_icon(),
    rx.box(
        rx.alert_title("State Vars should provide type annotations."),
        rx.alert_description(
            "Reflex relies on type annotations to determine the type of state vars during the "
            "compilation process. ",
            ".",
        ),
    ),
    status="warning",
    margin_bottom="3em",
)
```

```python exec
class TickerState(State):
    ticker: str ="AAPL"
    price: str = "$150"


def ticker_example():
    return rx.stat_group(
        rx.stat(
            rx.stat_label(TickerState.ticker),
            rx.stat_number(TickerState.price),
            rx.stat_help_text(
                rx.stat_arrow(type_="increase"),
                "4%",
            ),
        ),
    )
```

```python eval
docdemo_from(TickerState, component=ticker_example)
```

In this example `ticker` and `price` are base vars in the app, which can be modified at runtime.

```python eval
rx.alert(
    rx.alert_icon(),
    rx.box(
        rx.alert_title("Vars must be JSON serializable."),
        rx.alert_description(
            "Vars are used to communicate between the frontend and backend. ",
            "They must be primitive Python types, ",
            "Plotly figures, Pandas dataframes, or ",
            doclink("a custom defined type", custom_vars.path),
            ".",
        ),
    ),
    status="warning",
)
```

## Computed Vars

Computed vars have values derived from other properties on the backend. They are
defined as methods in your State class with the `@rx.var` decorator. A computed
var is recomputed whenever an event is processed against the state.

Try typing in the input box and clicking out.

```python exec
class UppercaseState(State):
    text: str = "hello"

    @rx.var
    def upper_text(self) -> str:
        # This will be recomputed whenever `text` changes.
        return self.text.upper()


def uppercase_example():
    return rx.vstack(
        rx.heading(UppercaseState.upper_text),
        rx.input(on_blur=UppercaseState.set_text, placeholder="Type here..."),
    )
```

```python eval
docdemo_from(UppercaseState, component=uppercase_example)
```

Here, `upper_text` is a computed var that always holds the upper case version of `text`.

We recommend always using type annotations for computed vars.

### Cached Vars

A cached var, decorated as `@rx.cached_var` is a special type of computed var
that is only recomputed when the other state vars it depends on change. This is
useful for expensive computations, but in some cases it may not update when you
expect it to.

```python exec
class CachedVarState(State):
    counter_a: int = 0
    counter_b: int = 0

    @rx.var
    def last_touch_time(self) -> str:
        # This is updated anytime the state is updated.
        return time.strftime("%H:%M:%S")

    def increment_a(self):
        self.counter_a += 1

    @rx.cached_var
    def last_counter_a_update(self) -> str:
        # This is updated only when `counter_a` changes.
        return f"{self.counter_a} at {time.strftime('%H:%M:%S')}"

    def increment_b(self):
        self.counter_b += 1

    @rx.cached_var
    def last_counter_b_update(self) -> str:
        # This is updated only when `counter_b` changes.
        return f"{self.counter_b} at {time.strftime('%H:%M:%S')}"


def cached_var_example():
    return rx.vstack(
        rx.text(f"State touched at: {CachedVarState.last_touch_time}"),
        rx.text(f"Counter A: {CachedVarState.last_counter_a_update}"),
        rx.text(f"Counter B: {CachedVarState.last_counter_b_update}"),
        rx.hstack(
            rx.button("Increment A", on_click=CachedVarState.increment_a),
            rx.button("Increment B", on_click=CachedVarState.increment_b),
        ),
    )
```

```python eval
docdemo_from(CachedVarState, component=cached_var_example)
```

In this example `last_touch_time` is a normal computed var, which updates any
time the state is modified. `last_counter_a_update` is a computed var that only
depends on `counter_a`, so it only gets recomputed when `counter_a` has changes.
Similarly `last_counter_b_update` only depends on `counter_b`, and thus is
updated only when `counter_b` changes.

## Client-storage Vars

You can use the browser's local storage to persist state between sessions. 
This allows user preferences, authentication cookies, other bits of information
to be stored on the client and accessed from different browser tabs.

A client-side storage var looks and acts like a normal `str` var, except the
default value is either `rx.Cookie` or `rx.LocalStorage` depending on where the
value should be stored.  The key name will be based on the var name, but this
can be overridden by passing `name="my_custom_name"` as a keyword argument.

For more information see [Browser Storage](/docs/api-reference/browser/).

Try entering some values in the text boxes below and then load the page in a separate 
tab or check the storage section of browser devtools to see the values saved in the browser. 

```python exec
class ClientStorageState(State):
    my_cookie: str = rx.Cookie("")
    my_local_storage: str = rx.LocalStorage("")
    custom_cookie: str = rx.Cookie(name="CustomNamedCookie", max_age=3600)


def client_storage_example():
    return rx.vstack(
        rx.hstack(rx.text("my_cookie"), rx.input(value=ClientStorageState.my_cookie, on_change=ClientStorageState.set_my_cookie)),
        rx.hstack(rx.text("my_local_storage"), rx.input(value=ClientStorageState.my_local_storage, on_change=ClientStorageState.set_my_local_storage)),
        rx.hstack(rx.text("custom_cookie"), rx.input(value=ClientStorageState.custom_cookie, on_change=ClientStorageState.set_custom_cookie)),
    )
```

```python eval
docdemo_from(ClientStorageState, component=client_storage_example)
```

## Backend-only Vars

Any Var in a state class that starts with an underscore is considered backend
only and will not be syncronized with the frontend. Data associated with a
specific session that is not directly rendered on the frontend should be stored
in a backend-only var to reduce network traffic and improve performance.

They have the advantage that they don't need to be JSON serializable, however
they must still be cloudpickle-able to be used with redis in prod mode. They are
not directly renderable on the frontend, and may be used to store sensitive
values that should not be sent to the client.

For example, a backend-only var is used to store a large data structure which is
then paged to the frontend using cached vars. 

```python exec
class BackendVarState(State):
    _backend: np.ndarray = np.array([random.randint(0, 100) for _ in range(100)])
    offset: int = 0
    limit: int = 10

    @rx.cached_var
    def page(self) -> list[int]:
        return [
            int(x)  # explicit cast to int
            for x in self._backend[self.offset : self.offset + self.limit]
        ]

    @rx.cached_var
    def page_number(self) -> int:
        return (self.offset // self.limit) + 1 + (1 if self.offset % self.limit else 0)

    @rx.cached_var
    def total_pages(self) -> int:
        return len(self._backend) // self.limit + (1 if len(self._backend) % self.limit else 0)

    def prev_page(self):
        self.offset = max(self.offset - self.limit, 0)

    def next_page(self):
        if self.offset + self.limit < len(self._backend):
            self.offset += self.limit

    def generate_more(self):
        self._backend = np.append(self._backend, [random.randint(0, 100) for _ in range(random.randint(0, 100))])


def backend_var_example():
    return rx.vstack(
        rx.hstack(
            rx.button(
                "Prev",
                on_click=BackendVarState.prev_page,
            ),
            rx.text(f"Page {BackendVarState.page_number} / {BackendVarState.total_pages}"),
            rx.button(
                "Next",
                on_click=BackendVarState.next_page,
            ),
            rx.text("Page Size"),
            rx.number_input(
                width="5em",
                value=BackendVarState.limit,
                on_change=BackendVarState.set_limit,
            ),
            rx.button("Generate More", on_click=BackendVarState.generate_more),
        ),
        rx.list(
            rx.foreach(
                BackendVarState.page,
                lambda x, ix: rx.text(f"_backend[{ix + BackendVarState.offset}] = {x}"),
            ),
        ),
    )
```
```python eval
docdemo_from(BackendVarState, component=backend_var_example, imports=["import numpy as np"])
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