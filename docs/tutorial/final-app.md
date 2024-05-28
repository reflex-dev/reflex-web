```python exec
import reflex as rx
from docs.tutorial.tutorial_utils import ChatappState
import docs.tutorial.tutorial_style as style
from pcweb.pages.docs import hosting
```

# Final App

We will use OpenAI's API to give our chatbot some intelligence.

## Using the API

We need to modify our event handler to send a request to the API.

```python exec
def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(rx.text(question, style=style.question_style), text_align="right"),
        rx.box(rx.text(answer, style=style.answer_style), text_align="left"),
        margin_y="1em",
    )


def chat1() -> rx.Component:
    return rx.box(
        rx.foreach(
            ChatappState.chat_history, lambda messages: qa(messages[0], messages[1])
        )
    )


def action_bar3() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=ChatappState.question,
            placeholder="Ask a question",
            on_change=ChatappState.set_question,
            style=style.input_style,
        ),
        rx.button("Ask", on_click=ChatappState.answer4, style=style.button_style),
    )
```

```python demo box
rx.center(
    rx.vstack(
        chat1(),
        action_bar3(),
        align="center",
        width="100%",
    )
)
```

```python
# state.py
import os

from openai import AsyncOpenAI

async def answer(self):
    # Our chatbot has some brains now!
    client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])

    session = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            \{"role": "user", "content": self.question}
        ],
        stop=None,
        temperature=0.7,
        stream=True,
    )

    # Add to the answer as the chatbot responds.
    answer = ""
    self.chat_history.append((self.question, answer))

    # Clear the question input.
    self.question = ""
    # Yield here to clear the frontend input before continuing.
    yield

    async for item in session:
        if hasattr(item.choices[0].delta, "content"):
            if item.choices[0].delta.content is None:
                # presence of 'None' indicates the end of the response
                break
            answer += item.choices[0].delta.content
            self.chat_history[-1] = (self.chat_history[-1][0], answer)
            yield
```

Finally, we have our chatbot!

## Final Code

We wrote all our code in three files, which you can find below.

```python
# chatapp.py
import reflex as rx

from chatapp import style
from chatapp.state import TutorialState


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(rx.text(question, text_align="right"), style=style.question_style),
        rx.box(rx.text(answer, text_align="left"), style=style.answer_style),
    )

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            TutorialState.chat_history,
            lambda messages: qa(messages[0], messages[1])
        )
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Ask a question",
            value=TutorialState.question,
            on_change=TutorialState.set_question,
            style=style.input_style,
        ),
        rx.button("Ask", on_click=TutorialState.answer, style=style.button_style),
    )


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            chat(),
            action_bar(),
            align="center",
        )
    )


app = rx.App()
app.add_page(index)
```

```python
# state.py
import os

from openai import AsyncOpenAI

import reflex as rx

class TutorialState(rx.State):

    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    async def answer(self):
        # Our chatbot has some brains now!
        client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
        session = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[\{"role": "user", "content": self.question}],
            stop=None,
            temperature=0.7,
            stream=True,
        )

        # Add to the answer as the chatbot responds.
        answer = ""
        self.chat_history.append((self.question, answer))

        # Clear the question input.
        self.question = ""
        # Yield here to clear the frontend input before continuing.
        yield

        async for item in session:
            if hasattr(item.choices[0].delta, "content"):
                if item.choices[0].delta.content is None:
                    # presence of 'None' indicates the end of the response
                    break
                answer += item.choices[0].delta.content
                self.chat_history[-1] = (self.chat_history[-1][0], answer)
                yield
```

```python
# style.py
import reflex as rx

# Common styles for questions and answers.
shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "20%"
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
    max_width="30em",
    display="inline-block",
)

# Set specific styles for questions and answers.
question_style = message_style | dict(
    background_color=rx.color("gray", 4), margin_left=chat_margin
)
answer_style = message_style | dict(
    background_color=rx.color("accent", 8), margin_right=chat_margin
)

# Styles for the action bar.
input_style = dict(border_width="1px", padding="1em", box_shadow=shadow, width="350px")
button_style = dict(
    background_color=rx.color("accent", 10), box_shadow=shadow
)

```

## Next Steps

Congratulations! You have built your first chatbot. From here, you can read through the rest of the documentations to learn about Reflex in more detail. The best way to learn is to build something, so try to build your own app using this as a starting point!

## One More Thing

With our hosting service, you can deploy this app with a single command within minutes. Check out our [Hosting Quick Start]({hosting.deploy_quick_start.path}).
