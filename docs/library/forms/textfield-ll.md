---
components:
    - rx.radix.text_field
    - rx.radix.text_field.root
    - rx.radix.text_field.input
    - rx.radix.text_field.slot
---

```python exec
import reflex as rx
rdx = rx.radix
```


# TextField

A text field is an input field that users can type into. This component uses Radix's [text field](https://radix-ui.com/primitives/docs/components/text-field) component.

## Basic Example

```python demo
rdx.text_field.root(
    rdx.text_field.slot(
        rdx.icon(tag="magnifying_glass"),
    ),
    rdx.text_field.input(
        placeholder="Search here...",
    ),
)
```

```python demo exec
class TextfieldBlur1(rx.State):
    text: str = "Hello World!"


def blur_example1():
    return rx.vstack(
        rdx.heading(TextfieldBlur1.text),
        rdx.text_field.root(
            rdx.text_field.slot(
                rdx.icon(tag="magnifying_glass"),
            ),
            rdx.text_field.input(
                placeholder="Search here...",
                on_blur=TextfieldBlur1.set_text,
            ),
            
        )
    )
```


```python demo exec
class TextfieldControlled1(rx.State):
    text: str = "Hello World!"


def controlled_example1():
    return rx.vstack(
        rdx.heading(TextfieldControlled1.text),
        rdx.text_field.root(
            rdx.text_field.slot(
                rdx.icon(tag="magnifying_glass"),
            ),
            rdx.text_field.input(
                placeholder="Search here...",
                value=TextfieldControlled1.text,
                on_change=TextfieldControlled1.set_text,
            ),
        ),
    )
```


# Real World Example

```python demo exec

def song(title, initials: str, genre: str):
    return rdx.card(rdx.flex(
        rdx.flex(
            rdx.avatar(fallback=initials),
            rdx.flex(
                rdx.text(title, size="2", weight="bold"),
                rdx.text(genre, size="1", color_scheme="gray"),
                direction="column",
                gap="1",
            ),
            direction="row",
            align_items="left",
            gap="1",
        ),
        rdx.flex(
            rdx.icon(tag="chevron_right"),
            align_items="center",
        ),
        justify="between",
    ))

def search():
    return rdx.card(
    rdx.flex(
        rdx.text_field.root(
            rdx.text_field.slot(
                rdx.icon(tag="magnifying_glass"),
            ),
            rdx.text_field.input(
                placeholder="Search songs...",
            ),
        ),
        rdx.flex(
            song("The Less I Know", "T", "Rock"),
            song("Breathe Deeper", "ZB", "Rock"),
            song("Let It Happen", "TF", "Rock"),
            song("Borderline", "ZB", "Pop"),
            song("Lost In Yesterday", "TO", "Rock"),
            song("Is It True", "TO", "Rock"),
            direction="column",
            gap="1",
        ),
        direction="column",
        gap="3",
    ),
    style={"maxWidth": 500},
)
```