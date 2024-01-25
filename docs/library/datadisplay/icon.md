---
components:
    - rx.radix.themes.Icon
---
# Icon

```python exec
import reflex.components.radix.themes as rdxt
from reflex.components.radix.themes.components.icons import *
from pcweb.templates.docpage import icon_grid
```

The Icon component is used to display an icon from a library of icons. This implementation is based on the [Radix icons](https://www.radix-ui.com/icons).

## Basic Example

To display an icon, specify the `tag` prop from the list of available icons.

```python demo
rdxt.icon(tag="calendar")
```

## List of Icons

### Abstract

```python eval
icon_grid("Abstract", ICON_ABSTRACT)
```

### Alignment

```python eval
icon_grid("Alignment", ICON_ALIGNS, columns="3")
```

### Arrows

```python eval
icon_grid("Arrows", ICON_ARROWS)
```

### Borders and Corners

```python eval
icon_grid("Borders and Corners", ICON_BORDERS)
```

### Design

```python eval
icon_grid("Design", ICON_DESIGN)
```

### Components

```python eval
icon_grid("Components", ICON_COMPONENTS, columns="5")
```

### Logos

```python eval
icon_grid("Logos", ICON_LOGOS)
```

### Music

```python eval
icon_grid("Music", ICON_MUSIC)
```

### Objects

```python eval
icon_grid("Objects", ICON_OBJECTS)
```

### Typography

```python eval
icon_grid("Typography", ICON_TYPOGRAPHY)
```

## Styling

An icon is based on the Radix primitive component, and is unstyled. **It does
not accept radix styling props such as `size` or `color_theme`**.

Instead, CSS props should be used; such as `width` and `height` to control the
size of the icon, and `color` to set the stroke color using CSS colors or radix
colors via the `var()` syntax.

### Width and Height

```python demo
rdxt.flex(
    rdxt.icon(tag="magnifying_glass", width=15, height=15),
    rdxt.icon(tag="magnifying_glass", width=20, height=20),
    rdxt.icon(tag="magnifying_glass", width=25, height=25),
    rdxt.icon(tag="magnifying_glass", width=30, height=30),
    align="center",
    gap="2",
)
```

## Color

Here is an example using basic colors in icons.

```python demo
rdxt.flex(
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="indigo"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="cyan"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="orange"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="crimson"),
    gap="2",
)
```

A radix color with a scale may also be specified using the `var()` token syntax seen below.

```python demo
rdxt.flex(
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-1)"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-2)"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-3)"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-4)"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-5)"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-6)"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-7)"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-8)"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-9)"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-10)"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-11)"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-12)"),
    gap="2",
)
```

Here is another example using the `accent` color with scales. The `accent` is the most dominant color in your theme.

```python demo
rdxt.flex(
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-1)"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-2)"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-3)"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-4)"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-5)"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-6)"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-7)"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-8)"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-9)"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-10)"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-11)"),
    rdxt.icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-12)"),
    gap="2",
)
```

## Final Example

Icons can be used as child components of many other components. For example, adding a magnifying glass icon to a search bar.

```python demo
rdxt.badge(
    rdxt.flex(
        rdxt.icon(tag="magnifying_glass", height=18, width=18),
        rdxt.text("Search documentation...", size="3", weight="medium"),
        direction="row",
        gap="1",
        align="center",
    ),
    size="2",
    radius="full",
    color_scheme="gray",
)
```
