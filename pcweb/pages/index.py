import asyncio
import json
import os
from datetime import datetime

import httpx
from email_validator import EmailNotValidError, validate_email
from sqlmodel import Field

import reflex as rx
from pcweb import constants, styles
from pcweb.components.spline import spline_component
from pcweb.pages.docs import (
    database,
    getting_started,
    hosting,
    state,
    styling,
    wrapping_react,
)
from pcweb.pages.docs.library import library
from pcweb.templates import webpage

link_style = {
    "color": "black",
    "font_weight": styles.BOLD_WEIGHT,
    "_hover": {"color": styles.ACCENT_COLOR},
}


class Confetti(rx.Component):
    """Confetti component."""

    library = "react-confetti"
    tag = "ReactConfetti"
    is_default = True


confetti = Confetti.create


class Waitlist(rx.Model, table=True):
    email: str
    date_created: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class IndexState(rx.State):
    """Hold the state for the home page."""

    # The waitlist email.
    email: str

    # Whether the user signed up for the waitlist.
    signed_up: bool = False

    # Whether to show the confetti.
    show_confetti: bool = False

    def add_contact_to_loops(self, contact_data):
        url = "https://app.loops.so/api/v1/contacts/create"
        loops_api_key = os.getenv("LOOPS_API_KEY")
        if loops_api_key is None:
            print("Loops API key does not exist")
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {loops_api_key}",
        }

        try:
            with httpx.Client() as client:
                response = client.post(url, headers=headers, json=contact_data)
                response.raise_for_status()  # Raise an exception for HTTP errors (4xx and 5xx)

        except httpx.RequestError as e:
            print(f"An error occurred: {e}")

    def signup(self):
        """Sign the user up for the waitlist."""
        # Check if the email is valid.
        try:
            validation = validate_email(self.email, check_deliverability=True)
            self.email = validation.email
        except EmailNotValidError as e:
            # Alert the error message.
            return rx.window_alert(str(e))

        # Check if the user is already on the waitlist.
        with rx.session() as session:
            user = session.query(Waitlist).filter(Waitlist.email == self.email).first()
            if user is None:
                # Add the user to the waitlist.
                session.add(Waitlist(email=self.email))
                session.commit()
                contact_data = json.dumps({"email": self.email})
                self.add_contact_to_loops(contact_data)

        self.signed_up = True
        return IndexState.play_confetti

    async def play_confetti(self):
        """Play confetti for 5sec then stop."""
        self.show_confetti = True
        yield
        await asyncio.sleep(5)
        self.show_confetti = False
        yield


def container(*children, **kwargs):
    kwargs = {"max_width": "1440px", "padding_x": ["1em", "2em", "3em"], **kwargs}
    return rx.chakra.container(
        *children,
        **kwargs,
    )


def tag(text):
    return rx.chakra.text(
        text,
        color="#5646ED",
        bg="#F5EFFE",
        padding_x="0.5em",
        padding_y="0.25em",
        border_radius="8px",
        font_weight=600,
    )


def landing():
    return container(
        rx.cond(
            IndexState.show_confetti,
            confetti(),
        ),
        rx.chakra.hstack(
            rx.center(
                rx.chakra.vstack(
                    rx.chakra.text(
                        rx.chakra.span("[", color="#DACEEE"),
                        rx.chakra.span("Frontend", color="#696287"),
                        rx.chakra.span("]", color="#DACEEE"),
                        rx.chakra.span("[", color="#DACEEE"),
                        rx.chakra.span("Backend", color="#696287"),
                        rx.chakra.span("]", color="#DACEEE"),
                        rx.chakra.span("[", color="#DACEEE"),
                        rx.chakra.span("Hosting", color="#696287"),
                        rx.chakra.span("]", color="#DACEEE"),
                        font_family=styles.MONO,
                        mb=2,
                    ),
                    rx.chakra.text(
                        "Web apps in pure Python.",
                        font_family=styles.MONO,
                        font_style="normal",
                        font_weight="600",
                        font_size="6xl",
                        line_height="1.2",
                        letter_spacing="-0.02em",
                    ),
                    rx.chakra.text(
                        "Build web apps in minutes. Deploy with a single command.",
                        color="#342E5C",
                        font_size="1.1em",
                        font_family=styles.SANS,
                        padding_top="1em",
                    ),
                    rx.cond(
                        ~IndexState.signed_up,
                        rx.chakra.wrap(
                            rx.chakra.input_group(
                                rx.chakra.input_left_element(
                                    rx.image(
                                        src="/landing_icons/custom_icons/email.png",
                                        height="1.2em",
                                    ),
                                ),
                                rx.chakra.input(
                                    placeholder="Your email address...",
                                    on_blur=IndexState.set_email,
                                    style=styles.INPUT_STYLE,
                                    type="email",
                                ),
                                style=styles.INPUT_STYLE,
                            ),
                            rx.chakra.button(
                                "Join Hosting Waitlist",
                                on_click=IndexState.signup,
                                style=styles.ACCENT_BUTTON,
                            ),
                            justify="left",
                            should_wrap_children=True,
                            spacing="1em",
                            padding_x=".25em",
                            padding_y="1em",
                        ),
                        rx.chakra.text(
                            rx.chakra.icon(
                                tag="check",
                            ),
                            " You're on the waitlist!",
                            color=styles.ACCENT_COLOR,
                        ),
                    ),
                    align_items="left",
                    padding="1em",
                ),
                width="100%",
            ),
            spline_component(),
        ),
        padding_top="6em",
        padding_bottom="6em",
        width="100%",
    )


