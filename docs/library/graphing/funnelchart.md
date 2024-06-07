---
components:
    - rx.recharts.FunnelChart
    - rx.recharts.Funnel
---

```python exec
import reflex as rx
import random
```

# Funnel Chart

A funnel chart is a graphical representation used to visualize how data moves through a process. In a funnel chart, the dependent variable’s value diminishes in the subsequent stages of the process. It can be used to demonstrate the flow of users through for example a business or sales process.

```python demo graphing
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

def funnel_simple():
  return rx.recharts.funnel_chart(
    rx.recharts.funnel(
      rx.recharts.label_list(
        position="right",
        data_key="name",
        fill="#000",
        stroke="none",
      ),
      rx.recharts.label_list(
        position="right",
        data_key="name",
        fill="#000",
        stroke="none",
      ),
      data_key="value",
      data=data,
    ),
    rx.recharts.graphing_tooltip(),
    width=730,
    height=250,
  )
```

Here is an example of a funnel chart with a `State`. Here we have defined a function `randomize_data`, which randomly changes the data when the graph is clicked on using `on_click=FunnelState.randomize_data`.

```python exec
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
```

```python demo exec
class FunnelState(rx.State):
    data = data
    def randomize_data(self):
        self.data[0]["value"] = 100
        for i in range(len(self.data) - 1):
            self.data[i + 1]["value"] = self.data[i][
                "value"
            ] - random.randint(0, 20)


def funnel_dynamic():
  return rx.recharts.funnel_chart(
    rx.recharts.funnel(
      rx.recharts.label_list(
        position="right",
        data_key="name",
        fill="#000",
        stroke="none",
      ),
      data_key="value",
      data=FunnelState.data,
      on_click=FunnelState.randomize_data,
    ),
    rx.recharts.graphing_tooltip(),
    width=730,
    height=250,
  )
```
