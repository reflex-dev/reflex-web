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
                        placeholder="Your email address...",
                        on_blur=IndexState.set_email,
                        color="#676767",
                        type="email",
                        size="md",
                        border="2px solid #f4f4f4",
                        box_shadow="rgba(0, 0, 0, 0.08) 0px 4px 12px",
                        bg="rgba(255,255,255,.5)",
                        _focus={
                            "border": f"2px solid {styles.ACCENT_COLOR}",
                        },
                    ),
                    pc.button(
                        "Join Hosting Waitlist",
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
                        tag="check",
                    ),
                    " You're on the waitlist!",
                    color=styles.ACCENT_COLOR,
                ),
            ),
            spacing="2em",
        ),
        padding_y="10em",
        width = "100%",
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
                        font_weight="bold",
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
        background="linear-gradient(179.94deg, #FFFFFF 0.05%, #F8F8F8 113.47%)",
        padding_top="30px",
        padding_bottom="80px",
    )

boxstyles = {
    "background": "white",
    "border": "1px solid #e5e5e5",
    "border_radius":"1em",
    "padding": "1em",
    "box_shadow": """
    rgba(17, 7, 53, 0.05) 0px 51px 78px 0px, rgba(17, 7, 53, 0.035) 0px 21.3066px 35.4944px 0px, rgba(17, 7, 53, 0.03) 0px 11.3915px 18.9418px 0px, rgba(17, 7, 53, 0.024) 0px 6.38599px 9.8801px 0px, rgba(17, 7, 53, 0.02) 0px 3.39155px 4.58665px 0px, rgba(17, 7, 53, 0.016) 0px 1.4113px 1.55262px 0px, rgba(41, 56, 78, 0.05) 0px 1px 0px 0px inset
    """,
    "height": "100%",
    "align_items":"left",
    "width": "100%",  
    "min_height":"25em",
    "padding": "2em",
    "bg": "rgba(248, 248, 248, .75)",
    "_hover": {
        "box_shadow": """
        rgba(23, 6, 100, 0.035) 0px 24px 22px 0px, rgba(23, 6, 100, 0.055) 0px 8.5846px 8.03036px 0px, rgba(23, 6, 100, 0.067) 0px 4.77692px 3.89859px 0px, rgba(23, 6, 100, 0.082) 0px 2.63479px 1.91116px 0px, rgba(23, 6, 100, 0.12) 0px 1.15891px 0.755676px 0px
        """,
    }
}

compbox = pc.vstack(
                    pc.image(
                        src="/icons/apps-add.svg",
                        height="2em",
                        width="2em",
                    ),
                    pc.text(
                        "Hit the ground running with ",
                        pc.span(
                            "60+",
                            background_image="linear-gradient(90deg,#6b63f6,#b563f6)",
                            background_clip="text",
                        ),
                        " built-in UI Components.",
                        font_size=styles.H2_FONT_SIZE,
                        font_weight=styles.BOLD_WEIGHT,
                        ),
                   pc.text(
                        "Pynecone comes with a large library of UI components ranging from simple buttons to complex graphs and tables.",
                        color="#676767",
                   ),
                    doclink(
                            "Check out the full library ->",
                            href=library.path,
                    ),
                    style=boxstyles,
                    align_items="left",
                    spacing = "1em",
                    width = "100%",
                )

reactbox = pc.vstack(
                    pc.image(
                        src="/icons/code-compare.svg",
                        height="2em",
                        width="2em",
                    ),
                    pc.text(
                        "Custom Components",
                        font_size=styles.H2_FONT_SIZE,
                        font_weight=styles.BOLD_WEIGHT,
                        ),
                   pc.text(
                       "Create your own components in a few lines of code. Simply wrap the React component of your choice.",
                        color="#676767",
                   ),
                    doclink(
                            "Wrapping React guide ->",
                            href="/docs/advanced-guide/wrapping-react",
                    ),
                    style=boxstyles,
                    align_items="left",
                    spacing = "1em",
                    background_image="react.svg",
                    background_repeat="no-repeat",
                    background_position="right bottom",
                    background_size="10em",
                )

