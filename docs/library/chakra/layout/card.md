---
components:
    - rx.chakra.Card
    - rx.chakra.CardHeader
    - rx.chakra.CardBody
    - rx.chakra.CardFooter
---

```python exec
import reflex as rx
```

Card is a flexible component used to group and display content in a clear and concise format.

```python demo
rx.card(
    rx.text("Body of the Card Component"), 
    header=rx.heading("Header", size="lg"), 
    footer=rx.heading("Footer",size="sm"),
)
```

You can pass a header with `header=` and/or a footer with `footer=`.

