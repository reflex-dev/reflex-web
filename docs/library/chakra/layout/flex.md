---
components:
    - rx.chakra.Flex
---

```python exec
import reflex as rx
```

Flexbox is a layout model that allows elements to align and distribute space within a container. Using flexible widths and heights, elements can be aligned to fill a space or distribute space between elements, which makes it a great tool to use for responsive design systems.

```python demo
rx.flex(
    rx.center("Center", bg="lightblue"),
    rx.square("Square", bg="lightgreen", padding=10),
    rx.box("Box", bg="salmon", width="150px"),
)
```

Combining flex with spacer allows for stackable and responsive components.

```python demo
rx.flex(
    rx.center("Center", bg="lightblue"),
    rx.spacer(),
    rx.square("Square", bg="lightgreen", padding=10),
    rx.spacer(),
    rx.box("Box", bg="salmon", width="150px"),
    width = "100%",
)
```