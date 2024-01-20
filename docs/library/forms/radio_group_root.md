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














# Radio Group

A set of interactive radio buttons where only one can be selected at a time.


## Basic example

```python demo
radio_group_root(
    radio_group_item(value="1"),
    radio_group_item(value="2"),
    radio_group_item(value="3"),
    default_value="1",
)

```

The `radio_group_root` contains all the parts of a radio group. The `radio_group_item` is an item in the group that can be checked.

The `default_value` prop can be used to set the value of the radio item that should be checked when initially rendered.


## Radio Group Root 


### Control the value
The controlled `value` of the radio item to check. Should be used in conjunction with `on_value_change` event handler.


```python demo exec
class RadioState1(rx.State):
    text: str = "No Selection"


def radio_state_example():
    return rx.vstack(
        rx.badge(RadioState1.text, color_scheme="green"),
        radio_group_root(
            radio_group_item(value="1"),
            radio_group_item(value="2"),
            radio_group_item(value="3"),
            on_value_change=RadioState1.set_text,
        ),
    )
```


When the `disabled` prop is set to `True`, it prevents the user from interacting with radio items.

```python demo
flex(
    radio_group_root(
        radio_group_item(value="1"),
        radio_group_item(value="2"),
    ),
    radio_group_root(
        radio_group_item(value="1"),
        radio_group_item(value="2"),
        disabled=True,
    ),
    gap="2",
)

```


### Submitting a form using Radio Group

The `name` prop is used to name the group. It is submitted with its owning form as part of a name/value pair.

When the `required` prop is `True`, it indicates that the user must check a radio item before the owning form can be submitted.

```python demo exec
class FormRadioState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def form_example():
    return rx.vstack(
        rx.form(
            rx.vstack(
                radio_group_root(
                    "Radio Group ",
                    radio_group_item(value="1"),
                    radio_group_item(value="2"),
                    radio_group_item(value="3"),
                    name="radio",
                    required=True,
                ),
                rx.button("Submit", type_="submit"),
            ),
            on_submit=FormRadioState.handle_submit,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(FormRadioState.form_data.to_string()),
    )
```




## Radio Group Item 


### value
The `value` given as data when submitted with a `name` on `radio_group_root`.


### disabled

Use the `disabled` prop to create a disabled radiobutton. When `True`, prevents the user from interacting with the radio item. This differs from the `disabled` prop used by the `radio_group_root`, which allows you to disable all the `radio_group_item` components within the `radio_group_root`.

```python demo
flex(
    radio_group_root(
        flex(
            text(
                flex(
                    radio_group_item(value="1"),
                    "Off",
                    gap="2",
                ),
                as_="label",
                size="2",
            ),
            text(
                flex(
                    radio_group_item(value="2"),
                    "On",
                    gap="2",
                ),
                as_="label",
                size="2",
            ),
            direction="column",
            gap="2",
        ),
    ),
    radio_group_root(
        flex(
            text(
                flex(
                    radio_group_item(value="1", disabled=True),
                    "Off",
                    gap="2",
                ),
                as_="label",
                size="2",
                color="gray",
            ),
            text(
                flex(
                    radio_group_item(value="2"),
                    "On",
                    gap="2",
                ),
                as_="label",
                size="2",
                color="gray",
            ),
            direction="column",
            gap="2",
        ),
    ),
    direction="column",
    gap="2",

)
```

### required


When `True`, indicates that the user must check the `radio_item_group` before the owning form can be submitted. This can only be used when a single `radio_group_item` is used.


```python demo exec
class FormRadioState2(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def form_example2():
    return rx.vstack(
        rx.form(
            rx.vstack(
                radio_group_root(
                    radio_group_item(value="1", required=True),
                    name="radio",
                ),
                rx.button("Submit", type_="submit"),
            ),
            on_submit=FormRadioState2.handle_submit,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(FormRadioState2.form_data.to_string()),
    )
```




## Styling

### size

```python demo
flex(
    radio_group_root(
        radio_group_item(value="1"),
        size="1",
    ),
    radio_group_root(
        radio_group_item(value="1"),
        size="2",
    ),
    radio_group_root(
        radio_group_item(value="1"),
        size="3",
    ),
    gap="2",
)

```

### variant

