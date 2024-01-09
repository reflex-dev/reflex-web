---
components:
    - rx.radix.themes.Badge
---

```python exec
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
# from reflex.components.radix.doc_functions import style_grid
```


# Radix badge example docs


## intro to the component 

A stylized badge element.

To create a simple badge component with only text inside we can pass the text that we will render inside the badge as an argument. Here we pass the text `New` to the badge.

```python demo
badge("New")
```

We can also set the `color_scheme` which will change the entire color of the `badge` component.

```python demo
badge("New", color_scheme="orange")
```


## examples of using all the props (exclude the style props: color, variant, size, high contrast)

N/A

## examples using all the event handlers

N/A

## give in context examples (use radix examples)



Here is a more advanced example of using an icon within the `badge` component. We use the `flex` component to align the icon and the text correctly, using the `gap` prop to ensure that we have the correct spacing.

```python demo
badge(
    flex(icon(tag="arrow_up"),
        text("8.8%"),
        gap="1",
    ), 
    color="grass",
)
```


could maybe add some more in context examples.
