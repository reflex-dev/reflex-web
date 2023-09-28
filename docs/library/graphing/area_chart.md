---
import reflex as rx
from pcweb.templates.docpage import docdemo

rangeData = [
  {
    "day": "05-01",
    "temperature": [
      -1,
      10
    ]
  },
  {
    "day": "05-02",
    "temperature": [
      2,
      15
    ]
  },
  {
    "day": "05-03",
    "temperature": [
      3,
      12
    ]
  },
  {
    "day": "05-04",
    "temperature": [
      4,
      12
    ]
  },
  {
    "day": "05-05",
    "temperature": [
      12,
      16
    ]
  },
  {
    "day": "05-06",
    "temperature": [
      5,
      16
    ]
  },
  {
    "day": "05-07",
    "temperature": [
      3,
      12
    ]
  },
  {
    "day": "05-08",
    "temperature": [
      0,
      8
    ]
  },
  {
    "day": "05-09",
    "temperature": [
      -3,
      5
    ]
  }
]

area_chart_example = """rx.area_chart(
                rx.area(
                    data_key="temperature",
                    stroke="#8884d8",
                    fill="#8884d8",), 
                rx.x_axis(data_key="day"), 
                rx.y_axis(),
                data=rangeData,
                width=730, 
                height=250)"""
---


An area chart combines the line chart and bar chart to show how one or more groups’ numeric values change over the progression of a second variable, typically that of time. An area chart is distinguished from a line chart by the addition of shading between lines and a baseline, like in a bar chart.

For an area chart we must define an `rx.area()` component that has a `data_key` which clearly states which variable in our data we are tracking. In this simple example we track temperature against time and therefore set the `rx.x_axis` to equal `day`.

```reflex
docdemo(area_chart_example, comp=eval(area_chart_example))
```


