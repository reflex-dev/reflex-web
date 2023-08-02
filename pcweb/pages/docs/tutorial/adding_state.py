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
        return rx.set_value("question", "")

    async def answer3(self):
        import asyncio
        # Our chatbot is not very smart right now...
        answer = "I don't know!"
        self.chat_history.append((self.question, ""))
        for i in range(len(answer)):
            await asyncio.sleep(0.1)
            self.chat_history[-1] = (self.question, answer[:i])
            yield
        yield rx.set_value("question", "")

    def answer4(self):
        # Our chatbot has some brains now!
        session = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": self.question}
            ],
            stop=None,
            temperature=0.7,
            stream=True,
        )

        answer = ""
        self.chat_history.append((self.question, answer))
        for item in session:
            if hasattr(item.choices[0].delta, "content"):
                answer += item.choices[0].delta.content
                self.chat_history[-1] = (self.question, answer)
                yield

        yield rx.set_value("question", "")


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
            ChatappState.chat_history,
            lambda messages: qa(messages[0], messages[1])
        )
    )
def action_bar1() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Ask a question", on_blur=ChatappState.set_question, style=style.input_style),
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
        rx.input(placeholder="Ask a question", on_blur=State.set_question, style=style.input_style),
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
    return rx.set_value("question", "")
"""
def action_bar2() -> rx.Component:
    return rx.hstack(
        rx.input(id="question", placeholder="Ask a question", on_blur=ChatappState.set_question, style=style.input_style),
        rx.button("Ask", on_click=ChatappState.answer2, style=style.button_style),
    )
code2 = """# chatapp.py
def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(id="question", placeholder="Ask a question", on_blur=State.set_question, style=style.input_style),
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
    for i in range(len(answer)):
        # Pause to show the streaming effect.
        await asyncio.sleep(0.1)
        # Add one letter at a time to the output.
        self.chat_history[-1] = (self.question, answer[:i])
        yield

    # Clear the input.
    yield rx.set_value("question", "")
"""
def action_bar3() -> rx.Component:
    return rx.hstack(
        rx.input(id="question", placeholder="Ask a question", on_blur=ChatappState.set_question, style=style.input_style),
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
            rx.code("on_blur"),
            " event to the ",
            rx.code("set_question"),
            " event handler, which will update the ",
            rx.code("question"),
            " state var when the user clicks away from the input. ",
            "We bind the button's ",
            rx.code("on_click"),
            " event to the ",
            rx.code("answer"),
            " event handler, which will process the question and add the answer to the chat history. ",
            "Learn more in the ",
            doclink("events docs", events.path),
            ".",
        ),
        subheader("Clearing the Input"),
        doctext(
            "Currently the input doesn't clear after the user clicks the button. ",
            "We can fix this by adding an ",
            rx.code("id"),
            " to the input and creating an event to clear it. ",
        ),
        docdemobox(code_out2),
        doccode(code2),
        doccode(state2),
        doctext(
            "After setting the question, we return an event from our ",
            rx.code("answer"),
            " event handler to clear the input. ",
            "Learn more about returning events in the ",
            doclink("events docs", f"{events.path}#returning-events-from-event-handlers"),
            ".",
        ),
        doctext(
            "We use the ",
            rx.code("set_value"),
            " function to set the value of the ",
            rx.code("question"),
            " state var to an empty string. ",
            "See the ",
            doclink("special events docs", special_events.path),
            " for more info on special events. ",
        ),
        subheader("Streaming Text"),
        doctext(
            "Normally state updates are sent to the frontend when an event handler returns. ",
            "However, we want to stream the text from the chatbot as it is generated. ",
            "We can do this by yielding from the event handler. ",
            "See the ",
            doclink("event yield docs", f"{events.path}#yielding-multiple-updates"),
            " for more info. ",
        ),
        doccode(state3),
        docdemobox(code_out3),
        doctext(
            "In the next section, we will finish our chatbot by adding AI!",
        ),
    )
