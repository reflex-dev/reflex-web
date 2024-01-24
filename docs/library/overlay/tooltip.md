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

```python demo

tooltip(
    button("Hover over me"),
    content="This is the tooltip content.",
)
```