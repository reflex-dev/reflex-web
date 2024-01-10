---
components:
    - rx.chakra.Select
---

```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo_from
```

# Select

The Select component is used to create a list of options, which allows a user to select one or more options from it.

```python exec
from typing import List
options: List[str] = ["Option 1", "Option 2", "Option 3"]

class SelectState(rx.State):
    option: str = "No selection yet."


def basic_select_example():
    return rx.vstack(
        rx.heading(SelectState.option),
        rx.select(
            options,
            placeholder="Select an example.",
            on_change=SelectState.set_option,
            color_schemes="twitter",
        ),
    )
```

```python eval
docdemo_from(SelectState, component=basic_select_example)
```

Select can also have multiple options selected at once.

```python exec
from typing import List
options: List[str] = ["Option 1", "Option 2", "Option 3"]

class MultiSelectState(rx.State):
    option: List[str] = []


def multiselect_example():
    return rx.vstack(
        rx.heading(MultiSelectState.option),
        rx.select(
            options, 
            placeholder="Select examples", 
            is_multi=True,
            on_change=MultiSelectState.set_option,
            close_menu_on_select=False,
            color_schemes="twitter",
        ),
    )
```

```python eval
docdemo_from(MultiSelectState, component=multiselect_example)
```

The component can also be customized and styled as seen in the next examples.

```python demo
rx.vstack(
    rx.select(options, placeholder="Select an example.", size="xs"),
    rx.select(options, placeholder="Select an example.", size="sm"),
    rx.select(options, placeholder="Select an example.", size="md"),
    rx.select(options, placeholder="Select an example.", size="lg"),
)
```

```python demo
rx.vstack(
    rx.select(options, placeholder="Select an example.", variant="outline"),
    rx.select(options, placeholder="Select an example.", variant="filled"),
    rx.select(options, placeholder="Select an example.", variant="flushed"),
    rx.select(options, placeholder="Select an example.", variant="unstyled"),
)
```

```python demo
rx.select(
    options,
    placeholder="Select an example.",
    color="white",
    bg="#68D391",
    border_color="#38A169",
)
```
