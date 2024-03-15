---
author: Nikhil Rao
date: 2024-03-14
title: "Building a Pure Python Web Framework"
description: "A look at how Reflex works under the hood."
image: /auth_blog.png
---

We started Reflex a year ago so that anyone who knows Python can easily build web apps and share them with the world, without needing to learn a new language and piecing together a bunch of different tools.

In this post, I wanted to share more about why we built Reflex, and how it works under the hood.

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

Before working on Reflex, I was at a startup and then at a big tech company working on AI projects. On these teams, we used Python for everything from data analysis to machine learning to backend services. But when it came to visualizing our work or building apps so that others could use our work, there wasn't a good option to stay in Python. Suddenly, we had to switch to JavaScript and learn a whole new ecosystem.

Making a UI for your project should be simple, but even though we had great engineers on our team, the overhead of learning a new language and tools was a huge barrier. Often making a UI was harder than the actual work we were doing!

Python is used for everything except web apps, and we wanted to fill that gap.

## Existing Python Solutions

Before building Reflex we looked for existing Python solutions, but none of them fit our needs.

On the one hand, there are frameworks like [Django](https://www.djangoproject.com/) and [Flask](https://flask.palletsprojects.com/) that are great for building web apps, but they only handle the backend. You still need to learn JavaScript and a frontend framework, as well as writing a lot of boilerplate code to connect the frontend and backend. 

On the other hand, there are pure Python libraries like [Dash](https://dash.plotly.com/) and [Streamlit](https://streamlit.io/) that are great for building data visualization apps. These can be great for small projects, but they are limited to a specific use case and don't have the features and performance to build a full web app.

We wanted to build to bridge this gap by creating a framework that is easy and intuitive, while remaining flexible and powerful to support any app.

## What about existing solutions?

## Motivation

## Core Concepts

### Frontend (Components)
- keep sections on how we leverage
We chose React because it is a popular library with a huge ecosystem - our goal isn't to recreate the web ecosystem, but to make it accessible to Python developers.

### Backend (State)

### Events

### Event Queue

### State Manager

### Event Handling

### State Updates

## Extendability

* styling, wrapping, react, call script

## Possible Future Plans

* wasm, etc.
* portability / embedding