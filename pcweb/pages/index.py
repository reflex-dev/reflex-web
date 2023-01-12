import asyncio
from datetime import datetime

import pynecone as pc
from email_validator import EmailNotValidError, validate_email
from sqlmodel import Field

from pcweb import constants, styles
from pcweb.base_state import State
from pcweb.pages.docs.advanced_guide import wrapping_react
from pcweb.pages.docs.getting_started import (
    introduction,
    installation as installation_page,
)
from pcweb.pages.docs.styling.overview import styling_overview
from pcweb.pages.docs.database.overview import database_overview
from pcweb.pages.docs.hosting import deploy
from pcweb.pages.docs.gallery import gallery as gallery_page
from pcweb.pages.docs.library import library
from pcweb.templates import webpage


from pcweb.templates.docpage import (
    doclink,
    doccode,
)

background_style = {
    "background_size": "cover",
    "background_repeat": "no-repeat",
    "background_image": "bg.svg",
}

link_style = {
    "color": "black",
    "font_weight": styles.BOLD_WEIGHT,
    "_hover": {"color": styles.ACCENT_COLOR},
}


class Confetti(pc.Component):
    """Confetti component."""

    library = "react-confetti"
    tag = "ReactConfetti"


confetti = Confetti.create


class Waitlist(pc.Model, table=True):
    email: str
    date_created: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class IndexState(State):
    """Hold the state for the home page."""

    # Whether to show the call to action.
    show_c2a: bool = True

    # The waitlist email.
    email: str

    # Whether the user signed up for the waitlist.
    signed_up: bool = False

    # Whether to show the confetti.
    show_confetti: bool = False

    def close_c2a(self):
        """Close the call to action."""
        self.show_c2a = False

    def signup(self):
        """Sign the user up for the waitlist."""
        # Check if the email is valid.
        try:
            validation = validate_email(self.email, check_deliverability=True)
            self.email = validation.email
        except EmailNotValidError as e:
            # Alert the error message.
            return pc.window_alert(str(e))

        # Check if the user is already on the waitlist.
        with pc.session() as session:
            user = session.query(Waitlist).filter(Waitlist.email == self.email).first()
            if user is None:
                # Add the user to the waitlist.
                session.add(Waitlist(email=self.email))
                session.commit()

        self.signed_up = True
        return self.start_confetti

    def start_confetti(self):
        """Start the confetti."""
        self.show_confetti = True
        return self.stop_confetti

    async def stop_confetti(self):
        """Stop the confetti."""
        await asyncio.sleep(5)
        self.show_confetti = False


def container(*children, **kwargs):
    kwargs = {"max_width": "1440px", "padding_x": ["1em", "2em", "3em"], **kwargs}
    return pc.container(
        *children,
        **kwargs,
    )


def landing():
    return pc.container(
        pc.cond(
            IndexState.show_confetti,
            confetti(),
        ),
        pc.vstack(
            pc.box(
                pc.text(
                    "Frontend. Backend. Hosting.",
                    font_size=styles.HERO_FONT_SIZE,
                    font_weight=700,
                    font_family=styles.TEXT_FONT_FAMILY,
                ),
                pc.text(
                    "Pure Python.",
                    font_size=styles.HERO_FONT_SIZE,
                    font_weight=800,
                    font_family=styles.TEXT_FONT_FAMILY,
                    background_image="linear-gradient(271.68deg, #EE756A 25%, #756AEE 50%)",
                    background_clip="text",
                ),
                text_align="center",
                line_height="1.15",
            ),
            pc.container(
                "Build web apps in minutes. Deploy with a single command.",
                color="grey",
                font_size="1.1em",
                font_family=styles.TEXT_FONT_FAMILY,
                text_align="center",
            ),
            pc.cond(
                ~IndexState.signed_up,
                pc.wrap(
                    pc.input(
                        placeholder="Your email address",
                        on_blur=IndexState.set_email,
                        color="#676767",
                        type="email",
                        size="md",
                        border="2px solid #f4f4f4",
                        box_shadow="rgba(0, 0, 0, 0.08) 0px 4px 12px",
                        bg="rgba(0,0,0,0)",
                        _focus={
                            "border": f"2px solid {styles.ACCENT_COLOR}",
                        },
                    ),
                    pc.button(
                        "Stay Updated!",
                        on_click=IndexState.signup,
                        bg=styles.DOC_TEXT_COLOR,
                        box_shadow=styles.DOC_SHADOW_LIGHT,
                        color="white",
                        margin_top=0,
                        size="md",
                        _hover={
                            "box_shadow": "0 0 .12em .07em #EE756A, 0 0 .25em .11em #756AEE",
                        },
                    ),
                    justify="center",
                    should_wrap_children=True,
                    spacing="1em",
                ),
                pc.text(
                    pc.icon(
                        tag="CheckIcon",
                    ),
                    " You're on the waitlist!",
                    color=styles.ACCENT_COLOR,
                ),
            ),
            spacing="2em",
        ),
        margin_y="5em",
    )


