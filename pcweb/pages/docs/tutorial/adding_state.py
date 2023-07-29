
import reflex as rx
from pcweb import styles
from pcweb.base_state import State
from pcweb.templates.docpage import (
    doc_section,
    doccode,
    docdemobox,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader_comp,
    text_comp,
    definition,
    docalert,
    subheader
)

@docpage()
def adding_state():
    return rx.box(
        docheader("Adding State"),
        doctext(
            """
            Now let’s make your chat app interactive. To do this, we will hook it up to Reflex’s state. The app's state is where we define all the vars that can change in the app and all the functions that can modify them. A detailed explanation of the state can be found here. 
            """,
        ),
        doctext("For this app we will need to keep track of two things the question asked and the answer to the question. We will also define a function process question which will call the OpenAI API to get the answer to our question. "),
        doccode(
            '''import reflex as rx
import openai
from .styles import input_style, message_style, button_style

# Replace 'YOUR_API_KEY' with your actual API key
openai.api_key = 'YOUR_API_KEY'

class State(rx.State):
    """The app state."""

    question: str = "What is the meaning of life?"
    
    answer: str = "42"

    async def process_question(self):
        self.answer = ""
        yield

        session = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                { "role": "user", "content": self.question}
            ],
            stop=None,
            temperature=0.7,
            stream=True,
        )

        for item in session:
            if hasattr(item.choices[0].delta, "content"):        
                self.answer += item.choices[0].delta.content
                yield
        '''
        ),
        doctext(
            """
            Now we can hook up the variable and event handlers to our UI.
            """,
        ),
        doccode(
            '''def qa() -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(
                State.question,
                bg="#F5EFFE",
                style=message_style,
            ),
            text_align="right",
            margin_top="1em",
        ),
        rx.box(
            rx.text(
                State.answer,
                bg="#DEEAFD",
                style=message_style,
            ),
            text_align="left",
            padding_top="1em",
        ),
        width="100%",
    )


def action_bar() -> rx.Component:
    """The action bar to send a new message."""
    return rx.hstack(
        rx.input(placeholder="Ask a question...", style=input_style, on_blur=State.set_question),
        rx.button("Ask", on_click=State.process_question, style=button_style),
        width="100%",
    )
            '''
        )


    )
