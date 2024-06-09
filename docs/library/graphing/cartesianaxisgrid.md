---
components:
    - rx.recharts.CartesianGrid
    - rx.recharts.CartesianAxis
---

# Cartesian Grid

```python exec
import reflex as rx
```

## Simple Example

A cartesian axis adds in reference axes to the cartesian graphs. Prop `stroke_dasharray` is used to specify the pattern of dashes and gaps for the grid line, it accepts a string value that represents the dash pattern.  `stroke_dasharray = "4"` will create a grid with dashes of length 4 and no gaps. `stroke_dasharray = "4 1"` will create a grid with dashes of length 4 and gaps of length 1. `stroke_dasharray = "4 1"` will create a grid with a repeating pattern of dashes and gaps. dash (length 4), gap (length 1), dash (length 2); dash (length 4), gap (length 1), dash (length 2), etc. 

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

def cartesian_simple():
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
