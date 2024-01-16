---
components:
    - rx.radix.themes.TextArea
---

```python exec
import reflex as rx
import reflex.components.radix.themes as rdxt
```

# TextArea

A text area is a multi-line text input field. This component uses Radix's [text area](https://radix-ui.com/primitives/docs/components/text-area) component.

## Basic Example

```python demo
rdxt.textarea(
    placeholder="Type here...",
)
```

```python demo exec
class TextAreaBlur(rx.State):
    text: str = "Hello World!"


def blur_example():
    return rx.vstack(
        rdxt.heading(TextAreaBlur.text),
        rdxt.textarea(
            on_blur=TextAreaBlur.set_text,
        ),
    )
```


```python demo exec
class TextAreaControlled(rx.State):
    text: str = "Hello World!"


def controlled_example():
    return rx.vstack(
        rdxt.heading(TextAreaControlled.text),
        rdxt.textarea(
            value=TextAreaControlled.text,
            on_change=TextAreaControlled.set_text,
        ),
    )
```