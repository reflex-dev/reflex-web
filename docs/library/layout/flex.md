---
import reflex as rx
from pcweb.templates.docpage import docdemo

flex_example = """rx.flex(
    rx.center("Center", bg="lightblue"),
    rx.square("Square", bg="lightgreen", padding=10),
    rx.box("Box", bg="salmon", width="150px"),
)"""

flex_example_with_spacer = """rx.flex(
    rx.center("Center", bg="lightblue"),
    rx.spacer(),
    rx.square("Square", bg="lightgreen", padding=10),
    rx.spacer(),
    rx.box("Box", bg="salmon", width="150px"),
    width = "100%",
)"""

---

Flexbox is a layout model that allows elements to align and distribute space within a container. Using flexible widths and heights, elements can be aligned to fill a space or distribute space between elements, which makes it a great tool to use for responsive design systems.

```reflex
docdemo(flex_example)
```

Combining flex with spacer allows for stackable and responsive components.

```reflex
docdemo(flex_example_with_spacer)
```