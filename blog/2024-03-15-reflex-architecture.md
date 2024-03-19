---
author: Nikhil Rao
date: 2024-03-14
title: Building a Pure Python Web Framework
description: A look at how Reflex works under the hood.
image: /auth_blog.png
---

We started Reflex a year ago so that anyone who knows Python can easily build web apps and share them with the world, without needing to learn a new language and piecing together a bunch of different tools.

In this post, I'll share more about why we built Reflex, and how it works under the hood.

We'll use the following basic app that displays Github profile images as an example to explain the different parts of the architecture.

```python demo exec
import reflex as rx

class GithubState(rx.State):
    username: str = "reflex-dev"

    def set_username(self, username: str):
        self.username = username


def index():
    return rx.hstack(
        rx.avatar(src=f"https://github.com/{GithubState.username}.png"),
        rx.input(
            placeholder="Enter your username",
            on_blur=GithubState.set_username,
        ),
    )
```

## The Starting Point

Before working on Reflex, I worked on AI projects at a startup and then at a big tech company. On these teams, we used Python for everything from data analysis to machine learning to backend services. But when it came to visualizing our work or building apps so that others could use our work, there wasn't a good option to stay in Python. Suddenly, we had to switch to JavaScript and learn a whole new ecosystem.

Making a UI for your project should be simple, but even though we had great engineers on our team, the overhead of learning a new language and tools was a huge barrier. Often making a UI was harder than the actual work we were doing!

Python is used for everything except web apps, and we wanted to fill that gap.

## Existing Python Solutions

Before building Reflex we looked for existing Python solutions, but none of them fit our needs.

On the one hand, there are frameworks like [Django](https://www.djangoproject.com/) and [Flask](https://flask.palletsprojects.com/) that are great for building web apps, but they only handle the backend. You still need to learn JavaScript and a frontend framework, as well as writing a lot of boilerplate code to connect the frontend and backend. 

On the other hand, there are pure Python libraries like [Dash](https://dash.plotly.com/) and [Streamlit](https://streamlit.io/) that are great for building data visualization apps. These can be great for small projects, but they are limited to a specific use case and don't have the features and performance to build a full web app.

We wanted to build to bridge this gap by creating a framework that is easy and intuitive, while remaining flexible and powerful to support any app.

## The Reflex Architecture

Reflex apps compile down to a [Next.js](https://github.com/vercel/next.js) frontend app and a [FastAPI](https://github.com/tiangolo/fastapi) backend app. Only the UI is compiled to Javascript; all the app logic and state management stays in Python and is run on the server. Reflex uses websockets to send events from the frontend to the backend, and to send state updates from the backend to the frontend.

When building Reflex, we wanted the final product to look and feel like a traditional web app to the end user, while still being easy to build and maintain for the developer. We chose to leverage the existing web ecosy

The diagram below shows a detailed overview of how a Reflex app works.
We'll go through each part in more detail in the following sections.

![Reflex Architecture](/architecture.png)

```python eval
rx.box(height="1em")
```

### Frontend (Components)

Reflex frontends are built using components that can be composed together to create complex UIs.

```python
def index():
    return rx.hstack(
        rx.avatar(src=f"https://github.com/{GithubState.username}.png"),
        rx.input(
            placeholder="Enter your username",
            on_blur=GithubState.set_username,
        ),
    )
```

In our example app, we have components such as `rx.hstack`, `rx.avatar`, and `rx.input`. Under the hood, these components compile down to React components.

For example, the above code compiles down to the following React code:

```jsx
<HStack>
    <Avatar src="https://github.com/{GithubState.username}.png">
    <Input
        placeholder="Enter your username"
        onBlur={GithubState.set_username}
    >
</HStack>
```

We chose React because it is a popular library with a huge ecosystem. Our goal isn't to recreate the web ecosystem, but to make it accessible to Python developers.

This also let's our users bring their own components if we don't have a component they need.

### Backend (State)

In Reflex only the frontend compiles to Javascript, while all the state and logic stays in Python and is run on the server.

```python
import reflex as rx

class GithubState(rx.State):
    username: str = "reflex-dev"

    def set_username(self, username: str):
        self.username = username
```

Normally when writing web apps, you have to write a lot of boilerplate code to connect the frontend and backend. With Reflex, you don't have to worry about that. We handle the communication between the frontend and backend for you.

We follow a reactive approach to state. All the variables that change over time are defined in a `State` class. When a variable changes, the frontend is automatically updated to reflect the new state.


## Event Processing

Now we get into the interesting part - how we handle events and state updates. Let's walk through it with our Github profile image example.

### Event Trigger

Events are initiated when the user interacts with the UI. In our example, when the user types in the input field and then clicks away, the `on_blur` event is triggered.

### Event Queue

On the frontend, we maintain an event queue of all pending events. When an event is triggered, it is added to the queue. We have a `processing` flag to make sure only one event is processed at a time. This ensures that the state is always consistent and there aren't any race conditions with two event handlers modifying the state at the same time.

Once the event is ready to be processed, it is sent to the backend through a websocket connection.

### State Manager

The event contains information including the token of the client, the event handler to run, and the arguments to pass to the event handler. The backend processes the event and updates the state.

The first step is to get the user's state. This is where the state manager comes in. It is essentially a mapping from a user's token to their state. When the backend receives an event, it looks up the user's state and runs the event handler on that state.

By default the state manager is just an in-memory dictionary, but it can be extended to use a database or cache. In production we use Redis to store the state.

### Event Handling

Once we have the user's state, the next step is to run the event handler.

```python
def set_username(self, username: str):
    self.username = username
```

In our example, the `set_username` event handler is run on the user's state. This updates the user's state with the new username.

### State Updates

After the event handler runs, it updates the state's vars. Whenever a state var updates it, Reflex marks it as "dirty". When the event handler is done processing, we find all the dirty vars and send them to the frontend to update the UI. This allows our apps to scale as the state grows.

The state delta is sent to the frontend through a websocket connection. The frontend then updates the UI to reflect the new state. In this case, the new Github profile image is displayed.

## Extendability

* styling, wrapping, react, call script

## Possible Future Plans

* wasm, etc.
* portability / embedding