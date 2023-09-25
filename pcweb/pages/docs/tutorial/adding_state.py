import reflex as rx
from pcweb.pages.docs.tutorial import style
from pcweb.base_state import State
from pcweb.templates.docpage import (
    doccode,
    docdemobox,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader,
)
import openai

openai.api_key = "YOUR_OPENAI_KEY"


class ChatappState(State):
    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    def answer(self):
        # Our chatbot is not very smart right now...
        answer = "I don't know!"
        self.chat_history.append((self.question, answer))

    def answer2(self):
        # Our chatbot is not very smart right now...
        answer = "I don't know!"
        self.chat_history.append((self.question, answer))
        # Clear the question input.
        self.question = ""

    async def answer3(self):
        import asyncio

        # Our chatbot is not very smart right now...
        answer = "I don't know!"
        self.chat_history.append((self.question, ""))

        # Clear the question input.
        self.question = ""
        # Yield here to clear the frontend input before continuing.
        yield

        for i in range(len(answer)):
            await asyncio.sleep(0.1)
            self.chat_history[-1] = (self.chat_history[-1][0], answer[: i + 1])
            yield

    def answer4(self):
        # Our chatbot has some brains now!
        session = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": self.question}],
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

        for item in session:
            if hasattr(item.choices[0].delta, "content"):
                answer += item.choices[0].delta.content
                self.chat_history[-1] = (self.chat_history[-1][0], answer)
                yield


state1 = """# state.py

class State(rx.State):

    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    def answer(self):
        # Our chatbot is not very smart right now...
        answer = "I don't know!"
        self.chat_history.append((self.question, answer))
"""
from pcweb.pages.docs.tutorial.frontend import qa4 as qa


def chat1() -> rx.Component:
    return rx.box(
        rx.foreach(
            ChatappState.chat_history, lambda messages: qa(messages[0], messages[1])
        )
    )


def action_bar1() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Ask a question",
            on_change=ChatappState.set_question,
            style=style.input_style,
        ),
        rx.button("Ask", on_click=ChatappState.answer, style=style.button_style),
    )


code1 = """# chatapp.py
from chatapp.state import State

...

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1])
        )
    )

...

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Ask a question", on_change=State.set_question, style=style.input_style),
        rx.button("Ask", on_click=State.answer, style=style.button_style),
    )
"""
code_out1 = rx.container(
    chat1(),
    action_bar1(),
)

state2 = """# state.py

def answer(self):
    # Our chatbot is not very smart right now...
    answer = "I don't know!"
    self.chat_history.append((self.question, answer))
    self.question = ""
"""


def action_bar2() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=ChatappState.question,
            placeholder="Ask a question",
            on_change=ChatappState.set_question,
            style=style.input_style,
        ),
        rx.button("Ask", on_click=ChatappState.answer2, style=style.button_style),
    )


code2 = """# chatapp.py
def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=ChatappState.question,
            placeholder="Ask a question",
            on_change=State.set_question,
            style=style.input_style),
        rx.button("Ask", on_click=State.answer, style=style.button_style),
    )
"""
code_out2 = rx.container(
    chat1(),
    action_bar2(),
)

state3 = """# state.py
import asyncio

...
async def answer(self):
    # Our chatbot is not very smart right now...
    answer = "I don't know!"
    self.chat_history.append((self.question, ""))

    # Clear the question input.
    self.question = ""
    # Yield here to clear the frontend input before continuing.
    yield

    for i in range(len(answer)):
        # Pause to show the streaming effect.
        await asyncio.sleep(0.1)
        # Add one letter at a time to the output.
        self.chat_history[-1] = (self.chat_history[-1][0], answer[:i + 1])
        yield
"""


def action_bar3() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=ChatappState.question,
            placeholder="Ask a question",
            on_change=ChatappState.set_question,
            style=style.input_style,
        ),
        rx.button("Ask", on_click=ChatappState.answer3, style=style.button_style),
    )


code_out3 = rx.container(
    chat1(),
    action_bar3(),
)


@docpage()
def adding_state():
    from pcweb.pages.docs.state.overview import state_overview
    from pcweb.pages.docs.state.events import events
    from pcweb.pages.docs.api_reference.special_events import special_events

    return rx.box(
        docheader("State", first=True),
        doctext(
            "Now let’s make the chat app interactive by adding state. ",
            "The state is where we define all the variables that can change in the app and all the functions that can modify them. ",
            "You can learn more about state in the ",
            doclink("state docs", state_overview.path),
            ".",
        ),
        subheader("Defining State"),
        doctext(
            "We will create a new file called ",
            rx.code("state.py"),
            " in the ",
            rx.code("chatapp"),
            " directory. ",
            "Our state will keep track of the current question being asked and the chat history. ",
            "We will also define an event handler ",
            rx.code("answer"),
            " which will process the current question and add the answer to the chat history. ",
        ),
        doccode(state1),
        subheader("Binding State to Components"),
        doctext(
            "Now we can import the state in ",
            rx.code("chatapp.py"),
            " and reference it in our frontend components. ",
            "We will modify the ",
            rx.code("chat"),
            " component to use the state instead of the current fixed questions and answers. ",
        ),
        docdemobox(code_out1),
        doccode(code1),
        doctext(
            "Normal Python ",
            rx.code("for"),
            " loops don't work for iterating over state vars because these values can change and ",
            " aren't known at compile time. ",
            "Instead, we use the ",
            doclink("foreach", href="/docs/library/layout/foreach"),
            " component to iterate over the chat history. ",
        ),
        doctext(
            "We also bind the input's ",
            rx.code("on_change"),
            " event to the ",
            rx.code("set_question"),
            " event handler, which will update the ",
            rx.code("question"),
            " state var while the user types in the input. ",
            "We bind the button's ",
            rx.code("on_click"),
            " event to the ",
            rx.code("answer"),
            " event handler, which will process the question and add the answer to the chat history. ",
            "The ",
            rx.code("set_question"),
            " event handler is a built-in implicitly defined event handler. Every base var has one.",
            "Learn more in the ",
            doclink("events docs", events.path),
            " under the Setters section.",
        ),
        
        subheader("Clearing the Input"),
        doctext(
            "Currently the input doesn't clear after the user clicks the button. ",
            "We can fix this by binding the value of the input to ",
            rx.code("question"),
            ", with ",
            rx.code("value=ChatappState.question"),
            ", and clear it when we run the event handler for ",
            rx.code("answer"),
            ", with ",
            rx.code("self.question = ''"),
            "."
        ),
        docdemobox(code_out2),
        doccode(code2),
        doccode(state2),
        subheader("Streaming Text"),
        doctext(
            "Normally state updates are sent to the frontend when an event handler returns. ",
            "However, we want to stream the text from the chatbot as it is generated. ",
            "We can do this by yielding from the event handler. ",
            "See the ",
            doclink("event yield docs", f"{events.path}#yielding-multiple-updates"),
            " for more info. ",
        ),
        docdemobox(code_out3),
        doccode(state3),
        doctext(
            "In the next section, we will finish our chatbot by adding AI!",
        ),
    )
