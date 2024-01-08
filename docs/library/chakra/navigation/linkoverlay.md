```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo_from
```

# LinkOverlay

Link overlay provides a semantic way to wrap elements (cards, blog post, articles, etc.) in a link.

```python demo
rx.link_overlay(
    rx.box("Example", bg="black", color="white", font_size=30),
)
```
