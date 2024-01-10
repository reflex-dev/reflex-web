---
components:
    - rx.Span
---

```python exec
import reflex as rx
```

# Span

The span component can be used to style inline text without creating a new line.

```python demo
rx.box(
    "Write some ",
    rx.span("stylized ", color="red"),    
    rx.span("text ", color="blue"),
    rx.span("using spans.", font_weight="bold")
)
```