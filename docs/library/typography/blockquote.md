```python exec
import reflex as rx
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
from pcweb.templates.docpage import docdemo_from
```

# Blockquote

```python demo
blockquote("Perfect typography is certainly the most elusive of all arts. Sculpture in stone alone comes near it in obstinacy.")
```


## Size

Use the `size` prop to control the size of the blockquote. The prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.


```python demo
flex(
    blockquote("Perfect typography is certainly the most elusive of all arts. Sculpture in stone alone comes near it in obstinacy.", size="1"),
    blockquote("Perfect typography is certainly the most elusive of all arts. Sculpture in stone alone comes near it in obstinacy.", size="2"),
    blockquote("Perfect typography is certainly the most elusive of all arts. Sculpture in stone alone comes near it in obstinacy.", size="3"),
    blockquote("Perfect typography is certainly the most elusive of all arts. Sculpture in stone alone comes near it in obstinacy.", size="4"),
    blockquote("Perfect typography is certainly the most elusive of all arts. Sculpture in stone alone comes near it in obstinacy.", size="5"),
    blockquote("Perfect typography is certainly the most elusive of all arts. Sculpture in stone alone comes near it in obstinacy.", size="6"),
    blockquote("Perfect typography is certainly the most elusive of all arts. Sculpture in stone alone comes near it in obstinacy.", size="7"),
    blockquote("Perfect typography is certainly the most elusive of all arts. Sculpture in stone alone comes near it in obstinacy.", size="8"),
    blockquote("Perfect typography is certainly the most elusive of all arts. Sculpture in stone alone comes near it in obstinacy.", size="9"),
    direction="column",
    gap="3",
)
```


## Weight

Use the `weight` prop to set the blockquote weight.

```python demo
flex(
    blockquote("Perfect typography is certainly the most elusive of all arts. Sculpture in stone alone comes near it in obstinacy.", weight="light"),
    blockquote("Perfect typography is certainly the most elusive of all arts. Sculpture in stone alone comes near it in obstinacy.", weight="regular"),
    blockquote("Perfect typography is certainly the most elusive of all arts. Sculpture in stone alone comes near it in obstinacy.", weight="medium"),
    blockquote("Perfect typography is certainly the most elusive of all arts. Sculpture in stone alone comes near it in obstinacy.", weight="bold"),
    direction="column",
    gap="3",
)
```



## Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.


```python demo
flex(
    blockquote("Perfect typography is certainly the most elusive of all arts. Sculpture in stone alone comes near it in obstinacy.", color_scheme="indigo"),
    blockquote("Perfect typography is certainly the most elusive of all arts. Sculpture in stone alone comes near it in obstinacy.", color_scheme="cyan"),
    blockquote("Perfect typography is certainly the most elusive of all arts. Sculpture in stone alone comes near it in obstinacy.", color_scheme="crimson"),
    blockquote("Perfect typography is certainly the most elusive of all arts. Sculpture in stone alone comes near it in obstinacy.", color_scheme="orange"),
    direction="column",
)
```

## High Contrast

Use the `high_contrast` prop to increase color contrast with the background.


```python demo
flex(
    blockquote("Perfect typography is certainly the most elusive of all arts. Sculpture in stone alone comes near it in obstinacy."),
    blockquote("Perfect typography is certainly the most elusive of all arts. Sculpture in stone alone comes near it in obstinacy.", high_contrast=True),
    direction="column",
)
```
