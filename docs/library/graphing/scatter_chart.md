---
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

scatter_chart_simple_example = """rx.scatter_chart(
                rx.scatter(
                    data=data01,
                    fill="#8884d8",),
                rx.x_axis(data_key="x"), 
                rx.y_axis(data_key="y")
                )"""

scatter_chart_simple_complex = """rx.scatter_chart(
                rx.scatter(
                    data=data01,
                    fill="#8884d8",
                    name="A"
                  ),
                rx.scatter(
                    data=data02,
                    fill="#82ca9d",
                    name="B"
                  ),
                rx.cartesian_grid(stroke_dasharray="3 3"),
                rx.x_axis(data_key="x"), 
                rx.y_axis(data_key="y"),
                rx.z_axis(data_key="z", range=[60, 400], name="score"),
                rx.legend(),
                rx.graphing_tooltip(),
                margin={"top": 20, "right": 20}
                )"""

---
A scatter chart always has two value axes to show one set of numerical data along a horizontal (value) axis and another set of numerical values along a vertical (value) axis. The chart displays points at the intersection of an x and y numerical value, combining these values into single data points.

For a scatter chart we must define an `rx.scatter()` component for each set of values we wish to plot. Each `rx.scatter()` component has a `data` prop which clearly states which data source we plot. We also must define `rx.x_axis()` and `rx.y_axis()` so that the graph knows what data to plot on each axis.

```reflex
docgraphing(scatter_chart_simple_example, comp=eval(scatter_chart_simple_example), data =  "data01=" + str(data01))
```

We can also add two scatters on one chart by using two `rx.scatter()` components, and we can define an `rx.z_axis()` which represents a third column of data and is represented by the size of the dots in the scatter plot.

```reflex
docgraphing(scatter_chart_simple_complex, comp=eval(scatter_chart_simple_complex), data =  "data01=" + str(data01) + "&data02=" + str(data02))
```