```python exec
import reflex as rx

from pcweb.templates.docpage import docdemo_from
```


# Yielding Multiple Updates


A regular event handler will send a `StateUpdate` when it has finished running. This works fine for basic event, but sometimes we need more complex logic. To update the UI multiple times in an event handler, we can `yield` when we want to send an update.

To do so, we can use the Python keyword `yield`. For every yield inside the function, a `StateUpdate` will be sent to the frontend with the changes up to this point in the execution of the event handler.


```python exec

import asyncio

class MultiUpdateState(rx.State):
    count: int = 0

    async def timed_update(self):
        for i in range(5):
            await asyncio.sleep(0.5)
            self.count += 1
            yield


def multi_update():
    return rx.vstack(
    rx.text(MultiUpdateState.count),
    rx.button("Start", on_click=MultiUpdateState.timed_update)
)

```

```python eval
docdemo_from(MultiUpdateState, component=multi_update, imports=["import asyncio"])
```

Here is another example of yielding multiple updates with a loading icon.

```python exec

import asyncio

class ProgressExampleState(rx.State):
    count: int = 0
    show_progress: bool = False

    async def increment(self):
        self.show_progress = True
        yield
        # Think really hard.
        await asyncio.sleep(0.5)
        self.count += 1
        self.show_progress = False

def progress_example():
    return rx.cond(
        ProgressExampleState.show_progress,
        rx.circular_progress(is_indeterminate=True),
        rx.heading(
            ProgressExampleState.count,
            on_click=ProgressExampleState.increment,
            _hover={"cursor": "pointer"},
        )
    )

```

```python eval
docdemo_from(ProgressExampleState, component=progress_example, imports=["import asyncio"])
```