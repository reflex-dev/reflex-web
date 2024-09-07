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


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/space-mission-data.csv")

column_defs = [
    { 'field': 'direction' },
    { 'field': 'strength' },
    { 'field': 'frequency'},
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