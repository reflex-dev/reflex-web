---
components:
    - rx.data_list
---

```python exec
import reflex as rx
```

# Data List

The `DataList` component displays key-value pairs and is particularly helpful for showing metadata.

A `DataList` needs to be initialized using `rx.data_list.root()` and currently takes in data list items: `rx.data_list.item`

```python demo
rx.data_list.root(
    rx.data_list.item(
        rx.data_list.label("test"), rx.data_list.value("test"),
    ),
    rx.data_list.item(
        rx.data_list.label("test"), rx.data_list.value("test"),
    ),
)
```
