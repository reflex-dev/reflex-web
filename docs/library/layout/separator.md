---
components:
    - rx.radix.themes.Separator
---

```python exec
import reflex.components.radix.themes as rdxt
```

# Separator

Visually or semantically separates content.

## Basic Example

```python demo
rdxt.flex(
    rdxt.card("Section 1"),
    rdxt.separator(),
    rdxt.card("Section 2"),
    gap="4",
    direction="column",
    align="center",
)
```

## Size

The `size` prop controls how long the separator is. Using `size="4"` will make
the separator fill the parent container. Setting CSS `width` or `height` prop to `"100%"`
can also achieve this effect, but `size` works the same regardless of the orientation.

```python demo
rdxt.flex(
    rdxt.card("Section 1"),
    rdxt.separator(size="4"),
    rdxt.card("Section 2"),
    gap="4",
    direction="column",
)
```

## Orientation

Setting the orientation prop to `vertical` will make the separator appear vertically.

```python demo
rdxt.flex(
    rdxt.card("Section 1"),
    rdxt.separator(orientation="vertical", size="4"),
    rdxt.card("Section 2"),
    gap="4",
    width="100%",
    height="10vh",
)
```