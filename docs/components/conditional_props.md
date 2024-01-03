```python exec
from pcweb.base_state import State
from pcweb.pages.docs.styling.overview import styling_overview
from pcweb.templates.docpage import docdemo, doclink
import reflex as rx
import inspect
```

# Conditional Props

Sometimes you want to set a prop based on a condition. You can use the `rx.cond` function to do this.

```python exec
class PropCondState(State):
    value: int


def cond_prop():
    return rx.slider(
        on_change_end=PropCondState.set_value,
        color_scheme=rx.cond(PropCondState.value > 50, "green", "pink"),
    )
```

```python eval
docdemo(inspect.getsource(cond_prop),
    comp=cond_prop(),
    state=inspect.getsource(PropCondState)
)
```