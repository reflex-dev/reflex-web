---
components:
    - rx.radix.separator
---

```python exec
import reflex as rx
rdx = rx.radix
```

# Separator

Visually or semantically separates content.

## Basic Example

```python demo
rdx.flex(
    rdx.card("Section 1"),
    rdx.separator(),
    rdx.card("Section 2"),
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
rdx.flex(
    rdx.card("Section 1"),
    rdx.separator(size="4"),
    rdx.card("Section 2"),
    gap="4",
    direction="column",
)
```

## Orientation

Setting the orientation prop to `vertical` will make the separator appear vertically.

```python demo
rdx.flex(
    rdx.card("Section 1"),
    rdx.separator(orientation="vertical", size="4"),
    rdx.card("Section 2"),
    gap="4",
    width="100%",
    height="10vh",
)
```