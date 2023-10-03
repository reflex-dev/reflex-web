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

```reflex
docgraphing(scatter_chart_simple_example, comp=eval(scatter_chart_simple_example), data =  "data=" + str(data01))
```

```reflex
docgraphing(scatter_chart_simple_complex, comp=eval(scatter_chart_simple_complex), data =  "data01=" + str(data01) + "&data02=" + str(data02))
```