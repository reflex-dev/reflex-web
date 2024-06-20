---
components:
    - rx.recharts.RadialBarChart
---

# Bar Chart

```python exec
import reflex as rx
```
## Radial Bar chart example

This example demonstrates how to use a `radial_bar_chart` with a `radial_bar`. The `radial_bar_chart` takes in `data` and then the `radial_bar` takes in a `data_key`.


```python demo graphing

data_radial_bar = [
    {
        "name": "18-24",
        "uv": 31.47,
        "pv": 2400,
        "fill": "#8884d8"
    },
    {
        "name": "25-29",
        "uv": 26.69,
        "pv": 4567,
        "fill": "#83a6ed"
    },
    {
        "name": "30-34",
        "uv": -15.69,
        "pv": 1398,
        "fill": "#8dd1e1"
    },
    {
        "name": "35-39",
        "uv": 8.22,
        "pv": 9800,
        "fill": "#82ca9d"
    },
    {
        "name": "40-49",
        "uv": -8.63,
        "pv": 3908,
        "fill": "#a4de6c"
    },
    {
        "name": "50+",
        "uv": -2.63,
        "pv": 4800,
        "fill": "#d0ed57"
    },
    {
        "name": "unknow",
        "uv": 6.67,
        "pv": 4800,
        "fill": "#ffc658"
    }
]

def radial_bar():
    return rx.recharts.radial_bar_chart(
        rx.recharts.radial_bar(
            data_key="uv",
            min_angle=90,
            background=True,
            label={"fill": '#666', "position": 'insideStart'},
        ),
        data=data_radial_bar,

        inner_radius="10%",
        outer_radius="80%",
        start_angle=180,
        end_angle=0,
        width = 600,
        height = 300,
    )
```