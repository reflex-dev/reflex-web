---
components:
    - ag_grid
---


# AG Grid

Reflex AG Grid is a high-performance and highly customizable grid that wraps AG Grid.

```bash
pip install reflex-ag-grid
```

## Your First Reflex AG Grid

A basic Reflex AG Grid contains column definitions `column_defs`, which define the columns to be displayed in the grid, and `row_data`, which contains the data to be displayed in the grid. Each grid also requires a unique `id`.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/wind_dataset.csv")

column_defs = [
    ag_grid.column_def(field="direction"),
    ag_grid.column_def(field="strength"),
    ag_grid.column_def(field="frequency"),

]

def ag_grid_simple():
    return ag_grid(
        id="ag_grid_basic_1",
        row_data=df.to_dict("records"),
        column_defs=column_defs,
    )
```

The previous example showed the `column_defs` written out in full. You can also extract the required information from the dataframe's column names:

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/wind_dataset.csv")


def ag_grid_simple_2():
    return ag_grid(
        id="ag_grid_basic_2",
        row_data=df.to_dict("records"),
        column_defs=[{"field": i} for i in df.columns],
        width="40vw",
        height="40vh",
    )
```




## Headers

In the above example, the first letter of the field names provided are capitalized when displaying the header name. You can customize the header names by providing a `header_name` key in the column definition. In this example, the `header_name` is customized for the second and third columns.



```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs = [
    ag_grid.column_def(field="country"),
    ag_grid.column_def(field="pop", header_name="Population"),
    ag_grid.column_def(field="lifeExp", header_name="Life Expectancy"),
]

def ag_grid_simple_headers():
    return ag_grid(
            id="ag_grid_basic_headers",
            row_data=df.to_dict("records"),
            column_defs=column_defs,
            width="40vw",
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
    ag_grid.column_def(field="country", header_name="Country", filter=True),
    ag_grid.column_def(field="pop", header_name="Population"),
    ag_grid.column_def(field="lifeExp", header_name="Life Expectancy", filter=True),
]

def ag_grid_simple_column_filtering():
    return ag_grid(
        id="ag_grid_basic_column_filtering",
        row_data=df.to_dict("records"),
        column_defs=column_defs,
        width="40vw",
        height="40vh",
    )
```



### Filter Types


You can set `filter=True` to enable the default filter for a column. 

You can also set the filter type using the `filter` key. The following filter types are available: `ag_grid.filters.date`, `ag_grid.filters.number` and `ag_grid.filters.text`. These ensure that the input you enter to the filter is of the correct type. 

(`ag_grid.filters.set` and `ag_grid.filters.multi` are available with AG Grid Enterprise)


```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/GanttChart-updated.csv")

column_defs =  [
    ag_grid.column_def(field="Task", filter=True),
    ag_grid.column_def(field="Start", filter=ag_grid.filters.date),
    ag_grid.column_def(field="Duration", filter=ag_grid.filters.number),
    ag_grid.column_def(field="Resource", filter=ag_grid.filters.text),
]

def ag_grid_simple_column_filtering():
    return ag_grid(
        id="ag_grid_basic_column_filtering",
        row_data=df.to_dict("records"),
        column_defs=column_defs,
        width="40vw",
        height="40vh",
    )
```




## Row Sorting

By default, the rows can be sorted by any column by clicking on the column header. You can disable sorting of the rows for a column by setting the `sortable` key to `False` in the column definition. 

In this example, we disable sorting for the first column.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs =  [
    ag_grid.column_def(field="country", sortable=False),
    ag_grid.column_def(field="pop", header_name="Population"),
    ag_grid.column_def(field="lifeExp", header_name="Life Expectancy"),
]

def ag_grid_simple_row_sorting():
    return ag_grid(
        id="ag_grid_basic_row_sorting",
        row_data=df.to_dict("records"),
        column_defs=column_defs,
        width="40vw",
        height="40vh",
    )
```




## Row Selection

Row Selection is enabled using the `row_selection` attribute. Setting it to `multiple` allows users to select multiple rows at a time. You can use the `checkbox_selection` column definition attribute to render checkboxes for selection.


```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs = [
    ag_grid.column_def(field="country", checkbox_selection=True),
    ag_grid.column_def(field="pop", header_name="Population"),
    ag_grid.column_def(field="continent"),
]

def ag_grid_simple_row_selection():
    return ag_grid(
        id="ag_grid_basic_row_selection",
        row_data=df.to_dict("records"),
        column_defs=column_defs,
        row_selection="multiple",
        width="40vw",
        height="40vh",
    )
