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
    subheader,
)


@docpage()
def starting_point():
    return rx.box(
        docheader("Starting Point"),
        doctext(
            """
            Let's start with defining the UI for our chat app. In Reflex, UI can be broken down into components. A more detailed guide about components can be found here, but in short, they let you split the UI into independent, reusable pieces, and let you think about each piece in isolation.
            """,
        ),
        doctext(
            "Below we will make a component that displays the question and answer."
        ),
        doccode(
            """def qa() -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(
                "Question"
            ),
            text_align="right",
            margin_top="1em",
        ),
        rx.box(
            rx.text(
                "Answer",
            ),
            text_align="left",
            padding_top="1em",
        ),
        width="100%",
    )
            """,
        ),
        doctext(
            """
            Now we want a way for the user to input a question. For this, we will use the input component to have the user add text and a button component to submit the question.
            """,
        ),
        doccode(
            """def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Ask a question...",
        ),
        rx.button("Ask"),
        width="100%",
    )
            """,
        ),
        doctext(
            """
            Let's add some styling to the apps. A detailed guide on how to style reflex apps can be found here. For cleanliness, we will put all styling in a separate file style.py:
            """,
        ),
        doccode(
            """message_style = dict(
    display="inline-block",
    padding="4",
    border_radius="5px",
    max_width="30em",
    box_shadow="rgba(17, 12, 46, 0.15) 0px 48px 100px 0px;",
)

question_style = {**dict(bg="#F5EFFE"), **message_style}
answer_style = {**dict(bg="#DEEAFD"), **message_style}

input_style = dict(
    border_width="1px", p="4", box_shadow="rgba(17, 12, 46, 0.15) 0px 48px 100px 0px;"
)

button_style = dict(
    bg="#CEFFEE", box_shadow="rgba(17, 12, 46, 0.15) 0px 48px 100px 0px;"
)
        """
        ),
        doctext(
            """
            The app so far should be the following:
            """,
        ),
        doccode(
            '''import reflex as rx
from .styles import question_style, answer_style, button_style, input_style
 
class State(rx.State):
	pass

def qa() -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(
                "What is the meaning of life?",
                style=question_style,
            ),
            text_align="right",
            margin_top="1em",
        ),
        rx.box(
            rx.text(
                "42",
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
        ),
        rx.button("Ask", style=button_style),
        width="100%",
    )


def index() -> rx.Component:
    """The index page."""
    return rx.vstack(
        qa(),
        action_bar(),
        width="100%",
        padding="1em",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
            '''
        ),
    )
