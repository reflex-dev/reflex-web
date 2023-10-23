```python exec
import reflex as rx
from pcweb.base_state import State
from pcweb import constants, styles
from pcweb.base_state import State
from pcweb.templates.docpage import doccode, doc_section, docdemobox
from pcweb.pages.docs.tutorial import intro
from pcweb.pages.docs.getting_started import installation
from pcweb.pages.docs.wrapping_react import overview
from pcweb.pages.docs.library import library
```

# Introduction

```python eval
rx.center(
    rx.span(
        "Looking for Pynecone? You are in the right place, Pynecone is now Reflex!",
        color="#494369",
    ),
    bg="#FAF8FB",
    font_family=styles.MONO,
    padding=4,
    margin_bottom="1em",
    border="1px solid #EAE4FD",
    border_radius=styles.DOC_BORDER_RADIUS,
    font_size=".8em",
)
```

**Reflex** is an open-source, full-stack Python framework that makes it easy to build and deploy web apps in minutes.
Reflex is a full-stack framework for building and deploying web apps.

## Motivation

Reflex was created with the following goals:

```python eval
doc_section(
    rx.vstack(
        rx.text(
            rx.span(
                "Pure Python",
                font_weight="bold",
            ),
            width="100%",
        ),
        rx.text(
            "Use Python for everything. Don't worry about learning a new language.",
            width="100%",
        ),
        rx.text(
            rx.span(
                "Easy to Learn",
                font_weight="bold",
            ),
            width="100%",
        ),
        rx.text(
            "Build and share your first app in minutes. No webdev experience required.",
            width="100%",
        ),
        rx.text(
            rx.span(
                "Full Flexibility",
                font_weight="bold",
            ),
            width="100%",
        ),
        rx.text(
            "Remain as flexible as traditional web frameworks. ",
            "Reflex is easy to get started with, but powerful enough for advanced use cases.",
            width="100%",
        ),
        rx.text(
            "Build anything from small data science apps to large, multi-page websites. ",
            width="100%",
        ),
        rx.text(
            "This entire site was built and deployed with Reflex!",
            color=styles.ACCENT_COLOR,
            width="100%",
        ),
        rx.text(
            rx.span(
                "Batteries Included",
                font_weight="bold",
            ),
            width="100%",
        ),
        rx.text(
            "No need to reach for a bunch of different tools. Reflex handles the frontend, backend, and deployment of your app.",
            width="100%",
        ),
        text_align="left",
        margin_bottom="2em",
    ),
)
```

## Get Started

Below is a quick example of a counter app to get a feel for how Reflex works.

For a more in depth example, we recommend going through the [tutorial]({intro.path}) or go straight to the [installation]({installation.path}) to start building your own app.

## First Example

Let's go over a simple counter app to explore the basics of Reflex.

```python exec
import inspect

class CounterExampleState(State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

state_code = inspect.getsource(CounterExampleState).replace("(State)", "(rx.State)").replace("CounterExampleState", "State").strip()

def index():
    return rx.hstack(
        rx.button(
            "Decrement",
            bg="#fef2f2",
            color="#b91c1c",
            border_radius="lg",
            on_click=CounterExampleState.decrement,
        ),
        rx.heading(CounterExampleState.count, font_size="2em"),
        rx.button(
            "Increment",
            bg="#ecfdf5",
            color="#047857",
            border_radius="lg",
            on_click=CounterExampleState.increment,
        ),
        spacing="1em",
    )

index_code = inspect.getsource(index).replace("CounterExampleState", "State").strip()

counter_code = f"""
import reflex as rx

{state_code}

{index_code}

app = rx.App()
app.add_page(index)
app.compile()
""".strip()
```

```python eval
rx.box(docdemobox(index()), margin_bottom="1em")
```

Here is the full code for this example:

```python
{counter_code}
```

## The Structure of a Reflex App

Let's break this example down.

## Import

```python eval
doccode(counter_code, lines=(0, 1))
```

We begin by importing the `reflex` library. All Reflex functions and classes begin with the `rx` prefix.

## State

```python eval
doccode(counter_code, lines=(2, 5))
```

The state defines all the variables (called **vars**) in an app that can change, as well as the functions that change them.

Here our state has a single var, `count`, which holds the current value of the counter. We initialize it to `0`.

## Event Handlers

```python eval
doccode(counter_code, lines=(5, 13))
```

Within the state, we define functions, called **event handlers**, that change the state vars.

Event handlers are the only way that we can modify the state in Reflex.
They can be called in response to user actions, such as clicking a button or typing in a text box.
These actions are called **events**.

Our counter app has two event handlers, `increment` and `decrement`.

## Frontend

```python eval
doccode(counter_code, lines=(13, 33))
```

This function defines the frontend of the app.

We use different components such as `rx.hstack`, `rx.button`, and `rx.heading` to build the frontend. Components can be nested to create complex layouts, and can be styled using the full power of CSS.

Reflex comes with [50+ built-in components]({library.path}) to help you get started.
We are actively adding more components, plus it's easy to [wrap your own React components]({overview.path}).

```python eval
doccode(counter_code, lines=(22, 23))
```

Components can reference the app's state vars.
The `rx.heading` component displays the current value of the counter by referencing `State.count`.
All components that reference state will reactively update whenever the state changes.

```python eval
doccode(counter_code, lines=(15, 22))
```

Components interact with the state by binding events triggers to event handlers.
For example, `on_click` is an event that is triggered when a user clicks a component.

The first button in our app binds its `on_click` event to the `State.decrement` event handler, and the second button binds its to the `State.increment` handler.

## Routing

```python eval
doccode(counter_code, lines=(33, 35))
```

Next we define our app and add the counter component to the base route.

## Compiling

```python eval
doccode(counter_code, lines=(35, 36))
```

Finally, we compile our app, and we are ready to run it.

## Next Steps

And that's it! We've created an entire frontend and backend in less than 30 lines of code.
From here we can continue developing or deploy it to the web in a single command.

Keep reading the docs to learn how to try Reflex yourself!