---
components:
  - rx.radix.grid
---

```python exec
import reflex as rx
rdx = rx.radix
```

# Grid

Component for creating grid layouts. Either `rows` or `columns` may be specified.

## Basic Example

```python demo
rdx.grid(
    rx.foreach(
        rx.Var.range(12),
        lambda i: rdx.card(f"Card {i + 1}", height="10vh"),
    ),
    columns="3",
    gap="4",
    width="100%",
)
```

```python demo
rdx.grid(
    rx.foreach(
        rx.Var.range(12),
        lambda i: rdx.card(f"Card {i + 1}", height="10vh"),
    ),
    rows="3",
    flow="column",
    justify="between",
    gap="4",
    width="100%",
)
```
