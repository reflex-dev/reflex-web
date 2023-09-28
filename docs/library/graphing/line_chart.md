---
import reflex as rx
from pcweb.templates.docpage import docdemo

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

line_chart_simple_example = """rx.line_chart(
                rx.line(
                    data_key="pv",
                    stroke="#8884d8",),
                rx.line(
                    data_key="uv",
                    stroke="#82ca9d",), 
                rx.x_axis(data_key="name"), 
                rx.y_axis(),
                data=data,
                width=730, 
                height=250)"""

line_chart_complex_example = """rx.line_chart(
                rx.line(
                    data_key="pv",
                    type_="monotone",
                    stroke="#8884d8",),
                rx.line(
                    data_key="uv",
                    type_="monotone",
                    stroke="#82ca9d",), 
                rx.x_axis(data_key="name"), 
                rx.y_axis(),
                rx.cartesian_grid(stroke_dasharray="3 3"),
                #rx.tooltip(),
                rx.legend(),
                data=data,
                width=730, 
                height=250)"""
---

A line chart is a type of chart used to show information that changes over time. Line charts are created by plotting a series of several points and connecting them with a straight line.

For a line chart we must define an `rx.line()` component for each set of values we wish to plot. Each `rx.line()` component has a `data_key` which clearly states which variable in our data we are tracking. In this simple example we plot `pv` and `uv` as separate lines against the `name` column which we set as the `data_key` in `rx.x_axis`.

```reflex
docdemo(line_chart_simple_example, comp=eval(line_chart_simple_example))
```

Our second example uses exactly the same data as our first example, except now we add some extra features to our line graphs. We add a `type_` prop to `rx.line` to style the lines differently. In addition, we add an `rx.cartesian_grid` to get a grid in the background and we add an `rx.legend` to give us a legend for our graphs. 

```reflex
docdemo(line_chart_complex_example, comp=eval(line_chart_complex_example))
```

