---
components:
    - rx.radix.kbd
---

```python exec
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
```

# Kbd (Keyboard)

Represents keyboard input or a hotkey.

```python demo
kbd("Shift + Tab")
```

## Size

Use the `size` prop to control text size. This prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.

```python demo
flex(
    kbd("Shift + Tab", size="1"),
    kbd("Shift + Tab", size="2"),
    kbd("Shift + Tab", size="3"),
    kbd("Shift + Tab", size="4"),
    kbd("Shift + Tab", size="5"),
    kbd("Shift + Tab", size="6"),
    kbd("Shift + Tab", size="7"),
    kbd("Shift + Tab", size="8"),
    kbd("Shift + Tab", size="9"),
    direction="column",
    gap="3",
)
```