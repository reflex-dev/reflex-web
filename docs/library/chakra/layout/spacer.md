---
components:
    - rx.chakra.Spacer
---

```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo
```

Creates an adjustable, empty space that can be used to tune the spacing between child elements within Flex.

```python eval
docdemo("""rx.flex(
    rx.center(rx.text("Example"), bg="lightblue"),
    rx.spacer(),
    rx.center(rx.text("Example"), bg="lightgreen"),
    rx.spacer(),
    rx.center(rx.text("Example"), bg="salmon"),
    width="100%",
)""")
```

