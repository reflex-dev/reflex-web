---
author: Nikhil Rao
date: 2024-03-20
title: Building a Pure Python Web Framework
description: A look at how Reflex works under the hood.
image: /blog/python.png
---

```python exec
# from pcweb.pages.docs import wrapping_react
```

We started Reflex a year ago so that anyone who knows Python can easily build web apps and share them with the world, without needing to learn a new language and piecing together a bunch of different tools.

In this post, I'll share more about what makes Reflex different, and how it works under the hood.

We'll use the following basic app that displays Github profile images as an example to explain the different parts of the architecture.

```python demo exec
import requests
import reflex as rx

class GithubState(rx.State):
    url: str = "https://github.com/reflex-dev"
    profile_image: str = "https://avatars.githubusercontent.com/u/104714959"

    def set_profile(self, username: str):
        github_data = requests.get(f"https://api.github.com/users/{username}").json()
        self.url = github_data["url"]
        self.profile_image = github_data["avatar_url"]


def index():
    return rx.hstack(
        rx.link(
            rx.avatar(src=GithubState.profile_image),
            href=GithubState.url,
        ),
        rx.input(
            placeholder="Your Github username",
            on_blur=GithubState.set_profile,
        ),
    )
```

## The Starting Point

Python is one of the most popular programming languages in the world. Web development is one of the most popular use cases for programming. So why can't we build web apps in Python?

Before working on Reflex, I worked on AI projects at a startup and then at a big tech company. On these teams, we used Python for everything from data analysis to machine learning to backend services. But when it came to building user interfaces or apps so that others could use our work, there wasn't a good option to stay in Python. Suddenly, we had to switch to JavaScript and learn a whole new ecosystem.

Making a UI should be simple, but even though we had great engineers on our team, the overhead of learning a new language and tools was a huge barrier. Often making a UI was harder than the actual work we were doing!

## Existing Python Solutions

There were a few ways already to build apps in Python, but none of them fit our needs.

