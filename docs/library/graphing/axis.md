---
components:
    - rx.recharts.XAxis
    - rx.recharts.YAxis
    - rx.recharts.ZAxis
---
```python exec
import reflex as rx
```

# Axis

The Axis component in Recharts is a powerful tool for customizing and configuring the axes of your charts. It provides a wide range of props that allow you to control the appearance, behavior, and formatting of the axis. Whether you're working with an AreaChart, LineChart, or any other chart type, the Axis component enables you to create precise and informative visualizations.

## Basic Example

```python demo graphing

data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def axis_1():
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="uv",
            stroke=rx.color("accent", 9),
            fill=rx.color("accent", 8),
        ),
        rx.recharts.x_axis(
            data_key="name",
        ),
        rx.recharts.y_axis(
            data_key="uv",
        ),
        data=data,
        width = "100%",
        padding_left = 40,
        height = 300,
    )
```

### Multiple Axes

Multiple axes can be used for displaying different data series with varying scales or units on the same chart. This allows for a more comprehensive comparison and analysis of the data.

```python demo graphing

data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

def area_multi_axis():
  return rx.recharts.area_chart(
    rx.recharts.area(
        data_key="uv", stroke="#8884d8", fill="#8884d8", y_axis_id="left",
    ),
    rx.recharts.area(
        data_key="pv", y_axis_id="right", type_="monotone", stroke="#82ca9d", fill="#82ca9d"
    ),
    rx.recharts.x_axis(data_key="name"),
    rx.recharts.y_axis(data_key="uv", y_axis_id="left", stroke="#8884d8"),
    rx.recharts.y_axis(data_key="pv", y_axis_id="right", orientation="right", stroke="#82ca9d"),
    rx.recharts.graphing_tooltip(),
    rx.recharts.legend(),
    data=data,
    width = "100%",
    height = 300,
  )
```
