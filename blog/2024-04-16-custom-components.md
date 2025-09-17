---
author: Nikhil Rao
date: 2024-04-16
title: Custom Components
description: Announcing our custom component ecosystem.
image: /blog/custom_components.webp
meta: [
    {"name": "keywords", "content": ""},
]
---

```python exec
from pcweb.pages.docs import wrapping_react, custom_components, styling, events, getting_started, state_structure
from pcweb.pages.docs.custom_components import custom_components as cc
```

We are excited to announce the launch of our [custom component ecosystem]({cc.path})!

Custom components allow developers to extend Reflex with their own components and share them with the Reflex community. This includes wrapping React components, as well as creating higher level Reflex components that encapsulate state and UI in a single class.

### New Features:

* A `reflex component` [subcommand]({custom_components.command_reference.path}) that allows you to create, test, and publish custom components.
* A new `rx.ComponentState` class that allows you to encapsulate state and UI for a component in a single class.
* A third party ecosystem to share and use custom components developed by the community.

## What are Custom Components?

Reflex has many built-in components to get you started, but in some cases you may want to create your own components. Custom components makes it easy to extend Reflex with your own components.

When you run `reflex component init`, you'll get a skeleton project with a `custom_components` folder where we generate a scaffold for your component that you can fill in with your own logic.

There are two categories of custom components: **React wrappers** and **high-level components**.

## React Wrappers

Since Reflex is built on top of React, you can easily [wrap any existing React component]({wrapping_react.overview.path}) from NPM and use it in your Reflex app. This has always been possible, but now we have a standard way to package and share these components. Over time we hope to grow the ecosystem so you can easily install the components you need instead of having to wrap them yourself.

For example, say you wanted to use an [image zoom](https://www.npmjs.com/package/react-medium-image-zoom) component that lets you click on an image to zoom in. Rather than figuring out how to wrap it, you can now run

```bash
pip install reflex-image-zoom
```

And use it right away like any other Reflex component.

```python demo exec
import reflex as rx
from reflex_image_zoom import image_zoom

def zoom():
    src = "/blog/custom_components.webp"
    return rx.hstack(
        rx.vstack(
            rx.text("Original Image"),
            rx.image(src=src),
        ),
        rx.vstack(
            rx.text("Click to Zoom Image"),
            image_zoom(
                rx.image(src=src),
                width="50%",
            )
        ),
    )
```

### Component State

A new feature we've added in 0.4.6 is the `rx.ComponentState` class. This class allows you to encapsulate state and UI for a component in a single class. In fact, this is what allows the `chat` component to work without having the user having to define a state - the component will dynamically create and handle its own state internally.

For example we can create a counter component that increments and decrements a count.

```python demo exec
class Counter(rx.ComponentState):
    count: int = 0

    @rx.event
    def increment(self):
        self.count += 1

    @rx.event
    def decrement(self):
        self.count -= 1

    @classmethod
    def get_component(cls, **props) -> rx.Component:
        return rx.hstack(
            rx.button("Decrement", on_click=cls.decrement),
            rx.heading(cls.count),
            rx.button("Increment", on_click=cls.increment),
        )

counter = Counter.create
```

Then we can create multiple instances of the counter, each with its own state.

```python demo
rx.vstack(
    counter(),
    counter(),
    counter(),
)
```

You can access the state of a component through `component.State`.

```python demo exec
counter1 = counter()
counter2 = counter()

def counter_sum():
    return rx.vstack(
        rx.heading(f"Sum: {counter1.State.count + counter2.State.count}"),
        counter1,
        counter2,
    )
```

See the [Component State]({state_structure.component_state.path}) page for more details on how to use this class.

## Testing and Publishing

In your project, we also create a sample Reflex app that uses your custom component. This allows you to test your component in a real app environment before publishing it.

Once you're ready to share your component, you can run `reflex component publish` to build and upload your package to PyPI. This will make your component available to the entire Reflex community. You will have the option of adding your component to our [gallery]({cc.path}) where other developers can find and use it.

We're looking forward to growing the custom component ecosystem and seeing what the community comes up with!
