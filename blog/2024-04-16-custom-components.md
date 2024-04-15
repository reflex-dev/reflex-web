---
author: Nikhil Rao
date: 2024-04-16
title: Custom Components
description: Announcing our third party custom component ecosystem.
image: /blog/python.png
---

```python exec
from pcweb.pages.docs import wrapping_react, custom_components, styling, events, tutorial
from pcweb.pages.docs.custom_components import custom_components as cc
```

We are excited to announce the launch of our [custom component ecosystem]({cc.path})! 
 
Custom components allow developers to build their own components and share them with the Reflex community. This includes wrapping React components, as well as creating higher level Reflex components.

### New Features:

* A `reflex components` subcommand that allows you to create, test, and publish custom components.
* Install third party components from PyPI with `pip`.
* A new `rx.ComponentState` class that allows you to encapsulate state and UI for a component in a single class.

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
    height="500px",
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

## Types Of Custom Components

There are two categories of custom components: **React wrappers** and **high-level components**.

### React Wrapper

Reflex is built on top of React, so if we don't have a component you need, you can easily [wrap your own React component]({wrapping_react.overview.path}) and use it in your Reflex app.


### High-Level Component

You can also create custom components that don't wrap React, but instead are built on top of existing Reflex components. For example, you could create a custom `Chat` component that encapsulates the logic for a chat app.

When you run `reflex components init`, you'll get a skeleton project with a `custom_components` folder where you can define your custom component. We generate a scaffold for your component that you can fill in with your own logic.

## Creating Custom Components

In Reflex 0.4.6 we're introducing a `reflex components` subcommand that allows you to create, test, and publish custom components. See the [Custom Components]({custom_components.overview.path}) docs for full details.
