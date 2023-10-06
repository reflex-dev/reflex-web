```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo, docgraphing

data01 = [
  {
    "x": 100,
    "y": 200,
    "z": 200
  },
  {
    "x": 120,
    "y": 100,
    "z": 260
  },
  {
    "x": 170,
    "y": 300,
    "z": 400
  },
  {
    "x": 170,
    "y": 250,
    "z": 280
  },
  {
    "x": 150,
    "y": 400,
    "z": 500
  },
  {
    "x": 110,
    "y": 280,
    "z": 200
  }
]

data02 = [
  {
    "x": 200,
    "y": 260,
    "z": 240
  },
  {
    "x": 240,
    "y": 290,
    "z": 220
  },
  {
    "x": 190,
    "y": 290,
    "z": 250
  },
  {
    "x": 198,
    "y": 250,
    "z": 210
  },
  {
    "x": 180,
    "y": 280,
    "z": 260
  },
  {
    "x": 210,
    "y": 220,
    "z": 230
  }
]

scatter_chart_simple_example = """rx.recharts.scatter_chart(
                rx.recharts.scatter(
                    data=data01,
                    fill="#8884d8",),
                rx.recharts.x_axis(data_key="x", type_="number"), 
                rx.recharts.y_axis(data_key="y")
                )"""

scatter_chart_simple_complex = """rx.recharts.scatter_chart(
                rx.recharts.scatter(
                    data=data01,
                    fill="#8884d8",
                    name="A"
                  ),
                rx.recharts.scatter(
                    data=data02,
                    fill="#82ca9d",
                    name="B"
                  ),
                rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
                rx.recharts.x_axis(data_key="x", type_="number"), 
                rx.recharts.y_axis(data_key="y"),
                rx.recharts.z_axis(data_key="z", range=[60, 400], name="score"),
                rx.recharts.legend(),
                rx.recharts.graphing_tooltip(),
                
                )"""

```

A scatter chart always has two value axes to show one set of numerical data along a horizontal (value) axis and another set of numerical values along a vertical (value) axis. The chart displays points at the intersection of an x and y numerical value, combining these values into single data points.

For a scatter chart we must define an `rx.recharts.scatter()` component for each set of values we wish to plot. Each `rx.recharts.scatter()` component has a `data` prop which clearly states which data source we plot. We also must define `rx.recharts.x_axis()` and `rx.recharts.y_axis()` so that the graph knows what data to plot on each axis.

```python eval
docgraphing(scatter_chart_simple_example, comp=eval(scatter_chart_simple_example), data =  "data01=" + str(data01))
```

We can also add two scatters on one chart by using two `rx.recharts.scatter()` components, and we can define an `rx.recharts.z_axis()` which represents a third column of data and is represented by the size of the dots in the scatter plot.

```python eval
docgraphing(scatter_chart_simple_complex, comp=eval(scatter_chart_simple_complex), data =  "data01=" + str(data01) + "&data02=" + str(data02))
```