stylebox = pc.vstack(
                    pc.image(
                        src="/icons/settings-sliders.svg",
                        height="2em",
                        width="2em",
                    ),
                    pc.text(
                        "Completely customizable.",
                        font_size=styles.H2_FONT_SIZE,
                        font_weight=styles.BOLD_WEIGHT,
                        ),
                   pc.text(
                        "All Pynecone components are fully customizable. Change the colors, fonts, and styles to match your project.",
                        color="#676767",
                   ),
                    doclink(
                            "Styling guide ->",
                            href="/docs/styling/overview",
                    ),
                    background_image="icons/api.svg",
                    background_repeat="no-repeat",
                    background_position="140% 135%",
                    background_size="15em",
                    style=boxstyles,
                    align_items="left",
                    spacing = "1em",
                )

powerful = pc.vstack(
                pc.image(
                        src="/icons/power.svg",
                        height="2em",
                        width="2em",
                ),
                pc.text(
                    "Now everyone can work across the ",
                    pc.span(
                            "full-stack",
                            background_image="linear-gradient(90deg,#6b63f6,#b563f6)",
                            background_clip="text",
                    ),
                    ".",
                    font_size=styles.H2_FONT_SIZE,
                    font_weight=styles.BOLD_WEIGHT,
                ),
                    pc.text(
                        "With Pynecone every engineer can work across the whole stack allowing for a more efficient and productive workflow.",
                        color="#676767",
                    ),
                    margin_bottom="1em",
                    style=boxstyles
                )

def frontend():
    return pc.box(container(pc.vstack(
       pc.center(
            "1",
            background_image = "linear-gradient(70deg,#6b63f6,#b563f6)",
            font_size = "2em",
            font_weight = "bold",
            color = "white",
            height = "2em",
            width = "2em",
            border_radius = "50%",
            box_shadow = """0 0 9px 6px rgba(255,255,255, .5), 0 0 6px 4px rgba(107,99,246, .5)""",
       ),
       pc.heading(
            "Frontend",
            background_image="linear-gradient(70deg,#6b63f6,#b563f6)",
            background_clip="text",
       ),
       pc.heading(
            "Write your entire app in Python.",
       ),
        pc.center(
            "No more switching between languages and frameworks. Use one language for your whole stack.",
            color="#676767",
        ),
        pc.hstack(
            pc.desktop_only(
                pc.vstack(
                    pc.hstack(
                        compbox,
                        stylebox,
                        spacing = "2em",
                        height = "100%",
                    ),
                    pc.hstack(
                        reactbox,
                        powerful,
                        height = "100%",
                        spacing = "2em",
                    ),
                    pc.icon(tag="chevron_down", height="3em", width="3em", color=styles.LIGHT_TEXT_COLOR),
                    width = "100%",
                    spacing = "2em", 
                )
            ),
            pc.mobile_and_tablet(
                pc.vstack(
                        compbox,
                        stylebox,
                        reactbox,
                        powerful,
                        pc.icon(tag="chevron_down", height="3em", width="3em", color=styles.LIGHT_TEXT_COLOR),
                        height = "100%",
                        spacing = "2em",
                )
            ),
            padding_y = "2em",
        ),
        margin_y = "5em",
        background= "radial-gradient(rgba(181, 99, 246, .12) 0, rgba(248, 248, 248, .1), #FFFFFF 100%)",
        padding_y = "2em",
    )))