```python demo
flex(
    flex(
        radio_group_root(
            radio_group_item(value="1"),
            radio_group_item(value="2"),
            variant="surface",
            default_value="1",
        ),
        direction="column",
        gap="2",
        as_child=True,
    ),
    flex(
        radio_group_root(
            radio_group_item(value="1"),
            radio_group_item(value="2"),
            variant="classic",
            default_value="1",
        ),
        direction="column",
        gap="2",
        as_child=True,
    ),
    flex(
        radio_group_root(
            radio_group_item(value="1"),
            radio_group_item(value="2"),
            variant="soft",
            default_value="1",
        ),
        direction="column",
        gap="2",
        as_child=True,
    ),
    gap="2",
)
```


### color

```python demo
flex(
    radio_group_root(
        radio_group_item(value="1"),
        color_scheme="indigo",
        default_value="1",
    ),
    radio_group_root(
        radio_group_item(value="1"),
        color_scheme="cyan",
        default_value="1",
    ),
    radio_group_root(
        radio_group_item(value="1"),
        color_scheme="orange",
        default_value="1",
    ),
    radio_group_root(
        radio_group_item(value="1"),
        color_scheme="crimson",
        default_value="1",
    ),
    gap="2"
)
```

### high_contrast

Use the `high_contrast` prop to increase color contrast with the background.

```python demo
grid(
    radio_group_root(
        radio_group_item(value="1"),
        color_scheme="cyan",
        default_value="1",
    ),
    radio_group_root(
        radio_group_item(value="1"),
        color_scheme="cyan",
        default_value="1",
        high_contrast=True,
    ),
    radio_group_root(
        radio_group_item(value="1"),
        color_scheme="indigo",
        default_value="1",
    ),
    radio_group_root(
        radio_group_item(value="1"),
        color_scheme="indigo",
        default_value="1",
        high_contrast=True,
    ),
    radio_group_root(
        radio_group_item(value="1"),
        color_scheme="orange",
        default_value="1",
    ),
    radio_group_root(
        radio_group_item(value="1"),
        color_scheme="orange",
        default_value="1",
        high_contrast=True,
    ),
    radio_group_root(
        radio_group_item(value="1"),
        color_scheme="crimson",
        default_value="1",
    ),
    radio_group_root(
        radio_group_item(value="1"),
        color_scheme="crimson",
        default_value="1",
        high_contrast=True,
    ),
    rows="2",
    gap="2",
    display="inline-grid",
    flow="column"
)
```


### alignment 


Composing `radio_group_item` within `text` automatically centers it with the first line of text.


```python demo
flex(
    radio_group_root(
        text(
            flex(
                radio_group_item(value="1"),
                "Default",
                gap="2",
            ),
            size="2",
            as_="label",
        ),
        text(
            flex(
                radio_group_item(value="2"),
                "Compact",
                gap="2",
            ),
            size="2",
            as_="label",
        ),
        default_value="1",
        size="1",
    ),
    radio_group_root(
        text(
            flex(
                radio_group_item(value="1"),
                "Default",
                gap="2",
            ),
            size="3",
            as_="label",
        ),
        text(
            flex(
                radio_group_item(value="2"),
                "Compact",
                gap="2",
            ),
            size="3",
            as_="label",
        ),
        default_value="1",
        size="2",
    ),
    radio_group_root(
        text(
            flex(
                radio_group_item(value="1"),
                "Default",
                gap="2",
            ),
            size="4",
            as_="label",
        ),
        text(
            flex(
                radio_group_item(value="2"),
                "Compact",
                gap="2",
            ),
            size="4",
            as_="label",
        ),
        default_value="1",
        size="3",
    ),
    gap="3",
    direction="column",
)
```


```python eval
style_grid(component_used=radio_group_root, component_used_str="radiogrouproot", variants=["classic", "surface", "soft"], components_passed=radio_group_item(), disabled=True,)
```




## Real World Example

```python demo
radio_group_root(
    flex(
        text(
            flex(
                radio_group_item(value="1"),
                "Default",
                gap="2",
            ),
            size="2",
            as_="label",
        ),
        text(
            flex(
                radio_group_item(value="2"),
                "Comfortable",
                gap="2",
            ),
            size="2",
            as_="label",
        ),
        text(
            flex(
                radio_group_item(value="3"),
                "Compact",
                gap="2",
            ),
            size="2",
            as_="label",
        ),
        direction="column",
        gap="2",
    ),
    default_value="1",
)
```
