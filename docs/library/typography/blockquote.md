---
components:
    - rx.radix.themes.Blockquote
---

```python exec
import reflex as rx
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
```

# Blockquote

```python demo
blockquote("Perfect typography is certainly the most elusive of all arts.")
```


## Size

Use the `size` prop to control the size of the blockquote. The prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.


```python demo
flex(
    blockquote("Perfect typography is certainly the most elusive of all arts.", size="1"),
    blockquote("Perfect typography is certainly the most elusive of all arts.", size="2"),
    blockquote("Perfect typography is certainly the most elusive of all arts.", size="3"),
    blockquote("Perfect typography is certainly the most elusive of all arts.", size="4"),
    blockquote("Perfect typography is certainly the most elusive of all arts.", size="5"),
    blockquote("Perfect typography is certainly the most elusive of all arts.", size="6"),
    blockquote("Perfect typography is certainly the most elusive of all arts.", size="7"),
    blockquote("Perfect typography is certainly the most elusive of all arts.", size="8"),
    blockquote("Perfect typography is certainly the most elusive of all arts.", size="9"),
    direction="column",
    gap="3",
)
```


## Weight

Use the `weight` prop to set the blockquote weight.

```python demo
flex(
    blockquote("Perfect typography is certainly the most elusive of all arts.", weight="light"),
    blockquote("Perfect typography is certainly the most elusive of all arts.", weight="regular"),
    blockquote("Perfect typography is certainly the most elusive of all arts.", weight="medium"),
    blockquote("Perfect typography is certainly the most elusive of all arts.", weight="bold"),
    direction="column",
    gap="3",
)
```



## Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.


```python demo
flex(
    blockquote("Perfect typography is certainly the most elusive of all arts.", color_scheme="indigo"),
    blockquote("Perfect typography is certainly the most elusive of all arts.", color_scheme="cyan"),
    blockquote("Perfect typography is certainly the most elusive of all arts.", color_scheme="crimson"),
    blockquote("Perfect typography is certainly the most elusive of all arts.", color_scheme="orange"),
    direction="column",
    gap="3",
)
```

## High Contrast

Use the `high_contrast` prop to increase color contrast with the background.


```python demo
flex(
    blockquote("Perfect typography is certainly the most elusive of all arts."),
    blockquote("Perfect typography is certainly the most elusive of all arts.", high_contrast=True),
    direction="column",
    gap="3",
)
```
