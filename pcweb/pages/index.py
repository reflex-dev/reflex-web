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


boxstyles = {}

compbox = rx.chakra.hstack(
    rx.image(
        src="/landing_icons/icon1.svg",
        height="4em",
        width="4em",
    ),
    rx.chakra.vstack(
        rx.chakra.text(
            "60+ built-in UI Components",
            font_size=styles.TEXT_FONT_SIZE,
            font_weight=styles.BOLD_WEIGHT,
        ),
        rx.chakra.text(
            "Reflex comes with a large library of UI components ranging from simple buttons to complex graphs and tables.",
            color="#342E5C",
        ),
        rx.chakra.box(
            rx.link(
                rx.chakra.button(
                    "Check out the full library",
                    rx.chakra.icon(tag="arrow_forward"),
                    style=styles.BUTTON_LIGHT_NO_BACKGROUND,
                ),
                href=library.path,
            )
        ),
        align_items="left",
        width="100%",
    ),
    style=boxstyles,
    align_items="left",
    spacing="1em",
    width="100%",
)

stylebox = rx.chakra.hstack(
    rx.image(
        src="/landing_icons/icon2.svg",
        height="4em",
        width="4em",
    ),
    rx.chakra.vstack(
        rx.chakra.text(
            "Completely customizable",
            font_size=styles.TEXT_FONT_SIZE,
            font_weight=styles.BOLD_WEIGHT,
        ),
        rx.chakra.text(
            "All Reflex components are fully customizable. Change the colors, fonts, and styles to match your project.",
            color="#342E5C",
        ),
        rx.chakra.box(
            rx.link(
                rx.chakra.button(
                    "Styling Guide",
                    rx.chakra.icon(tag="arrow_forward"),
                    style=styles.BUTTON_LIGHT_NO_BACKGROUND,
                ),
                href=styling.overview.path,
            )
        ),
        align_items="left",
        width="100%",
    ),
    style=boxstyles,
    align_items="left",
    spacing="1em",
    width="100%",
)

reactbox = rx.chakra.hstack(
    rx.image(
        src="/landing_icons/icon3.svg",
        height="4em",
        width="4em",
    ),
    rx.chakra.vstack(
        rx.chakra.text(
            "Custom Components",
            font_size=styles.TEXT_FONT_SIZE,
            font_weight=styles.BOLD_WEIGHT,
        ),
        rx.chakra.text(
            "Create your own components in a few lines of code. Simply wrap the React component of your choice.",
            color="#342E5C",
        ),
        rx.chakra.box(
            rx.link(
                rx.chakra.button(
                    "Wrapping React guide",
                    rx.chakra.icon(tag="arrow_forward"),
                    style=styles.BUTTON_LIGHT_NO_BACKGROUND,
                ),
                href=wrapping_react.overview.path,
            )
        ),
        align_items="left",
        width="100%",
    ),
    style=boxstyles,
    align_items="left",
    spacing="1em",
    width="100%",
)

powerful = rx.chakra.hstack(
    rx.image(
        src="/landing_icons/icon4.svg",
        height="4em",
        width="4em",
    ),
    rx.chakra.vstack(
        rx.chakra.text(
            "Now everyone can work across the full-stack",
            font_size=styles.TEXT_FONT_SIZE,
            font_weight=styles.BOLD_WEIGHT,
        ),
        rx.chakra.text(
            "With Reflex every engineer can work across the whole stack allowing for a more efficient and productive workflow.",
            color="#342E5C",
        ),
        align_items="left",
        width="100%",
    ),
    style=boxstyles,
    align_items="left",
    spacing="1em",
    width="100%",
)


