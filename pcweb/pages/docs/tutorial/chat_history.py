import reflex as rx
from pcweb import styles
from pcweb.base_state import State
from pcweb.templates.docpage import (
    doccode,
    docdemobox,
    docheader,
    docpage,
    doctext,
    subheader,
)
from pcweb.pages.docs.tutorial.adding_state import ChatappState, chat1, style

state1 = """# state.py
import os
import openai

openai.API_KEY = os.environ["OPENAI_API_KEY"]

...

def answer(self):
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

    # Add to the answer as the chatbot responds.
    answer = ""
    self.chat_history.append((self.question, answer))
    for item in session:
        if hasattr(item.choices[0].delta, "content"):
            answer += item.choices[0].delta.content
            self.chat_history[-1] = (self.question, answer)
            yield

    yield rx.set_value("question", "")
"""


def action_bar3() -> rx.Component:
    return rx.hstack(
        rx.input(
            id="question",
            placeholder="Ask a question",
            on_blur=ChatappState.set_question,
            style=style.input_style,
        ),
        rx.button("Ask", on_click=ChatappState.answer4, style=style.button_style),
    )


code_out1 = rx.container(
    chat1(),
    action_bar3(),
)

final_code = """# chatapp.py
import reflex as rx

from chatapp import style
from chatapp.state import State


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(rx.text(question, text_align="right"), style=style.question_style),
        rx.box(rx.text(answer, text_align="left"), style=style.answer_style),
        margin_y="1em",
    )

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1])
        )
    )

    
def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(id="question", placeholder="Ask a question", on_blur=State.set_question, style=style.input_style),
        rx.button("Ask", on_click=State.answer, style=style.button_style),
    )


def index() -> rx.Component:
    return rx.container(
        chat(),
        action_bar(),
    )


app = rx.App()
app.add_page(index)
app.compile()
"""

final_state = """# state.py
import reflex as rx
import os
import openai


openai.api_key = os.environ["OPENAI_API_KEY"]

class State(rx.State):

    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    def answer(self):
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

"""

final_style = """# style.py

# Common styles for questions and answers.
shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "20%"
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
)

# Set specific styles for questions and answers.
question_style = message_style | dict(bg="#F5EFFE", margin_left=chat_margin)
answer_style = message_style | dict(bg="#DEEAFD", margin_right=chat_margin)

# Styles for the action bar.
input_style = dict(
    border_width="1px", padding="1em", box_shadow=shadow
)
button_style = dict(
    bg="#CEFFEE", box_shadow=shadow
)
"""


@docpage()
def final_app():
    from pcweb.pages.docs.hosting.self_hosting import self_hosting

    return rx.box(
        docheader("Final App"),
        doctext("We will use OpenAI's API to give our chatbot some intelligence. "),
        subheader("Using the API"),
        doctext("We need to modify our event handler to send a request to the API. "),
        doccode(state1),
        docdemobox(code_out1),
        doctext("Finally, we have our chatbot! "),
        subheader("Final Code"),
        doctext("We wrote all our code in three files, which you can find below. "),
        doccode(final_code),
        doccode(final_state),
        doccode(final_style),
        subheader("Next Steps"),
        doctext(
            "Congratulations! You have built your first chatbot. "
            "From here, you can read through the rest of the documentations to learn about Reflex ",
            "in more detail. ",
            "The best way to learn is to build something, so try to build your own app using this ",
            "as a starting point! ",
        ),
        doctext(
            "Once you've built your app, you can deploy it to the web. ",
            "We are working on a single command deployment, but for now, you can follow ",
            "the instructions in the ",
            rx.link("self hosting", self_hosting),
            " guide to deploy your app. ",
        ),
    )
