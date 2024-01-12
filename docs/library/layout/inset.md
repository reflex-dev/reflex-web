---
components:
    - rx.radix.themes.Inset
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
        clip="padding-box",
        side="top",
        pb="current",
    ),
    rdxt.text("Reflex is a web framework that allows developers to build their app in pure Python."),
    width="25vw",
)
```