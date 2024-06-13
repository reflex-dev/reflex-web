---
components:
    - rx.recharts.CartesianGrid
    # - rx.recharts.CartesianAxis
---

# Cartesian Grid

```python exec
import reflex as rx
```

## Simple Example

A cartesian axis adds in reference axes to the cartesian graphs. Prop `stroke_dasharray` is used to specify the pattern of dashes and gaps for the grid line, it accepts a string value that represents the dash pattern.  `stroke_dasharray = "4"` will create a grid with dashes of length 4 and no gaps. `stroke_dasharray = "4 1"` will create a grid with dashes of length 4 and gaps of length 1. `stroke_dasharray = "4 1 2"` will create a grid with a repeating pattern of dashes and gaps. dash (length 4), gap (length 1), dash (length 2); dash (length 4), gap (length 1), dash (length 2), etc. 

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

def cgrid_1():
  return rx.recharts.composed_chart(
    rx.recharts.area(
        data_key="uv",
        stroke="#8884d8",
        fill="#8884d8"
    ), 
    rx.recharts.bar(
        data_key="amt",
        bar_size=20,
        fill="#413ea0"
    ),
    rx.recharts.line(
        data_key="pv",
        type_="monotone",
        stroke="#ff7300"
    ), 
    rx.recharts.x_axis(data_key="name"), 
    rx.recharts.y_axis(),
    rx.recharts.cartesian_grid(stroke_dasharray="4 1"),
    rx.recharts.graphing_tooltip(),
    data=data,
    width = 600,
    height = 300,
  )
```

## Example with Hidden Axises

Axises can be set show or hidden using `horizontal` and `vertical` props. If set to `False`, no horizontal/vertical grid will be drawn. 

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

def cgrid_1():
  return rx.recharts.composed_chart(
    rx.recharts.area(
        data_key="uv",
        stroke="#8884d8",
        fill="#8884d8"
    ), 
    rx.recharts.bar(
        data_key="amt",
        bar_size=20,
        fill="#413ea0"
    ),
    rx.recharts.line(
        data_key="pv",
        type_="monotone",
        stroke="#ff7300"
    ), 
    rx.recharts.x_axis(data_key="name"), 
    rx.recharts.y_axis(),
    rx.recharts.cartesian_grid(
      stroke_dasharray="4 1",
      vertical=False, 
      horizontal=True,
    ),
    rx.recharts.graphing_tooltip(),
    data=data,
    width = 600,
    height = 300,
  )
```

## Example with Custom Grid Lines

`horizontal_points` and `vertical_points` props are used to specify custom grid lines on the chart. The `horizontal_points` prop defines the positions of horizontal grid lines along the y-axis, while the `vertical_points` prop defines the positions of vertical grid lines along the x-axis. 

```md alert info
# Note that the values provided to these props are not directly related to the axis values but rather represent pixel offsets from the top and right edges of the chart, respectively.
```

```python demo graphing

data2 = [
    {"x": 100, "y": 200, "z": 200},
    {"x": 120, "y": 100, "z": 260},
    {"x": 170, "y": 300, "z": 400},
    {"x": 170, "y": 250, "z": 280},
    {"x": 150, "y": 400, "z": 500},
    {"x": 110, "y": 280, "z": 200},
    {"x": 200, "y": 150, "z": 300},
    {"x": 130, "y": 350, "z": 450},
    {"x": 90, "y": 220, "z": 180},
    {"x": 180, "y": 320, "z": 350},
    {"x": 140, "y": 230, "z": 320},
    {"x": 160, "y": 180, "z": 240},
]


def cgrid_2():
    return rx.recharts.scatter_chart(
        rx.recharts.scatter(
            data=data2,
            fill="#8884d8",
        ),
        rx.recharts.x_axis(data_key="x", type_="number"),
        rx.recharts.y_axis(data_key="y"),
        rx.recharts.cartesian_grid(
            stroke_dasharray="3 3",
            horizontal_points=[0, 25, 50],
            vertical_points=[65, 90, 115],
        ),
        height = 200,
        width = 500,
    )

```

## Example with Color Filling

The `fill` prop specifies the color of the grid area, and the `fill_opacity` prop specifies the opacity of the grid color.

```python demo graphing

data3 = [
    {"x": 100, "y": 200, "z": 200},
    {"x": 120, "y": 100, "z": 260},
    {"x": 170, "y": 300, "z": 400},
    {"x": 170, "y": 250, "z": 280},
    {"x": 150, "y": 400, "z": 500},
    {"x": 110, "y": 280, "z": 200},
    {"x": 200, "y": 150, "z": 300},
    {"x": 130, "y": 350, "z": 450},
    {"x": 90, "y": 220, "z": 180},
    {"x": 180, "y": 320, "z": 350},
    {"x": 140, "y": 230, "z": 320},
    {"x": 160, "y": 180, "z": 240},
]

def cgrid_3():
    return rx.recharts.scatter_chart(
        rx.recharts.scatter(
            data=data3,
            fill="#8884d8",
        ),
        rx.recharts.x_axis(data_key="x", type_="number"),
        rx.recharts.y_axis(data_key="y"),
        rx.recharts.cartesian_grid(
            stroke_dasharray="3 3",
            fill="red",
            fill_opacity=0.25,
        ),
        height = 200,
        width = 500,
    )

```