def frontend():
    return rx.chakra.box(
        container(
            height="8em",
            width="100%",
            background="radial-gradient(55.39% 67.5% at 50% 100%, rgba(188, 136, 255, 0.16) 0%, rgba(255, 255, 255, 0) 100%);",
            opacity="0.4;",
            transform="matrix(1, 0, 0, -1, 0, 0);",
        ),
        container(
            rx.chakra.vstack(
                rx.chakra.box(
                    rx.chakra.text(
                        "[",
                        rx.chakra.span("Frontend", bg="#F5EFFE", color="#5646ED"),
                        "]",
                        color="#5646ED",
                        font_family=styles.MONO,
                    )
                ),
                rx.heading(
                    "Write your entire app in Python.",
                    font_size=styles.H3_FONT_SIZE,
                    font_family=styles.MONO,
                ),
                rx.chakra.text(
                    "No more switching between languages and frameworks. Use one language for your whole stack.",
                    color="#342E5C",
                    max_width="50%",
                ),
                rx.chakra.hstack(
                    rx.desktop_only(
                        rx.chakra.vstack(
                            rx.chakra.hstack(
                                compbox,
                                stylebox,
                                spacing="2em",
                                height="100%",
                            ),
                            rx.chakra.hstack(
                                reactbox,
                                powerful,
                                height="100%",
                                spacing="2em",
                            ),
                            padding_bottom="2em",
                            width="100%",
                            spacing="2em",
                        )
                    ),
                    rx.mobile_and_tablet(
                        rx.chakra.vstack(
                            compbox,
                            stylebox,
                            reactbox,
                            powerful,
                            padding_bottom="2em",
                            height="100%",
                            spacing="2em",
                        )
                    ),
                    padding_y="2em",
                ),
                padding_bottom="2em",
                align_items="left",
            )
        ),
        bg="rgba(247, 247, 250, 0.6);",
    )


battery_icon = rx.chakra.hstack(
    rx.image(
        src="/landing_icons/battery-icon.svg",
        height="4em",
        width="4em",
    ),
    rx.chakra.vstack(
        rx.chakra.text(
            "Batteries included",
            font_size=styles.TEXT_FONT_SIZE,
            font_weight=styles.BOLD_WEIGHT,
        ),
        rx.chakra.text(
            "Skip the boilerplate and get started faster. Reflex integrates the frontend and backend so there is no need to write API endpoints.",
            color="#342E5C",
        ),
        rx.chakra.box(
            rx.link(
                rx.chakra.button(
                    "State docs",
                    rx.chakra.icon(tag="arrow_forward"),
                    style=styles.BUTTON_LIGHT_NO_BACKGROUND,
                ),
                href=state.overview.path,
            )
        ),
        align_items="left",
        width="100%",
    ),
    style=boxstyles,
    align_items="left",
    spacing="1em",
    width="100%",
)

orm_icon = rx.chakra.hstack(
    rx.image(
        src="/landing_icons/orm-icon.svg",
        height="4em",
        width="4em",
    ),
    rx.chakra.vstack(
        rx.chakra.text(
            "Built in database ORM",
            font_size=styles.TEXT_FONT_SIZE,
            font_weight=styles.BOLD_WEIGHT,
        ),
        rx.chakra.text(
            "Integrate with existing databases with a single line of code. Or use our built in SQLite database.",
            color="#342E5C",
        ),
        rx.chakra.box(
            rx.link(
                rx.chakra.button(
                    "Database docs",
                    rx.chakra.icon(tag="arrow_forward"),
                    style=styles.BUTTON_LIGHT_NO_BACKGROUND,
                ),
                href=database.overview.path,
            )
        ),
        align_items="left",
        width="100%",
    ),
    style=boxstyles,
    align_items="left",
    spacing="1em",
    width="100%",
)

python_icon = rx.chakra.hstack(
    rx.image(
        src="/landing_icons/python-icon.svg",
        height="4em",
        width="4em",
    ),
    rx.chakra.vstack(
        rx.chakra.text(
            "Seamlessly integrate with any Python library",
            font_size=styles.TEXT_FONT_SIZE,
            font_weight=styles.BOLD_WEIGHT,
        ),
        rx.chakra.text(
            "Never get locked into a framework that doesn't support your existing tech stack.",
            color="#342E5C",
        ),
        align_items="left",
        width="100%",
    ),
    style=boxstyles,
    align_items="left",
    spacing="1em",
    width="100%",
)


