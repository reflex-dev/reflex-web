---
components:
    - rx.radix.themes.HighLevelSelect
    - rx.radix.themes.SelectRoot
    - rx.radix.themes.SelectTrigger
    - rx.radix.themes.SelectContent
    - rx.radix.themes.SelectGroup
    - rx.radix.themes.SelectItem
    - rx.radix.themes.SelectLabel
    - rx.radix.themes.SelectSeparator
    
---


```python exec
import random
import reflex as rx
import reflex.components.radix.themes as rdxt
import reflex.components.radix.primitives as rdxp
from pcweb.templates.docpage import style_grid
```

# High Level Select

Displays a list of options for the user to pick from—triggered by a button.

## Basic Example

```python demo
rdxt.select(["Apple", "Orange", "Banana", "Grape", "Pear"])
```




## Disabling

To prevent the user from interacting with select, set the `disabled` prop to `True`.

```python demo
rdxt.select(["Apple", "Orange", "Banana", "Grape", "Pear"], disabled=True)
```


## Setting Defaults 


It is possible to set several default values when constructing a `select`. 

Can set the `placeholder` prop, which is the content that will be rendered when no value or no default_value is set.

Can set the `label` prop, which is a label in the `select`.


```python demo
rdxt.select(["Apple", "Orange", "Banana", "Grape", "Pear"], placeholder="Selection of Fruits", label="Fruits")
```

Can set the `default_value` prop, which is the value of the `select` when initially rendered.


```python demo
rdxt.select(["Apple", "Orange", "Banana", "Grape", "Pear"], default_value="Orange")
```



## Simple Styling

Can set the `color`, `variant` and `radius` to easily style the `select`.


```python demo
rdxt.select(["Apple", "Orange", "Banana", "Grape", "Pear"], color="pink", variant="soft", radius="full", width="100%")
```




## High control of select component (value and open changes)


The `on_value_change` event is called when the value of the `select` changes. In this example we set the `value` prop to change the select `value` using a button in this case. 

```python demo exec
class SelectState3(rx.State):
    
    values: list[str] = ["apple", "grape", "pear"]
    
    value: str = "apple"

    def change_value(self):
        """Change the select value var."""
        self.value = random.choice(self.values)


def select_example3():
    return rx.vstack(
        rdxt.select(
            SelectState3.values,
            value=SelectState3.value,
            on_value_change=SelectState3.set_value,
        ),
        rdxt.button("Change Value", on_click=SelectState3.change_value),
        
    )
```


The `on_open_change` event handler acts in a similar way to the `on_value_change` and is called when the open state of the select changes.

```python demo
rdxt.select(
    ["apple", "grape", "pear"],
    on_value_change=rx.window_alert("on_value_change event handler called"),
)

```
 



### Submitting a form using select

The `name` prop is needed to submit with its owning form as part of a name/value pair.

When the `required` prop is `True`, it indicates that the user must select a value before the owning form can be submitted.


```python demo exec
class FormSelectState1(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def form_select1():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rdxt.select(
                    ["apple", "grape", "pear"],
                    default_value="apple",
                    name="select",
                ),
                rdxt.button("Submit", type_="submit"),
                width="100%",
            ),
            on_submit=FormSelectState1.handle_submit,
            reset_on_submit=True,
            width="100%",
        ),
        rdxt.separator(width="100%"),
        rdxt.heading("Results"),
        rdxt.text(FormSelectState1.form_data.to_string()),
        width="100%",
    )
```





## Real World Example


