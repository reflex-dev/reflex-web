---
components:
    - rx.chakra.Spacer
---

```python exec
import reflex as rx
```

Creates an adjustable, empty space that can be used to tune the spacing between child elements within Flex.

```python demo
rx.flex(
    rx.center(rx.text("Example"), bg="lightblue"),
    rx.spacer(),
    rx.center(rx.text("Example"), bg="lightgreen"),
    rx.spacer(),
    rx.center(rx.text("Example"), bg="salmon"),
    width="100%",
)
```

