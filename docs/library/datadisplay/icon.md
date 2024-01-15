---
components:
    - rx.radix.themes.Icon
---
# Icon

```python exec
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.components.icons import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
from pcweb.templates.docpage import icon_grid
```

The Icon component is used to display an icon from a library of icons. This implementation is based on the [Radix icons](https://www.radix-ui.com/icons).

## Basic Example

To create an icon, we specify the `tag` prop from the list of available icons.

```python demo
icon(tag="calendar")
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

The icons are based on the Radix primitive component, and it is unstyled. **It does not accept common styling props such as `size` or `color_theme`**. You can still use `width` and `height` together to control the size of the icon, and specify its `color`.

### Width and Height

```python demo
flex(
    icon(tag="magnifying_glass", width=15, height=15),
    icon(tag="magnifying_glass", width=20, height=20),
    icon(tag="magnifying_glass", width=25, height=25),
    icon(tag="magnifying_glass", width=30, height=30),
    align="center",
    gap="2",
)
```

## Color

Here is an example using basic colors in icons.

```python demo
flex(
    icon(tag="magnifying_glass", width=18, height=18, color="indigo"),
    icon(tag="magnifying_glass", width=18, height=18, color="cyan"),
    icon(tag="magnifying_glass", width=18, height=18, color="orange"),
    icon(tag="magnifying_glass", width=18, height=18, color="crimson"),
    gap="2",
)
```

You can also use color with a scale such as below.

```python demo
flex(
    icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-1)"),
    icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-2)"),
    icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-3)"),
    icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-4)"),
    icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-5)"),
    icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-6)"),
    icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-7)"),
    icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-8)"),
    icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-9)"),
    icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-10)"),
    icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-11)"),
    icon(tag="magnifying_glass", width=18, height=18, color="var(--purple-12)"),
    gap="2",
)
```

Here is another example using the `accent` color with scales. The `accent` is the most dominant color in your theme.

```python demo
flex(
    icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-1)"),
    icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-2)"),
    icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-3)"),
    icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-4)"),
    icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-5)"),
    icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-6)"),
    icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-7)"),
    icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-8)"),
    icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-9)"),
    icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-10)"),
    icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-11)"),
    icon(tag="magnifying_glass", width=18, height=18, color="var(--accent-12)"),
    gap="2",
)
```

## Final Example

Icons can be used as child components of many other components. Here is an example of a search bar with a magnifying glass icon.

```python demo
badge(
    flex(
        icon(tag="magnifying_glass", height=18, width=18),
        text("Search documentation...", size="3", weight="medium"),
        direction="row",
        gap="1",
        align="center",
    ),
    size="2",
    radius="full",
    color_scheme="gray",
)
```
