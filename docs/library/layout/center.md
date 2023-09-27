---
import reflex as rx
from pcweb.templates.docpage import docdemo

hello_world_center_example = """rx.center(
    rx.text("Hello World!"),
    border_radius="15px",
    border_width="thick",
    width="50%",
)
"""
circle_square_example = """rx.hstack(
    rx.square(
        rx.vstack(rx.text("Square")),
        border_width="thick",
        border_color="purple",
        padding="1em",
    ),
    rx.circle(
        rx.vstack(rx.text("Circle")),
        border_width="thick",
        border_color="orange",
        padding="1em",
    ),
    spacing="2em",
)"""

---

Center, Square, and Circle are components that center its children within itself.

```reflex
docdemo(hello_world_center_example)
```

Below are examples of circle and square.

```reflex
docdemo(circle_square_example)
```