```python demo
rdxt.card(
    rx.vstack(
        rx.image(src="/reflex_logo.png", width="100%", height="auto"),
        rdxt.flex(
            rdxt.heading("Reflex Swag", size="4", mb="1"),
            rdxt.heading("$99", size="6", mb="1"),
            direction="row", justify="between",
            width="100%",
        ),
        rdxt.text("Reflex swag with a sense of nostalgia, as if they carry whispered tales of past adventures", size="2", mb="1"),
        rdxt.separator(width="100%"),
        rdxt.flex(
            rdxt.flex(
                rdxt.text("Color", size="2", mb="1", color_scheme="gray"),
                rdxt.select(["light", "dark"], default_value="light"),
                direction="column",
            ),
            rdxt.flex(
                rdxt.text("Size", size="2", mb="1", color_scheme="gray"),
                rdxt.select(["24", "26", "28", "30", "32", "34", "36"], default_value="30"),
                direction="column",
            ),
            rdxt.flex(
                rdxt.text(".", size="2",),
                rdxt.button("Add to cart"),
                direction="column",
            ),
            direction="row",
            justify="between",
            width="100%",
        ),
        width="20vw",
    ),
)
```
















# Select

Displays a list of options for the user to pick from, triggered by a button.


## Basic Example


```python demo
rdxt.select_root(
    rdxt.select_trigger(),
    rdxt.select_content(
        rdxt.select_group(
            rdxt.select_label("Fruits"),
            rdxt.select_item("Orange", value="orange"),
            rdxt.select_item("Apple", value="apple"),
            rdxt.select_item("Grape", value="grape", disabled=True),
        ),
        rdxt.select_separator(),
        rdxt.select_group(
            rdxt.select_label("Vegetables"),
            rdxt.select_item("Carrot", value="carrot"),
            rdxt.select_item("Potato", value="potato"),
        ),
    ),
    default_value="apple",
)
```


## Usage


## Disabling 


It is possible to disable individual items in a `select` using the `disabled` prop associated with the `rdxt.select_item`.

```python demo
rdxt.select_root(
    rdxt.select_trigger(placeholder="Select a Fruit"),
    rdxt.select_content(
        rdxt.select_group(
            rdxt.select_item("Apple", value="apple"),
            rdxt.select_item("Grape", value="grape", disabled=True),
            rdxt.select_item("Pineapple", value="pineapple"),
        ),
    ),
)
```

To prevent the user from interacting with select entirely, set the `disabled` prop to `True` on the `rdxt.select_root` component.

```python demo
rdxt.select_root(
    rdxt.select_trigger(placeholder="This is Disabled"),
    rdxt.select_content(
        rdxt.select_group(
            rdxt.select_item("Apple", value="apple"),
            rdxt.select_item("Grape", value="grape"),
        ),
    ),
    disabled=True,
)
```


## Setting Defaults 


It is possible to set several default values when constructing a `select`. 


The `placeholder` prop in the `rdxt.select_trigger` specifies the content that will be rendered when `value` or `default_value` is empty or not set.


```python demo
rdxt.select_root(
    rdxt.select_trigger(placeholder="pick a fruit"),
    rdxt.select_content(
        rdxt.select_group(
            rdxt.select_item("Apple", value="apple"),
            rdxt.select_item("Grape", value="grape"),
        ),
    ),
)
```

The `default_value` in the `rdxt.select_root` specifies the value of the `select` when initially rendered.
The `default_value` should correspond to the `value` of a child `rdxt.select_item`.


```python demo
rdxt.select_root(
    rdxt.select_trigger(),
    rdxt.select_content(
        rdxt.select_group(
            rdxt.select_item("Apple", value="apple"),
            rdxt.select_item("Grape", value="grape"),
        ),
    ),
    default_value="apple",
)
```



## Fully controlled


The `on_value_change` event trigger is fired when the value of the select changes.
In this example the `rdxt.select_root` `value` prop specifies which item is selected, and this 
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
        rdxt.select_root(
            rdxt.select_trigger(placeholder="No Selection"),
            rdxt.select_content(
                rdxt.select_group(
                    rx.foreach(SelectState2.values, lambda x: rdxt.select_item(x, value=x))
                ),
            ),
            value=SelectState2.value,
            on_value_change=SelectState2.set_value,
            
        ),
        rdxt.button("Choose Randomly", on_click=SelectState2.choose_randomly),
        rdxt.button("Reset", on_click=SelectState2.set_value("")),
    )
```



The `open` prop and `on_open_change` event trigger work similarly to `value` and `on_value_change` to control the open state of the select.
If `on_open_change` handler does not alter the `open` prop, the select will not be able to be opened or closed by clicking on the
`select_trigger`.


 ```python demo exec
