---
components:
    - rx.recharts.XAxis
    - rx.recharts.YAxis
    - rx.recharts.ZAxis
---
```python exec
import reflex as rx
```

<!-- # Axis

The Axis component in Recharts is a powerful tool for customizing and configuring the axes of your charts. It provides a wide range of props that allow you to control the appearance, behavior, and formatting of the axis. Whether you're working with an AreaChart, LineChart, or any other chart type, the Axis component enables you to create precise and informative visualizations.

## Basic Example
Setting `hide` to true will hide the axis, `datakey` allows you to specify a unique identifier for the axis. The `width` and `height` props give you control over the dimensions of the axis. By default, the width is calculated internally based on the chart's layout. The height prop allows you to set a specific height for the axis. This is useful when you want to allocate more or less space for the axis depending on your chart's requirements.
``` python demo exec
def axis_1():
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="uv", stroke="#8884d8", fill="#8884d8"
        ),
        rx.recharts.x_axis(
            data_key="name",
            height = 50,
        ),
        rx.recharts.y_axis(
            width = 50,
        ),
        data=data,
        width = 500,
        height = 400,
    )
```


## Example with Ticks

```python demo exec
def axis_2():
    return rx.recharts.line_chart(
        rx.recharts.line(
            data_key="y",
            stroke="#8884d8",
        ),
        rx.recharts.x_axis(
            data_key="x", 
            tick_count = 7, 
            min_tick_gap = 30
        ),
        rx.recharts.y_axis(
            tick_line = False,
            ticks = [200, 300, 500, 800],
        ),
        data=data2,
        width = 500,
        height = 400,
    )
``` -->