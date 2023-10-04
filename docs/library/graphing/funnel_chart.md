---
import reflex as rx
from pcweb.templates.docpage import docdemo, docgraphing

data = [
  {
    "value": 100,
    "name": "Sent",
    "fill": "#8884d8"
  },
  {
    "value": 80,
    "name": "Viewed",
    "fill": "#83a6ed"
  },
  {
    "value": 50,
    "name": "Clicked",
    "fill": "#8dd1e1"
  },
  {
    "value": 40,
    "name": "Add to Cart",
    "fill": "#82ca9d"
  },
  {
    "value": 26,
    "name": "Purchased",
    "fill": "#a4de6c"
  }
]

funnel_chart_example = """rx.funnel_chart(
                rx.funnel(
                    data_key="value",
                    data=data),
                #rx.label_list(position="right", data_key="name"),
                data=data,
                width=730, 
                height=250)"""
---

A funnel chart is a graphical representation used to visualize how data moves through a process. In a funnel chart, the dependent variable’s value diminishes in the subsequent stages of the process. It can be used to demonstrate the flow of users through for example a business or sales process.


```reflex
docgraphing(
  funnel_chart_example, 
  comp = eval(funnel_chart_example),
  data =  "data=" + str(data)
)
```