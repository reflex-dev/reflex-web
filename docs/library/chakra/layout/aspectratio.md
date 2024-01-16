---
components:
    - rx.chakra.AspectRatio
---

```python exec
import reflex as rx
```

Preserve the ratio of the components contained within a region.

```python demo
rx.box(element="iframe", src="https://bit.ly/naruto-sage", border_color="red")
```

```python demo
rx.aspect_ratio(
    rx.box(
        element="iframe",
        src="https://bit.ly/naruto-sage",
        border_color="red"
    ),
    ratio=4/3
)
```