class SelectState8(rx.State):
    is_open: bool = False
    
def select_example8():    
    return rdxt.flex(
        rdxt.select_root(
            rdxt.select_trigger(placeholder="No Selection"),
            rdxt.select_content(
                rdxt.select_group(
                    rdxt.select_item("Apple", value="apple"),
                    rdxt.select_item("Grape", value="grape"),
                ),
            ),
            open=SelectState8.is_open,
            on_open_change=SelectState8.set_is_open,
        ),
        rdxt.button("Toggle", on_click=SelectState8.set_is_open(~SelectState8.is_open)),
        gap="2",
    )
```



### Submitting a Form with Select

When a select is part of a form, the `name` prop of the `rdxt.select_root` sets the key that will be submitted with the form data.

The `value` prop of `rdxt.select_item` provides the value to be associated with the `name` key when the form is submitted with that item selected.

When the `required` prop of the `rdxt.select_root` is `True`, it indicates that the user must select a value before the form may be submitted.

```python demo exec
class FormSelectState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def form_select():
    return rdxt.flex(
        rdxp.form_root(
            rdxt.flex(
                rdxt.select_root(
                    rdxt.select_trigger(),
                    rdxt.select_content(
                        rdxt.select_group(
                            rdxt.select_label("Fruits"),
                            rdxt.select_item("Orange", value="orange"),
                            rdxt.select_item("Apple", value="apple"),
                            rdxt.select_item("Grape", value="grape"),
                        ),
                        rdxt.select_separator(),
                        rdxt.select_group(
                            rdxt.select_label("Vegetables"),
                            rdxt.select_item("Carrot", value="carrot"),
                            rdxt.select_item("Potato", value="potato"),
                        ),
                    ),
                    default_value="apple",
                    name="select",
                ),
                rdxt.button("Submit"),
                width="100%",
                direction="column",
                gap="2",
            ),
            on_submit=FormSelectState.handle_submit,
            reset_on_submit=True,
        ),
        rdxt.separator(size="4"),
        rdxt.heading("Results"),
        rdxt.text(FormSelectState.form_data.to_string()),
        width="100%",
        direction="column",
        gap="2",
    )
```

## Real World Example

```python demo
rdxt.card(
    rdxt.flex(
        rx.image(src="/reflex_logo.png", width="100%", height="auto"),
        rdxt.flex(
            rdxt.heading("Reflex Swag", size="4", margin_bottom="4px"),
            rdxt.heading("$99", size="6", margin_bottom="4px"),
            direction="row", justify="between",
            width="100%",
        ),
        rdxt.text("Reflex swag with a sense of nostalgia, as if they carry whispered tales of past adventures", size="2", margin_bottom="4px"),
        rdxt.separator(size="4"),
        rdxt.flex(
            rdxt.flex(
                rdxt.text("Color", size="2", margin_bottom="4px", color_scheme="gray"),
                rdxt.select_root(
                    rdxt.select_trigger(),
                    rdxt.select_content(
                        rdxt.select_group(
                            rdxt.select_item("Light", value="light"),
                            rdxt.select_item("Dark", value="dark"),
                        ),
                    ),
                    default_value="light",
                ),
                direction="column",
            ),
            rdxt.flex(
                rdxt.text("Size", size="2", margin_bottom="4px", color_scheme="gray"),
                rdxt.select_root(
                    rdxt.select_trigger(),
                    rdxt.select_content(
                        rdxt.select_group(
                            rdxt.select_item("24", value="24"),
                            rdxt.select_item("26", value="26"),
                            rdxt.select_item("28", value="28", disabled=True),
                            rdxt.select_item("30", value="30"),
                            rdxt.select_item("32", value="32"),
                            rdxt.select_item("34", value="34"),
                            rdxt.select_item("36", value="36"),
                        ),
                    ),
                    default_value="30",
                ),
                direction="column",
            ),
            rdxt.button(rdxt.icon(tag="plus"), "Add"),
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