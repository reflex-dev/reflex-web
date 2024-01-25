---
components:
    - rx.radix.themes.Input
    - rx.radix.themes.TextFieldRoot
    - rx.radix.themes.TextFieldInput
    - rx.radix.themes.TextFieldSlot
---

```python exec
import reflex as rx
import reflex.components.radix.themes as rdxt
```


# Input (High Level API for TextField)


The `input` component is an input field that users can type into. 


## Basic Example

```python demo
rdxt.input(icon="magnifying_glass")
```

Can set an `icon` for the `input` component using the `icon` prop. 


### Setting Defaults

Can set defaults for a `placeholder` for text to show in the `input` box before any text is input into it.

Can limit the `max_length` allowed as input into the `input` box.

```python demo
rdxt.input(icon="magnifying_glass", placeholder="Search here...", max_length="20")
```




### Using Event Handlers


The `on_blur` event handler is called when focus has left the `input` for example, it’s called when the user clicks outside of a focused text input.

```python demo exec
class TextfieldBlur(rx.State):
    text: str = "Hello World!"


def blur_example():
    return rx.vstack(
        rdxt.heading(TextfieldBlur.text),
        rdxt.input(
            icon="magnifying_glass", 
            placeholder="Search here...", 
            on_blur=TextfieldBlur.set_text,
        ),
    )
```


The `on_change` event handler is called when the `value` of `input` has changed.

```python demo exec
class TextfieldControlled(rx.State):
    text: str = "Hello World!"


def controlled_example():
    return rx.vstack(
        rdxt.heading(TextfieldControlled.text),
        rdxt.input(
            icon="magnifying_glass", 
            placeholder="Search here...", 
            value=TextfieldControlled.text,
            on_change=TextfieldControlled.set_text,
        ),
    )
```




### Submitting a form using input

The `name` prop is needed to submit with its owning form as part of a name/value pair.

When the `required` prop is `True`, it indicates that the user must input text before the owning form can be submitted.


```python demo exec
class FormInputState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def form_input1():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rdxt.input(name="input", default_value="search", placeholder="Input text here...",),
                rdxt.button("Submit", type_="submit"),
                width="100%",
            ),
            on_submit=FormInputState.handle_submit,
            reset_on_submit=True,
            width="100%",
        ),
        rdxt.separator(width="100%"),
        rdxt.heading("Results"),
        rdxt.text(FormInputState.form_data.to_string()),
        width="100%",
    )
```




## Real World Example

```python demo exec

def song(title, initials: str, genre: str):
    return rdxt.card(rdxt.flex(
        rdxt.flex(
            rdxt.avatar(fallback=initials),
            rdxt.flex(
                rdxt.text(title, size="2", weight="bold"),
                rdxt.text(genre, size="1", color_scheme="gray"),
                direction="column",
                gap="1",
            ),
            direction="row",
            align_items="left",
            gap="1",
        ),
        rdxt.flex(
            rdxt.icon(tag="chevron_right"),
            align_items="center",
        ),
        justify="between",
    ))


def search():
    return rdxt.card(
    rdxt.flex(
        rdxt.input(icon="magnifying_glass", placeholder="Search songs...", ),
        rdxt.flex(
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







