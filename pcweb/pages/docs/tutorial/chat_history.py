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
def chat_history():
    return rx.box(
        docheader("Chat History"),
        doctext(
            """
            This is great for a single question-answer format, but what if we want to keep track of past answers?
            """,
        ),
        doccode(
            '''class State(rx.State):
    """The app state."""

    qa: list[dict[str, str]] = [{"Q": "What is the meaning of life?", "A": "42"}]

    question: str = ""

    answer: str = ""

    async def process_question(self):
        """Process the question."""
        self.qa.append({"Q": self.question, "A": ""})

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
                self.qa[-1]["A"] += item.choices[0].delta.content
                yield



def qa(question, answer) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(
                question,
                style=question_style,
            ),
            text_align="right",
            margin_top="1em",
        ),
        rx.box(
            rx.text(
                answer,
                style=answer_style,
            ),
            text_align="left",
            padding_top="1em",
        ),
        width="100%",
    )


def action_bar() -> rx.Component:
    """The action bar to send a new message."""
    return rx.hstack(
        rx.input(
            placeholder="Ask a question...",
            style=input_style,
            on_blur=State.set_question,
        ),
        rx.button("Ask", on_click=State.process_question, style=button_style),
        width="100%",
        padding_top="1em",
    )


def index() -> rx.Component:
    """The index page."""
    return rx.vstack(
        rx.foreach(
            State.qa,
            lambda item: qa(item["Q"], item["A"]),
        ),
        action_bar(),
        width="100%",
        padding="1em",
    )
        '''
        ),
    )
