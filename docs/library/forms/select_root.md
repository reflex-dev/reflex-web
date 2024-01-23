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
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
from pcweb.templates.docpage import style_grid
import reflex.components.radix.themes as rdxt
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
select(
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

Displays a list of options for the user to pick from—triggered by a button.


## Basic Example


```python demo
select_root(
    select_trigger(),
    select_content(
        select_group(
            select_label("Fruits"),
            select_item("Orange", value="orange"),
            select_item("Apple", value="apple"),
            select_item("Grape", value="grape", disabled=True),
        ),
        select_separator(),
        select_group(
            select_label("Vegetables"),
            select_item("Carrot", value="carrot"),
            select_item("Potato", value="potato"),
        ),
    ),
    default_value="apple",
)
```


## Usage


## Disabling 


It is possible to disable individual items in a `select` using the `disabled` prop associated with the `select_item`.

```python demo
select_root(
    select_trigger(),
    select_content(
        select_group(
            select_item("Apple", value="apple"),
            select_item("Grape", value="grape", disabled=True),
            select_item("Pineapple", value="pineapple"),
        ),
    ),
)
```

To prevent the user from interacting with select entirely, set the `select_root` components `disabled` prop to `True`.

```python demo
select_root(
    select_trigger(),
    select_content(
        select_group(
            select_item("Apple", value="apple"),
            select_item("Grape", value="grape"),
        ),
    ),
    disabled=True,
)
```


## Setting Defaults 


It is possible to set several default values when constructing a `select`. 

Can set the `placeholder` in the `select_trigger`, which is the content that will be rendered when no value or no default_value is set.


```python demo
select_root(
    select_trigger(placeholder="pick a fruit"),
    select_content(
        select_group(
            select_item("Apple", value="apple"),
            select_item("Grape", value="grape"),
        ),
    ),
)
```

Can set the `default_value` in the `select_root`, which is the value of the `select` when initially rendered.


```python demo
select_root(
    select_trigger(),
    select_content(
        select_group(
            select_item("Apple", value="apple"),
            select_item("Grape", value="grape"),
        ),
    ),
    default_value="apple",
)
```



## High control of select component (value and open changes)


The `on_value_change` event is called when the value of the select changes. In this example we set the `select_root` `value` prop to change the select `value` using a button in this case. 

```python demo exec
class SelectState2(rx.State):
    
    values: list[str] = ["apple", "grape", "pear"]
    
    value: str = "apple"

    def change_value(self):
        """Change the select value var."""
        self.value = random.choice(self.values)


def select_example2():
    return rx.vstack(
        select_root(
            select_trigger(),
            select_content(
                select_group(
                    rx.foreach(SelectState2.values, lambda x: select_item(x, value=x))
                ),
            ),
            value=SelectState2.value,
            on_value_change=SelectState2.set_value,
            
        ),
        button("Change Value", on_click=SelectState2.change_value),
        
    )
```



The `on_open_change` event handler acts in a similar way to the `on_value_change` and is called when the open state of the select changes.

```python demo
select_root(
    select_trigger(),
    select_content(
        select_group(
            select_item("Apple", value="apple"),
            select_item("Grape", value="grape"),
        ),
        
    ),

    on_value_change=rx.window_alert("on_value_change event handler called"),
)

```
 



### Submitting a form using select

The `name` of the select, a prop of the `select_root` is needed to submit with its owning form as part of a name/value pair.

When the `required` prop of the `select_root` is `True`, it indicates that the user must select a value before the owning form can be submitted.

The `value` prop of `select_item` is only used for form submission, and is given as data when submitted with a `name`. Use the `value` prop to control state of the `select`.

```python demo exec
class FormSelectState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def form_select():
    return rx.vstack(
        rx.form(
            rx.vstack(
                select_root(
                    select_trigger(),
                    select_content(
                        select_group(
                            select_label("Fruits"),
                            select_item("Orange", value="orange"),
                            select_item("Apple", value="apple"),
                            select_item("Grape", value="grape"),
                        ),
                        select_separator(),
                        select_group(
                            select_label("Vegetables"),
                            select_item("Carrot", value="carrot"),
                            select_item("Potato", value="potato"),
                        ),
                    ),
                    default_value="apple",
                    name="select",
                ),
                rx.button("Submit", type_="submit"),
                width="100%",
            ),
            on_submit=FormSelectState.handle_submit,
            reset_on_submit=True,
            width="100%",
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(FormSelectState.form_data.to_string()),
        width="100%",
    )
```









## Styling


### root size

### trigger variant

### trigger color

### trigger radius


### content variant


### content color

### content high contrast


### content position


### content side and side offset


### content align and align offset



## Real World Example

```python demo
card(
    rx.vstack(
        rx.image(src="/reflex_logo.png", width="100%", height="auto"),
        flex(
            heading("Reflex Swag", size="4", mb="1"),
            heading("$99", size="6", mb="1"),
            direction="row", justify="between",
            width="100%",
        ),
        text("Reflex swag with a sense of nostalgia, as if they carry whispered tales of past adventures", size="2", mb="1"),
        rx.divider(),
        flex(
            flex(
                text("Color", size="2", mb="1", color_scheme="gray"),
                select_root(
                    select_trigger(),
                    select_content(
                        select_group(
                            select_item("Light", value="light"),
                            select_item("Dark", value="dark"),
                        ),
                    ),
                    default_value="light",
                ),
                direction="column",
            ),
            flex(
                text("Size", size="2", mb="1", color_scheme="gray"),
                select_root(
                    select_trigger(),
                    select_content(
                        select_group(
                            select_item("24", value="24"),
                            select_item("26", value="26"),
                            select_item("28", value="28", disabled=True),
                            select_item("30", value="30"),
                            select_item("32", value="32"),
                            select_item("34", value="34"),
                            select_item("36", value="36"),
                        ),
                    ),
                    default_value="30",
                ),
                direction="column",
            ),
            flex(
                text(".", size="2",),
                button("Add to cart"),
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