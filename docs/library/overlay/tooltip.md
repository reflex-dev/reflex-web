---
components:
    - rx.radix.tooltip
---

```python exec
import reflex as rx
rdx = rx.radix
```

# Tooltip

```python demo

rdx.tooltip(
    rdx.button("Hover over me"),
    content="This is the tooltip content.",
)
```