def backend():
    return rx.chakra.box(
        container(
            height="8em",
            width="100%",
            background="radial-gradient(55.39% 67.5% at 50% 100%, #EBEBFF 0%, rgba(255, 255, 255, 0) 100%)",
            opacity="0.4;",
            transform="matrix(1, 0, 0, -1, 0, 0);",
        ),
        container(
            rx.chakra.vstack(
                rx.chakra.box(
                    rx.chakra.text(
                        "[",
                        rx.chakra.span("Backend", color="#2B199C", bg="#F3F7FE"),
                        "]",
                        color="#2B199C",
                        font_family=styles.MONO,
                    )
                ),
                rx.heading(
                    "Skip the boilerplate and get started faster",
                    font_size=styles.H3_FONT_SIZE,
                    font_family=styles.MONO,
                ),
                rx.chakra.text(
                    "Reflex comes with a powerful backend built with FastAPI and SQLAlchemy.",
                    color="#342E5C",
                    max_width="50%",
                ),
                rx.chakra.hstack(
                    rx.desktop_only(
                        rx.chakra.vstack(
                            rx.chakra.hstack(
                                battery_icon,
                                orm_icon,
                                spacing="2em",
                                height="100%",
                            ),
                            rx.chakra.hstack(
                                python_icon,
                                spacing="2em",
                                height="100%",
                                width="50%",
                            ),
                            padding_bottom="2em",
                            width="100%",
                            spacing="2em",
                            align_items="left",
                        )
                    ),
                    rx.mobile_and_tablet(
                        rx.chakra.vstack(
                            battery_icon,
                            orm_icon,
                            python_icon,
                            padding_bottom="2em",
                            height="100%",
                            spacing="2em",
                        )
                    ),
                    padding_y="2em",
                ),
                padding_bottom="2em",
                align_items="left",
            )
        ),
        bg="rgba(247, 247, 250, 0.6);",
    )


deploy_icon = rx.chakra.hstack(
    rx.image(
        src="/landing_icons/deploy-icon.svg",
        height="4em",
        width="4em",
    ),
    rx.chakra.vstack(
        rx.chakra.text(
            "Deploy your app with a single command",
            font_size=styles.TEXT_FONT_SIZE,
            font_weight=styles.BOLD_WEIGHT,
        ),
        rx.chakra.text(
            "Autoconfigured CDN, HTTPS, SSL, and more to make sure your app is performant and secure.",
            color="#342E5C",
        ),
        rx.chakra.box(
            rx.link(
                rx.chakra.button(
                    "Deploy your app",
                    rx.chakra.icon(tag="arrow_forward"),
                    style=styles.BUTTON_LIGHT_NO_BACKGROUND,
                ),
                href=hosting.deploy_quick_start.path,
            )
        ),
        align_items="left",
        width="100%",
    ),
    style=boxstyles,
    align_items="left",
    spacing="1em",
    width="100%",
)

host_icon = rx.chakra.hstack(
    rx.image(
        src="/landing_icons/host-icon.svg",
        height="4em",
        width="4em",
    ),
    rx.chakra.vstack(
        rx.chakra.text(
            "Self-host your app",
            font_size=styles.TEXT_FONT_SIZE,
            font_weight=styles.BOLD_WEIGHT,
        ),
        rx.chakra.text(
            "Learn how to configure your own server and deploy your app on your own infrastructure. With Reflex you are not locked into a specific hosting provider.",
            color="#342E5C",
        ),
        rx.chakra.box(
            rx.link(
                rx.chakra.button(
                    "Self-host your app",
                    rx.chakra.icon(tag="arrow_forward"),
                    style=styles.BUTTON_LIGHT_NO_BACKGROUND,
                ),
                href=hosting.self_hosting.path,
            )
        ),
        align_items="left",
        width="100%",
    ),
    style=boxstyles,
    align_items="left",
    spacing="1em",
    width="100%",
)