ecosystem = pc.box(
                    pc.text(
                    "Seamlessly integrate with any Python library.",
                    font_size=styles.H2_FONT_SIZE,
                    font_weight=styles.BOLD_WEIGHT,
                ),
                    pc.text(
                        "",
                        color="#676767",
                    ),
                    pc.text(
                        "Never get locked into a framework doesn't support your existing tech stack. ",
                        color="#676767",
                    ),
                    margin_bottom="1em",
                    style=boxstyles,
                    min_height="20-em",
                    background_image=["none","none","none", "icons/python.svg"],
                    background_repeat="no-repeat",
                    background_position="95% 80%",
                    background_size="7em",
                )

batteries_included = pc.box(pc.vstack(
                pc.image(
                        src="/icons/battery-bolt.svg",
                        height="2em",
                        width="2em",
                ),
                pc.text(
                    "Batteries included.",
                    font_size=styles.H2_FONT_SIZE,
                    font_weight=styles.BOLD_WEIGHT,
                ),
                    pc.text(
                        "Skip the boilerplate and get started faster. ",
                        "Pynecone integrates the frontend and backend so there is no need to write API endpoints.",
                        color="#676767",
                    ),
                    doclink(
                        "Learn about Pynecone's State ->",
                        href="/docs/state/overview",
                    ),
                    margin_bottom="1em",
                    style=boxstyles,
                    min_height="20em",
                ))

database = pc.box(pc.vstack(
                pc.image(
                        src="/icons/database.svg",
                        height="2em",
                        width="2em",
                ),
                pc.text(
                    "Built in database ORM.",
                    font_size=styles.H2_FONT_SIZE,
                    font_weight=styles.BOLD_WEIGHT,
                ),
                    pc.text(
                        "Integrate with existing databases with a single line of code. ",
                        "Or use our built in SQLite database.",
                        color="#676767",
                    ),
                    doclink(
                        "Database docs ->",
                        href="/docs/database/overview",
                    ),
                    margin_bottom="1em",
                    style=boxstyles,
                    min_height="20em",
                ), width = "100%"
                )


def backend():
    return pc.box(container(pc.vstack(
       pc.center(
            "2",
            background_image = "linear-gradient(75deg,#b563f6, #f663ee)",
            font_size = "2em",
            font_weight = "bold",
            color = "white",
            height = "2em",
            width = "2em",
            border_radius = "50%",
            box_shadow = """0 0 9px 6px rgba(255,255,255, .5), 0 0 6px 4px rgba(181, 99, 246, .5)""",

       ),
       pc.heading(
            "Backend",
            background_image="linear-gradient(75deg,#b563f6, #f663ee)",
            background_clip="text",
       ),
       pc.heading(
            "Skip the boilerplate and get started faster. ",
       ),
        pc.center(
            "Pynecone comes with a powerful backend built with FastAPI and SQLAlchemy.",
            color="#676767",
        ),
        pc.hstack(
            pc.desktop_only(
                pc.vstack(
                    pc.hstack(
                        batteries_included,
                        database,
                        spacing = "2em",
                        height = "100%",
                    ),
                    ecosystem,
                    pc.icon(tag="chevron_down", height="3em", width="3em", color=styles.LIGHT_TEXT_COLOR),
                    width = "100%",
                    spacing = "2em",
                )
            ),
            pc.mobile_and_tablet(
                pc.vstack(
                    batteries_included,
                    database,
                    ecosystem,
                    pc.icon(tag="chevron_down", height="3em", width="3em", color=styles.LIGHT_TEXT_COLOR),
                    spacing = "2em",
                    height = "100%",
                    width = "100%",
                )
            ),
            padding_y = "2em",
        ),
        margin_y = "5em",
        background= "radial-gradient(rgba(246, 99, 238, .15) 0, rgba(255, 255, 255, .1), #f8f8f8 100%)",
        padding_y = "2em",
    )),
    bg = "#f8f8f8",
    border = "1px solid #e5e5e5",
    )

