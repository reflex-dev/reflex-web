---
title: MultiSelect
---

# MultiSelect component

`rxe.mantine.multi_select` is a component for selecting multiple options from a list. It allows users to choose one or more items, making it suitable for scenarios where multiple selections are required.

```python demo exec
import reflex as rx
import reflex_enterprise as rxe

class MultiSelectState(rx.State):
    selected_fruits: list = []


def multi_select_example():
    return rx.vstack(
        rxe.mantine.multi_select(
            label="Select fruits",
            placeholder="Pick all that you like",
            data=["Apple", "Banana", "Cherry", "Date", "Elderberry"],
            value=MultiSelectState.selected_fruits,
            on_change=lambda value: MultiSelectState.setvar("selected_fruits", value),
        )
    )
```