def hosting():
    return rx.chakra.box(
        container(
            height="8em",
            width="100%",
            background="radial-gradient(55.39% 67.5% at 50% 100%, rgba(32, 17, 126, 0.1) 0%, rgba(255, 255, 255, 0) 100%)",
            opacity="0.4;",
            transform="matrix(1, 0, 0, -1, 0, 0);",
        ),
        container(
            rx.chakra.vstack(
                rx.chakra.box(
                    rx.chakra.text(
                        "[",
                        rx.chakra.span("Hosting", color="#342E5C", bg="#FAF8FB"),
                        "]",
                        color="#342E5C",
                        font_family=styles.MONO,
                    ),
                ),
                rx.heading(
                    "Deploy your app in seconds",
                    font_size=styles.H3_FONT_SIZE,
                    font_family=styles.MONO,
                ),
                rx.chakra.text(
                    "Simplify the process of deploying your app with Reflex.",
                    color="#342E5C",
                    max_width="50%",
                ),
                rx.chakra.hstack(
                    rx.desktop_only(
                        rx.chakra.vstack(
                            rx.chakra.hstack(
                                deploy_icon,
                                host_icon,
                                spacing="2em",
                                height="100%",
                            ),
                            padding_bottom="2em",
                            width="100%",
                            spacing="2em",
                        )
                    ),
                    rx.mobile_and_tablet(
                        rx.chakra.vstack(
                            deploy_icon,
                            host_icon,
                            padding_bottom="2em",
                            height="100%",
                            spacing="2em",
                        )
                    ),
                    padding_top="2em",
                    padding_bottom="2em",
                ),
                padding_y="2em",
                align_items="left",
            ),
            padding_bottom="2em",
        ),
        bg="rgba(247, 247, 250, 0.6);",
    )


def stat(number, icon, metric):
    """A statistic."""
    return rx.chakra.vstack(
        rx.heading(number, color="#DACEEE"),
        rx.chakra.hstack(
            rx.image(
                src=f"/landing_icons/stats_icons/{icon}.svg",
                height="1em",
            ),
            rx.chakra.text(
                metric,
                color="#82799E",
                text_align="center",
            ),
        ),
        padding_x="2em",
    )


def format_with_commas(number):
    return "{:,}+".format(number)


def gallery():
    return rx.center(
        container(
            rx.chakra.vstack(
                rx.center(
                    rx.chakra.text(
                        "Join the growing ",
                        rx.chakra.span(
                            "open-source ",
                            color="#DACEEE",
                        ),
                        "community of Reflex developers.",
                        font_family=styles.MONO,
                        font_size=styles.H2_FONT_SIZE,
                        font_weight=styles.BOLD_WEIGHT,
                        text_align="center",
                        color="white",
                    ),
                    width="55%",
                    padding_bottom="2em",
                    padding_top="6em",
                ),
                rx.desktop_only(
                    rx.flex(
                        rx.chakra.spacer(),
                        stat(
                            format_with_commas(constants.MONTHLY_USERS),
                            "project",
                            "Projects created per month",
                        ),
                        stat(
                            format_with_commas(constants.GITHUB_STARS),
                            "github",
                            "GitHub stars",
                        ),
                        stat(
                            format_with_commas(constants.DISCORD),
                            "discord",
                            "Discord members",
                        ),
                        rx.chakra.spacer(),
                        height="100%",
                        min_height="10em",
                        width="100%",
                        margin_x="2em",
                    ),
                ),
                rx.mobile_and_tablet(
                    rx.chakra.vstack(
                        rx.chakra.vstack(
                            rx.heading(
                                format_with_commas(constants.MONTHLY_USERS),
                                color="#DACEEE",
                            ),
                            rx.image(
                                src="/landing_icons/stats_icons/project.svg",
                                height="1em",
                            ),
                            rx.chakra.text(
                                "Projects created per month",
                                color="#82799E",
                                text_align="center",
                            ),
                        ),
                        rx.chakra.vstack(
                            rx.heading(
                                format_with_commas(constants.GITHUB_STARS),
                                color="#DACEEE",
                            ),
                            rx.image(
                                src="/landing_icons/stats_icons/github.svg",
                                height="1em",
                            ),
                            rx.chakra.text(
                                "GitHub stars", color="#82799E", text_align="center"
                            ),
                        ),
                        rx.chakra.vstack(
                            rx.heading(
                                format_with_commas(constants.DISCORD), color="#DACEEE"
                            ),
                            rx.image(
                                src="/landing_icons/stats_icons/discord.svg",
                                height="1em",
                            ),
                            rx.chakra.text(
                                "Discord members",
                                color="#82799E",
                                text_align="center",
                            ),
                        ),
                        height="100%",
                        min_height="10em",
                        width="100%",
                    ),
                ),
                padding="2em",
            ),
            width="100%",
        ),
        bg="#110F1F",
        width="100%",
    )


def prompt_sign():
    return rx.chakra.text(
        "$",
        color=styles.ACCENT_COLOR,
        font_family=styles.SANS,
        style={"userSelect": "none"},
    )


