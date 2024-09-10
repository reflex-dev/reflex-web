---
components:
    - rx.lucide.Icon
---


# AG Grid

Reflex AG Grid is a high-performance and highly customizable grid that wraps AG Grid.

```bash
pip install reflex-ag-grid
```

## Your First Reflex AG Grid

A basic Reflex AG Grid contains column definitions `column_defs`, which define the columns to be displayed in the grid, and `row_data`, which contains the data to be displayed in the grid.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/wind_dataset.csv")

column_defs = [
    {'field': 'direction'},
    {'field': 'strength'},
    {'field': 'frequency'},
]

def ag_grid_simple():
    return rx.box(
        ag_grid(
            id="ag_grid_basic_1",
            row_data=df.to_dict("records"),
            column_defs=column_defs,
        ),
        width="45vw",
        height="40vh",
    )
```

The previous example showed the column_defs written out in full. You can also extract the required information from the dataframe's column names:

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/wind_dataset.csv")


def ag_grid_simple_2():
    return rx.box(
        ag_grid(
            id="ag_grid_basic_2",
            row_data=df.to_dict("records"),
            column_defs=[{"field": i} for i in df.columns],
        ),
        width="45vw",
        height="40vh",
    )
```




## Headers  (still need to fix this)

In the above example, the first letter of the field names provided are capitalized when displaying the header name. You can customize the header names by providing a `header_name` key in the column definition. In this example, the `header_name` is customized for the second and third columns.



```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs = [
    {'field': 'country'},
    {'field': 'pop', 'header_name': 'Population'},
    {'field': 'lifeExp', 'header_name': 'Life Expectancy'},
]

def ag_grid_simple_headers():
    return rx.box(
        ag_grid(
            id="ag_grid_basic_headers",
            row_data=df.to_dict("records"),
            column_defs=column_defs,
        ),
        width="45vw",
        height="40vh",
    )
```



## Column Filtering

Allow a user to filter a column by setting the `filter` key to `True` in the column definition. In this example we enable filtering for the first and last columns.


```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs =  [
    {'field': 'country', 'filter': True},
    {'field': 'pop', 'header_name': 'Population'},
    {'field': 'lifeExp', 'header_name': 'Life Expectancy', 'filter': True},
]

def ag_grid_simple_column_filtering():
    return rx.box(
        ag_grid(
            id="ag_grid_basic_column_filtering",
            row_data=df.to_dict("records"),
            column_defs=column_defs,
        ),
        width="45vw",
        height="40vh",
    )
```

### Floating Filters

Floating Filters embed the Column Filter into the header for ease of access. Set the `floating_filter` key to `True`. For this example we enable floating filters for just the first column.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs =  [
    {'field': 'country', 'filter': True, 'floating_filter': True},
    {'field': 'pop', 'header_name': 'Population'},
    {'field': 'lifeExp', 'header_name': 'Life Expectancy', 'filter': True},
]

def ag_grid_simple_floating_filters():
    return rx.box(
        ag_grid(
            id="ag_grid_basic_floating_filters",
            row_data=df.to_dict("records"),
            column_defs=column_defs,
        ),
        width="45vw",
        height="40vh",
    )
```




## Row Sorting

By default, the rows can be sorted by any column by clicking on the column header. You can disable sorting of the rows for a column by setting the `sortable` key to `False` in the column definition. In this example, we disable sorting for the first column.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs =  [
    {'field': 'country', 'sortable': False},
    {'field': 'pop', 'header_name': 'Population'},
    {'field': 'lifeExp', 'header_name': 'Life Expectancy'},
]

def ag_grid_simple_row_sorting():
    return rx.box(
        ag_grid(
            id="ag_grid_basic_row_sorting",
            row_data=df.to_dict("records"),
            column_defs=column_defs,
        ),
        width="45vw",
        height="40vh",
    )
```




## Row Selection

Row Selection is enabled using the `row_selection` attribute. You can use the `checkbox_selection` column definition attribute to render checkboxes for selection.


