---
title: Aligned Grids
---

AgGrid provides a way to align multiple grids together. This is useful when you want to display related data in a synchronized manner.

You can do so through the `aligned_grids` prop. This prop takes a list of grid IDs that you want to align. 

```python demo exec
import pandas as pd

import reflex_enterprise as rxe

df = pd.read_json("https://www.ag-grid.com/example-assets/olympic-winners.json")

row_data = df.to_dict("records")

column_defs = [
    {"field": "athlete"},
    {"field": "age"},
    {"field": "country"},
    {"field": "year"},
    {"field": "sport"},
    {
        "header_name": "Medals",
        "children": [
            {
                "field": "total",
                "column_group_show": "closed",
                "col_id": "total",
                "value_getter": "params.data.gold + params.data.silver + params.data.bronze",
                "width": 100,
            },
            {"field": "gold", "column_group_show": "open", "width": 100},
            {"field": "silver", "column_group_show": "open", "width": 100},
            {"field": "bronze", "column_group_show": "open", "width": 100},
        ],
    },
]

def aligned_grids_page():
    """Aligned grids demo."""
    return rxe.ag_grid(
        id="grid1",
        column_defs=column_defs,
        row_data=row_data,
        aligned_grids=["grid2"],
        width="100%",
    ), rxe.ag_grid(
        id="grid2",
        column_defs=column_defs,
        row_data=row_data,
        aligned_grids=["grid1"],
        width="100%",
    )

```

```md alert warning
# The pivot functionality does not work with aligned grids. This is because pivoting data changes the columns, which would make the aligned grids incompatible, as they are no longer sharing the same set of columns.
```
