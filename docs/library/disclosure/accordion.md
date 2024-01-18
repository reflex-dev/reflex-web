---
components:
    - rx.components.radix.primitives.AccordionRoot
    - rx.components.radix.primitives.AccordionHeader
    - rx.components.radix.primitives.AccordionContent
---

```python exec
import reflex as rx
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
from reflex.components.radix.primitives import *
from reflex.components.core import *
from reflex.components.radix.themes import *
```

# Accordion

An accordion is a vertically stacked set of interactive headings that each reveal an associated section of content.
The accordion component us made up of `accordion` which is the root of the component and takes in an `accordion_item`
which contains all the contents of the collapsible section.

## Basic Example

```python demo
accordion(
    accordion_item("First Item", "The first accordion item's content", font_size="3em"),
    accordion_item(
        "Second Item", "The second accordion item's content", font_size="3em"
    ),
    accordion_item("Third item", "The third accordion item's content", font_size="3em"),
    width="300px",
)
```

## Styling

### Type
We use the `type_` prop to determine whether multiple items can be opened at once. The allowed values for this prop are 
`single` and `multiple` where `single` will only open one item at a time. The default value for this prop is `single`.

```python demo
accordion(
    accordion_item("First Item", "The first accordion item's content", font_size="3em"),
    accordion_item(
        "Second Item", "The second accordion item's content", font_size="3em"
    ),
    accordion_item("Third item", "The third accordion item's content", font_size="3em"),
    collapsible=True,
    width="300px",
    type_="multiple",
)
```

### Default Value

We use the `default_value` prop to specify which item should open by default. The value for this prop should be any of the 
unique values set by an `accordion_item`.

```python demo
flex(
    accordion(
        accordion_item(
            "First Item",
            "The first accordion item's content",
            font_size="3em",
            value="item_1",
        ),
        accordion_item(
            "Second Item",
            "The second accordion item's content",
            font_size="3em",
            value="item_2",
        ),
        accordion_item(
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
flex(
    accordion(
        accordion_item("First Item", "The first accordion item's content", font_size="3em"),
        accordion_item("Second Item", "The second accordion item's content", font_size="3em"),
        accordion_item("Third item", "The third accordion item's content", font_size="3em"),
        collapsible=True,
        width="300px",
    ),
    accordion(
        accordion_item("First Item", "The first accordion item's content", font_size="3em"),
        accordion_item("Second Item", "The second accordion item's content", font_size="3em"),
        accordion_item("Third item", "The third accordion item's content", font_size="3em"),
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
accordion(
    accordion_item("First Item", "The first accordion item's content", font_size="3em"),
    accordion_item("Second Item", "The second accordion item's content", font_size="3em"),
    accordion_item("Third item", "The third accordion item's content", font_size="3em"),
    collapsible=True,
    width="300px",
    disabled=True,
)
```

### Direction

We use the `dir` prop to specify the reading direction of the accordion when applicable. This can be set to `ltr`
or `rtl`. By default, the direction is set to `ltr`

```python demo
accordion(
    accordion_item("First Item", "The first accordion item's content", font_size="3em"),
    accordion_item(
        "Second Item", "The second accordion item's content", font_size="3em"
    ),
    accordion_item("Third item", "The third accordion item's content", font_size="3em"),
    collapsible=True,
    width="300px",
    dir="rtl",
)
```

### Orientation

We use `orientation` prop to set the orientation of the accordion to `vertical` or `horizontal`. By default, the orientation
will be set to `vertical`. Note that, the orientation prop wont change the visual orientation but the 
functional orientation of the accordion. This means that for vertical orientation, the up and down arrow keys moves focus between the next or previous item,
while for horizontal orientation, the left or right arrow keys moves focus between items.

```python demo
accordion(
    accordion_item("First Item", "The first accordion item's content", font_size="3em"),
    accordion_item(
        "Second Item", "The second accordion item's content", font_size="3em"
    ),
    accordion_item("Third item", "The third accordion item's content", font_size="3em"),
    collapsible=True,
    width="300px",
    orientation="vertical",
)
```

```python demo
accordion(
    accordion_item("First Item", "The first accordion item's content", font_size="3em"),
    accordion_item(
        "Second Item", "The second accordion item's content", font_size="3em"
    ),
    accordion_item("Third item", "The third accordion item's content", font_size="3em"),
    collapsible=True,
    width="300px",
    orientation="horizontal",
)
```

### Variant

```python demo
flex(
    accordion(
        accordion_item("First Item", "The first accordion item's content", font_size="3em"),
        accordion_item(
            "Second Item", "The second accordion item's content", font_size="3em"
        ),
        accordion_item("Third item", "The third accordion item's content", font_size="3em"),
        collapsible=True,
        width="300px",
        variant="classic",
    ),
    accordion(
        accordion_item("First Item", "The first accordion item's content", font_size="3em"),
        accordion_item(
            "Second Item", "The second accordion item's content", font_size="3em"
        ),
        accordion_item("Third item", "The third accordion item's content", font_size="3em"),
        collapsible=True,
        width="300px",
        variant="soft",
    ),
    accordion(
        accordion_item("First Item", "The first accordion item's content", font_size="3em"),
        accordion_item(
            "Second Item", "The second accordion item's content", font_size="3em"
        ),
        accordion_item("Third item", "The third accordion item's content", font_size="3em"),
        collapsible=True,
        width="300px",
        variant="outline",
    ),
    accordion(
        accordion_item("First Item", "The first accordion item's content", font_size="3em"),
        accordion_item(
            "Second Item", "The second accordion item's content", font_size="3em"
        ),
        accordion_item("Third item", "The third accordion item's content", font_size="3em"),
        collapsible=True,
        width="300px",
        variant="surface",
    ),
    accordion(
        accordion_item("First Item", "The first accordion item's content", font_size="3em"),
        accordion_item(
            "Second Item", "The second accordion item's content", font_size="3em"
        ),
        accordion_item("Third item", "The third accordion item's content", font_size="3em"),
        collapsible=True,
        width="300px",
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
flex(
    accordion(
        accordion_item("First Item", "The first accordion item's content", font_size="3em"),
        accordion_item(
            "Second Item", "The second accordion item's content", font_size="3em"
        ),
        accordion_item("Third item", "The third accordion item's content", font_size="3em"),
        collapsible=True,
        width="300px",
        color_scheme="primary",
    ),
    accordion(
        accordion_item("First Item", "The first accordion item's content", font_size="3em"),
        accordion_item(
            "Second Item", "The second accordion item's content", font_size="3em"
        ),
        accordion_item("Third item", "The third accordion item's content", font_size="3em"),
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
    return theme(
        container(
            text(AccordionState.item_selected),
            flex(
                accordion(
                    accordion_item(
                        "Is it accessible?",
                        button("Test button"),
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

The accordion item contains all the parts of a collapsible section.

## Styling

### Value

```python demo
accordion(
    accordion_item(
        "First Item",
        "The first accordion item's content",
        font_size="3em",
        value="item_1",
    ),
    accordion_item(
        "Second Item",
        "The second accordion item's content",
        font_size="3em",
        value="item_2",
    ),
    accordion_item(
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
accordion(
    accordion_item(
        "First Item",
        "The first accordion item's content",
        font_size="3em",
        disabled=True,
    ),
    accordion_item(
        "Second Item", "The second accordion item's content", font_size="3em"
    ),
    accordion_item("Third item", "The third accordion item's content", font_size="3em"),
    collapsible=True,
    width="300px",
    color_scheme="primary",
)
```