hosting_service = pc.box(pc.vstack(
                pc.image(
                        src="/icons/globe.svg",
                        height="2em",
                        width="2em",
                ),
                pc.text(
                    "Deploy your app with a single command.",
                    font_size=styles.H2_FONT_SIZE,
                    font_weight=styles.BOLD_WEIGHT,
                ),
                    pc.text(
                        "Autoconfigured CDN, HTTPS, SSL, and more to make sure your app is preformant and secure.",
                        color="#676767",
                    ),
                    doclink(
                        "Deploy your app ->",
                        href="/docs/hosting/deploy",
                    ),
                    background_image="icons/globelight.svg",
                    background_repeat="no-repeat",
                    background_position="135% 150%",
                    background_size="15em",
                    margin_bottom="1em",
                    style=boxstyles
                ), width = "100%",)

self_host = pc.box(pc.vstack(
                pc.image(
                        src="/icons/laptop-code.svg",
                        height="2em",
                        width="2em",
                ),
                pc.text(
                    "Self-host your app.",
                    font_size=styles.H2_FONT_SIZE,
                    font_weight=styles.BOLD_WEIGHT,
                ),
                    pc.text(
                        "Learn how to configure your own server and deploy your app on your own infrastructure. ",
                        "With Pynecone you are not locked into a specific hosting provider.", 
                        color="#676767",
                    ),
                    doclink(
                        "Self-host your app ->",
                        href="/docs/hosting/self-hosting",
                    ),
                    background_image="icons/laptop-codelight.svg",
                    background_repeat="no-repeat",
                    background_position="130% 130%",
                    background_size="15em",
                    margin_bottom="1em",
                    style=boxstyles
                ), width = "100%")

def hosting():
    return pc.box(container(pc.vstack(
       pc.center(
            "3",
            background_image = "linear-gradient(75deg,#f55d55, #f6b563)",
            font_size = "2em",
            font_weight = "bold",
            color = "white",
            height = "2em",
            width = "2em",
            border_radius = "50%",
            box_shadow = """0 0 9px 6px rgba(255,255,255, .5), 0 0 6px 4px rgba(245, 93, 85, .5)""",

       ),
       pc.heading(
            "Hosting",
            background_image="linear-gradient(75deg,#f55d55, #f6b563)",
            background_clip="text",
       ),
       pc.heading(
            "Deploy your app in seconds.",
       ),
        pc.center(
            "Simplify the process of deploying your app with Pynecone.",
            color="#676767",
        ),
        pc.desktop_only(
            pc.hstack(
                    hosting_service,
                    self_host,
                    spacing = "2em",
                    height = "100%",
                    margin = "2em",
            )
        ),
        pc.mobile_and_tablet(
            pc.vstack(
                    hosting_service,
                    self_host,
                    spacing = "2em",
                    height = "100%",
                    padding_y = "2em"
            )
        ),
        margin_y = "5em",
        background= "radial-gradient(rgba(245, 93, 85, .15) 0, rgba(248, 248, 248, .1), #FFFFFF 100%)",
        padding_y = "2em",
    )))

