import reflex as rx
from pcweb import styles
from pcweb.base_state import State
from pcweb.templates.docpage import (
    doc_section,
    doccode,
    docdemo,
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

code1 = """# chatapp.py
import reflex as rx


def index() -> rx.Component:
    return rx.container(
        rx.box(
            "What is Reflex?",
            # The user's question is on the right.
            text_align="right",
        ),
        rx.box(
            "A way to build web apps in pure Python!",
            # The answer is on the left.
            text_align="left",
        ),
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
"""
code1_out = rx.container(
    rx.box(
        "What is Reflex?",
        # The user's question is on the right.
        text_align="right",
    ),
    rx.box(
        "A way to build web apps in pure Python!",
        # The answer is on the left.
        text_align="left",
    ),
)

code2 = """def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(question, text_align="right"),
        rx.box(answer, text_align="left"),
        margin_y="1em",
    )

def chat() -> rx.Component:
    qa_pairs = [
        ("What is Reflex?", "A way to build web apps in pure Python!"),
        ("What can I make with it?", "Anything from a simple website to a complex web app!"),
    ]
    return rx.box(*[qa(question, answer) for question, answer in qa_pairs]) 
    
def index() -> rx.Component:
    return rx.container(chat())
    """

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(question, text_align="right"),
        rx.box(answer, text_align="left"),
        margin_y="1em",
    )
qa_pairs = [
        ("What is Reflex?", "A way to build web apps in pure Python!"),
        ("What can I make with it?", "Anything from a simple website to a complex web app!"),
    ]
def chat() -> rx.Component:
    qa_pairs = [
        ("What is Reflex?", "A way to build web apps in pure Python!"),
        ("What can I make with it?", "Anything from a simple website to a complex web app!"),
    ]
    return rx.box(*[qa(question, answer) for question, answer in qa_pairs]) 
code2_out = rx.container(chat())

code3 = """def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Ask a question"),
        rx.button("Ask"),
    )
    
def index() -> rx.Component:
    return rx.container(
        chat(),
        action_bar(),
    )
    """
def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Ask a question"),
        rx.button("Ask"),
    )
code3_out = rx.container(
        chat(),
        action_bar(),
    )


@docpage()
def starting_point():
    from pcweb.pages.docs.components.overview import components_overview
    from pcweb.pages.docs.components.props import props
    return rx.box(
        docheader("Basic Frontend", first=True),
        doctext(
            "Let's start with defining the frontend for our chat app. ",
            "In Reflex, the frontend can be broken down into independent, reusable components. ",
            "See the ",
            doclink("components docs", components_overview.path),
            " for more information.",
        ),
        subheader("Display A Question  And Answer"),
        doctext(
            "We will modify the ",
            rx.code("index"),
            " function in ",
            rx.code("chatapp/chatapp.py"),
            " file to return a component that displays a single question and answer. ",
        ),
        docdemobox(code1_out),
        doccode(code1),
        doctext(
            "Components can be nested inside each other to create complex layouts. ",
            "Here we create a parent container that contains two boxes for ",
            "the question and answer. ",
        ),
        doctext(
            "We also add some basic styling to the components. ",
            "Components take in keyword arguments, called ",
            doclink("props", href=props.path),
            ", that modify the appearance and functionality of the component. ",
            "We use the ",
            rx.code("text_align"),
            " prop to align the text to the left and right.",
        ),
        subheader("Reusing Components"),
        doctext(
            "Now that we have a component that displays a single question and answer, ",
            "we can reuse it to display multiple questions and answers. ",
            "We will move the component to a separate function ",
            rx.code("question_answer"),
            " and call it from the ",
            rx.code("index"),
            " function.",
        ),
        docdemobox(code2_out),
        doccode(code2),
        subheader("Chat Input"),
        doctext(
            "Now we want a way for the user to input a question. ",
            "For this, we will use the ",
            doclink("input", href="/docs/library/forms/input"),
            " component to have the user add text and a ",
            doclink("button", href="/docs/library/forms/button"),
            " component to submit the question.",
        ),
        docdemobox(code3_out),
        doccode(code3),
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
