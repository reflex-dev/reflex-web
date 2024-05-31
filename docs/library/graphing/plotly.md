---
components:
    - rx.plotly
---

# Plotly

```python exec
import reflex as rx
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pcweb import constants
```

Plotly is a graphing library that can be used to create interactive graphs.

## Basic Example
Let's create a line graph of life expectancy in Canada.

```python demo exec
import plotly.express as px

df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')  

def line_chart():
    return rx.center(
        rx.plotly(data=fig),
    )
```

```md alert info
# When integrating Plotly graphs into your UI code, note that the method for displaying the graph differs from a regular Python script. Instead of using `fig.show()`, use `rx.plotly(data=fig)` within your UI code to ensure the graph is properly rendered and displayed within the user interface
```
## A More Complex Example
Let's create a 3D surface plot of Mount Bruno. 

```python demo exec
import plotly.graph_objects as go
import pandas as pd

# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

fig = go.Figure(data=[go.Surface(z=z_data.values)])
fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                  highlightcolor="limegreen", project_z=True))
fig.update_layout(
    scene_camera_eye=dict(x=1.87, y=0.88, z=-0.64),
    width=500, height=500,
    margin=dict(l=65, r=50, b=65, t=90)
)

def mountain_surface():
    return rx.center(
        rx.plotly(data=fig),
    )
```

## Plot as State Var
Set plot as a State var when the plot need to be updated during run time. 

```python demo exec
import plotly.express as px
class PlotlyState(rx.State):
    df = px.data.gapminder().query(f"country=='Canada'")
    figure = px.line(
        df,
        x="year",
        y="lifeExp",
        title="Life expectancy in Canada",
    )

    def set_selected_country(self, country):
        self.df = px.data.gapminder().query(f"country=='{country}'")
        self.figure = px.line(
            self.df,
            x="year",
            y="lifeExp",
            title=f"Life expectancy in {country}",
        )


def line_chart_with_state():
    return rx.vstack(
        rx.select(
            ['China', 'France', 'United Kingdom', 'United States', 'Canada'],
            default_value="United States",
            on_change=PlotlyState.set_selected_country,
        ),
        rx.plotly(data=PlotlyState.figure),
    )
```

<!-- ## Adding styles to the chart
Use `update_layout()` method to update the layout of your chart. Checkout [Plotly Layouts](https://plotly.com/python/reference/layout/) for all layouts props.  -->

<!-- in progress -->

