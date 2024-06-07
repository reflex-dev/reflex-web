---
components:
    - rx.recharts.AreaChart
    - rx.recharts.Area
---

# Area Chart

```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo, docgraphing
import random

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

range_data = [
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

```



An area chart combines the line chart and bar chart to show how one or more groups’ numeric values change over the progression of a second variable, typically that of time. An area chart is distinguished from a line chart by the addition of shading between lines and a baseline, like in a bar chart.

For an area chart we must define an `rx.recharts.area()` component that has a `data_key` which clearly states which variable in our data we are tracking. In this simple example we track `uv` against `name` and therefore set the `rx.recharts.x_axis` to equal `name`.

## Simple Example

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

def area_simple():
  return rx.recharts.area_chart(
    rx.recharts.area(
        data_key="uv",
        stroke="#8884d8",
        fill="#8884d8",
    ),
    rx.recharts.x_axis(data_key="name"),
    rx.recharts.y_axis(),
    data=data,
    width = 600,
    height = 250,
  )
```

Multiple areas can be placed on the same `area_chart`. `Tooltips` are the little boxes that pop up when you hover over something that shows it's value.
## Example with Sync ID

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

def area_sync():
  return rx.vstack(
    rx.recharts.bar_chart(
      rx.recharts.bar(
          data_key="uv", stroke="#8884d8", fill="#8884d8"
      ),
      rx.recharts.bar(
          data_key="pv", stroke="#82ca9d", fill="#82ca9d",
      ),
      rx.recharts.x_axis(data_key="name"),
      rx.recharts.y_axis(),
      rx.recharts.graphing_tooltip(),
      data=data,
      sync_id="1",
      width = 600,
      height = 200,
    ),
    rx.recharts.composed_chart(
      rx.recharts.area(
          data_key="uv", stroke="#8884d8", fill="#8884d8"
      ),
      rx.recharts.line(
          data_key="pv", type_="monotone", stroke="#ff7300",
      ),
      
      rx.recharts.x_axis(data_key="name"),
      rx.recharts.y_axis(),
      rx.recharts.graphing_tooltip(),
      rx.recharts.brush(
          data_key="name", height=30, stroke="#8884d8"
      ),
      data=data,
      sync_id="1",
      width = 600,
      height = 250,
    )
  )
```

You can also assign a range in the area by assiging the data_key in the `rx.recharts.area` to a list with two elements, i.e. here a range of two temperatures for each date. Using `layout` prop to specify whether the graph is `horizontal` or `vertical`.

## Example with StackID

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

rx.recharts.area_chart(
  rx.recharts.area(
      data_key="uv", stroke="#8884d8", fill="#8884d8", stack_id="1", 
      base_value=1000,
  ),
  rx.recharts.area(
      data_key="pv", stroke="#82ca9d", fill="#82ca9d", stack_id="1",
      base_value=1000,
  ),
  rx.recharts.x_axis(data_key="name"),
  rx.recharts.y_axis(),
  data=data,
  stack_offset="none",
  margin={"top": 5, "right": 5, "bottom": 5, "left": 5},
  layout="horizontal",
  width = 600,
  height = 250,
)
```
## Example with Multiple Axis

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
        data_key="uv", stroke="#8884d8", fill="#8884d8", x_axis_id="primary", y_axis_id="left",
    ),
    rx.recharts.area(
        data_key="pv", x_axis_id="secondary", y_axis_id="right", type="monotone", stroke="#82ca9d", fill="#82ca9d"
    ),
    rx.recharts.x_axis(data_key="name", x_axis_id="primary"),
    rx.recharts.x_axis(data_key="name", x_axis_id="secondary", orientation="top"),
    rx.recharts.y_axis(data_key="uv", y_axis_id="left"),
    rx.recharts.graphing_tooltip(),
    rx.recharts.legend(),
    data=data,
    width = 600,
    height = 300,
  )
```


Here is an example of an area graph with a `State`. Here we have defined a function `randomize_data`, which randomly changes the data for both graphs when the first defined `area` is clicked on using `on_click=AreaState.randomize_data`.

```python demo exec
class AreaState(rx.State):
    data = data
    curve_type = ""
    def randomize_data(self):
        for i in range(len(self.data)):
            self.data[i]["uv"] = random.randint(0, 10000)
            self.data[i]["pv"] = random.randint(0, 10000)
            self.data[i]["amt"] = random.randint(0, 10000)

    def change_curve_type(self, type_input):
        self.curve_type = type_input

def area_4():
    return rx.vstack(
      rx.hstack(
        rx.text("Select Curve Type"),
        rx.select(
          [
            'basis',
            'basisClosed',
            'basisOpen',
            'bumpX',
            'bumpY',
            'bump',
            'linear',
            'linearClosed',
            'natural',
            'monotoneX',
            'monotoneY',
            'monotone',
            'step',
            'stepBefore',
            'stepAfter'
          ],
          on_change = AreaState.change_curve_type,
          default_value = 'basis',
        ),
      ),
        rx.recharts.area_chart(
            rx.recharts.area(
                data_key="uv",
                stroke="#8884d8",
                fill="#8884d8",
                on_click=AreaState.randomize_data,
                type_ = AreaState.curve_type,
            ),
            rx.recharts.area(
                data_key="pv",
                stroke="#82ca9d",
                fill="#82ca9d",
                on_click=AreaState.randomize_data,
                type_ = AreaState.curve_type,
            ),
            rx.recharts.x_axis(
                data_key="name",
            ),
            rx.recharts.y_axis(),
            rx.recharts.legend(),
            rx.recharts.cartesian_grid(
                stroke_dasharray="3 3",
            ),
            data=AreaState.data,
            width=500,
            height=400,
        )
    )
```
