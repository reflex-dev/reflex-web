---
components:
    - rx.radix.themes.HighLevelRadioGroup
    - rx.radix.themes.RadioGroupRoot
    - rx.radix.themes.RadioGroupItem
---


```python exec
import reflex as rx
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
import reflex.components.radix.primitives as rdxp
import reflex.components.radix.themes as rdxt
from pcweb.templates.docpage import style_grid
```


# High Level Radio Group

A set of interactive radio buttons where only one can be selected at a time.

## Basic example


```python demo
rdxt.radio_group(["1", "2", "3"], default_value="1")
```

The `default_value` prop can be used to set the value of the radio item that should be checked when initially rendered.



## Setting direction, spacing and size


The direction of the `radio_group` can be set using the `direction` prop which takes values `'row' | 'column' | 'row-reverse' | 'column-reverse' |`. 

The gap between the `radio_group` items can also be set using the `gap` prop, which takes values `'1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' |`.

The size of the `radio_group` items and the associated text can be set with the `size` prop, which can take values `1' | '2' | '3' |`

```python demo
radio_group(["1", "2", "3", "4", "5"], direction="row", gap="8", size="3")
```


## Using State Vars in the RadioGroup


State vars can also be passed in as the `items` to the `radiogroup`.


```python demo exec
class RadioState_HL1(rx.State):
    items: list[str] = ["1", "2", "3"]

def radio_state_example_HL1():
    return rdxt.radio_group(RadioState_HL1.items, direction="row", gap="9")
```


### Control the value
The controlled `value` of the radio item to check. Should be used in conjunction with `on_value_change` event handler.


```python demo exec
class RadioState_HL(rx.State):
    text: str = "No Selection"


def radio_state_example_HL():
    return rx.vstack(
        rdxt.badge(RadioState_HL.text, color_scheme="green"),
        rdxt.radio_group(["1", "2", "3"], on_value_change=RadioState_HL.set_text),
    )
```


When the `disabled` prop is set to `True`, it prevents the user from interacting with radio items.

```python demo
flex(
    rdxt.radio_group(["1", "2"]),
    rdxt.radio_group(["1", "2"], disabled=True),
    gap="2",
)

```


### Submitting a form using Radio Group

The `name` prop is used to name the group. It is submitted with its owning form as part of a name/value pair.

When the `required` prop is `True`, it indicates that the user must check a radio item before the owning form can be submitted.

```python demo exec
class FormRadioState_HL(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def form_example_HL():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rdxt.radio_group(["1", "2", "3"], name="radio", required=True,),
                rx.button("Submit", type_="submit"),
            ),
            on_submit=FormRadioState_HL.handle_submit,
            reset_on_submit=True,
        ),
        rdxt.separator(width="100%"),
        rdxt.heading("Results"),
        rdxt.text(FormRadioState_HL.form_data.to_string()),
    )
```




