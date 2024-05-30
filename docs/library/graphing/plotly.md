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

def line():
    df = pd.read_csv("data/canada_life.csv")
    line = px.line(df, x="year", y="lifeExp", title="Life expectancy in Canada")
    return line


# Read data from a csv
def mount():
    z_data = pd.read_csv("data/mt_bruno_elevation.csv")
    mount = go.Figure(data=[go.Surface(z=z_data.values)])
    mount.update_traces(
        contours_z=dict(
            show=True, usecolormap=True, highlightcolor="limegreen", project_z=True
        )
    )
    mount.update_layout(
        scene_camera_eye=dict(x=1.87, y=0.88, z=-0.64),
        width=500,
        height=500,
        margin=dict(l=65, r=50, b=65, t=90),
    )
    return mount

style = {
    "box": {
        "borderRadius": "1em",
        "bg": "white",
        "boxShadow": "rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px",
        "padding": 4,
        "width": "100%",
        "overflow_x": "auto",
    }
}
```

Plotly is a graphing library that can be used to create interactive graphs.

## Basic Example
Let's create a line graph of life expectancy in Canada.

```python eval
rx.center(
    rx.plotly(data=line()),
    style=style["box"],
)
```


First create a plotly figure. In this example we use plotly express to do so.

```python
import plotly.express as px

df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')      
```

Now pass the plotly figure to the Plotly component.

```python
rx.plotly(data=fig)
```
```md alert info
# When integrating Plotly graphs into your UI code, note that the method for displaying the graph differs from a regular Python script. Instead of using `fig.show()`, use `rx.plotly(data=fig)` within your UI code to ensure the graph is properly rendered and displayed within the user interface
```
## A More Complex Example
Let's create a 3D surface plot of Mount Bruno.

```python eval
rx.center(
  rx.vstack(
      rx.plotly(data=mount()),
  ),
  style=style["box"],
)
```

Read in the Mount Bruno data as a csv and create a plotly figure.

```python
import plotly.graph_objects as go
import pandas as pd

# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

fig = go.Figure(data=[go.Surface(z=z_data.values)])
fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                  highlightcolor="limegreen", project_z=True))
fig.update_layout(scene_camera_eye=dict(x=1.87, y=0.88, z=-0.64),
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90)
)
```

Now pass the plotly figure again to the plotly component.


```python
rx.plotly(data=fig)
```

## Plot as State Var
Set plot as a State var when the plot need to be updated during run time. 

```python demo exec
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


def line_with_state():
    return rx.vstack(
        rx.select(
            ['China', 'France', 'United Kingdom', 'United States', 'Canada'],
            default_value="United States",
            on_change=PlotlyState.set_selected_country,
        ),
        rx.plotly(data=PlotlyState.figure),
    )
```



