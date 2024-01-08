```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo_from
```

# Menu

An accessible dropdown menu for the common dropdown menu button design pattern.

```python demo
rx.menu(
    rx.menu_button("Menu"),
    rx.menu_list(
        rx.menu_item("Example"),
        rx.menu_divider(),
        rx.menu_item("Example"),
        rx.menu_item("Example"),
    ),
)
```
