---
import reflex as rx
from pcweb.templates.docpage import docdemo

container_example = """rx.container(
    rx.box("Example", bg="blue", color="white", width="50%"),
    center_content=True,
    bg="lightblue",
)"""

---

Containers are used to constrain a content's width to the current breakpoint, while keeping it fluid.

```reflex
docdemo(container_example)
```
