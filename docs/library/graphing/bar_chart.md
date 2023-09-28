---
import reflex as rx
from pcweb.templates.docpage import docdemo

data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300
  }
]

bar_chart_example = """rx.bar_chart(
                rx.bar(
                    data_key="pv",
                    fill="#8884d8",),
                rx.bar(
                    data_key="uv",
                    fill="#82ca9d",),
                rx.x_axis(data_key="name"), 
                rx.y_axis(),
                rx.legend(),
                data=data,
                width=730, 
                height=250)"""
---

A bar chart presents categorical data with rectangular bars with heights or lengths proportional to the values that they represent.

For a bar chart we must define an `rx.bar()` component for each set of values we wish to plot. Each `rx.bar()` component has a `data_key` which clearly states which variable in our data we are tracking. In this simple example we plot `pv` and `uv` as separate bars against the `name` column which we set as the `data_key` in `rx.x_axis`.

```reflex
docdemo(bar_chart_example, comp=eval(bar_chart_example))
```


