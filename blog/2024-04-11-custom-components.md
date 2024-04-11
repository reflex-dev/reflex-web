---
author: Nikhil Rao
date: 2024-04-11
title: Custom Components
description: Announcing our third party custom component ecosystem.
image: /blog/python.png
---

```python exec
from pcweb.pages.docs import wrapping_react, custom_components, styling, events, tutorial
from pcweb.pages.docs.custom_components import custom_components as cc
```

We are excited to announce the launch of our [custom component ecosystem]({cc.path})! Custom components allow developers to build their own reusable components and share them with the Reflex community. This includes wrapping new React components, as well as creating higher level Reflex components.

Components can be published to Pypi and installed through `pip`. We already have some components available.

## What are Custom Components?

Reflex has many built-in components for common use cases, but sometimes you may want to create your own components. Custom components allow you to encapsulate complex logic and styling into a single reusable component.

For example, in our [tutorial]({tutorial.final_app.path}) we share the code for creating a chat component in Reflex. In order to build a chat app, you would have to copy and paste the code for the chat component into your own app. 

With custom components, we now have a [reflex-chat](https://github.com/picklelo/reflex-chat/) package that you can install with `pip` and use in your app.

```bash
pip install reflex-chat
```

You can then import the chat component into your app and use it like any other Reflex component. All the styling and logic is encapsulated, you only need to pass in the actual LLM logic.

```python exec
import reflex as rx
from openai import OpenAI
from reflex_chat import chat

client = OpenAI()

# Only define your logic, the chat component handles the rest.
async def process(chat):
    # Start a new session to answer the question.
    session = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat.get_value(chat.messages),
        stream=True,
    )

    # Stream the results, yielding after every word.
    for item in session:
        if hasattr(item.choices[0].delta, "content"):
            answer_text = item.choices[0].delta.content
            # Ensure answer_text is not None before concatenation
            chat.messages[-1]["content"] += answer_text or ""
            yield
```

```python demo
rx.box(
    chat(process=process),
    width="100%"
)
```

```md alert info
# Just define your `process`function to connect the chat component to any LLM.

\```python
async def process(chat):
    # Start a new session to answer the question.
    session = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat.get_value(chat.messages),
        stream=True,
    )

    # Stream the results, yielding after every word.
    for item in session:
        if hasattr(item.choices[0].delta, "content"):
            answer_text = item.choices[0].delta.content
            # Ensure answer_text is not None before concatenation
            chat.messages[-1]["content"] += answer_text or ""
            yield
\```
```

## How To Create Custom Components

There are two categories of custom components: **React wrappers** and **high-level components**.

### React Wrapper

Reflex is built on top of React, so if we don't have a component you need, you can easily [wrap your own React component]({wrapping_react.overview.path}) and use it in your Reflex app.

We've

## How It works

Since Reflex 0.4.6, there is a `reflex components` subcommand that allows you to create and publish your own custom components.

First run

```python
reflex component init
```

to create a new custom component project.

