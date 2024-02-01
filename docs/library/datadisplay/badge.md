---
components:
    - rx.radix.badge
---
# Badge

```python exec
import reflex as rx
rdx = rx.radix
from pcweb.templates.docpage import style_grid
```

Badges are used to highlight an item's status for quick recognition.

## Basic Example

To create a badge component with only text inside, pass the text as an argument.

```python demo
rdx.badge("New")
```

## Styling

```python eval
style_grid(component_used=rdx.badge, component_used_str="rdx.badge", variants=["solid", "soft", "surface", "outline"], components_passed="England!",)
```

### Size

The `size` prop controls the size and padding of a badge. It can take values of `"1" | "2"`, with default being `"1"`.

```python demo
rdx.flex(
    rdx.badge("New"),
    rdx.badge("New", size="1"),
    rdx.badge("New", size="2"),
    align="center",
    gap="2",
)
```

### Variant

The `variant` prop controls the visual style of the badge. The supported variant types are `"solid" | "soft" | "surface" | "outline"`. The variant default is `"soft"`.

```python demo
rdx.flex(
    rdx.badge("New", variant="solid"),
    rdx.badge("New", variant="soft"),
    rdx.badge("New"),
    rdx.badge("New", variant="surface"),
    rdx.badge("New", variant="outline"),
    gap="2",
)
```

### Color Scheme

The `color_scheme` prop sets a specific color, ignoring the global theme.

```python demo
rdx.flex(
    rdx.badge("New", color_scheme="indigo"),
    rdx.badge("New", color_scheme="cyan"),
    rdx.badge("New", color_scheme="orange"),
    rdx.badge("New", color_scheme="crimson"),
    gap="2",
)
```

### High Contrast

The `high_contrast` prop increases color contrast of the fallback text with the background.

```python demo
rdx.flex(
    rdx.flex(
        rdx.badge("New", variant="solid"),
        rdx.badge("New", variant="soft"),
        rdx.badge("New", variant="surface"),
        rdx.badge("New", variant="outline"),
        gap="2",
    ),
    rdx.flex(
        rdx.badge("New", variant="solid", high_contrast=True),
        rdx.badge("New", variant="soft", high_contrast=True),
        rdx.badge("New", variant="surface", high_contrast=True),
        rdx.badge("New", variant="outline", high_contrast=True),
        gap="2",
    ),
    direction="column",
    gap="2",
)
```

### Radius

The `radius` prop sets specific radius value, ignoring the global theme. It can take values `"none" | "small" | "medium" | "large" | "full"`.

```python demo
rdx.flex(
    rdx.badge("New", radius="none"),
    rdx.badge("New", radius="small"),
    rdx.badge("New", radius="medium"),
    rdx.badge("New", radius="large"),
    rdx.badge("New", radius="full"),
    gap="3",
)
```

## Final Example

A badge may contain more complex elements within it. This example uses a `flex` component to align an icon and the text correctly, using the `gap` prop to
ensure a comfortable spacing between the two.

```python demo
rdx.badge(
    rdx.flex(
        rdx.icon(tag="arrow_up"),
        rdx.text("8.8%"),
        gap="1",
    ),
    color_scheme="grass",
)
```
