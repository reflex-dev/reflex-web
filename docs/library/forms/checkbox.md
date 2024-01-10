---
components:
    - rx.radix.themes.Checkbox
---

```python exec
import reflex as rx
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
```


# Checkbox

Selects a single value, typically for submission in a form.


```python demo
text(
  flex(
    checkbox(default_checked=True),
    "Agree to Terms and Conditions", 
    gap="2",
  ),
  as_="label",
  size="2",
)
```