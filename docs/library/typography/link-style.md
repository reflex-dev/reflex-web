```python exec
import reflex as rx
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
from pcweb.templates.docpage import docdemo_from
```


# Link Style


## Size

Use the `size` prop to control the size of the link. The prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.


```python demo
flex(
    link("The quick brown fox jumps over the lazy dog.", size="1"),
    link("The quick brown fox jumps over the lazy dog.", size="2"),
    link("The quick brown fox jumps over the lazy dog.", size="3"),
    link("The quick brown fox jumps over the lazy dog.", size="4"),
    link("The quick brown fox jumps over the lazy dog.", size="5"),
    link("The quick brown fox jumps over the lazy dog.", size="6"),
    link("The quick brown fox jumps over the lazy dog.", size="7"),
    link("The quick brown fox jumps over the lazy dog.", size="8"),
    link("The quick brown fox jumps over the lazy dog.", size="9"),
    direction="column",
    gap="3",
)
```


## Weight

Use the `weight` prop to set the text weight.

```python demo
flex(
    link("The quick brown fox jumps over the lazy dog.", weight="light"),
    link("The quick brown fox jumps over the lazy dog.", weight="regular"),
    link("The quick brown fox jumps over the lazy dog.", weight="medium"),
    link("The quick brown fox jumps over the lazy dog.", weight="bold"),
    direction="column",
    gap="3",
)
```



## Trim

Use the `trim` prop to trim the leading space at the start, end, or both sides of the rendered text.


```python demo
flex(
    link("Without Trim",
        trim="normal",
        style={"background": "var(--gray-a2)",
                "border_top": "1px dashed var(--gray-a7)",
                "border_bottom": "1px dashed var(--gray-a7)",}
    ),
    link("With Trim",
        trim="both",
        style={"background": "var(--gray-a2)",
                "border_top": "1px dashed var(--gray-a7)",
                "border_bottom": "1px dashed var(--gray-a7)",}
    ),
    direction="column",
    gap="3",
)
```


## Underline

Use the `underline` prop to manage the visibility of the underline affordance. It defaults to `auto`.

```python demo
flex(
    link("The quick brown fox jumps over the lazy dog.", underline="auto"),
    link("The quick brown fox jumps over the lazy dog.", underline="hover"),
    link("The quick brown fox jumps over the lazy dog.", underline="always"),
    direction="column",
    gap="3",
)
```


## Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.


```python demo
flex(
    link("The quick brown fox jumps over the lazy dog.", color_scheme="indigo"),
    link("The quick brown fox jumps over the lazy dog.", color_scheme="cyan"),
    link("The quick brown fox jumps over the lazy dog.", color_scheme="crimson"),
    link("The quick brown fox jumps over the lazy dog.", color_scheme="orange"),
    direction="column",
)
```

## High Contrast

Use the `high_contrast` prop to increase color contrast with the background.


```python demo
flex(
    link("The quick brown fox jumps over the lazy dog."),
    link("The quick brown fox jumps over the lazy dog.", high_contrast=True),
    direction="column",
)
```
