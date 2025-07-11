---
author: Masen Furer
date: 2023-09-28
title: Unlocking New Workflows with Background Tasks
description: What is a background task and how can it help you build better apps?
image: /blog/background_tasks.jpeg
meta: [
    {"name": "keywords", "content": ""},
]
---

```python exec
import reflex as rx

# hacks because curly braces always evaluate python code
pid = "{pid}"
class self(object):
    last_id = "{self.last_id}"
```


Reflex just released v0.2.8 earlier last week and with it, one of the most
exciting features I've worked on: **background tasks**.

## Why?

If you're a current developer of Reflex apps, you've no doubt noticed that **slow
events block the UI from receiving input**. This is because Reflex intentionally
processes events one at a time. While this is great for keeping your app's state
consistent, it can be frustrating when you need to execute a long-running task
and still keep the UI interactive and responsive to user input.

In previous releases, the main way to retain interactivity while running a long
task was to explicitly chain steps of the calculation together using `yield` or
`return` statements.

The following code example defines `State.get_post` which recursively queues itself
to fetch 10 posts from an API, while still allowing over queued events to be
processed in between.

```python
class State(rx.State):
    last_id: int = 0
    posts: List[str] = []
     
    def get_post(self):
        if self.last_id < 10:
            response = httpx.get(f"https://dummyjson.com/products/{self.last_id}")
            self.posts.append(response.text)
            self.last_id += 1
            return State.step
```

This works okay for some types of problems, but it complicates the code,
hindering readability and future maintenance. Further, the event queue **is
still blocked** while each step in the process runs. So while this does allow
for _some_ interactivity, it's not a complete solution.

## Enter background tasks...

A background task is a special type of async `EventHandler` that may run
concurrently with other `EventHandler` functions. They mostly work like normal
`EventHandler` functions on a State, however they must be `async` and they
**cannot _directly_ modify the state**.

**Wait a sec... if they cannot modify the state, how are they useful?**

Well, a background task _can_ modify the state, but **only inside of an `async
with self` context block**. Python 3.7 added support for async contextmanagers,
and Reflex takes advantage of this feature to provide a safe way to modify the
state from a background task.

**So what does `async with self` actually do?**

When a background task enters an `async with self` context block, it refreshes
the state instance and takes an exclusive lock on it.

* Inside the context block, the background task is guaranteed that `self` has the **latest
  values** and **no other `EventHandler` functions are modifying the state**.

* After exiting the context block, **an update is sent to the frontend** to reflect
  the new state, and **the lock is released**, allowing any queued events to be processed.

* Outside of the context block, the state may be _stale_, but **other event handlers
  can execute** while the task is `await`ing long-running processes.

## Using Background Tasks

Rewriting the example above shows how background tasks work in practice:

```python
class State(rx.State):
    posts: List[str] = []
    
    @rx.event(background=True)
    async def get_posts(self):
        with httpx.AsyncClient() as client:
            for pid in range(10):
                response = await client.get(f"https://dummyjson.com/products/{pid}")
                async with self:
                    self.posts.append(response.text)
```

The background task can fetch all of the posts while allowing the app to
continue processing UI events in the foreground.  The only time the UI is
blocked is during the short period of time where the response is being appended
to the state.


```md alert warning
# `@rx.event(background=True)` used to be called `@rx.background`.
In Reflex version 0.6.5 and later, the `@rx.background` decorator has been renamed to `@rx.event(background=True)`.
```

## Parallelizing Work

Aside from UI interactivity, the other motivation for using background tasks is
to parallelize work within the app. For example the user can be monitoring
responses from several API calls at once. Or the app can define different
background tasks for a multi-view dashboard UI and have separate portions of the
screen updating and processing simultaneously.

```python eval
rx.center(
    rx.video(url="https://user-images.githubusercontent.com/1524005/271007407-09c832ff-ecbd-4a9d-a8a5-67779c673045.mov"),
    rx.box(height="3em"),
    width="100%",
    padding_y="2em"
)
```

Full code for this example is available in [reflex-examples/lorem-stream](https://github.com/reflex-dev/reflex-examples/tree/main/lorem-stream).

# Next Steps

Background tasks is a powerful new feature that enables you to build
long-running workflows that can respond to user input in real time. We hope you
find unique and creative ways to use them in your apps.

Please see the docs for more information on [background
tasks](/docs/events/background-events/) and check out the complete
[v0.2.8](https://github.com/reflex-dev/reflex/releases/tag/v0.2.8)
release notes for all the new features and bug fixes.

🔧 Happy Building 🚀

-- Reflex Team