def list_circle(text):
    return pc.flex(
        pc.text(text),
        width="2em",
        height="2em",
        border_radius="4em",
        bg="#756aee11",
        color="#756aee",
        align_items="center",
        justify_content="center",
        font_weight="800",
    )


def intro():
    return pc.box(
        container(
            pc.image(src="icon.svg", width="4em", height="4em", margin_bottom="1em"),
            pc.flex(
                pc.box(
                    pc.text(
                        "Build anything, faster.",
                        font_style="normal",
                        font_weight=800,
                        font_size="2em",
                        padding_bottom="0.5em",
                    ),
                    pc.text(
                        "Create your whole app in a single language. ",
                        "Don't worry about writing APIs to connect your frontend and backend. ",
                        color="#666",
                        margin_bottom="1.5em",
                    ),
                    pc.hstack(
                        list_circle("1"),
                        pc.text("Any use case.", font_weight="600"),
                        margin_bottom="0.5em",
                    ),
                    pc.text(
                        "With Pynecone you can build anything from internal tools and data apps to complex multi-page apps.",
                        color="#666",
                        margin_bottom=".5em",
                    ),
                    pc.text(
                        "This entire website is made in Pynecone!",
                        color=styles.ACCENT_COLOR_DARK,
                        font_style="normal",
                        margin_bottom="1.5em",
                    ),
                    pc.hstack(
                        list_circle("2"),
                        pc.text("It’s just Python.", font_weight="600"),
                        margin_bottom="0.5em",
                    ),
                    pc.text(
                        "The app state is just a class. ",
                        "State updates are methods in the class. ",
                        "And the UI is a reflection of the state. ",
                        color="#666",
                    ),
                    flex=1,
                    margin_right=[0, 0, "1em"],
                    margin_bottom=["2em", "2em", 0],
                ),
                pc.vstack(
                    pc.image(
                        src="code.png",
                        max_width="100%",
                        box_shadow=styles.DOC_SHADOW,
                        border_radius="1em",
                        margin=["1em", "1em", "1em", "1em", "0"],
                    ),
                    pc.text(
                        "A simple counter app in Pynecone. ",
                        doclink(
                            pc.span("See the full example →"),
                            href=introduction.path,
                        ),
                        font_size="14px",
                        color="#666",
                    ),
                    align_items="center",
                    margin_left=[0, 0, "1em"],
                    flex=1,
                ),
                flex_direction=["column", "column", "column", "row", "row"],
            ),
        ),
        background="linear-gradient(179.94deg, #FFFFFF 0.05%, #F8F7F8 113.47%)",
        padding_y="60px",
    )


def card(*args, **kwargs):
    kwargs.update(
        {
            "padding": ["1em", "2em"],
            "border": "1px solid #E3E3E3",
            "border_radius": "1em",
            "box_shadow": styles.DOC_SHADOW_LIGHT,
            "align_items": "left",
            "_hover": {"box_shadow": styles.DOC_SHADOW},
        }
    )
    return pc.vstack(*args, **kwargs)


import plotly.graph_objects as go

colors = [
    "#756AEE",
] * 4
colors[2] = "#EE756A"

