---
components:
    - rx.radix.themes.Code
---

```python exec
import reflex as rx
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
from pcweb.templates.docpage import docdemo_from
```

# Code

```python demo
code("console.log()")
```



## Size

Use the `size` prop to control text size. This prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.


```python demo
flex(
    code("console.log()", size="1"),
    code("console.log()", size="2"),
    code("console.log()", size="3"),
    code("console.log()", size="4"),
    code("console.log()", size="5"),
    code("console.log()", size="6"),
    code("console.log()", size="7"),
    code("console.log()", size="8"),
    code("console.log()", size="9"),
    direction="column",
    gap="3",
    align="start",
)
```




## Weight

Use the `weight` prop to set the text weight.

```python demo
flex(
    code("console.log()", weight="light"),
    code("console.log()", weight="regular"),
    code("console.log()", weight="medium"),
    code("console.log()", weight="bold"),
    direction="column",
    gap="3",
)
```

## Variant

Use the `variant` prop to control the visual style.

```python demo
flex(
    code("console.log()", variant="solid"),
    code("console.log()", variant="soft"),
    code("console.log()", variant="outline"),
    code("console.log()", variant="ghost"),
    direction="column",
    gap="2",
    align="start",
)
```



## Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.


```python demo
flex(
    code("console.log()", color_scheme="indigo"),
    code("console.log()", color_scheme="crimson"),
    code("console.log()", color_scheme="orange"),
    code("console.log()", color_scheme="cyan"),
    direction="column",
    gap="2",
    align="start",
)
```


## High Contrast

Use the `high_contrast` prop to increase color contrast with the background.


```python demo
flex(
    flex(
        code("console.log()", variant="solid"),
        code("console.log()", variant="soft"),
        code("console.log()", variant="outline"),
        code("console.log()", variant="ghost"),
        direction="column",
        align="start",
        gap="2",
    ),
    flex(
        code("console.log()", variant="solid", high_contrast=True),
        code("console.log()", variant="soft", high_contrast=True),
        code("console.log()", variant="outline", high_contrast=True),
        code("console.log()", variant="ghost", high_contrast=True),
        direction="column",
        align="start",
        gap="2",
    ),
    gap="3",
)
```

