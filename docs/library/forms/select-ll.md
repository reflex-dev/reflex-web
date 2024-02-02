---
components:
    - rx.radix.select
    - rx.radix.select.root
    - rx.radix.select.trigger
    - rx.radix.select.content
    - rx.radix.select.group
    - rx.radix.select.item
    - rx.radix.select.label
    - rx.radix.select.separator
---


```python exec
import random
import reflex as rx
rdx = rx.radix
import reflex.components.radix.primitives as rdxp
from pcweb.templates.docpage import style_grid
```



# Select

Displays a list of options for the user to pick from, triggered by a button.


## Basic Example


```python demo
rdx.select.root(
    rdx.select.trigger(),
    rdx.select.content(
        rdx.select.group(
            rdx.select.label("Fruits"),
            rdx.select.item("Orange", value="orange"),
            rdx.select.item("Apple", value="apple"),
            rdx.select.item("Grape", value="grape", disabled=True),
        ),
        rdx.select.separator(),
        rdx.select.group(
            rdx.select.label("Vegetables"),
            rdx.select.item("Carrot", value="carrot"),
            rdx.select.item("Potato", value="potato"),
        ),
    ),
    default_value="apple",
)
```


## Usage


## Disabling 


It is possible to disable individual items in a `select` using the `disabled` prop associated with the `rdx.select.item`.

```python demo
rdx.select.root(
    rdx.select.trigger(placeholder="Select a Fruit"),
    rdx.select.content(
        rdx.select.group(
            rdx.select.item("Apple", value="apple"),
            rdx.select.item("Grape", value="grape", disabled=True),
            rdx.select.item("Pineapple", value="pineapple"),
        ),
    ),
)
```

To prevent the user from interacting with select entirely, set the `disabled` prop to `True` on the `rdx.select.root` component.

```python demo
rdx.select.root(
    rdx.select.trigger(placeholder="This is Disabled"),
    rdx.select.content(
        rdx.select.group(
            rdx.select.item("Apple", value="apple"),
            rdx.select.item("Grape", value="grape"),
        ),
    ),
    disabled=True,
)
```


## Setting Defaults 


It is possible to set several default values when constructing a `select`. 


The `placeholder` prop in the `rdx.select.trigger` specifies the content that will be rendered when `value` or `default_value` is empty or not set.


```python demo
rdx.select.root(
    rdx.select.trigger(placeholder="pick a fruit"),
    rdx.select.content(
        rdx.select.group(
            rdx.select.item("Apple", value="apple"),
            rdx.select.item("Grape", value="grape"),
        ),
    ),
)
```

The `default_value` in the `rdx.select.root` specifies the value of the `select` when initially rendered.
The `default_value` should correspond to the `value` of a child `rdx.select.item`.


```python demo
rdx.select.root(
    rdx.select.trigger(),
    rdx.select.content(
        rdx.select.group(
            rdx.select.item("Apple", value="apple"),
            rdx.select.item("Grape", value="grape"),
        ),
    ),
    default_value="apple",
)
```



## Fully controlled


The `on_change` event trigger is fired when the value of the select changes.
In this example the `rdx.select_root` `value` prop specifies which item is selected, and this 
can also be controlled using state and a button without direct interaction with the select component.

```python demo exec
class SelectState2(rx.State):
    
    values: list[str] = ["apple", "grape", "pear"]
    
    value: str = ""

    def choose_randomly(self):
        """Change the select value var."""
        original_value = self.value
        while self.value == original_value:
            self.value = random.choice(self.values)


def select_example2():
    return rx.vstack(
        rdx.select.root(
            rdx.select.trigger(placeholder="No Selection"),
            rdx.select.content(
                rdx.select.group(
                    rx.foreach(SelectState2.values, lambda x: rdx.select.item(x, value=x))
                ),
            ),
            value=SelectState2.value,
            on_change=SelectState2.set_value,
            
        ),
        rdx.button("Choose Randomly", on_click=SelectState2.choose_randomly),
        rdx.button("Reset", on_click=SelectState2.set_value("")),
    )
```



