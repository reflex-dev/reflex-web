---
author: Alek Petuskey
date: 2023-10-11
title: "New Core Graphing Components"
description: "Using Reflex's new core graphing feature to build a live streaming graphing app."
image: /blog/graphing.png
---

```python exec
import reflex as rx
import random
import asyncio
from pcweb.pages.docs import library
# hacks because curly braces always evaluate python code
pid = "{pid}"
class self(object):
    last_id = "{self.last_id}"
```

With the release of [Reflex v0.2.9](https://github.com/reflex-dev/reflex/releases/tag/v0.2.9) we've reworked the core graphing components from the ground up. The new components are more flexible and easier to use. 

In this post we'll walk through the new components and show how to build a live streaming graphing app. This will also build on the [Unlocking New Workflows with Background Tasks](https://reflex.dev/blog/2023-09-28-unlocking-new-workflows-with-background-tasks/)  post, so if you haven't read that yet, check it out first.

## Striking a Balance

With our new graphing components we are aiming to strike a balance between flexibility and ease of use. We want to make it easy to build a graph, but we also want to make it easy to customize the graph to your needs.

Check out our [graphing docs]({library.graphing.areachart.path}) for more details on the new components.


## Livestreaming Example

In this example we will create a live streaming graph that updates every second with random data.

We start by defining some initial data for our chart to use as well as some imports we will use for the project:

```python
from typing import Any, Dict, List
import reflex as rx
import random
import asyncio

data = [
    \{"name": "A", "uv": 10, "pv": 110, "amt": 210\},
    \{"name": "B", "uv": 20, "pv": 120, "amt": 230\},
    \{"name": "C", "uv": 30, "pv": 120, "amt": 240\},
    \{"name": "D", "uv": 30, "pv": 130, "amt": 210\},
    \{"name": "E", "uv": 20, "pv": 140, "amt": 230\},
    \{"name": "F", "uv": 40, "pv": 170, "amt": 250\},
    \{"name": "G", "uv": 50, "pv": 190, "amt": 260\},
]
```

Here `uv` stands for unique visitors, `pv` stands for page views, and `amt` stands for amount. They are arbitrary values that we will use to populate our graph.

Next we define a `StreamingState` class that will be used to store the data and update it with an event handler:

```python
class StreamingState(rx.State):
    data: List[Dict[str, Any]] = data
    stream: bool = False

    def stop_stream(self):
        self.stream = False

    @rx.background
    async def start_stream(self):
        async with self:
            self.stream = True
        while self.stream:
            async with self:
                for i in range(len(self.data)):
                    self.data[i]["uv"] = random.randint(0, 100)
                    self.data[i]["pv"] = random.randint(100, 200)
                    self.data[i]["amt"] = random.randint(200, 300)
            await asyncio.sleep(3)
```

Here we define a `stop_stream` method that will stop the stream when called. We also define a `start_stream` method that will start the stream. We use the `@rx.background` decorator to run the method in the background. This allows us to update the data without blocking the UI.

Remember to use `async with self:` when updating the state in a background task.

Finally we will define our UI using Reflex's new graphing components. We pass the data from our `StreamingState` class to the `area_chart` component and reference the data key we want to use in `area` component. We also add a buttons to start and stop the stream.

```python exec
data = [
    {"name": "A", "uv": 10, "pv": 110, "amt": 210},
    {"name": "B", "uv": 20, "pv": 120, "amt": 230},
    {"name": "C", "uv": 30, "pv": 120, "amt": 240},
    {"name": "D", "uv": 30, "pv": 130, "amt": 210},
    {"name": "E", "uv": 20, "pv": 140, "amt": 230},
    {"name": "F", "uv": 40, "pv": 170, "amt": 250},
    {"name": "G", "uv": 50, "pv": 190, "amt": 260},
]

class StreamingState(rx.State):
    data = data
    stream = False

    def stop_stream(self):
        self.stream = False

    @rx.background
    async def start_stream(self):
        async with self:
            self.stream = True
        while self.stream:
            async with self:
                for i in range(len(self.data)):
                    self.data[i]["uv"] = random.randint(0, 100)
                    self.data[i]["pv"] = random.randint(100, 200)
                    self.data[i]["amt"] = random.randint(200, 300)
            await asyncio.sleep(3)
```

The result is a live updating graph that looks like this:

```python eval
rx.vstack(
    rx.recharts.area_chart(
        rx.recharts.area(
            data_key="pv",
            fill="#48BB78",
            stroke="#48BB78",
            type_="natural",
        ),
        rx.recharts.x_axis(
            data_key="name",
        ),
        rx.recharts.y_axis(),
        data=StreamingState.data,
        width="90%",
        height=400,
    ),
    rx.hstack(
        rx.button(
            "Start Stream",
            on_click=StreamingState.start_stream,
            is_disabled=StreamingState.stream,
            width="50%",
            color_scheme="green",
        ),
        rx.button(
            "Stop Stream",
            on_click=StreamingState.stop_stream,
            is_disabled=StreamingState.stream == False,
            width="50%",
            color_scheme="red",
        ),
        width="100%",
    )
)
```

```python
def index():
    return rx.vstack(
    rx.recharts.area_chart(
        rx.recharts.area(
            data_key="pv",
            stroke="#82ca9d",
            fill="#82ca9d",
            type_="natural",
        ),
        rx.recharts.x_axis(
            data_key="name",
        ),
        rx.recharts.y_axis(),
        rx.recharts.legend(),
        data=StreamingState.data,
        width="100%",
        height=400,
    ),
    rx.hstack(
        rx.button(
            "Start Stream",
            on_click=StreamingState.start_stream,
            disabled=StreamingState.stream,
            width="50%",
        ),
        rx.button(
            "Stop Stream",
            on_click=StreamingState.stop_stream,
            width="50%",
        ),
        width="100%",
    ),
    width="100%",
)
```

## Extra Example

We can add extra `area` components to our chart to show the `uv` and `amt` data as well. We can also add a `graphing_tooltip` an `cartesian_grid` component to show the data when we hover over the chart.

Keep in mind the child coming first will be display in the back so the order of the `area` components matters.

```python eval
rx.vstack(
    rx.recharts.area_chart(
        rx.recharts.area(
            data_key="amt",
            fill="#4299E1",
            stroke="#4299E1",
            type_="natural",
        ),
        rx.recharts.area(
            data_key="pv",
            fill="#48BB78",
            stroke="#48BB78",
            type_="natural",
        ),
        rx.recharts.area(
            data_key="uv",
            fill="#F56565",
            stroke="#F56565",
            type_="natural",
        ),
        rx.recharts.x_axis(
            data_key="name",
        ),
        rx.recharts.y_axis(),
        rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
        rx.recharts.graphing_tooltip(),
        data=StreamingState.data,
        width="90%",
        height=400,
    ),
    rx.hstack(
        rx.button(
            "Start Stream",
            on_click=StreamingState.start_stream,
            is_disabled=StreamingState.stream,
            width="50%",
            color_scheme="green",
        ),
        rx.button(
            "Stop Stream",
            on_click=StreamingState.stop_stream,
            is_disabled=StreamingState.stream == False,
            width="50%",
            color_scheme="red",

        ),
        width="100%",
    )
)
```

```python
rx.vstack(
    rx.recharts.area_chart(
        rx.recharts.area(
            data_key="pv",
            fill="#48BB78",
            stroke="#48BB78",
            type_="natural",
        ),
        rx.recharts.area(
            data_key="uv",
            fill="#F56565",
            stroke="#F56565",
            type_="natural",
        ),
        rx.recharts.area(
            data_key="amt",
            fill="#4299E1",
            stroke="#4299E1",
            type_="natural",
        ),
        rx.recharts.x_axis(
            data_key="name",
        ),
        rx.recharts.y_axis(),
        data=StreamingState.data,
        width="90%",
        height=400,
    ),
    rx.hstack(
        rx.button(
            "Start Stream",
            on_click=StreamingState.start_stream,
            is_disabled=StreamingState.stream,
            width="50%",
            color_scheme="green",
        ),
        rx.button(
            "Stop Stream",
            on_click=StreamingState.stop_stream,
            is_disabled=StreamingState.stream == False,
            width="50%",
            color_scheme="red",
        ),
        width="100%",
    )
)
```

## Conclusion

We hope you enjoy the new graphing components. We are excited to see what you build with them. If you have any questions or feedback, please reach out to us on [Discord](https://discord.gg/T5WSbC2YtQ).

-- Reflex Team