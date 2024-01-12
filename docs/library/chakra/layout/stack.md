---
components:
    - rx.chakra.Stack
    - rx.chakra.Hstack
    - rx.chakra.Vstack
---

```python exec
import reflex as rx
```

Below are two examples the different types of stack components vstack and hstack for ordering items on a page.

```python demo
rx.hstack(
    rx.box("Example", bg="red", border_radius="md", width="10%"),
    rx.box("Example", bg="orange", border_radius="md", width="10%"),
    rx.box("Example", bg="yellow", border_radius="md", width="10%"),
    rx.box("Example", bg="lightblue", border_radius="md", width="10%"),
    rx.box("Example", bg="lightgreen", border_radius="md", width="60%"),
    width="100%",
)
```

```python demo
rx.vstack(
    rx.box("Example", bg="red", border_radius="md", width="20%"),
    rx.box("Example", bg="orange", border_radius="md", width="40%"),
    rx.box("Example", bg="yellow", border_radius="md", width="60%"),
    rx.box("Example", bg="lightblue", border_radius="md", width="80%"),
    rx.box("Example", bg="lightgreen", border_radius="md", width="100%"),
    width="100%",
)
```
