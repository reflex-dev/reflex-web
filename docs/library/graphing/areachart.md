---
components:
    - rx.recharts.AreaChart
    - rx.recharts.Area
---

# Area Chart

```python exec
import reflex as rx
import random
```

## Simple Example

A Recharts area chart is a type of chart that displays quantitative data using filled areas between a line connecting data points and the axis.

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
    ),
    rx.recharts.x_axis(data_key="name"),
    rx.recharts.y_axis(),
    data=data,
    width = "100%",
    height = 250,
  )
```

## Example with Sync ID

The `sync_id` prop allows you to sync two graphs. In the example, it is set to "1" for both charts, indicating that they should be synchronized. This means that any interactions (such as brushing) performed on one chart will be reflected in the other chart.

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

## Example with StackID

The `stack_id`prop allows you to stack multiple graphs on top of each other. In the example, it is set to "1" for both charts, indicating that they should be stacked together. This means that the bars or areas of the charts will be vertically stacked, with the values of each chart contributing to the total height of the stacked areas or bars.

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

def area_stack():
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="uv", 
            stroke=rx.color("accent", 9),
            fill=rx.color("accent", 8),
            stack_id="1", 
        ),
        rx.recharts.area(
            data_key="pv", 
            stroke=rx.color("green", 9),
            fill=rx.color("green", 8),
            stack_id="1",
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=data,
        stack_offset="none",
        margin={"top": 5, "right": 5, "bottom": 5, "left": 5},
        width = "100%",
        height = 300,
    )
```
## Example with Multiple Axis

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
        data_key="uv", stroke="#8884d8", fill="#8884d8", x_axis_id="primary", y_axis_id="left",
    ),
    rx.recharts.area(
        data_key="pv", x_axis_id="secondary", y_axis_id="right", type_="monotone", stroke="#82ca9d", fill="#82ca9d"
    ),
    rx.recharts.x_axis(data_key="name", x_axis_id="primary"),
    rx.recharts.x_axis(data_key="name", x_axis_id="secondary", orientation="top"),
    rx.recharts.y_axis(data_key="uv", y_axis_id="left"),
    rx.recharts.y_axis(data_key="pv", y_axis_id="right", orientation="right"),
    rx.recharts.graphing_tooltip(),
    rx.recharts.legend(),
    data=data,
    width = "100%",
    height = 300,
  )
```

## Example with State

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
        width = "100%",
        height=400,
      ),
      width="100%",
    )
```
