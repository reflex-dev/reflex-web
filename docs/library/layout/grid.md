---
components:
  - rx.radix.themes.Grid
---

```python exec
import reflex as rx
import reflex.components.radix.themes as rdxt
```

# Grid

Component for creating grid layouts. Either `rows` or `columns` may be specified.

## Basic Example

```python demo
rdxt.grid(
    rx.foreach(
        rx.Var.range(12),
        lambda i: rdxt.card(f"Card {i + 1}", height="10vh"),
    ),
    columns="3",
    gap="4",
    width="100%",
)
```

```python demo
rdxt.grid(
    rx.foreach(
        rx.Var.range(12),
        lambda i: rdxt.card(f"Card {i + 1}", height="10vh"),
    ),
    rows="3",
    flow="column",
    justify="between",
    gap="4",
    width="100%",
)
```