On the one hand, there are frameworks like [Django](https://www.djangoproject.com/) and [Flask](https://flask.palletsprojects.com/) that are great for building production-grade web apps. But they only handle the backend - you still need to use JavaScript and a frontend framework, as well as writing a lot of boilerplate code to connect the frontend and backend.

On the other hand, there are pure Python libraries like [Dash](https://dash.plotly.com/) and [Streamlit](https://streamlit.io/) can be great for small projects, but they are limited to a specific use case and don't have the features and performance to build a full web app. As your app grows in features and complexity, you may find yourself hitting the limits of the framework, at which point you either have to limit your idea to fit the framework, or scrap your project and rebuild it using a "real web framework".

We wanted to bridge this gap by creating a framework that is easy and intuitive to get started with, while remaining flexible and powerful to support any app.

## Goals of Reflex

* **Pure Python**: Use one language for everything.
* **Easy to get started**: Build your ideas easily without needing web development experience.
* **Full Flexibility**: Web apps should match the customizability and performance of traditional web frameworks.
* **Batteries Included**: Handle the full-stack from the frontend, backend, to deployment.

Now let's dive into how we built Reflex to meet these goals.

## The Reflex Architecture

Full-stack web apps are made up of a frontend and a backend. The frontend the user interface, and is served as a web page that runs on the user's browser. The backend handles the logic and state management (such as databases and APIs), and is run on a server.

In traditional web development, these are usually two separate apps, and are often written in different frameworks or languages. For example, you may combine a Flask backend with a React frontend. With this approach, you have to maintain two separate apps and end up writing a lot of boilerplate code to connect the frontend and backend.

We wanted to simplify this proces in Reflex by defining both the frontend and backend in a single codebase, while using Python for everything. Developers should only worry about their app's logic and not about the low-level implementation details.

### TLDR

Under the hood, Reflex apps compile down to a [React](https://react.dev) frontend app that and a [FastAPI](https://github.com/tiangolo/fastapi) backend app. Only the UI is compiled to Javascript; all the app logic and state management stays in Python and is run on the server. Reflex uses websockets to send events from the frontend to the backend, and to send state updates from the backend to the frontend.

The diagram below shows a detailed overview of how a Reflex app works. We'll go through each part in more detail in the following sections.

```python exec
from reflex_image_zoom import image_zoom
```

```python eval
image_zoom(rx.image(src="/architecture.png"))
```

```python eval
rx.box(height="1em")
```

## Frontend

We wanted Reflex apps to look and feel like a traditional web app to the end user, while still being easy to build and maintain for the developer. To do this, we built on top of mature and popular web technologies.

When you `reflex run` your app, Reflex compiles frontends compile down to a single-page [Next.js](https://nextjs.org) app and serves it on a port (by default `3000`) that you can access in your browser.

The frontend's job is to reflect the app's state, and send events to the backend when the user interacts with the UI. No actual logic is run on the frontend.

In production mode, the frontend can be statically exported using [static site generation](https://nextjs.org/docs/pages/building-your-application/rendering/static-site-generation), and can be hosted on any static hosting service such as [Github Pages](https://pages.github.com). However to work, we must also host the backend separately for the app interactivity to work.

### Components 

Reflex frontends are built using components that can be composed together to create complex UIs. Instead of using a templating language that mixes HTML and Python, we just use Python functions to define the UI.

```python
def index():
    return rx.hstack(
        rx.link(
            rx.avatar(src=GithubState.profile_image),
            href=GithubState.url,
        ),
        rx.input(
            placeholder="Your Github username",
            on_blur=GithubState.set_profile,
        ),
    )
```

In our example app, we have components such as `rx.hstack`, `rx.avatar`, and `rx.input`. These components can have different **props** that affect their appearance and functionality - for example the `rx.input` component has a `placeholder` prop to display the default text. Components can also be hooked up to the state through event triggers such as `on_blur` which we will discuss more below.

Under the hood, these components compile down to React components. For example, the above code compiles down to the following React code:

```jsx
<HStack>
    <Link href=\{GithubState.url}>
        <Avatar src=\{GithubState.profile_image}/>
    </Link>
    <Input
        placeholder="Your Github username"
        // This would actually be a websocket call to the backend.
        onBlur=\{GithubState.set_profile}
    >
</HStack>
```

Many of our core components are based on [Radix](https://radix-ui.com/), but we also have many other components for graphing, datatables, and more.

We chose React because it is a popular library with a huge ecosystem. Our goal isn't to recreate the web ecosystem, but to make it accessible to Python developers. 

This also let's our users bring their own components if we don't have a component they need. Users can [wrap their own React components](link) and then [publish them](link) for others to use. Over time we're trying to build out our [third party component ecosystem](link) so that users can easily find and use components that others have built.


### Styling

We wanted to make sure Reflex apps look good out of the box, while still giving developers full control over the appearance of their app.

We have a core [theming system](link) that lets you set high level styling options such as dark mode and accent color throughout your app to give it a unified look and feel.

Beyond this, Reflex components can be styled using the full power of CSS. We leverage the [Emotion](https://emotion.sh/docs/introduction) library to allow "CSS-in-Python" styling, so you can pass any CSS prop as a keyword argument to a component. This includes [responsive props](link) by passing a list of values, as well as [pseudo-classes](link) such as `hover` and `focus` styles.

## Backend

Now let's look into how we added interactivity to our apps.

In Reflex only the frontend compiles to Javascript and runs on the user's browser, while all the state and logic stays in Python and is run on the server. When you `reflex run`, we start a FastAPI server (by default on port `8000`) that the frontend connects to through a websocket.

All the state and logic are defined within a `State` class.

```python
class GithubState(rx.State):
    url: str = "https://github.com/reflex-dev"
    profile_image: str = "https://avatars.githubusercontent.com/u/104714959"

    def set_profile(self, username: str):
        github_data = requests.get(f"https://api.github.com/users/\{username}").json()
        self.url = github_data["url"]
        self.profile_image = github_data["avatar_url"]
```

The state is made up of **vars** that change over time, and **event handlers** that are called when the user interacts with the UI and update the state vars. In our example, `url` and `profile_image` are state vars, and `set_profile` is an event handler that updates the state vars.

Since event handlers are run on the backend, you can use any Python library to handle events. In our example, we use the `requests` library to make an API call to Github to get the user's profile image.

## Event Processing

Now we get into the interesting part - how we handle events and state updates.

Normally when writing web apps, you have to write a lot of boilerplate code to connect the frontend and backend. With Reflex, you don't have to worry about that - we handle the communication between the frontend and backend for you. Developers just have to write their event handler logic, and when the vars are updated the UI is automatically updated.

You can refer to the diagram above for a visual representation of the process. Let's walk through it with our Github profile image example. 

### Event Triggers

Events are initiated when the user interacts with the UI through **event triggers**, which can be bound to event handlers. These include things like clicking a button, typing in a text box, or hovering over an element.

```python
rx.input(
    placeholder="Your Github username",
    on_blur=GithubState.set_profile,
)
```

In our example we bind the `on_blur` event trigger to the `set_profile` event handler. This means that when the user types in the input field and then clicks away, the `set_profile` event handler is called.

### Event Queue

On the frontend, we maintain an event queue of all pending events. An event consists of three major pieces of data:

* **client token**: Each client (browser tab) has a unique token to identify it. This let's the backend know which state to update.
* **event handler**: The event handler to run on the state.
* **arguments**: The arguments to pass to the event handler.

Let's assume the user typed in "reflex-dev" into the input. In this example, our event would look something like this:

```json
\{
    client_token: "abc123",
    event_handler: "GithubState.set_profile",
    arguments: ["reflex-dev"]
}
```

On the frontend, we maintain an event queue of all pending events. 

When an event is created, it is added to the queue. We have a `processing` flag to make sure only one event is processed at a time. This ensures that the state is always consistent and there aren't any race conditions with two event handlers modifying the state at the same time.

```md alert info
There are exceptions to this, such as [background events](link) which allow you to run events in the background without blocking the UI.
```

Once the event is ready to be processed, it is sent to the backend through a [websocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) connection.

### State Manager

Once the event is received, it is processed on the backend.

Reflex uses a **state manager** which maintains a mapping between client token's and their state. By default, the state manager is just an in-memory dictionary, but it can be extended to use a database or cache. In production we use Redis as our state manager.

### Event Handling

Once we have the user's state, the next step is to run the event handler with the arguments.

```python
def set_profile(self, username: str):
    github_data = requests.get(f"https://api.github.com/users/\{username}").json()
    self.url = github_data["url"]
    self.profile_image = github_data["avatar_url"]
```

In our example, the `set_profile` event handler is run on the user's state. This makes an API call to Github to get the user's profile image, and then updates the state's `url` and `profile_image` vars.

### State Updates

Every time an event handler returns (or [yields](link)), send the state updates to the frontend to update the UI.

To maintain performance as your state grows, internally Reflex keeps track of all the **dirty vars** that were updated during the event handler. When the event handler is done processing, we find all the dirty vars and create a **state delta** to send to the frontend.

In our case, the state delta may look something like this:

```json
{
    "url": "https://github.com/reflex-dev",
    "profile_image": "https://avatars.githubusercontent.com/u/104714959" 
}
```

We save the new state in our state manager, and then send the state delta to the frontend. The frontend then updates the UI to reflect the new state. In our example, the new Github profile image is displayed.

## Conclusion

I hope this gives a good overview of how Reflex works under the hood. We will have more posts coming out to share how we made Reflex scalable and performant through features such as state sharding and compiler optimizations.

As always you can follow us for more:

* [Join our Discord]({constants.DISCORD_URL})
* [Follow us on X]({constants.TWITTER_URL})
* [Star us on GitHub]({constants.GITHUB_URL})