def list_circle(text):
    return rx.flex(
        rx.chakra.text(text),
        width="2em",
        height="2em",
        border_radius="6px",
        bg="#F5EFFE",
        color="#5646ED",
        align_items="center",
        justify_content="center",
        font_weight="800",
    )


def example_card(title, tags, href, image):
    return rx.chakra.hstack(
        rx.image(src=image, height="1em", width="1em"),
        rx.chakra.text(title, color="#494369", font_weight="400"),
        rx.chakra.spacer(),
        *[tag(t) for t in tags],
        rx.link(
            rx.center(
                rx.chakra.icon(tag="arrow_forward", color="#494369"),
                border_radius="6px",
                box_shadow="0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14);",
                min_width="2em",
                min_height="2em",
            ),
            href=href,
        ),
        border="1px solid #F5EFFE",
        width="100%",
        padding=".5em",
        border_radius="8px",
    )


def intro():
    return rx.chakra.box(
        container(
            rx.chakra.text(
                "Build anything, faster.",
                font_size="4xl",
                font_family=styles.MONO,
                font_style="normal",
                font_weight=600,
                pb=1,
                letter_spacing="-0.02em",
                mb=4,
            ),
            rx.chakra.text(
                "Create your whole app in a single language. ",
                "Don't worry about writing APIs to connect your frontend and backend. ",
                color="#666",
                mb=8,
                max_width="50%",
            ),
            rx.flex(
                rx.chakra.box(
                    rx.chakra.hstack(
                        list_circle("1"),
                        rx.chakra.text("Any use case.", font_weight="600"),
                        mb=4,
                    ),
                    rx.chakra.text(
                        "With Reflex you can build anything from internal tools and data apps to complex multi-page apps.",
                        color="#666",
                        mb=4,
                    ),
                    rx.chakra.text(
                        rx.chakra.span('"""', color="#AA9EC3"),
                        rx.chakra.span(
                            "This entire website is made in Reflex!",
                            color="#494369",
                        ),
                        rx.chakra.span('"""', color="#AA9EC3"),
                        bg="#FAF8FB",
                        font_family=styles.MONO,
                        p=4,
                        border="1px solid #EAE4FD",
                        mb=8,
                        border_radius="lg",
                    ),
                    rx.chakra.hstack(
                        list_circle("2"),
                        rx.chakra.text("It’s just Python.", font_weight="600"),
                        mb=4,
                    ),
                    rx.chakra.text(
                        "The app state is just a class. ",
                        "State updates are methods in the class. ",
                        "And the UI is a reflection of the state. ",
                        color="#666",
                    ),
                    flex=1,
                    margin_right=[0, 0, "1em"],
                    margin_bottom=["2em", "2em", 0],
                ),
                rx.chakra.vstack(
                    example_card(
                        "Chat GPT",
                        ["LLM", "Chatbot"],
                        "https://github.com/pynecone-io/pynecone-chat",
                        "/landing_icons/custom_icons/chat.svg",
                    ),
                    example_card(
                        "Sales email generator",
                        ["OpenAI", "Database"],
                        "https://github.com/pynecone-io/pynecone-examples/tree/main/sales",
                        "/landing_icons/custom_icons/draw.svg",
                    ),
                    example_card(
                        "DALL-E",
                        ["ML", "Image Generation"],
                        "https://github.com/pynecone-io/pynecone-examples/tree/main/dalle",
                        "/landing_icons/custom_icons/bucket.svg",
                    ),
                    example_card(
                        "Graphing Traversal",
                        ["DFS", "BFS", "Graph"],
                        "https://github.com/pynecone-io/pynecone-examples/tree/main/traversal",
                        "/landing_icons/custom_icons/nodes.svg",
                    ),
                    example_card(
                        "Todo App",
                        ["Short"],
                        "https://github.com/pynecone-io/pynecone-examples/tree/main/todo",
                        "/landing_icons/custom_icons/check.svg",
                    ),
                    align_items="center",
                    margin_left=[0, 0, "1em"],
                    flex=1,
                ),
                flex_direction=["column", "column", "column", "row", "row"],
            ),
        ),
        padding_top="5em",
        padding_bottom="5em",
    )


@webpage(path="/", title="Reflex: Web apps in Pure Python")
def index() -> rx.Component:
    """Get the main Reflex landing page."""
    return rx.chakra.box(
        landing(),
        intro(),
        width="100%",
        margin_top="80px",
    )
