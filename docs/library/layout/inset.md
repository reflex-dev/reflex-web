---
components:
    - rx.radix.themes.Inset

Inset: |
    lambda **props: rx.radix.themes.card(
        rx.radix.themes.inset(
            rx.image(src="/reflex_banner.png", width="50%", height="auto"),
            **props
        ),
        rx.radix.themes.text("Reflex is a web framework that allows developers to build their app in pure Python."),
    )
---

```python exec
import reflex as rx
import reflex.components.radix.themes as rdxt
```

# Inset

Applies a negative margin to allow content to bleed into the surrounding container.

## Basic Example

Nesting an Inset component inside a Card will render the content from edge to edge of the card.

```python demo
rdxt.card(
    rdxt.inset(
        rx.image(src="/reflex_banner.png", width="100%", height="auto"),
        side="top",
        pb="current",
    ),
    rdxt.text("Reflex is a web framework that allows developers to build their app in pure Python."),
    width="25vw",
)
```

## Other Directions

The `side` prop controls which side the negative margin is applied to. When using a specific side,
it is helpful to set the padding for the opposite side to `current` to retain the same padding the
content would have had if it went to the edge of the parent component.

```python demo
rdxt.card(
    rdxt.text("The inset below uses a bottom side."),
    rdxt.inset(
        rx.image(src="/reflex_banner.png", width="100%", height="auto"),
        side="bottom",
        pt="current",
    ),
    width="25vw",
)
```

```python demo
rdxt.card(
    rdxt.flex(
        rdxt.text("This inset uses a right side, which requires a flex with direction row."),
        rdxt.inset(
            rdxt.box(background="center/cover url('/reflex_banner.png')", height="100%"),
            width="100%",
            side="right",
            pl="current",
        ),
        direction="row",
        width="100%",
    ),
    width="25vw",
)
```

```python demo
rdxt.card(
    rdxt.flex(
        rdxt.inset(
            rdxt.box(background="center/cover url('/reflex_banner.png')", height="100%"),
            width="100%",
            side="left",
            pr="current",
        ),
        rdxt.text("This inset uses a left side, which also requires a flex with direction row."),
        direction="row",
        width="100%",
    ),
    width="25vw",
)
```
