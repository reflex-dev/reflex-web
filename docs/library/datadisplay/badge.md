---
components:
    - rx.radix.themes.Badge
---
# Badge

```python exec
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
from pcweb.templates.docpage import style_grid
```

Badges are used to highlight an item's status for quick recognition.

## Basic Example

To create a badge component with only text inside, we pass the text as an argument.

```python demo
badge("New")
```

## Styling

```python eval
style_grid(component_used=badge, component_used_str="badge", variants=["solid", "soft", "surface", "outline"], components_passed="England!",)
```

### Size

We use the `size` prop to change the size of a badge. It can take values of `"1" | "2"`, with default being `"1"`.

```python demo
flex(
    badge("New"),
    badge("New", size="1"),
    badge("New", size="2"),
    align="center",
    gap="2",
)
```

### Variant

We use the `variant` prop to control the visual style. The supported variant types are `"solid" | "soft" | "surface" | "outline"`. The variant default is `"soft"`.

```python demo
flex(
    badge("New", variant="solid"),
    badge("New", variant="soft"),
    badge("New"),
    badge("New", variant="surface"),
    badge("New", variant="outline"),
    gap="2",
)
```

### Color Scheme

We use the `color_scheme` prop to assign a specific color, ignoring the global theme.

```python demo
flex(
    badge("New", color_scheme="indigo"),
    badge("New", color_scheme="cyan"),
    badge("New", color_scheme="orange"),
    badge("New", color_scheme="crimson"),
    gap="2",
)
```

### High Contrast

We use the `high_contrast` prop to increase color contrast with the background.

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

### Radius

We use the `radius` prop to assign a specific radius value, ignoring the global theme. It can take values `"none" | "small" | "medium" | "large" | "full"`.

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

## Final Example

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
