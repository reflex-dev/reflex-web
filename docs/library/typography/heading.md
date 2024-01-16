---
components:
    - rx.radix.themes.Heading
---

```python exec
import reflex as rx
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
```

# Heading

```python demo
heading("The quick brown fox jumps over the lazy dog.")
```

## As another element

Use the `as_` prop to change the heading level. This prop is purely semantic and does not change the visual appearance.

```python demo
flex(
    heading("Level 1", as_="h1"),
    heading("Level 2", as_="h2"),
    heading("Level 3", as_="h3"),
    direction="column",
    gap="3",
)             
```

## Size

Use the `size` prop to control the size of the heading. The prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease


```python demo
flex(
    heading("The quick brown fox jumps over the lazy dog.", size="1"),
    heading("The quick brown fox jumps over the lazy dog.", size="2"),
    heading("The quick brown fox jumps over the lazy dog.", size="3"),
    heading("The quick brown fox jumps over the lazy dog.", size="4"),
    heading("The quick brown fox jumps over the lazy dog.", size="5"),
    heading("The quick brown fox jumps over the lazy dog.", size="6"),
    heading("The quick brown fox jumps over the lazy dog.", size="7"),
    heading("The quick brown fox jumps over the lazy dog.", size="8"),
    heading("The quick brown fox jumps over the lazy dog.", size="9"),
    direction="column",
    gap="3",
)
```



## Weight

Use the `weight` prop to set the text weight.

```python demo
flex(
    heading("The quick brown fox jumps over the lazy dog.", weight="light"),
    heading("The quick brown fox jumps over the lazy dog.", weight="regular"),
    heading("The quick brown fox jumps over the lazy dog.", weight="medium"),
    heading("The quick brown fox jumps over the lazy dog.", weight="bold"),
    direction="column",
    gap="3",
)
```


## Align

Use the `align` prop to set text alignment.


```python demo
flex(
    heading("Left-aligned", align="left"),
    heading("Center-aligned", align="center"),
    heading("Right-aligned", align="right"),
    direction="column",
    gap="3",
    width="100%",
)
```


## Trim

Use the `trim` prop to trim the leading space at the start, end, or both sides of the text.


```python demo
flex(
    heading("Without Trim",
        trim="normal",
        style={"background": "var(--gray-a2)",
                "border_top": "1px dashed var(--gray-a7)",
                "border_bottom": "1px dashed var(--gray-a7)",}
    ),
    heading("With Trim",
        trim="both",
        style={"background": "var(--gray-a2)",
                "border_top": "1px dashed var(--gray-a7)",
                "border_bottom": "1px dashed var(--gray-a7)",}
    ),
    direction="column",
    gap="3",
)
```


Trimming the leading is useful when dialing in vertical spacing in cards or other “boxy” components. Otherwise, padding looks larger on top and bottom than on the sides.


```python demo
flex(
    box(
        heading("Without trim", mb="1", size="3",),
        text("The goal of typography is to relate font size, line height, and line width in a proportional way that maximizes beauty and makes reading easier and more pleasant."),
        style={"background": "var(--gray-a2)", 
                "border": "1px dashed var(--gray-a7)",},
        p="4",
    ),
    box(
        heading("With trim", mb="1", size="3", trim="start"),
        text("The goal of typography is to relate font size, line height, and line width in a proportional way that maximizes beauty and makes reading easier and more pleasant."),
        style={"background": "var(--gray-a2)", 
                "border": "1px dashed var(--gray-a7)",},
        p="4",
    ),
    direction="column",
    gap="3",
)
```

## Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.


```python demo
flex(
    heading("The quick brown fox jumps over the lazy dog.", color_scheme="indigo"),
    heading("The quick brown fox jumps over the lazy dog.", color_scheme="cyan"),
    heading("The quick brown fox jumps over the lazy dog.", color_scheme="crimson"),
    heading("The quick brown fox jumps over the lazy dog.", color_scheme="orange"),
    direction="column",
)
```

## High Contrast

Use the `high_contrast` prop to increase color contrast with the background.


```python demo
flex(
    heading("The quick brown fox jumps over the lazy dog.", color_scheme="indigo", high_contrast=True),
    heading("The quick brown fox jumps over the lazy dog.", color_scheme="cyan", high_contrast=True),
    heading("The quick brown fox jumps over the lazy dog.", color_scheme="crimson", high_contrast=True),
    heading("The quick brown fox jumps over the lazy dog.", color_scheme="orange", high_contrast=True),
    direction="column",
)
```

