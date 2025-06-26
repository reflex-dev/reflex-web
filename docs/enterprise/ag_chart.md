---
order: 4
---

```python exec
from flexd.flexd import docs
```

# AG Charts

To use AG Charts, you'll need to pass a dict to the `options` prop of the `ag_chart` component. The dict should contain the following properties:
- `data`: A list of dictionaries representing the data to be displayed in the chart.
- `series`: A list of dictionaries representing the series to be displayed in the chart. Each dictionary should contain the following properties:
  - `type`: The type of chart to be displayed (e.g., "bar", "line", etc.).
  - `xKey`: The key in the data dict to be used for the x-axis.
  - `yKey`: The key in the data dict to be used for the y-axis.

## Example

```python demo exec toggle
import reflex_enterprise as rxe

chart_options: dict = {
        "data": [
            {"month": "Jan", "avgTemp": 2.3, "iceCreamSales": 162000},
            {"month": "Feb", "avgTemp": 3.1, "iceCreamSales": 200000},
            {"month": "Mar", "avgTemp": 6.3, "iceCreamSales": 302000},
            {"month": "May", "avgTemp": 16.2, "iceCreamSales": 800000},
            {"month": "Jul", "avgTemp": 22.8, "iceCreamSales": 1254000},
            {"month": "Aug", "avgTemp": 24.1, "iceCreamSales": 1500000},
            {"month": "Sep", "avgTemp": 14.5, "iceCreamSales": 950000},
            {"month": "Oct", "avgTemp": 12.4, "iceCreamSales": 500000},
            {"month": "Nov", "avgTemp": 7.2, "iceCreamSales": 300000},
            {"month": "Dec", "avgTemp": 3.5, "iceCreamSales": 200000},
        ],
        "series": [
            {
                "type": "bar",
                "xKey": "month",
                "yKey": "iceCreamSales",
            }
        ],
    }

def ag_chart():
    return rxe.ag_chart(
        options=chart_options,
    )
```
