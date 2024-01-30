---
components:
    - rx.radix.themes.Tooltip
---

```python exec
import reflex as rx
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
```

# Tooltip

A `tooltip` displays informative information when users hover over or focus on an element. 

It takes a `content` prop, which is the content associated with the tooltip.


```python demo
tooltip(
    button("Hover over me"),
    content="This is the tooltip content.",
)
```