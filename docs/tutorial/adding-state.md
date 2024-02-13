```python exec
import os

import reflex as rx
import openai

from pcweb.pages.docs import events
from pcweb.pages.docs import library
from pcweb.pages.docs import state

from docs.tutorial.tutorial_utils import ChatappState
import docs.tutorial.tutorial_style as style

# If it's in environment, no need to hardcode (openai SDK will pick it up)
if "OPENAI_API_KEY" not in os.environ:
    openai.api_key = "YOUR_OPENAI_KEY"

```

# State

Now let’s make the chat app interactive by adding state. The state is where we define all the variables that can change in the app and all the functions that can modify them. You can learn more about state in the [state docs]({state.overview.path}).

## Defining State

We will create a new file called `state.py` in the `chatapp` directory. Our state will keep track of the chat history. We will also define an event handler `answer` which will handle the form `on_submit` event, process the current question and add the answer to the chat history.

```python
# state.py
import reflex as rx


class State(rx.State):
    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    def answer(self, data):
        # Our chatbot is not very smart right now...
        answer = "I don't know!"
        self.chat_history.append((data["message"], answer))

```

## Binding State to Components

Now we can import the state in `chatapp.py` and reference it in our frontend components. We will modify the `chat` component to use the state instead of the current fixed questions and answers.

```python exec
def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(rx.text(question, style=style.question_style), text_align="right"),
        rx.box(rx.text(answer, style=style.answer_style), text_align="left"),
        margin_y="1em",
        width="100%",
    )


def chat1() -> rx.Component:
    return rx.box(
        rx.foreach(
            ChatappState.chat_history, lambda messages: qa(messages[0], messages[1])
        )
    )


def action_bar1() -> rx.Component:
    return rx.form(
        rx.hstack(
            rx.input(placeholder="Ask a question", name="message", style=style.input_style),
            rx.button("Ask", _type="submit", style=style.button_style),
            width="100%",
        ),
        reset_on_submit=True,
        on_submit=ChatappState.answer,
        width="100%",
    )
```

```python demo box
rx.container(
    chat1(),
    action_bar1(),
)
```

```python
# chatapp.py
from chatapp.state import State
...

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1])
        )
    )

def action_bar() -> rx.Component:
    return rx.form(
        rx.hstack(
            rx.input(placeholder="Ask a question", name="message", style=style.input_style),
            rx.button("Ask", _type="submit", style=style.button_style),
            width="100%",
        ),
        reset_on_submit=True,
        on_submit=State.answer,
        width="100%",
    )
```

Normal Python `for` loops don't work for iterating over state vars because these values can change and aren't known at compile time. Instead, we use the [foreach]({library.layout.foreach.path}) component to iterate over the chat history.

We also bind the input's `on_change` event to the `set_question` event handler, which will update the `question` state var while the user types in the input. We bind the button's `on_click` event to the `answer` event handler, which will process the question and add the answer to the chat history. The `set_question` event handler is a built-in implicitly defined event handler. Every base var has one. Learn more in the [events docs]({events.setters.path}) under the Setters section.

## Streaming Text

Normally state updates are sent to the frontend when an event handler returns. However, we want to stream the text from the chatbot as it is generated. We can do this by yielding from the event handler. See the [yield events docs]({events.yield_events.path}) for more info.

```python exec
def action_bar3() -> rx.Component:
    return rx.form(
        rx.hstack(
            rx.input(placeholder="Ask a question", name="message", style=style.input_style),
            rx.button("Ask", _type="submit", style=style.button_style),
            width="100%",
        ),
        reset_on_submit=True,
        on_submit=ChatappState.answer3,
        width="100%"
    )
```

```python demo box
rx.container(
    chat1(),
    action_bar3(),
)
```

```python
# state.py
import asyncio

...
async def answer(self, data):
    # Our chatbot is not very smart right now...
    answer = "I don't know!"
    self.chat_history.append((data["message"], ""))

    # Yield here to clear the frontend input before continuing.
    yield

    for i in range(len(answer)):
        # Pause to show the streaming effect.
        await asyncio.sleep(0.1)
        # Add one letter at a time to the output.
        self.chat_history[-1] = (self.chat_history[-1][0], answer[:i + 1])
        yield
```

In the next section, we will finish our chatbot by adding AI!
