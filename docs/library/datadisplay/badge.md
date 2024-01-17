---
components:
    - rx.radix.themes.Badge
---
# Badge

```python exec
import reflex.components.radix.themes as rdxt
from pcweb.templates.docpage import style_grid
```

Badges are used to highlight an item's status for quick recognition.

## Basic Example

To create a badge component with only text inside, pass the text as an argument.

```python demo
rdxt.badge("New")
```

## Styling

```python eval
style_grid(component_used=rdxt.badge, component_used_str="rdxt.badge", variants=["solid", "soft", "surface", "outline"], components_passed="England!",)
```

### Size

The `size` prop controls the size and padding of a badge. It can take values of `"1" | "2"`, with default being `"1"`.

```python demo
rdxt.flex(
    rdxt.badge("New"),
    rdxt.badge("New", size="1"),
    rdxt.badge("New", size="2"),
    align="center",
    gap="2",
)
```

### Variant

The `variant` prop controls the visual style of the badge. The supported variant types are `"solid" | "soft" | "surface" | "outline"`. The variant default is `"soft"`.

```python demo
rdxt.flex(
    rdxt.badge("New", variant="solid"),
    rdxt.badge("New", variant="soft"),
    rdxt.badge("New"),
    rdxt.badge("New", variant="surface"),
    rdxt.badge("New", variant="outline"),
    gap="2",
)
```

### Color Scheme

The `color_scheme` prop sets a specific color, ignoring the global theme.

```python demo
rdxt.flex(
    rdxt.badge("New", color_scheme="indigo"),
    rdxt.badge("New", color_scheme="cyan"),
    rdxt.badge("New", color_scheme="orange"),
    rdxt.badge("New", color_scheme="crimson"),
    gap="2",
)
```

### High Contrast

The `high_contrast` prop increases color contrast of the fallback text with the background.

```python demo
rdxt.flex(
    rdxt.flex(
        rdxt.badge("New", variant="solid"),
        rdxt.badge("New", variant="soft"),
        rdxt.badge("New", variant="surface"),
        rdxt.badge("New", variant="outline"),
        gap="2",
    ),
    rdxt.flex(
        rdxt.badge("New", variant="solid", high_contrast=True),
        rdxt.badge("New", variant="soft", high_contrast=True),
        rdxt.badge("New", variant="surface", high_contrast=True),
        rdxt.badge("New", variant="outline", high_contrast=True),
        gap="2",
    ),
    direction="column",
    gap="2",
)
```

### Radius

The `radius` prop sets specific radius value, ignoring the global theme. It can take values `"none" | "small" | "medium" | "large" | "full"`.

```python demo
rdxt.flex(
    rdxt.badge("New", radius="none"),
    rdxt.badge("New", radius="small"),
    rdxt.badge("New", radius="medium"),
    rdxt.badge("New", radius="large"),
    rdxt.badge("New", radius="full"),
    gap="3",
)
```

## Final Example

A badge may contain more complex elements within it. This example uses a `flex`.
component to align an icon and the text correctly, using the `gap` prop to
ensure a comfortable spacing between the two.

```python demo
rdxt.badge(
    rdxt.flex(
        rdxt.icon(tag="arrow_up"),
        rdxt.text("8.8%"),
        gap="1",
    ),
    color_scheme="grass",
)
```
