---
components:
    - rx.radix.accordion.root
    - rx.radix.accordion.item
    - rx.radix.accordion.header
    - rx.radix.accordion.content
---

```python exec
import reflex as rx
from reflex.components.core import *
```

# Accordion

An accordion is a vertically stacked set of interactive headings that each reveal an associated section of content.
The accordion component is made up of `accordion`, which is the root of the component and takes in an `accordion.item`,
which contains all the contents of the collapsible section.

## Basic Example

```python demo
rx.accordion.root(
    rx.accordion.item("First Item", "The first accordion item's content", font_size="3em"),
    rx.accordion.item(
        "Second Item", "The second accordion item's content", font_size="3em"
    ),
    rx.accordion.item("Third item", "The third accordion item's content", font_size="3em"),
    width="300px",
)
```

## Styling

### Type
We use the `type_` prop to determine whether multiple items can be opened at once. The allowed values for this prop are 
`single` and `multiple` where `single` will only open one item at a time. The default value for this prop is `single`.

```python demo
rx.accordion.root(
    rx.accordion.item("First Item", "The first accordion item's content", font_size="3em"),
    rx.accordion.item(
        "Second Item", "The second accordion item's content", font_size="3em"
    ),
    rx.accordion.item("Third item", "The third accordion item's content", font_size="3em"),
    collapsible=True,
    width="300px",
    type_="multiple",
)
```

### Default Value

We use the `default_value` prop to specify which item should open by default. The value for this prop should be any of the 
unique values set by an `accordion.item`.

```python demo
rx.flex(
    rx.accordion.root(
        rx.accordion.item(
            "First Item",
            "The first accordion item's content",
            font_size="3em",
            value="item_1",
        ),
        rx.accordion.item(
            "Second Item",
            "The second accordion item's content",
            font_size="3em",
            value="item_2",
        ),
        rx.accordion.item(
            "Third item",
            "The third accordion item's content",
            font_size="3em",
            value="item_3",
        ),
        width="300px",
        default_value="item_2",
    ),
    direction="row",
    gap="2"
)
```

### Collapsible

We use the `collapsible` prop to allow all items to close. If set to `False`, an opened item cannot be closed.

```python demo
rx.flex(
    rx.accordion.root(
        rx.accordion.item("First Item", "The first accordion item's content", font_size="3em"),
        rx.accordion.item("Second Item", "The second accordion item's content", font_size="3em"),
        rx.accordion.item("Third item", "The third accordion item's content", font_size="3em"),
        collapsible=True,
        width="300px",
    ),
    rx.accordion.root(
        rx.accordion.item("First Item", "The first accordion item's content", font_size="3em"),
        rx.accordion.item("Second Item", "The second accordion item's content", font_size="3em"),
        rx.accordion.item("Third item", "The third accordion item's content", font_size="3em"),
        collapsible=False,
        width="300px",
    ),
    direction="row",
    gap="2"
)
```

### Disable

We use the `disabled` prop to prevent interaction with the accordion and all its items.

```python demo
rx.accordion.root(
    rx.accordion.item("First Item", "The first accordion item's content", font_size="3em"),
    rx.accordion.item("Second Item", "The second accordion item's content", font_size="3em"),
    rx.accordion.item("Third item", "The third accordion item's content", font_size="3em"),
    collapsible=True,
    width="300px",
    disabled=True,
)
```



### Orientation

We use `orientation` prop to set the orientation of the accordion to `vertical` or `horizontal`. By default, the orientation
will be set to `vertical`. Note that, the orientation prop wont change the visual orientation but the 
functional orientation of the accordion. This means that for vertical orientation, the up and down arrow keys moves focus between the next or previous item,
while for horizontal orientation, the left or right arrow keys moves focus between items.

```python demo
rx.accordion.root(
    rx.accordion.item("First Item", "The first accordion item's content", font_size="3em"),
    rx.accordion.item(
        "Second Item", "The second accordion item's content", font_size="3em"
    ),
    rx.accordion.item("Third item", "The third accordion item's content", font_size="3em"),
    collapsible=True,
    width="300px",
    orientation="vertical",
)
```

```python demo
rx.accordion.root(
    rx.accordion.item("First Item", "The first accordion item's content", font_size="3em"),
    rx.accordion.item(
        "Second Item", "The second accordion item's content", font_size="3em"
    ),
    rx.accordion.item("Third item", "The third accordion item's content", font_size="3em"),
    collapsible=True,
    width="300px",
    orientation="horizontal",
)
```


### Variant

