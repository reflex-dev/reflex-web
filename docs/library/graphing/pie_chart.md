---
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

---

```reflex
docgraphing(pie_chart_simple_example, comp=eval(pie_chart_simple_example),  data =  "data01=" + str(data01))
```

```reflex
docgraphing(pie_chart_complex_example, comp=eval(pie_chart_complex_example),  data =  "data01=" + str(data01))
```
