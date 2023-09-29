---
from pcweb.base_state import State
from pcweb.pages.docs.advanced_guide.background_tasks import LowLevelState, low_level_code, low_level_render_code, MyTaskState, my_task_code, my_task_render_code
---

# Background Tasks

A background task is a special type of `EventHandler` that may run
concurrently with other `EventHandler` functions. This enables long-running
tasks to execute without blocking UI interactivity.

A background task is defined by decorating an async `State` method with
`@rx.background`.

Whenever a background task needs to interact with the state, **it must enter an
`async with self` context block** which refreshes the state and takes an
exclusive lock to prevent other tasks or event handlers from modifying it
concurrently.  Because other `EventHandler` functions may modify state while the
task is running, **outside of the context block, Vars accessed by the background
task may be _stale_**. Attempting to modify the state from a background task
outside of the context block will raise an `ImmutableStateError` exception.

In the following example, the `my_task` event handler is decorated with
`@rx.background` and increments the `counter` variable every half second, as
long as certain conditions are met. While it is running, the UI remains
interactive and continues to process events normally.

```reflex
docdemobox(
    eval(my_task_render_code)
)
```

```python
{my_task_code.strip()}
```

## Task Lifecycle

When a background task is triggered, it starts immediately, saving a reference to
the task in `app.background_tasks`. When the task completes, it is removed from
the set.

Multiple instances of the same background task may run concurrently, and the
framework makes no attempt to avoid duplicate tasks from starting.

It is up to the developer to ensure that duplicate tasks are not created under
the circumstances that are undesirable. In the example above, the `_n_tasks`
backend var is used to control whether `my_task` will enter the increment loop,
or exit early.

## Background Task Limitations

Background tasks mostly work like normal `EventHandler` methods, with certain exceptions:

* Background tasks must be `async` functions.
* Background tasks cannot modify the state outside of an `async with self` context block.
* Background tasks may read the state outside of an `async with self` context block, but the value may be stale.
* Background tasks may not be directly called from other event handlers or background tasks. Instead use `yield` or `return` to trigger the background task.

## Low-level API

The `@rx.background` decorator is a convenience wrapper around the lower-level
`App.modify_state` async contextmanager. If more control over task lifecycle is
needed, arbitrary async tasks may safely manipulate the state using an
`async with app.modify_state(token) as state` context block. In this case the
`token` for a state is retrieved from `state.get_token()` and identifies a
single instance of the state (i.e. the state for an individual browser tab).

Care must be taken to **never directly modify the state outside of the
`modify_state` contextmanager**. If the code that creates the task passes a
direct reference to the state instance, this can introduce subtle bugs or not
work at all (if redis is used for state storage).

The following example creates an arbitrary `asyncio.Task` to fetch data and then
uses the low-level API to safely update the state and send the changes to the
frontend.

```reflex
docdemobox(
    eval(low_level_render_code)
)
```

```python
{low_level_code.strip()}
```
