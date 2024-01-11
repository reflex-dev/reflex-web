---
components:
  - rx.radix.themes.Card
---

```python exec
import reflex as rx
import reflex.components.radix.themes as rdxt
```

# Card

A Card component is used for grouping related components. It is similar to the Box, except it has a
border, uses the theme colors and border radius, and provides a `size` prop to control spacing
and margin according to the Radix `"1"` - `"5"` scale.

The Card requires less styling than a Box to achieve consistent visual results when used with
themes.

## Basic Example

```python demo
rdxt.flex(
    rdxt.card("Card 1", size="1"),
    rdxt.card("Card 2", size="2"),
    rdxt.card("Card 3", size="3"),
    rdxt.card("Card 4", size="4"),
    rdxt.card("Card 5", size="5"),
    gap="2",
    align_items="flex-start",
    flex_wrap="wrap",
)
```

## Rendering as a Different Element

The `as_child` prop may be used to render the Card as a different element. Link and Button are
commonly used to make a Card clickable.

```python demo
rdxt.card(
    rdxt.link(
        rdxt.flex(
            rdxt.avatar(src="/reflex_banner.png"),
            rdxt.box(
                rdxt.heading("Quick Start"),
                rdxt.text("Get started with Reflex in 5 minutes."),
            ),
            gap="2",
        ),
    ),
    as_child=True,
)
```

## Using Inset Content

Nesting an Inset component inside a Card will render the content from edge to edge of the card.

```python demo
rdxt.card(
    rdxt.inset(
        rx.image(src="/reflex_banner.png", width="100%", height="auto"),
        clip="padding-box",
        side="top",
        pb="current",
    ),
    rdxt.text("Reflex is a web framework that allows developers to build their app in pure Python."),
    width="25vw",
)
```