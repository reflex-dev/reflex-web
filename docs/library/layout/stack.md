---
import reflex as rx
from pcweb.templates.docpage import docdemo

hstack_example = """rx.hstack(
    rx.box("Example", bg="red", border_radius="md", width="10%"),
    rx.box("Example", bg="orange", border_radius="md", width="10%"),
    rx.box("Example", bg="yellow", border_radius="md", width="10%"),
    rx.box("Example", bg="lightblue", border_radius="md", width="10%"),
    rx.box("Example", bg="lightgreen", border_radius="md", width="60%"),
    width="100%",
)"""

vstack_example = """rx.vstack(
    rx.box("Example", bg="red", border_radius="md", width="20%"),
    rx.box("Example", bg="orange", border_radius="md", width="40%"),
    rx.box("Example", bg="yellow", border_radius="md", width="60%"),
    rx.box("Example", bg="lightblue", border_radius="md", width="80%"),
    rx.box("Example", bg="lightgreen", border_radius="md", width="100%"),
    width="100%",
)"""

---

Below are two examples the different types of stack components vstack and hstack for ordering items on a page.

```reflex
docdemo(hstack_example)
```

```reflex
docdemo(vstack_example)
```