```



## Editing 

Enable Editing by setting the `editable` attribute to `True`. The cell editor is inferred from the cell data type. Set the cell editor type using the `cell_editor` attribute. 

There are 7 provided cell editors in AG Grid: 
1. `ag_grid.editors.text` 
2. `ag_grid.editors.large_text`
3. `ag_grid.editors.select`
4. `ag_grid.editors.rich_select`
5. `ag_grid.editors.number`
6. `ag_grid.editors.date`
7. `ag_grid.editors.checkbox`

In this example, we enable editing for the second and third columns. The second column uses the `number` cell editor, and the third column uses the `select` cell editor.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs = [
    ag_grid.column_def(field="country"),
    ag_grid.column_def(field="pop", header_name="Population", editable=True, cell_editor=ag_grid.editors.number),
    ag_grid.column_def(field="continent", editable=True, cell_editor=ag_grid.editors.select, cell_editor_params={"values": ['Asia', 'Europe', 'Africa', 'Americas', 'Oceania']}),
]

def ag_grid_simple_editing():
    return ag_grid(
        id="ag_grid_basic_editing",
        row_data=df.to_dict("records"),
        column_defs=column_defs,
        width="40vw",
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
    ag_grid.column_def(field="country"),
    ag_grid.column_def(field="pop", header_name="Population"),
    ag_grid.column_def(field="lifeExp", header_name="Life Expectancy"),
]

def ag_grid_simple_pagination():
    return ag_grid(
        id="ag_grid_basic_pagination",
        row_data=df.to_dict("records"),
        column_defs=column_defs,
        pagination=True,
        pagination_page_size=10,
        pagination_page_size_selector=[10, 40, 100],
        width="40vw",
        height="40vh",
    )
```







## Themes 

You can style your grid with a theme. AG Grid includes the following themes: 

1. `quartz`
2. `alpine`
3. `balham`
4. `material`

The grid uses `quartz` by default. To use any other theme, set it using the `theme` prop, i.e. `theme="alpine"`.


```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd

class AGGridThemeState(rx.State):
    """The app state."""

    theme: str = "quartz"
    themes: list[str] = ["quartz", "balham", "alpine", "material"]

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs = [
    ag_grid.column_def(field="country"),
    ag_grid.column_def(field="pop", header_name="Population"),
    ag_grid.column_def(field="lifeExp", header_name="Life Expectancy"),
]

def ag_grid_simple_themes():
    return rx.vstack(
        rx.hstack(
            rx.text("Theme:"),
            rx.select(AGGridThemeState.themes, value=AGGridThemeState.theme, on_change=AGGridThemeState.set_theme),
        ),
        ag_grid(
            id="ag_grid_basic_themes",
            row_data=df.to_dict("records"),
            column_defs=column_defs,
            theme=AGGridThemeState.theme,
            width="40vw",
            height="40vh",
        ),
    )
```






## Using AG Grid with State

You can use State to update the grid based on a users input. In this example, we update the `column_defs` of the grid when a user clicks a button.


```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd

class AgGridState(rx.State):
    """The app state."""
    all_columns = [
        ag_grid.column_def(field="country"),
        ag_grid.column_def(field="pop"),
        ag_grid.column_def(field="continent"),
        ag_grid.column_def(field="lifeExp"),
        ag_grid.column_def(field="gdpPercap"),
    ]

    two_columns = [
        ag_grid.column_def(field="country"),
        ag_grid.column_def(field="pop"),
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
            width="40vw",
            height="40vh",
        ),
    )
```




## Using AG Grid Enterprise

AG Grid offers both community and enterprise versions. See the [AG Grid docs](https://www.ag-grid.com/archive/31.2.0/react-data-grid/licensing/) for details on purchasing a license key.

To use an AG Grid Enterprise license key with Reflex AG Grid set the environment variable `AG_GRID_LICENSE_KEY`: 

```bash
export AG_GRID_LICENSE_KEY="your_license_key"
```


## column_def props

The following props are available for `column_defs` as well as many others that can be found here: [AG Grid Column Def Docs](https://www.ag-grid.com/react-data-grid/column-properties/). (it is necessary to use snake_case for the keys in Reflex, unlike in the AG Grid docs where camelCase is used)
    
- `field`: `str`: The field of the row object to get the cell's data from.
- `col_id`: `str | None`: The unique ID to give the column. This is optional. If missing, the ID will default to the field.
- `type`: `str | None`: The type of the column.
- `cell_data_type`: `bool | str | None`: The data type of the cell values for this column. Can either infer the data type from the row data (true - the default behaviour), define a specific data type (string), or have no data type (false). 
- `hide`: `bool`: Set to true for this column to be hidden.
- `editable`: `bool | None`: Set to true if this column is editable, otherwise false.
- `filter`: `AGFilters | str | None`: Filter component to use for this column. Set to true to use the default filter. Set to the name of a provided filter to use that filter. (Check out the Filter Types section of this page for more information)
- `floating_filter`: `bool`: Whether to display a floating filter for this column.
- `header_name`: `str | None`: The name to render in the column header. If not specified and field is specified, the field name will be used as the header name.
- `header_tooltip`: `str | None`: Tooltip for the column header.
- `checkbox_selection`: `bool | None`: Set to true to render a checkbox for row selection. 
- `cell_editor`: `AGEditors | str | None`: Provide your own cell editor component for this column's cells. (Check out the Editing section of this page for more information)
- `cell_editor_params`: `dict[str, list[Any]] | None`: Params to be passed to the cellEditor component.