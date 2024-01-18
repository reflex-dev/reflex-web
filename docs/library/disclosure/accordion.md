---
components:
    - rx.components.radix.primitives.AccordionRoot
    - rx.components.radix.primitives.AccordionHeader
    - rx.components.radix.primitives.AccordionContent


---

```python exec
import reflex as rx
# from reflex.components.radix.themes.components import *
# from reflex.components.radix.themes.layout import *
# from reflex.components.radix.themes.typography import *
from reflex.components.radix.primitives import *
```

# Accordion

An accordion is a vertically stacked set of interactive headings that each reveal an associated section of content.


The accordion component us made up of `accordion` which is the root of the component and groups 

## Basic Example

```python demo
accordion(
            accordion_item("Is it accessible?", "content", font_size="3em"),
            collapsible=True,
            width="300px",
            color_scheme="primary"
)

```

## Styling

### Type
```python demo
accordion(
            accordion_item("Is it accessible?", "content", font_size="3em"),
            collapsible=True,
            width="300px",
            multiple=True
)

```

### Default Value
```python demo
accordion(
            accordion_item("Is it accessible?", "content", font_size="3em", value="item_1"),
            accordion_item("Is it accessible?", "content", font_size="3em", value="item_2"),
            accordion_item("Is it accessible?", "content", font_size="3em", value="item_3"),
            collapsible=True,
            width="300px",
            default_value="item_2"
)

```

### Collapsible
```python demo
accordion(
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            collapsible=True,
            width="300px",
            disabled=True,
)

accordion(
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            collapsible=False,
            width="300px",
            disabled=True,
)

```

### Disabled

```python demo
accordion(
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            collapsible=True,
            width="300px",
            disabled=True,
)

```

### Direction


### Orientation

```python demo
accordion(
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            collapsible=True,
            width="300px",
            variant="classic",
            color_scheme="primary",
            orientation="veritcal"
)

```

```python demo
accordion(
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            collapsible=True,
            width="300px",
            variant="classic",
            color_scheme="primary",
            orientation="horizontal"
)

```

### Variant

```python demo
accordion(
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            collapsible=True,
            width="300px",
            variant="classic",
)

accordion(
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            collapsible=True,
            width="300px",
            variant="soft",
)

accordion(
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            collapsible=True,
            width="300px",
            variant="outline",

)

accordion(
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            collapsible=True,
            width="300px",
            variant="surface",
)

accordion(
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            collapsible=True,
            width="300px",
            variant="ghost",
)


```



### Color Scheme

```python demo
accordion(
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            collapsible=True,
            width="300px",
            color_scheme="primary",
)

accordion(
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            collapsible=True,
            width="300px",
            color_scheme="accent",
)

```


### Value

```python demo exec
class AccordionState(rx.State):
    """The app state."""

    value: str = "item_1"
    item_selected: str

    def change_value(self, value):
        self.value = value
        self.item_selected = f"{value} selected"


def index() -> rx.Component:
    return rdxt.theme(
        rdxt.container(
            rdxt.text(AccordionState.item_selected),
            rdxt.flex(
                rdxp.accordion(
                    accordion_item(
                        "Is it accessible?",
                        rdxt.button("Test button"),
                        font_size="3em",
                        value="item_1",
                    ),
                    accordion_item(
                        "Is it unstyled?",
                        "Yes. It's unstyled by default, giving you freedom over the look and feel.",
                        value="item_2",
                    ),
                    accordion_item(
                        "Is it finished?",
                        "It's still in beta, but it's ready to use in production.",
                        value="item_3",
                    ),
                    collapsible=True,
                    width="300px",
                    value=AccordionState.value,
                    on_value_change=lambda value: AccordionState.change_value(value),
                ),
                direction="column",
                gap="2",
            ),
            padding="2em",
            font_size="2em",
            text_align="center",
        )
    )


```

## AccordionItem

## Styling

### Value

```python demo
accordion(
            accordion_item("Is it accessible?", "content", font_size="3em", value="item_1"),
            accordion_item("Is it accessible?", "content", font_size="3em", value="item_2"),
            accordion_item("Is it accessible?", "content", font_size="3em", value="item_3"),
            collapsible=True,
            width="300px",
)

```

### Disable

```python demo
accordion(
            accordion_item("Is it accessible?", "content", font_size="3em", disable=True),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            accordion_item("Is it accessible?", "content", font_size="3em"),
            collapsible=True,
            width="300px",
            color_scheme="primary",
)
```



