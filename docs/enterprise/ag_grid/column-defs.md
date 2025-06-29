---
order: 1
---


# Column Definitions

## Basic Columns

AgGrid allows you to define the columns of your grid, passed to the prop `column_defs`. Each dictionary represents a column.

```python
import reflex as rx

def camelcase_warning():
    return rx.callout(
        "If you are converting from other AG Grid implementation, we also support camelCase for the name of the properties.",
        icon="triangle_alert",
        color_scheme="orange",
    )
```

```python
camelcase_warning()
```

Here we define a grid with 3 columns:
```python
column_defs = [
    dict(field="direction"),
    dict(field="strength"),
    dict(field="frequency"),
]
```

To set default properties for all your columns, you can define `default_col_def` in your grid:

```python
default_col_def = dict(editable=True)
```

Any column can override the default properties defined above by setting their own value:

```python
column_defs = [
    dict(field="direction"),
    dict(field="strength", editable=False),
    dict(field="frequency"),
]
default_col_def = dict(editable=True)
```

Here is an example using both `column_defs` and `default_col_def`:

```python
import reflex as rx
import reflex_enterprise as rxe
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/wind_dataset.csv")

column_defs = [
    dict(field="direction", editable=False),
    dict(field="strength"),
    dict(field="frequency"),
]

def ag_grid_simple_col_def():
    return rxe.ag_grid(
        id="ag_grid_basic_col_1",
        row_data=df.to_dict("records"),
        column_defs=column_defs,
        default_col_def=dict(editable=True),
        width="100%",
    )

```


## Columns Groups
It is also possible to group columns by defining a `children` property in the column definition. This property should be a list of column definitions.

```python
column_defs = [
    dict(field="direction"),
    dict(
        header_name="Wind",
        children=[
            dict(field="strength"),
            dict(field="frequency"),
        ],
    ),
]
```

### Example

```python
import reflex as rx
import reflex_enterprise as rxe
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/wind_dataset.csv")

column_defs = [
    dict(field="direction"),
    dict(
        header_name="Wind",
        children=[
            dict(field="strength"),
            dict(field="frequency"),
        ],
    ),
]

def ag_grid_column_groups():
    return rxe.ag_grid(
        id="ag_grid_column_groups",
        row_data=df.to_dict("records"),
        column_defs=column_defs,
        width="100%",
    )

```

## Column Types

It is also possible to define column types that can be reused across multiple columns. This is useful when you have multiple columns with the same properties.

```python
column_types = dict(
    price=dict(editable=False, value_formatter="'$' + params.value"),
)
```

### Example

```python
import reflex as rx
import reflex_enterprise as rxe

data = [
    dict(product_name="Product A", price=100, price_eur=90),
    dict(product_name="Product B", price=200, price_eur=180),
    dict(product_name="Product C", price=300, price_eur=270),
    dict(product_name="Product D", price=400, price_eur=360),
    dict(product_name="Product E", price=500, price_eur=450),
]

column_types = dict(
    price=dict(editable=False, value_formatter="'$' + params.value"),
    price_eur=dict(editable=False, value_formatter="params.value + ' €'"),
)

column_defs = [
    dict(field="product_name", header_name="Product Name"),
    dict(field="price", header_name="Price in $", type="price"),
    dict(field="price_eur", header_name="Price in €", type="price_eur"),
]

def ag_grid_column_types():
    return rxe.ag_grid(
        id="ag_grid_column_types",
        row_data=data,
        column_defs=column_defs,
        column_types=column_types,
        width="100%",
    )
```

## Cell Renderer

A cell renderer is a function that takes a cell value and returns a string or a Reflex component to be rendered in the cell. You can use this to customize the appearance of the cell.

```python
import reflex as rx
import reflex_enterprise as rxe
import pandas as pd


data = [
    dict(product_name="Product A", link="https://example.com/product-a"),
    dict(product_name="Product B", link="https://example.com/product-b"),
    dict(product_name="Product C", link="https://example.com/product-c"),
]


column_defs = [
    dict(field="product_name"),
    dict(field="link", cell_renderer=rxe.ag_grid.renderers.link_external),
]

def ag_grid_cell_renderer():
    return rxe.ag_grid(
        id="ag_grid_cell_renderer",
        row_data=data,
        column_defs=column_defs,
        width="100%",
    )
```

It is also possible to define your own cell renderer by using the decorator `rxe.arrow_func` on a function. The decorated function should take `params` (of type `RendererParams`) as input and return a Reflex component to be rendered in the cell.

```python
import reflex as rx
import reflex_enterprise as rxe

from reflex_enterprise.components.ag_grid.resource import RendererParams

data = [
    dict(product_name="Product A", count=5),
    dict(product_name="Product B", count=2),
    dict(product_name="Product C", count=7),
]


@rxe.arrow_func
def count_renderer(params: RendererParams):
    return rx.hstack(
        rx.icon_button(
            "minus",
            color="red",
            on_click=rx.toast(f"Clicked minus for \{params.data['product_name']}"),
        ),
        rx.text(params.value, size="5"),
        rx.icon_button(
            "plus",
            color="green",
            on_click=rx.toast(f"Clicked plus for \{params.data['product_name']}"),
        ),
        align="center",
    )


column_defs = [
    dict(field="product_name"),
    dict(field="count", cell_renderer=count_renderer),
]


def ag_grid_custom_cell_renderer():
    return rxe.ag_grid(
        id="ag_grid_custom_cell_renderer",
        row_data=data,
        column_defs=column_defs,
        width="100%",
    )

```