The `open` prop and `on_open_change` event trigger work similarly to `value` and `on_change` to control the open state of the select.
If `on_open_change` handler does not alter the `open` prop, the select will not be able to be opened or closed by clicking on the
`select_trigger`.


 ```python demo exec
class SelectState8(rx.State):
    is_open: bool = False
    
def select_example8():    
    return rdx.flex(
        rdx.select.root(
            rdx.select.trigger(placeholder="No Selection"),
            rdx.select.content(
                rdx.select.group(
                    rdx.select.item("Apple", value="apple"),
                    rdx.select.item("Grape", value="grape"),
                ),
            ),
            open=SelectState8.is_open,
            on_open_change=SelectState8.set_is_open,
        ),
        rdx.button("Toggle", on_click=SelectState8.set_is_open(~SelectState8.is_open)),
        gap="2",
    )
```



### Submitting a Form with Select

When a select is part of a form, the `name` prop of the `rdx.select.root` sets the key that will be submitted with the form data.

The `value` prop of `rdx.select.item` provides the value to be associated with the `name` key when the form is submitted with that item selected.

When the `required` prop of the `rdx.select.root` is `True`, it indicates that the user must select a value before the form may be submitted.

```python demo exec
class FormSelectState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def form_select():
    return rdx.flex(
        rdx.form.root(
            rdx.flex(
                rdx.select.root(
                    rdx.select.trigger(),
                    rdx.select.content(
                        rdx.select.group(
                            rdx.select.label("Fruits"),
                            rdx.select.item("Orange", value="orange"),
                            rdx.select.item("Apple", value="apple"),
                            rdx.select.item("Grape", value="grape"),
                        ),
                        rdx.select.separator(),
                        rdx.select.group(
                            rdx.select.label("Vegetables"),
                            rdx.select.item("Carrot", value="carrot"),
                            rdx.select.item("Potato", value="potato"),
                        ),
                    ),
                    default_value="apple",
                    name="select",
                ),
                rdx.button("Submit"),
                width="100%",
                direction="column",
                gap="2",
            ),
            on_submit=FormSelectState.handle_submit,
            reset_on_submit=True,
        ),
        rdx.separator(size="4"),
        rdx.heading("Results"),
        rdx.text(FormSelectState.form_data.to_string()),
        width="100%",
        direction="column",
        gap="2",
    )
```

## Real World Example

```python demo
rdx.card(
    rdx.flex(
        rx.image(src="/reflex_logo.png", width="100%", height="auto"),
        rdx.flex(
            rdx.heading("Reflex Swag", size="4", margin_bottom="4px"),
            rdx.heading("$99", size="6", margin_bottom="4px"),
            direction="row", justify="between",
            width="100%",
        ),
        rdx.text("Reflex swag with a sense of nostalgia, as if they carry whispered tales of past adventures", size="2", margin_bottom="4px"),
        rdx.separator(size="4"),
        rdx.flex(
            rdx.flex(
                rdx.text("Color", size="2", margin_bottom="4px", color_scheme="gray"),
                rdx.select.root(
                    rdx.select.trigger(),
                    rdx.select.content(
                        rdx.select.group(
                            rdx.select.item("Light", value="light"),
                            rdx.select.item("Dark", value="dark"),
                        ),
                    ),
                    default_value="light",
                ),
                direction="column",
            ),
            rdx.flex(
                rdx.text("Size", size="2", margin_bottom="4px", color_scheme="gray"),
                rdx.select.root(
                    rdx.select.trigger(),
                    rdx.select.content(
                        rdx.select.group(
                            rdx.select.item("24", value="24"),
                            rdx.select.item("26", value="26"),
                            rdx.select.item("28", value="28", disabled=True),
                            rdx.select.item("30", value="30"),
                            rdx.select.item("32", value="32"),
                            rdx.select.item("34", value="34"),
                            rdx.select.item("36", value="36"),
                        ),
                    ),
                    default_value="30",
                ),
                direction="column",
            ),
            rdx.button(rdx.icon(tag="plus"), "Add"),
            align="end",
            justify="between",
            gap="2",
            width="100%",
        ),
        width="15em",
        direction="column",
        gap="2",
    ),
)
```