fig = go.Figure(
    data=[
        go.Bar(
            x=["A", "B", "C", "D"],
            y=[20, 13, 23, 27],
            marker_color=colors,  # marker color can be a single color value or an iterable
        )
    ]
)

components_card = card(
    pc.text(
        "Hit the ground running with ",
        pc.span(
            "60+",
            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            background_clip="text",
        ),
        " built-in UI Components.",
        font_size=styles.H3_FONT_SIZE,
        font_weight=styles.BOLD_WEIGHT,
    ),
    pc.text(
        "Pynecone has all the components you need to get started.",
        color="#676767",
    ),
    doclink(
        "Check out the full library ->",
        href=library.path,
    ),
    background_image="graphbg.png",
    background_repeat="no-repeat",
    background_position="bottom",
    min_height="35em",
    height = "100%",
    width = "100%",
    margin_bottom="1em",
)

styling_card = card(
    pc.text(
        "Fully Customizable UI.",
        font_size=styles.H3_FONT_SIZE,
        font_weight=styles.BOLD_WEIGHT,
    ),
    pc.text(
        "Style your frontend with the full power of CSS.",
        color="#676767",
        margin_bottom="1em",
    ),
    doclink(
        "See styling docs ->",
        href=styling_overview.path,
    ),
    pc.center(
        pc.box(
            position="absolute",
            top="calc(50% - 4.5em)",
            left="calc(50% - 4.5em)",
            width="9em",
            height="9em",
            border_radius="50%",
            z_index="20",
            box_shadow="""
inset 0 0 0.75em #fff,
inset 0.625em 0 1.25em #756AEE,
inset -0.625em 0 1.25em #EE756A,
inset 0.625em 0 4.5em #756AEE,
inset -0.625em 0 4.5em #EE756A,
0 0 0.75em #fff,
-0.3125em 0 1.25em #756AEE,
0.3125em 0 1.25em #EE756A
""",
        ),
        doccode(
            """pc.box(
width= "9em",
height="9em",
border_radius= "50%",
box_shadow='''
inset 0 0 0.75em #fff,
inset 0.625em 0 1.25em #756AEE,
inset -0.625em 0 1.25em #EE756A,
inset 0.625em 0 4.5em #756AEE,
inset -0.625em 0 4.5em #EE756A,
0 0 0.75em #fff,
-0.3125em 0 1.25em #756AEE,
0.3125em 0 1.25em #EE756A
'''
)""",
            theme="dark",
        ),
        position="relative",
        width="100%",
    ),
    height="100%",
    margin_bottom="1em",
)

react_card = card(
    pc.text(
        "Easily wrap any React component.",
        font_size=styles.H3_FONT_SIZE,
        font_weight=styles.BOLD_WEIGHT,
    ),
    pc.text(
        "Leverage the expansive React ecosystem. ",
        color="#676767",
    ),
    pc.text(
        "Need a special component we dont support yet? ",
        "Wrap any React component with just a few lines of Python.",
        color="#676767",
    ),
    doclink(
        "Learn how ->",
        href=wrapping_react.path,
    ),
    background_image="react.svg",
    background_repeat="no-repeat",
    background_position="right bottom",
    background_size="10em",
    height="100%",
    margin_bottom="1em",
)

db_card = card(
    pc.text(
        "Connect to any SQL database.",
        font_size=styles.H3_FONT_SIZE,
        font_weight=styles.BOLD_WEIGHT,
    ),
    pc.vstack(
        pc.vstack(
            pc.text(
                "Use our built-in SQLite database or easily connect your own.",
                color="#676767",
                margin_bottom="1em",
            ),
            doccode(
                """config = pc.Config(
app_name="my_app",
db_uri="sqlite:///pynecone.db",
)""",
                theme="dark",
            ),
            align_items="start",
            width="100%",
        ),
        align_items="start",
    ),
    doclink("Check out the DB docs →", href=database_overview.path),
    height="100%",
    margin_bottom="1em",
)