def installation():
    return rx.chakra.vstack(
        container(
            rx.flex(
                rx.center(
                    rx.chakra.vstack(
                        rx.heading(
                            "Get up and running in seconds!",
                            font_family=styles.MONO,
                            font_weight=styles.BOLD_WEIGHT,
                            font_size=styles.H3_FONT_SIZE,
                        ),
                        rx.chakra.box(
                            rx.chakra.text(
                                "Reflex requires Python 3.7+",
                            ),
                            color="#82799E",
                            font_family=styles.SANS,
                            padding_y=".5em",
                        ),
                        align_items="start",
                        min_width="10em",
                        margin_x="auto",
                        width="100%",
                    ),
                    min_width="10em",
                    width="100%",
                    mb=8,
                ),
                rx.chakra.vstack(
                    rx.chakra.text(
                        "Install our library to get started:",
                        font_family=styles.MONO,
                        padding_x="1em",
                        padding_top=".5em",
                    ),
                    rx.chakra.divider(),
                    rx.chakra.vstack(
                        rx.chakra.hstack(
                            rx.chakra.text("1", color="#494369"),
                            prompt_sign(),
                            rx.chakra.text(
                                "pip install reflex",
                                font_family=styles.MONO,
                                font_weight="500",
                            ),
                        ),
                        rx.chakra.hstack(
                            rx.chakra.text("2", color="#494369"),
                            prompt_sign(),
                            rx.chakra.text(
                                "reflex init",
                                font_family=styles.MONO,
                                font_weight="500",
                            ),
                        ),
                        rx.chakra.hstack(
                            rx.chakra.text("3", color="#494369"),
                            prompt_sign(),
                            rx.chakra.text(
                                "reflex run",
                                font_family=styles.MONO,
                                font_weight="500",
                            ),
                        ),
                        width="100%",
                        align_items="left",
                        padding_x="1em",
                    ),
                    rx.chakra.divider(),
                    rx.chakra.hstack(
                        rx.chakra.text(
                            "And you should see your first Reflex app!",
                        ),
                        rx.chakra.spacer(),
                        rx.link(
                            rx.chakra.button(
                                "View Docs",
                                style=styles.ACCENT_BUTTON,
                                padding_x="1em",
                            ),
                            href=getting_started.introduction.path,
                            style=styles.NAV_TEXT_STYLE,
                        ),
                        width="100%",
                        padding=4,
                    ),
                    height="100%",
                    border="1px solid #342E5C;",
                    box_shadow="0px 2px 3px rgba(3, 3, 11, 0.32), 0px 4px 8px rgba(3, 3, 11, 0.32), 0px 4px 10px -2px rgba(3, 3, 11, 0.52), inset 0px 1px 0px rgba(255, 255, 255, 0.16), inset 0px 20px 32px -10px rgba(86, 70, 237, 0.32);",
                    bg="radial-gradient(69.66% 165.73% at 70.23% 84.65%, rgba(86, 70, 237, 0.12) 0%, rgba(20, 18, 39, 0.12) 100%) /* warning: gradient uses a rotation that is not supported by CSS and may not behave as expected */, #110F1F;",
                    border_radius="8px;",
                    align_items="left",
                    width="100%",
                    min_width="25em",
                ),
                width="100%",
                flex_direction=["column", "column", "column", "column", "row"],
            ),
            width="100%",
        ),
        rx.chakra.box(
            height="5em",
            width="100%",
            background="radial-gradient(55.39% 67.5% at 50% 100%, rgba(188, 136, 255, 0.16) 0%, rgba(255, 255, 255, 0) 100%);",
            opacity="0.75;",
        ),
        font_family=styles.SANS,
        color="white",
        width="100%",
        bg="#110F1F",
        padding_top="2em",
        display=["none", "flex", "flex", "flex", "flex"],
    )


@webpage(path="/", title="Reflex: Web apps in Pure Python")
def index() -> rx.Component:
    """Get the main Reflex landing page."""
    return rx.chakra.box(
        landing(),
        container(rx.chakra.divider(border_color="#F4F3F6")),
        intro(),
        frontend(),
        backend(),
        hosting(),
        gallery(),
        installation(),
        width="100%",
        margin_top="80px"
    )