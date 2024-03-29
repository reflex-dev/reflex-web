import reflex as rx
from pcweb import constants, styles
from pcweb.components.logo import logo
from pcweb.pages.docs import getting_started
from pcweb.pages.docs.gallery import gallery
from pcweb.pages.docs.library import library
from pcweb.pages.index import index

import asyncio
import json
import os
from datetime import datetime
import httpx
from email_validator import EmailNotValidError, validate_email
from sqlmodel import Field

footer_item_style = {
    "font_family": styles.SANS,
    "font_weight": "500",
    "_hover": {"color": "#82799E"},
    "color": "#AA9EC3",
}

footer_style = {
    "box_shadow": "medium-lg",
    "border_top": "0.1em solid #82799E",
    "vertical_align": "bottom",
    "padding_top": "4em",
    "padding_bottom": "2em",
    "padding_x": styles.PADDING_X2,
    "bg": "#110F1F",
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


def footer(style=footer_style):
    from pcweb.pages.blog import blg
    from pcweb.pages.changelog import changelog
    from pcweb.pages.faq import faq

    return rx.box(
        rx.vstack(
            rx.cond(
                IndexState.show_confetti,
                confetti(),
            ),
            rx.hstack(
                rx.desktop_only(
                    rx.vstack(
                        logo(
                            width=["5em", "6em", "7em"],
                        ),
                        align_items="left",
                    )
                ),
                rx.vstack(
                    rx.text("Site", color="#DACEEE"),
                    rx.link("Home", href=index.path, style=footer_item_style),
                    rx.link("Gallery", href=gallery.path, style=footer_item_style),
                    rx.link("Blog", href=blg.path, style=footer_item_style),
                    rx.link(
                        "Changelog",
                        href=changelog.path,
                        style=footer_item_style,
                    ),
                    align_items="start",
                ),
                rx.vstack(
                    rx.text("Documentation", color="#DACEEE"),
                    rx.link(
                        "Introduction",
                        href=getting_started.introduction.path,
                        style=footer_item_style,
                    ),
                    rx.link(
                        "Installation",
                        href=getting_started.installation.path,
                        style=footer_item_style,
                    ),
                    rx.link(
                        "Components",
                        href=library.path,
                        style=footer_item_style,
                    ),
                    align_items="start",
                ),
                rx.vstack(
                    rx.text("Resources", color="#DACEEE"),
                    rx.link(
                        "FAQ",
                        href=faq.path,
                        style=footer_item_style,
                    ),
                    rx.link(
                        "Roadmap",
                        href=constants.ROADMAP_URL,
                        style=footer_item_style,
                    ),
                    rx.link(
                        "Forum",
                        href=constants.GITHUB_DISCUSSIONS_URL,
                        style=footer_item_style,
                    ),
                    align_items="start",
                ),
                rx.tablet_and_desktop(
                rx.vstack(
                    rx.text("Subscribe to newsletter", color="#DACEEE"),
                    rx.chakra.input_group(
                        rx.chakra.input_right_element(
                                rx.chakra.button(
                                "->",
                                color="#FFF",
                                on_click=IndexState.signup,
                                background="#82799E",
                                border_top_left_radius="0px",
                                border_bottom_left_radius="0px",
                                _hover={"background": "#82799E"},
                                )           
                        ),
                        rx.chakra.input(
                            placeholder="Email...",
                            on_blur=IndexState.set_email,
                            color="#82799E",
                            type="email",
                            border="1px solid #82799E",
                            _focus={"border": "1px solid #82799E"},
                            border_radius="8px",
                        ),
                    ),
                    align_items="left",
                )
                ),
                justify="between",
                color=styles.LIGHT_TEXT_COLOR,
                align_items="top",
                padding_bottom="3em",
                min_width="100%",
            ),
            rx.hstack(
                rx.text(
                    "Copyright © 2024 Pynecone, Inc.",
                    color="#86848D"
                ),
                rx.hstack(
                    rx.link(
                        rx.image(src="/companies/light/github.svg", alt="A link to Reflex's Github", height="1.75em"),
                        href=constants.GITHUB_URL,
                    ),
                    rx.link(
                        rx.image(src="/companies/light/linkedin.svg", alt="A link to Reflex's Linkedin", height="1.75em"),
                        href=constants.LINKEDIN_URL,
                    ),
                    rx.link(
                        rx.image(src="/companies/light/twitter.svg", alt="A link to Reflex's Twitter", height="1.75em"),
                        href=constants.TWITTER_URL,
                    ),
                    rx.link(
                        rx.image(src="/companies/light/discord.svg", alt="A link to Reflex's Discord", height="1.75em"),
                        href=constants.DISCORD_URL,
                    ),
                    gap="1em",
                ),
                justify="between",
                color=styles.LIGHT_TEXT_COLOR,
                padding_bottom="2em",
                min_width="100%",
            ),
        ),
        **style,
    )