```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs = [
    {'field': 'country', 'checkbox_selection': True},
    {'field': 'pop', 'header_name': 'Population'},
    {'field': 'continent'},
]

def ag_grid_simple_row_selection():
    return rx.box(
        ag_grid(
            id="ag_grid_basic_row_selection",
            row_data=df.to_dict("records"),
            column_defs=column_defs,
            row_selection="multiple",
        ),
        width="45vw",
        height="40vh",
    )
```



## Editing 

Enable Editing by setting the `editable` attribute to `True`. The cell editor is inferred from the cell data type. Set the cell editor type using the `cell_editor` attribute. 

There are 7 provided cell editors in AG Grid: `agTextCellEditor`, `agLargeTextCellEditor`, `agSelectCellEditor`, `agRichSelectCellEditor`, `agNumberCellEditor`, `agDateCellEditor`, `agCheckboxCellEditor`.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs = [
    {'field': 'country'},
    {'field': 'pop', 'header_name': 'Population', 'editable': True, "cell_editor": 'agNumberCellEditor',},
    {'field': 'continent', 'editable': True, "cell_editor": 'agSelectCellEditor', "cell_editor_params": {
            "values": ['Asia', 'Europe', 'Africa', 'Americas', 'Oceania'],
        },
    },
]

def ag_grid_simple_editing():
    return rx.box(
        ag_grid(
            id="ag_grid_basic_editing",
            row_data=df.to_dict("records"),
            column_defs=column_defs,
        ),
        width="45vw",
        height="40vh",
    )
```




## Pagination 

By default, the grid uses a vertical scroll. You can reduce the amount of scrolling required by adding pagination. To add pagination, set `pagination=True`. You can set the `pagination_page_size` to the number of rows per page and `pagination_page_size_selector` to a list of options for the user to select from.


```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs = [
    {'field': 'country'},
    {'field': 'pop', 'header_name': 'Population'},
    {'field': 'lifeExp', 'header_name': 'Life Expectancy'},
]

def ag_grid_simple_pagination():
    return rx.box(
        ag_grid(
            id="ag_grid_basic_pagination",
            row_data=df.to_dict("records"),
            column_defs=column_defs,
            pagination=True,
            pagination_page_size=10,
            pagination_page_size_selector=[10, 40, 100],
        ),
        width="45vw",
        height="40vh",
    )
```







## Themes 

You can style your grid with a theme. AG Grid includes the following themes: `ag-theme-quartz`, `ag-theme-quartz-dark`, `ag-theme-alpine`, `ag-theme-alpine-dark`, `ag-theme-balham`, `ag-theme-balham-dark,` `ag-theme-material`.

The grid uses `ag-theme-alpine` by default. To use any other theme, set it using `class_name`. For example, `class_name="ag-theme-alpine-dark"`, like in the following example.

!!!!!!!!! Come back to this when the themes work !!!!!!!!!!!


Explore how to customise a theme and customise cell and row style!













## Using AG Grid with State

You can use State to update the grid based on a users input. In this example, we update the `column_defs` of the grid when a user clicks a button.


```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd

class AgGridState(rx.State):
    """The app state."""
    all_columns = [
        { 'field': 'country' },
        { 'field': 'pop'},
        { 'field': 'continent' },
        { 'field': 'lifeExp'},
        { 'field': 'gdpPercap'},
    ]

    two_columns = [
        { 'field': 'country' },
        { 'field': 'pop'},
    ]
    column_defs = all_columns
    n_clicks = 0

    def update_columns(self):
        self.n_clicks += 1
        if self.n_clicks % 2 != 0:
            self.column_defs = self.two_columns
        else:
            self.column_defs = self.all_columns


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")


def ag_grid_simple_with_state():
    return rx.box(
        rx.button("Toggle Columns", on_click=AgGridState.update_columns),
        ag_grid(
            id="ag_grid_basic_with_state",
            row_data=df.to_dict("records"),
            column_defs=AgGridState.column_defs,
        ),
        width="45vw",
        height="40vh",
    )
```




## Using AG Grid Enterprise