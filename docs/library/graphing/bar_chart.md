```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo, docgraphing

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


bar_chart_example = """rx.recharts.bar_chart(
                rx.recharts.bar(
                    data_key="uv",
                    stroke="#8884d8",
                    fill="#8884d8"
                ), 
                rx.recharts.x_axis(data_key="name"), 
                rx.recharts.y_axis(),
                data=data)"""

bar_chart_example_2 = """rx.recharts.bar_chart(
                rx.recharts.bar(
                    data_key="uv",
                    stroke="#8884d8",
                    fill="#8884d8"
                ), 
                rx.recharts.bar(
                    data_key="pv",
                    stroke="#82ca9d",
                    fill="#82ca9d"
                ), 
                rx.recharts.x_axis(data_key="name"), 
                rx.recharts.y_axis(),
                data=data)"""


range_bar_chart = """rx.recharts.bar_chart(
                rx.recharts.bar(
                    data_key="temperature",
                    stroke="#8884d8",
                    fill="#8884d8"
                ), 
                rx.recharts.x_axis(data_key="day"), 
                rx.recharts.y_axis(),
                data=range_data)"""
```


A bar chart presents categorical data with rectangular bars with heights or lengths proportional to the values that they represent.

For a bar chart we must define an `rx.recharts.bar()` component for each set of values we wish to plot. Each `rx.recharts.bar()` component has a `data_key` which clearly states which variable in our data we are tracking. In this simple example we plot `uv` as a bar against the `name` column which we set as the `data_key` in `rx.recharts.x_axis`.


```python eval
docgraphing(
  bar_chart_example, 
  comp = eval(bar_chart_example),
  data =  "data=" + str(data)
)
```

Multiple bars can be placed on the same `bar_chart`, using multiple `rx.recharts.bar()` components.

```python eval
docgraphing(
  bar_chart_example_2, 
  comp = eval(bar_chart_example_2),
  data =  "data=" + str(data)
)
```

You can also assign a range in the bar by assiging the data_key in the `rx.recharts.bar` to a list with two elements, i.e. here a range of two temperatures for each date.

```python eval
docgraphing(
  range_bar_chart, 
  comp = eval(range_bar_chart),
  data =  "data=" + str(range_data)
)
```