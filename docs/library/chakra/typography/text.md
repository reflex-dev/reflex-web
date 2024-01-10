---
components:
    - rx.chakra.Text
---

```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo_from
```

# Text

The text component displays a paragraph of text.

```python demo
rx.text("Hello World!", font_size="2em")
```

The text element can be visually modified using the `as_` prop.

```python demo
rx.vstack(
    rx.text("Hello World!", as_="i"),
    rx.text("Hello World!", as_="s"),
    rx.text("Hello World!", as_="mark"),
    rx.text("Hello World!", as_="sub"),
)
```
