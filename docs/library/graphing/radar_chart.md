---
import reflex as rx
from pcweb.templates.docpage import docdemo, docgraphing

data = [
  {
    "subject": "Math",
    "A": 120,
    "B": 110,
    "fullMark": 150
  },
  {
    "subject": "Chinese",
    "A": 98,
    "B": 130,
    "fullMark": 150
  },
  {
    "subject": "English",
    "A": 86,
    "B": 130,
    "fullMark": 150
  },
  {
    "subject": "Geography",
    "A": 99,
    "B": 100,
    "fullMark": 150
  },
  {
    "subject": "Physics",
    "A": 85,
    "B": 90,
    "fullMark": 150
  },
  {
    "subject": "History",
    "A": 65,
    "B": 85,
    "fullMark": 150
  }
]

radar_chart_simple_example = """rx.radar_chart(
                rx.radar(
                    data_key="A",
                    stroke="#8884d8",
                    fill="#8884d8",
                    ),
                    rx.polar_grid(),
                    rx.polar_angle_axis(data_key="subject"),
                    data=data
                    )"""

radar_chart_complex_example = """rx.radar_chart(
                rx.radar(
                    data_key="A",
                    stroke="#8884d8",
                    fill="#8884d8",
                    ),
                rx.radar(
                    data_key="B",
                    stroke="#82ca9d",
                    fill="#82ca9d",
                    fill_opacity=0.6,
                    ),
                    rx.polar_grid(),
                    rx.polar_angle_axis(data_key="subject"),
                    rx.legend(),
                    data=data
                    )"""

---
A radar chart shows multivariate data of three or more quantitative variables mapped onto an axis. 

For a radar chart we must define an `rx.radar()` component for each set of values we wish to plot. Each `rx.radar()` component has a `data_key` which clearly states which variable in our data we are plotting. In this simple example we plot the `A` column of our data against the `subject` column which we set as the `data_key` in `rx.polar_angle_axis`. 


```reflex
docgraphing(radar_chart_simple_example, comp=eval(radar_chart_simple_example),  data =  "data=" + str(data))
```

We can also add two radars on one chart by using two `rx.radar` components.

```reflex
docgraphing(radar_chart_complex_example, comp=eval(radar_chart_complex_example),  data =  "data=" + str(data))
```