def gallery():
    return pc.center(
            container(
                pc.vstack(
                pc.center(
                   pc.text(
                        "Join the growing ",
                        pc.span(
                            "open-source ",
                            background_image="linear-gradient(90deg,#f55d55, #f6b563)",
                            background_clip="text",
                        ),
                        "community of Pynecone developers.",
                        font_size=styles.H2_FONT_SIZE,
                        font_weight=styles.BOLD_WEIGHT,
                        text_align="center",
                        color="white"
                    ),
                    width = "100%",
                ),
                pc.desktop_only(
                pc.flex(
                pc.spacer(),
                pc.vstack(
                    pc.heading("3000+"),
                    pc.text("Projects created per month", text_align="center"),
                    margin = "1em",
                    padding = "1em",
                    min_height = "9em",
                    align_items = "center",
                    bg = "rgba(29,33,37, 1)",
                    width = "30%",
                    height = "100%",
                    color= "white",
                    border_radius= "1em",
                    border = f"2px dashed rgba(255,255,255,.5)",
                    _hover = {
                        "border": f"2px solid #f55d55",
                    },
                ),
                pc.vstack(
                    pc.heading("5600+"),
                    pc.text("GitHub stars", text_align="center"),
                    min_height = "9em",
                    height = "100%",
                    border = f"2px dashed rgba(255,255,255,.5)",
                    margin = "1em",
                    color= "white",
                    padding = "1em",
                    width = "30%",
                    bg = "rgba(29,33,37, 1)",
                    border_radius= "1em",
                    _hover = {
                        "border": f"2px solid #f6b563",
                    },
                ),
                pc.vstack(
                    pc.heading("600+"),
                    pc.text("Discord community members", text_align="center"),
                    min_height = "9em",
                    height = "100%",
                    border = f"2px dashed rgba(255,255,255,.5)",
                    margin = "1em",
                    padding = "1em",
                    color= "white",
                    width = "30%",
                    align_items = "center",
                    bg = "rgba(29,33,37, 1)",
                    border_radius= "1em",
                    _hover = {
                        "border": f"2px solid #f55d55", 
                    },
                ),
                pc.spacer(),
                height = "100%",
                min_height = "10em",
                width = "100%",
                margin_x = "2em",
                ),
                ),
                pc.mobile_and_tablet(
                pc.vstack(
                pc.vstack(
                    pc.heading("3000+"),
                    pc.text("Projects created per month", text_align="center"),
                    margin = "1em",
                    padding = "1em",
                    min_height = "9em",
                    align_items = "center",
                    bg = "rgba(29,33,37, 1)",
                    height = "100%",
                    width = "100%",
                    color= "white",
                    border_radius= "1em",
                    border = f"2px dashed rgba(255,255,255,.5)",
                    _hover = {
                        "border": f"2px solid #f55d55",
                    },
                ),
                pc.vstack(
                    pc.heading("5600+"),
                    pc.text("GitHub stars", text_align="center"),
                    min_height = "9em",
                    height = "100%",
                    border = f"2px dashed rgba(255,255,255,.5)",
                    margin = "1em",
                    width = "100%",
                    color= "white",
                    padding = "1em",
                    bg = "rgba(29,33,37, 1)",
                    border_radius= "1em",
                    _hover = {
                        "border": f"2px solid #f6b563",
                    },
                ),
                pc.vstack(
                    pc.heading("600+"),
                    pc.text("Discord community members", text_align="center"),
                    min_height = "9em",
                    height = "100%",
                    border = f"2px dashed rgba(255,255,255,.5)",
                    margin = "1em",
                    padding = "1em",
                    width = "100%",
                    color= "white",
                    align_items = "center",
                    bg = "rgba(29,33,37, 1)",
                    border_radius= "1em",
                    _hover = {
                        "border": f"2px solid #f55d55", 
                    },
                ),
                height = "100%",
                min_height = "10em",
                width = "100%",
                ),
                ),
                box_shadow=styles.DOC_SHADOW,
                bg = "black",
                border_radius = "1em",
                border = f"2px solid #e5e5e5",
                padding="2em",
            ),
            width = "100%"
        ),
        bg = "linear-gradient(#f8f8f8, #ffffff)",
        width = "100%",
        border = "1px solid #e5e5e5",
        padding_y=["6em", "6em", "10em", "12em", "12em"],
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
                    "pip install pynecone",
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
                            tag="star",
                            color="#eec600",
                            margin_left="0.2em",
                            margin_bottom="0.2em",
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
                pc.icon(tag="close", color="white", height=".5em", width=".5em"),
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
        frontend(),
        backend(),
        hosting(),
        gallery(),
        installation(),
        pc.cond(
            IndexState.show_c2a,
            c2a(),
        ),
        background_image="/grid.png",
        background_repeat="no-repeat",
        background_position="top",
        width = "100%",
    )
