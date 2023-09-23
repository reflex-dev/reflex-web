---
author: Masen Furer
date: 2023-09-22
title: "Unlocking New Workflows with Background Tasks"
description: "What is a background task and how can it help you build better apps?"
image: reflex_banner.png
---
---
import asyncio
import inspect

from pcweb.base_state import State
from pcweb.templates.docpage import docalert, doccode, docheader, subheader, docdemobox
from pcweb.pages.blog.unlocking_new_workflows_with_background_tasks import (
    CollatzBackgroundState,
    collatz_background_render_code,
    prev_collatz_state,
)
---


Reflex just released v0.2.8 earlier this afternoon and with it, one of the most
exciting features I've worked on: **background tasks**.

## Why?

If you're a current developer of Reflex apps, you've no doubt noticed that **slow
events block the UI from receiving input**. This is because Reflex intentionally
processes events one at a time. While this is great for keeping your app's state
consistent, it can be frustrating when you need to execute a long-running task
and still keep the UI interactive and responsive to user input.

In previous releases, the main way to retain interactivity while running a long
task was to explicitly chain steps of the calculation together using `yield` or
`return` statements:

```python
{prev_collatz_state}
```

This works okay for some types of problems, but it complicates the code,
hindering readability and future maintenance. Further, the event queue **is
still blocked** while each step the process runs. So while this does allow for
_some_ interactivity, it's not a complete solution.

## Enter background tasks...

A background task is a special type of async `EventHandler` that may run
concurrently with other `EventHandler` functions. They mostly work like normal
`EventHandler` functions on a State, however they must be `async` and they
**cannot _directly_ modify the state**.

### _Wait a sec... if they cannot modify the state, how are they useful?_

Well, a background task _can_ modify the state, but **only inside of an `async
with self` context block**. Python 3.7 added support for async contextmanagers,
and Reflex takes advantage of this feature to provide a safe way to modify the
state from a background task.

### _So what does `async with self` actually do?_

When a background task enters an `async with self` context block, it refreshes
the state instance and takes an exclusive lock on the it.

Inside the context block, the background task is guaranteed that `self` has the latest
values and no other `EventHandler` functions are modifying the state.

After exiting the context block, an update is sent to the frontend to reflect
the new state, and the lock is released, allowing any queued events to be processed.

Outside of the context block, the state may be _stale_, but other event handlers
can execute while the task is `await`ing long-running processes.

## Using Background Tasks

We'll rewrite the `CollatzState` example above to see how background tasks work
in practice:

```python
{inspect.getsource(CollatzBackgroundState).strip().replace("(State)", "(rx.State)")}
```

## _Hold on... that looks **more** complicated than before!_

Yes, it does. But the key difference is that the background task can now respond
to user input while it is running. With the addition of the `task_running` flag,
the UI can present a "Running" switch to the user, allowing them to stop or pause
the task and resume it later. The user can also change the input value while the
task is running, and it will continue with the new value.

Here is the frontend code:

```python
{inspect.getsource(collatz_background_render_code).strip().replace("collatz_background_render_code", "index")}
```

And the demo:

```reflex
docdemobox(
    {inspect.getsource(collatz_background_render_code).partition("return")[2].strip()}
)
```

# ✌️

Background tasks are a powerful new feature that enables you to build
long-running workflows that can respond to user input in real time. We hope you
find unique and creative ways to use them in your apps.

Please see the docs for more information on [background
tasks](/docs/advanced-guide/background-tasks/) and check out the complete
[v0.2.8](https://github.com/reflex-dev/reflex/releases/tag/v0.2.8)
release notes for all the new features and bug fixes.

🔧 Happy Building 🚀

```reflex
rx.text("- Reflex Team", margin_bottom="5em")
```
```reflex
rx.box(height="8em")
```