deploy_card = card(
    pc.text(
        "Deploy your app in a single command.",
        font_size=styles.H3_FONT_SIZE,
        font_weight=styles.BOLD_WEIGHT,
    ),
    pc.text(
        "No more wasting time configuring infrastructure.",
        color="#676767",
    ),
    pc.text(
        "Zero-config set up with HTTPS, CDN,",
        " and everything you need to go to production.  ",
        color="#676767",
    ),
    doccode(
        """$ pc deploy
Deploying ...
Your App is live at: https://counter.pynecone.app
""",
        language="bash",
        theme="dark",
    ),
    doclink("See deploy docs →", href=deploy.path),
    height="100%",
    margin_bottom="1em",
)


def intro_grid():
    return pc.flex(
        container(
            pc.grid(
                pc.grid_item(
                    components_card,
                    col_span=2,
                ),
                pc.grid_item(
                    styling_card,
                    col_span=2,
                ),
                pc.grid_item(
                    react_card,
                    col_span=1,
                ),
                pc.grid_item(
                    db_card,
                    col_span=2,
                ),
                pc.grid_item(
                    deploy_card,
                    col_span=3,
                ),
                h="60em",
                template_rows="repeat(2, 1fr)",
                template_columns="repeat(5, 1fr)",
                width="100%",
                gap=4,
            ),
            min_height="60em",
            template_rows="repeat(2, 1fr)",
            template_columns="repeat(5, 1fr)",
            width="100%",
            gap=4,
        ),
        margin_y="60px",
    )


def intro_gridmobile():
    return pc.box(
        container(
            components_card,
            styling_card,
            db_card,
            deploy_card,
            width="100%",
            padding_y="1em",
        ),
    )


def gallery_card(gif, website):
    return pc.link(
        pc.box(
            pc.image(
                src=gif,
                height="18em",
            ),
            border_radius="1em",
            box_shadow=styles.DOC_SHADOW_DARK,
            overflow="hidden",
            _hover={
                "box_shadow": "0 0 .25em .11em #756AEE",
            },
        ),
        href=website,
    )


def gallery():
    return container(
        pc.vstack(
            pc.text(
                "Gallery", font_size=styles.H2_FONT_SIZE, font_weight=styles.BOLD_WEIGHT
            ),
            pc.text(
                "See what you can build with Pynecone. ",
                doclink("View gallery →", href=gallery_page.path),
                color="#676767",
            ),
            pc.center(
                pc.hstack(
                    gallery_card(
                        gif="/gallery/dalle.gif", website="https://dalle.pynecone.app"
                    ),
                    pc.box(
                        gallery_card(
                            gif="/gallery/nba.gif", website="https://nba.pynecone.app"
                        ),
                        display=["none", "none", "none", "block", "block"],
                    ),
                    pc.box(
                        gallery_card(
                            gif="/gallery/clock.gif",
                            website="https://clock.pynecone.app",
                        ),
                        display=["none", "none", "none", "none", "block"],
                    ),
                    spacing="1em",
                    margin_top="1em",
                ),
                width="100%",
            ),
            align_items="left",
            border="1px solid #E3E3E3",
            box_shadow=styles.DOC_SHADOW_LIGHT,
            border_radius="12px",
            width="100%",
            padding=["1em", "2em"],
        ),
        margin_top=["3em", "3em", "5em", "12em", "12em"],
        margin_bottom="2em",
    )


def prompt_sign():
    return pc.text(
        "$",
        color=styles.ACCENT_COLOR,
        font_size=styles.H3_FONT_SIZE,
        font_family=styles.TEXT_FONT_FAMILY,
        style={"userSelect": "none"},
    )


def view_docs_button():
    return pc.link(
        pc.button(
            "View Docs",
            font_weight="700",
            font_family=styles.TEXT_FONT_FAMILY,
            bg=styles.ACCENT_COLOR,
            color="white",
            padding="1.5em",
            style={
                "_hover": {
                    "background": "white",
                    "color": styles.ACCENT_COLOR,
                    "transform": "scale3d(1.1, 1.1, 1.1)",
                    "transition_duration": ".5s",
                },
            },
        ),
        style={
            "_hover": {},
        },
        href=installation_page.path,
    )


