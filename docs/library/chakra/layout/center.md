---
components:
    - rx.chakra.Center
    - rx.chakra.Circle
    - rx.chakra.Square
---

```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo
```

Center, Square, and Circle are components that center its children within itself.

```python eval
docdemo("""rx.center(
    rx.text("Hello World!"),
    border_radius="15px",
    border_width="thick",
    width="50%",
)""")
```

Below are examples of circle and square.

```python eval
docdemo("""rx.hstack(
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
)""")
```

