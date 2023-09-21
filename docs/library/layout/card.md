---
import reflex as rx
from pcweb.templates.docpage import docdemo

card_example = """rx.card(
    rx.text("Body of the Card Component"), 
    header=rx.heading("Header", size="lg"), 
    footer=rx.heading("Footer",size="sm"),
)"""

---

Card is a flexible component used to group and display content in a clear and concise format.

```reflex
docdemo(card_example)
```

You can pass a header with `header=` and/or a footer with `footer=`.

