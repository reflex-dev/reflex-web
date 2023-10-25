A datagrid editor based on [Glide Data Grid](https://grid.glideapps.com/)

```python exec
import reflex as rx

from pcweb.base_state import State

class DataEditorState(State):
    columns: list[dict[str, str]] = [
        {"title":"Code"},
        {"title":"Value"}, 
        {"title":"Activated"},
    ]
    data: list[list[Any]] = [
        ["A", 1, True],
        ["B", 2, False],
        ["C", 3, False],
        ["D", 4, True],
        ["E", 5, True],
        ["F", 6, False],
    ]

data_editor_example = """
rx.data_editor(
    columns=DataEditorState.columns,
    data=DataEditorState.data,
    height="20vh",
)
"""

```

This component is introduced as an alternative to the [datatable](docs/library/datadisplay/datatable) to support editing the displayed data.



## Columns

The columns definition should be a `list` of `dict`, each `dict` describing the associated columns.
Property of a column dict:
- `title`: The text to display in the header of the column.
```reflex eval
rx.badge("Required")
```
- `id`: An id for the column, if not defined, will default to a lower case of `title`
- `width`: The width of the column.
- `type`: The type of the columns, default to `"str"`.

## Data

The `data` props of `rx.data_editor` accept a `list` of `list`, where each `list` represent a row of data to display in the table.


## Examples

Here we will show an example of data_editor.




"https://media.geeksforgeeks.org/wp-content/uploads/nba.csv"