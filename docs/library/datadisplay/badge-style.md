```python exec
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
# from reflex.components.radix.doc_functions import style_grid
```

# Styling 

blurb about the grid for this one ...


## Size

To change the size of the badge use the `size` prop. It can take values of `"1" | "2"`.

```python demo
flex(
    badge("New", size="1"),
    badge("New", size="2"),
    align="center",
    gap="2",
    )
```


## Variant

Use the `variant` prop to control the visual style.

```python demo
flex(
    badge("New", variant="solid"),
    badge("New", variant="soft"),
    badge("New", variant="surface"),
    badge("New", variant="outline"),
    gap="2",
)
```


## Color


Use the `color_scheme` prop to assign a specific color, ignoring the global theme.

```python demo
flex(
    badge("New", color_scheme="indigo"),
    badge("New", color_scheme="cyan"),
    badge("New", color_scheme="orange"),
    badge("New", color_scheme="crimson"),
    gap="2",
    )
```


## High Contrast

Use the `high_contrast` prop to increase color contrast with the background.


```python demo
flex(
    flex(
        badge("New", variant="solid"),
        badge("New", variant="soft"),
        badge("New", variant="surface"),
        badge("New", variant="outline"),
        gap="2",
    ),
    flex(
        badge("New", variant="solid", high_contrast=True),
        badge("New", variant="soft", high_contrast=True),
        badge("New", variant="surface", high_contrast=True),
        badge("New", variant="outline", high_contrast=True),
        gap="2",
    ),
    direction="column",
    gap="2",
)
```


## Radius

Use the `radius` prop to assign a specific radius value, ignoring the global theme. It can take values `"none" | "small" | "medium" | "large" | "full"`. 

```python demo
flex(
    badge("New", radius="none"),
    badge("New", radius="small"),
    badge("New", radius="medium"),
    badge("New", radius="large"),
    badge("New", radius="full"),
    gap="3",
    )
```