def installation():
    return pc.box(
        pc.vstack(
            pc.heading(
                "Get up and running in seconds!",
                font_weight=styles.BOLD_WEIGHT,
                font_size=styles.H2_FONT_SIZE,
            ),
            pc.box(
                pc.text(
                    "Pynecone requires Python 3.7+ and NodeJS 12+",
                    font_size=styles.H4_FONT_SIZE,
                ),
                pc.text(
                    "(Don't worry, you'll never have to write any Javascript)",
                    font_size=styles.H4_FONT_SIZE,
                ),
                color="rgba(255,255,255,.7)",
                font_family=styles.TEXT_FONT_FAMILY,
                padding_y="1em",
            ),
            pc.text(
                "Install our library to get started:",
                font_weight=styles.BOLD_WEIGHT,
                font_size=styles.H3_FONT_SIZE,
                font_family=styles.TEXT_FONT_FAMILY,
            ),
            pc.hstack(
                prompt_sign(),
                pc.text(
                    "pip install pynecone-io",
                    font_size=styles.H4_FONT_SIZE,
                    font_family=styles.CODE_FONT_FAMILY,
                    font_weight="500",
                ),
            ),
            pc.hstack(
                prompt_sign(),
                pc.text(
                    "pc init",
                    font_size=styles.H4_FONT_SIZE,
                    font_family=styles.CODE_FONT_FAMILY,
                    font_weight="500",
                ),
            ),
            pc.hstack(
                prompt_sign(),
                pc.text(
                    "pc run",
                    font_size=styles.H4_FONT_SIZE,
                    font_family=styles.CODE_FONT_FAMILY,
                    font_weight="500",
                ),
            ),
            pc.text(
                "And you should see your first Pynecone app!",
                font_size=styles.H4_FONT_SIZE,
                font_family=styles.TEXT_FONT_FAMILY,
                padding_top="1em",
            ),
            pc.text(
                "Check out our docs to learn more.",
                font_size=styles.H4_FONT_SIZE,
                font_family=styles.TEXT_FONT_FAMILY,
                padding_bottom="1em",
            ),
            view_docs_button(),
            align_items="start",
            max_width="38em",
            margin_x="auto",
        ),
        padding_x=styles.PADDING_X2,
        font_family=styles.TEXT_FONT_FAMILY,
        font_size="1.2em",
        padding_y="8em",
        color="white",
        bg="black",
    )


def c2a():
    return pc.box(
        pc.button_group(
            pc.button(
                pc.link(
                    pc.box(
                        "Star on GitHub",
                        pc.icon(
                            tag="StarIcon",
                            color="#eec600",
                            margin_bottom="0.3em",
                            margin_left="0.2em",
                        ),
                        width="100%",
                        height="100%",
                    ),
                    href=constants.GITHUB_URL,
                    _hover={},
                ),
                bg=styles.ACCENT_COLOR,
                color="white",
                border_color=styles.ACCENT_COLOR_DARK,
                _hover={"bg": styles.ACCENT_COLOR_DARK},
            ),
            pc.button(
                pc.icon(tag="CloseIcon", color="white", height=".5em", width=".5em"),
                on_click=IndexState.close_c2a,
                bg=styles.ACCENT_COLOR,
                color="white",
                _hover={"bg": styles.ACCENT_COLOR_DARK},
            ),
            opacity="0.95",
            backdrop_filter="blur(6px)",
            is_attached=True,
            variant="outline",
            box_shadow="xl",
        ),
        z_index="50",
        display="flex",
        justify_content="center",
        position="fixed",
        bottom="2em",
        left="0",
        right="0",
    )


@webpage(path="/")
def index() -> pc.Component:
    """Get the main Pynecone landing page."""
    return pc.box(
        landing(),
        intro(),
        pc.desktop_only(
            intro_grid(),
        ),
        pc.mobile_and_tablet(
            intro_gridmobile(),
        ),
        gallery(),
        installation(),
        pc.cond(
            IndexState.show_c2a,
            c2a(),
        ),
    )
