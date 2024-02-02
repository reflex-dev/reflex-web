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
    

prototype: |
    lambda **props: rx.radix.themes.select(["apple", "grape", "pear"], default_value="pear", **props)
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


The `on_change` event is called when the value of the `select` changes. In this example we set the `value` prop to change the select `value` using a button in this case. 

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
            on_change=SelectState3.set_value,
        ),
        rdxt.button("Change Value", on_click=SelectState3.change_value),
        
    )
```


The `on_open_change` event handler acts in a similar way to the `on_change` and is called when the open state of the select changes.

```python demo
rdxt.select(
    ["apple", "grape", "pear"],
    on_change=rx.window_alert("on_change event handler called"),
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
