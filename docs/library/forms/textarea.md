---
components:
    - rx.radix.text_area
---

```python exec
import reflex as rx
rdx = rx.radix
```

# TextArea

A text area is a multi-line text input field. This component uses Radix's [text area](https://radix-ui.com/primitives/docs/components/text-area) component.

## Basic Example

```python demo
rdx.text_area(
    placeholder="Type here...",
)
```

```python demo exec
class TextAreaBlur(rx.State):
    text: str = "Hello World!"


def blur_example():
    return rx.vstack(
        rdx.heading(TextAreaBlur.text),
        rdx.text_area(
            on_blur=TextAreaBlur.set_text,
        ),
    )
```


```python demo exec
class TextAreaControlled(rx.State):
    text: str = "Hello World!"


def controlled_example():
    return rx.vstack(
        rdx.heading(TextAreaControlled.text),
        rdx.text_area(
            value=TextAreaControlled.text,
            on_change=TextAreaControlled.set_text,
        ),
        rdx.text_area(
            value="Simon says: " + TextAreaControlled.text,
        ),
    )
```

# Real World Example

```python demo
rdx.card(
    rdx.flex(
        rdx.text("Are you enjoying Reflex?"),
        rdx.text_area(placeholder="Write your feedback…"),
        rdx.flex(
            rdx.text("Attach screenshot?", size="2"),
            rdx.switch(size="1", default_checked=True),
            justify="between",
        ),
        rdx.grid(
            rdx.button("Back", variant="surface"),
            rdx.button("Send"),
            columns="2",
            gap="2",
        ),
        direction="column",
        gap="3",
    ),
    style={"maxWidth": 500},
)
```