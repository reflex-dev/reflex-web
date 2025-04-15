---
components:
  - pyplot
---

```python exec
import reflex as rx
from reflex_pyplot import pyplot
import numpy as np
import random
import matplotlib.pyplot as plt
from reflex.style import toggle_color_mode
```

# Pyplot

Pyplot (`reflex-pyplot`) is a graphing library that wraps Matplotlib. Use the `pyplot` component to display any Matplotlib plot in your app. Check out [Matplotlib](https://matplotlib.org/) for more information.

## Installation

Install the `reflex-pyplot` package using pip.

```bash
pip install reflex-pyplot
```

## Basic Example

To display a Matplotlib plot in your app, you can use the `pyplot` component. Pass in the figure you created with Matplotlib to the `pyplot` component as a child.

```python demo exec
import matplotlib.pyplot as plt
import reflex as rx
from reflex_pyplot import pyplot
import numpy as np

def create_contour_plot():
    X, Y = np.meshgrid(np.linspace(-3, 3, 256), np.linspace(-3, 3, 256))
    Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)
    levels = np.linspace(Z.min(), Z.max(), 7)

    fig, ax = plt.subplots()
    ax.contourf(X, Y, Z, levels=levels)
    plt.close(fig)
    return fig

def pyplot_simple_example():
    return rx.card(
            pyplot(create_contour_plot(), width="100%", height="400px"),
            bg_color='#ffffff',
            width="100%",
        )
```

```md alert info
# You must close the figure after creating

Not closing the figure could cause memory issues.
```

## Stateful Example

Lets create a scatter plot of random data. We'll also allow the user to randomize the data and change the number of points.

In this example, we'll use a `color_mode_cond` to display the plot in both light and dark mode. We need to do this manually here because the colors are determined by the matplotlib chart and not the theme.

```python demo exec
import random
from typing import Literal
import matplotlib.pyplot as plt
import reflex as rx
from reflex_pyplot import pyplot
import numpy as np


def create_plot(theme: str, plot_data: tuple, scale: list):
    bg_color, text_color = ('#1e1e1e', 'white') if theme == 'dark' else ('white', 'black')
    grid_color = '#555555' if theme == 'dark' else '#cccccc'

    fig, ax = plt.subplots(facecolor=bg_color)
    ax.set_facecolor(bg_color)

    for (x, y), color in zip(plot_data, ["#4e79a7", "#f28e2b", "#59a14f"]):
        ax.scatter(x, y, c=color, s=scale, label=color, alpha=0.6, edgecolors="none")

    ax.legend(facecolor=bg_color, edgecolor='none', labelcolor=text_color)
    ax.grid(True, color=grid_color)
    ax.tick_params(colors=text_color)
    for spine in ax.spines.values():
        spine.set_edgecolor(text_color)

    for item in [ax.xaxis.label, ax.yaxis.label, ax.title]:
        item.set_color(text_color)
    plt.close(fig)

    return fig

class PyplotState(rx.State):
    num_points: int = 100
    plot_data: tuple
    scale: list
    fig: plt.Figure = plt.Figure()

    @rx.event
    def randomize(self):
        self.plot_data = tuple(np.random.rand(2, self.num_points) for _ in range(3))
        self.scale = [random.uniform(0, 100) for _ in range(self.num_points)]

    @rx.event
    def set_num_points(self, num_points: list[int]):
        self.num_points = num_points[0]
        self.randomize()
    
    @rx.event
    def create_fig(self, theme: Literal["light", "dark"]):
        self.plot_data = tuple(np.random.rand(2, 100) for _ in range(3))
        self.scale = [random.uniform(0, 100) for _ in range(100)]
        self.fig = create_plot(
            theme, self.plot_data, self.scale
        )

def pyplot_example():
    return rx.vstack(
        rx.card(
            pyplot(
                PyplotState.fig,
                width="100%",
                height="100%",
                on_mount=rx.color_mode_cond(PyplotState.create_fig("light"), PyplotState.create_fig("dark")),
            ),
            rx.vstack(
                rx.hstack(
                    rx.button(
                        "Randomize",
                        on_click=PyplotState.randomize,
                    ),
                    rx.text("Number of Points:"),
                    rx.slider(
                        default_value=100,
                        min_=10,
                        max=1000,
                        on_value_commit=PyplotState.set_num_points,
                    ),
                    width="100%",
                ),
                width="100%",
            ),
            width="100%",
        ),
        justify_content="center",
        align_items="center",
        height="100%",
        width="100%",
    )
```