```python demo
rx.flex(
    rx.accordion.root(
        rx.accordion.item("First Item", "The first accordion item's content", font_size="3em"),
        rx.accordion.item(
            "Second Item", "The second accordion item's content", font_size="3em"
        ),
        rx.accordion.item("Third item", "The third accordion item's content", font_size="3em"),
        collapsible=True,
        variant="classic",
    ),
    rx.accordion.root(
        rx.accordion.item("First Item", "The first accordion item's content", font_size="3em"),
        rx.accordion.item(
            "Second Item", "The second accordion item's content", font_size="3em"
        ),
        rx.accordion.item("Third item", "The third accordion item's content", font_size="3em"),
        collapsible=True,
        variant="soft",
    ),
    rx.accordion.root(
        rx.accordion.item("First Item", "The first accordion item's content", font_size="3em"),
        rx.accordion.item(
            "Second Item", "The second accordion item's content", font_size="3em"
        ),
        rx.accordion.item("Third item", "The third accordion item's content", font_size="3em"),
        collapsible=True,
        variant="outline",
    ),
    rx.accordion.root(
        rx.accordion.item("First Item", "The first accordion item's content", font_size="3em"),
        rx.accordion.item(
            "Second Item", "The second accordion item's content", font_size="3em"
        ),
        rx.accordion.item("Third item", "The third accordion item's content", font_size="3em"),
        collapsible=True,
        variant="surface",
    ),
    rx.accordion.root(
        rx.accordion.item("First Item", "The first accordion item's content", font_size="3em"),
        rx.accordion.item(
            "Second Item", "The second accordion item's content", font_size="3em"
        ),
        rx.accordion.item("Third item", "The third accordion item's content", font_size="3em"),
        collapsible=True,
        variant="ghost",
    ),
    direction="row",
    gap="2"
    
)
```

### Color Scheme

We use the `color_scheme` prop to assign a specific color to the accordion background, ignoring the global theme. There
are two color schemes for the accordion: `primary` and `accent`. The default color scheme is `primary`

```python demo
rx.flex(
    rx.accordion.root(
        rx.accordion.item("First Item", "The first accordion item's content", font_size="3em"),
        rx.accordion.item(
            "Second Item", "The second accordion item's content", font_size="3em"
        ),
        rx.accordion.item("Third item", "The third accordion item's content", font_size="3em"),
        collapsible=True,
        width="300px",
        color_scheme="primary",
    ),
    rx.accordion.root(
        rx.accordion.item("First Item", "The first accordion item's content", font_size="3em"),
        rx.accordion.item(
            "Second Item", "The second accordion item's content", font_size="3em"
        ),
        rx.accordion.item("Third item", "The third accordion item's content", font_size="3em"),
        collapsible=True,
        width="300px",
        color_scheme="accent",
    ),
    direction="row",
    gap="2"
)
```


### Value

We use the `value` prop to specify the controlled value of the accordion item that we want to activate.
This property should be used in conjunction with the `on_value_change` event argument.

```python demo exec
class AccordionState(rx.State):
    """The app state."""

    value: str = "item_1"
    item_selected: str

    def change_value(self, value):
        self.value = value
        self.item_selected = f"{value} selected"


def index() -> rx.Component:
    return rx.theme(
        rx.container(
            rx.text(AccordionState.item_selected),
            rx.flex(
                rx.accordion.root(
                    rx.accordion.item(
                        "Is it accessible?",
                        rx.button("Test button"),
                        font_size="3em",
                        value="item_1",
                    ),
                    rx.accordion.item(
                        "Is it unstyled?",
                        "Yes. It's unstyled by default, giving you freedom over the look and feel.",
                        value="item_2",
                    ),
                    rx.accordion.item(
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

The accordion item contains all the parts of a collapsible section.

## Styling

### Value

```python demo
rx.accordion.root(
    rx.accordion.item(
        "First Item",
        "The first accordion item's content",
        font_size="3em",
        value="item_1",
    ),
    rx.accordion.item(
        "Second Item",
        "The second accordion item's content",
        font_size="3em",
        value="item_2",
    ),
    rx.accordion.item(
        "Third item",
        "The third accordion item's content",
        font_size="3em",
        value="item_3",
    ),
    collapsible=True,
    width="300px",
)
```

### Disable

```python demo
rx.accordion.root(
    rx.accordion.item(
        "First Item",
        "The first accordion item's content",
        font_size="3em",
        disabled=True,
    ),
    rx.accordion.item(
        "Second Item", "The second accordion item's content", font_size="3em"
    ),
    rx.accordion.item("Third item", "The third accordion item's content", font_size="3em"),
    collapsible=True,
    width="300px",
    color_scheme="primary",
)
```



