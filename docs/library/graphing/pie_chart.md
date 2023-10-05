```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo, docgraphing

data01 = [
  {
    "name": "Group A",
    "value": 400
  },
  {
    "name": "Group B",
    "value": 300
  },
  {
    "name": "Group C",
    "value": 300
  },
  {
    "name": "Group D",
    "value": 200
  },
  {
    "name": "Group E",
    "value": 278
  },
  {
    "name": "Group F",
    "value": 189
  }
]
data02 = [
  {
    "name": "Group A",
    "value": 2400
  },
  {
    "name": "Group B",
    "value": 4567
  },
  {
    "name": "Group C",
    "value": 1398
  },
  {
    "name": "Group D",
    "value": 9800
  },
  {
    "name": "Group E",
    "value": 3908
  },
  {
    "name": "Group F",
    "value": 4800
  }
]

pie_chart_simple_example = """rx.pie_chart(
                rx.pie(
                    data=data01,
                    data_key="value",
                    name_key="name",
                    cx="50%",
                    cy="50%",
                    fill="#8884d8",
                    label=True,
                    )
                    )"""

pie_chart_complex_example = """rx.pie_chart(
                  rx.pie(
                    data=data01,
                    data_key="value",
                    name_key="name",
                    cx="50%",
                    cy="50%",
                    fill="#82ca9d",
                    inner_radius="60%",
                    ),
                    rx.pie(
                    data=data02,
                    data_key="value",
                    name_key="name",
                    cx="50%",
                    cy="50%",
                    fill="#8884d8",
                    outer_radius="50%",
                    ),
                    rx.graphing_tooltip(),
                    )"""

```

A pie chart is a circular statistical graphic which is divided into slices to illustrate numerical proportion.

For a pie chart we must define an `rx.pie()` component for each set of values we wish to plot. Each `rx.pie()` component has a `data`, a `data_key` and a `name_key` which clearly states which data and which variables in our data we are tracking. In this simple example we plot `value` column as our `data_key` against the `name` column which we set as our `name_key`.

```python eval
docgraphing(pie_chart_simple_example, comp=eval(pie_chart_simple_example),  data =  "data01=" + str(data01))
```

We can also add two pies on one chart by using two `rx.pie` components.

```python eval
docgraphing(pie_chart_complex_example, comp=eval(pie_chart_complex_example),  data =  "data01=" + str(data01) + "&data02=" + str(data02))
```
