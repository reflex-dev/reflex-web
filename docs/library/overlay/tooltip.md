---
components:
    - rx.radix.tooltip
---

```python exec
import reflex as rx
rdx = rx.radix
```

# Tooltip

A `tooltip` displays informative information when users hover over or focus on an element.

It takes a `content` prop, which is the content associated with the tooltip.

```python demo
rdx.tooltip(
    rdx.button("Hover over me"),
    content="This is the tooltip content.",
)
```