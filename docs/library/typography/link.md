---
components:
    - rx.radix.link
---

```python exec
import reflex as rx
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
```


# Link

Links are accessible elements used primarily for navigation. Use the `href` prop to specify the location for the link to navigate to.

```python demo
link("Reflex Home Page.", href="https://reflex.dev")
```


You can also provide local links to other pages in your project without writing the full url.


```python demo
link("Example", href="/docs/library",)
```

The `link` component can be used to wrap other components to make them link to other pages.


```python demo
link(button("Example"), href="https://reflex.dev")
```

You can also create anchors to link to specific parts of a page using the `id` prop.

```python demo
box("Example", id="example")
```

To reference an anchor, you can use the `href` prop of the `link` component. The `href` should be in the format of the page you want to link to followed by a # and the id of the anchor.


```python demo
link("Example", href="/docs/library/typography/link#example")
```




# Style


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