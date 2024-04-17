import reflex as rx
from pcweb import styles
from pcweb.templates import webpage

from .demos_on_landing_page.auth.auth import auth
from .demos_on_landing_page.forms.forms import forms
from .demos_on_landing_page.dashboard.dashboard import dashboard

from .landing_page_components.logo import landing


link_style = {
    "color": "black",
    "font_weight": styles.BOLD_WEIGHT,
    "_hover": {"color": rx.color("accent")},
}

button_style_landing= {
    "border_radius": "50px;",
    "border": "1px solid rgba(186, 199, 247, 0.12);",
    "background": "rgba(161, 157, 213, 0.03);",
    "backdrop_filter": "blur(2px);",
    "padding": "7px 12px;",
    "align_items": "center;",
    "color": "#848496;"
}


features_url = "https://github.com/reflex-dev/reflex/issues?q=is%3Aopen"
contribution_url = "https://github.com/reflex-dev/reflex/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22"
github_url = "https://github.com/reflex-dev/reflex"
bugs_url="https://github.com/reflex-dev/reflex/issues?q=is%3Aopen+is%3Aissue"


def container(*children, **kwargs):
    kwargs = {"max_width": "1440px", "padding_x": ["1em", "2em", "3em"], **kwargs}
    return rx.chakra.container(
        *children,
        **kwargs, 
    )

class DemoState(rx.State):

    demo = "Forms"

    def set_demo(self, demo):
        self.demo = demo

import openai
openai_client = openai.OpenAI()


class ImageGenState(rx.State):
    """The app state."""

    image_url = ""
    processing = False
    complete = False

    def get_image(self, form_data):
        """Get the image from the prompt."""
        prompt = form_data["prompt"]
        if prompt == "":
            return rx.window_alert("Prompt Empty")

        self.processing, self.complete = True, False
        yield
        response = openai_client.images.generate(
            prompt=prompt, n=1, size="512x512"
        )
        self.image_url = response.data[0].url
        self.processing, self.complete = False, True


def image_gen():
    return rx.theme(rx.hstack(
        rx.vstack(
            rx.hstack(
                rx.menu.root(
                    rx.menu.trigger(
                        rx.button(
                            rx.icon("ellipsis"),
                            variant="soft"
                        ),
                    ),
                    rx.menu.content(
                        rx.menu.item("Share", shortcut="⌘ E"),
                        rx.menu.item("Duplicate", shortcut="⌘ D"),
                        rx.menu.separator(),
                        rx.menu.item("Archive", shortcut="⌘ N"),
                        rx.menu.sub(
                            rx.menu.sub_trigger("More"),
                            rx.menu.sub_content(
                                rx.menu.item("Move to project…"),
                                rx.menu.item("Move to folder…"),
                                rx.menu.separator(),
                                rx.menu.item("Advanced options…"),
                            ),
                        ),
                        rx.menu.separator(),
                        rx.menu.item("Add to favorites"),
                        rx.menu.separator(),
                        rx.menu.item("Delete", shortcut="⌘ ⌫", color="red"),
                    ),
                ),
                width="100%", 
                justify_content="space-between",    
            ),
            rx.center(
                rx.form(
                    rx.cond(
                        ImageGenState.processing,
                        rx.text("Processing..."),
                        rx.image(src=ImageGenState.image_url, width="100%"),
                    ),
                    rx.vstack(
                        rx.input(placeholder="Enter description", name="prompt", width="100%"),
                        rx.button("Generate Image ->", width="100%", disabled=ImageGenState.processing),
                    ),
                    on_submit=ImageGenState.get_image,
                ),
                width="100%",
                height="100%",
            ),
            width="60%",
            height="100%",
            padding_top="1em",
        ),
        rx.vstack(
            "Settings",
            rx.radix.input.root(
                rx.input(placeholder="Seed"),
                width="100%"
            ),
            rx.select(["Model 1", "Model 2", "Model 3"], default_value="Model 1", width="100%"),
            rx.text("Temperature"),
            rx.slider(default_value=25, width="100%"),
            rx.text("Width"),
            rx.slider(default_value=50, width="100%"),
            rx.text("Height"),
            rx.slider(default_value=75, width="100%"),
            rx.text("Share Results"),
            rx.switch(),
            rx.button("Save", width="100%", variant="outline"),
            width="40%",
            height="100%",
            border_left="1px solid #2F2B37;",
            padding_left="1em",
            align_items="start",
            justify_content="center"
        ),
        padding_x="1em",
        height="100%",
    ),
    appearance="dark",
    )

def example_button(text):
    return rx.button(
    text,
    border_radius="8px;",
    border="1px solid rgba(186, 199, 247, 0.12);",
    background= rx.cond(
        DemoState.demo == text,
        "#282828",
        "rgba(161, 157, 213, 0.03);",
    ),
    backdrop_filter= "blur(2px);",
    on_click= lambda: DemoState.set_demo(text)
)


def demos():
    return rx.vstack(
        rx.vstack(
            rx.text(
                "Build web apps, faster.",
                font_size="54px;",
                text_align="left",
                color="#D6D6ED",
                font_weight="bold",
                line_height="1",
            ),
            rx.text("Create your whole app in a single language. Don't worry about writing APIs to connect your frontend and backend.", color="#6C6C81"),
            padding_y="2em",
        ),
        rx.hstack(
            example_button("Forms"),
            example_button("Dashboard"),
            example_button("Auth"),
            example_button("Image Generator"),
            rx.spacer(),
            rx.box(),
            align_items="left"
        ),
        rx.box(
            rx.match(
                DemoState.demo,
                ("Forms", forms()),
                ("Dashboard", dashboard()),
                ("Auth", auth()),
                ("Image Generator", image_gen()),
                forms()
            ),
            border_radius= "10px;",
            border= "1px solid #2F2B37;",
            background= "linear-gradient(218deg, #1D1B23 -35.66%, #131217 100.84%);",
            width="100%", 
        ),
        padding_bottom="4em",
        width="100%",
    )

def user_count_item(count, platform) -> rx.Component:
    return rx.flex(
        rx.text(f"{count}+", color="#E8E8F4", font_size="32px"),
        rx.text(platform, color="#6C6C81"),
        direction="column",
        align="center",
    )

def user_count_comp() -> rx.Component:
    return rx.center(
        rx.tablet_and_desktop(user_count_item(110, "Contributors")),
        rx.mobile_only(user_count_item(110, "Contributors")),
        rx.divider(size="4", orientation="vertical"),
        rx.tablet_and_desktop(user_count_item(5000, "Project created per month")),
        rx.mobile_only(user_count_item(5000, "Project")),
        rx.divider(size="4", orientation="vertical"),
        rx.tablet_and_desktop(user_count_item(3700, "Discord Members")),
        rx.mobile_only(user_count_item(3700, "On Discord")),
        spacing="5",
        padding="1em",
    )

def open_source_badge() -> rx.Component:
    return rx.button(
        rx.flex(
            rx.text(
                "Open Source",
                color="transparent",
                font_size="14px",
                font_style="normal",
                font_weight="400",
                line_height="normal",
                letter_spacing="-0.28px",
                background="linear-gradient(95deg, #B1A9FB 25.71%, #867BF1 83.81%);",
                background_clip="text",
                _webkit_background_clip="text",
            ),
            height="31px",
            padding="0px 10px",
            justify="center",
            align="center",
            gap="10px",
            border_radius="15px",
            border="1px solid #4435D4",
            background="linear-gradient(180deg, rgba(97, 81, 243, 0.20) 0%, rgba(86, 70, 237, 0.20) 100%);",
            box_shadow="0px 0px 4px -1px rgba(27, 21, 90, 0.40), 0px 3px 6px -3px rgba(34, 25, 121, 0.60);",
        ),
        background="transparent",
        on_click=rx.redirect(
            github_url,
            external=True,
        ),
        _hover={
            "cursor": "pointer",
        },
    )

def github_button() -> rx.Component:
    return rx.button(
        rx.flex(
            rx.image(src="/companies/light/github.svg", height="20px", width="20px"),
            rx.center(
                "Github",
                color="#FFFFFF",
                font_size="14px",
                font_style="normal",
                font_weight="400",
                line_height="normal",
                letter_spacing="-0.28px",
            ),
            rx.center(
                "15.7k",
                color="#6151F3",
                font_size="12px",
                font_style="normal",
                font_weight="400",
                line_height="normal",
                letter_spacing="-0.24px",
            ),
            spacing="2",
        ),

        position="relative",
        top="32px",
        right="-140px",
        z_index="999",
        padding="var(--Space-4, 16px);",
        align="center",
        width="151px",
        height="42px",
        border_radius="70px",
        border="1px solid #3C3646",
        background="linear-gradient(243deg, #16141A -74.32%, #222029 69.37%);",
        box_shadow="0px 0px 27px -4px rgba(0, 0, 0, 0.30);",
        on_click=rx.redirect(
            github_url,
            external=True,
        ),
        _hover={
            "cursor": "pointer",
        },
    )

def invite_message() -> rx.Component:
    return rx.box(
        rx.text(
            "Contribute to our open-source community.",
            color="#D6D6ED",
            font_size="38px",
            weight="bold",
            align="center",
            line_height="1",
        ),
        width="30em",
    )

def request_buttons() -> rx.Component:
    return rx.hstack(
        rx.button(
            "Bugs",
            color="#2BCEEA",
            weight="Medium",
            height="24px",
            width="138px",
            border="1px solid #2BCEEA",
            background_color="rgba(43, 206, 234, 0.25)",
            on_click=rx.redirect(
                bugs_url,
                external=True,
            ),
            _hover={
                "cursor": "pointer",
            },
        ),
        rx.button(
            "Good First Issues",
            color="#2BEA8E",
            weight="Medium",
            height="24px",
            border="1px solid #2BEA8E",
            background_color="rgba(43, 234, 142, 0.25)",
            on_click=rx.redirect(
                contribution_url,
                external=True,
            ),
            _hover={
                "cursor": "pointer",
            },
        ),
    )

def invite_card_comp() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.text(
                "Contribute to Reflex!", 
                color="#D6D6ED",
                weight="medium",
            ),
            request_buttons(),
            rx.text(
                "Start contributing today, checkout our Github for Details",
                color="#6C6C81",
                weight="medium",
            ),
            justify="start",
            direction="column",
            spacing="2",
        ),
        border_radius="10px",
        padding="1em",
        width="30em",
        border="1px solid #3C3646;",
        background="linear-gradient(218deg, #1D1B23 -35.66%, #131217 100.84%);",
        box_shadow= "0px 27px 44px -13px rgba(214, 214, 237, 0.10) inset, 0px 0px 27px -4px rgba(0, 0, 0, 0.30);",
    )

def stats() -> rx.Component:
    return rx.vstack(
        open_source_badge(),
        invite_message(),
        github_button(),
        invite_card_comp(),
        user_count_comp(),
        padding="2em",
        style={
            "@media screen and (max-width: 1024px)": {
                "transform": "scale(0.9)",
            },
            "@media screen and (max-width: 837px)": {
                "transform": "scale(0.85)",
            },
            "@media screen and (max-width: 768px)": {
                "transform": "scale(0.8)",
            },
            "@media screen and (max-width: 627px)": {
                "transform": "scale(0.75)",
            },
            "@media screen and (max-width: 480px)": {
                "transform": "scale(0.65)",
            },
        },
    )

def spacer_box_will_fix_later():
    return rx.box(height="60px")

def feature_button(name: str):
    return rx.button(
        name,
        color="848496",
        border_radius="50px;",
        border="1px solid rgba(186, 199, 247, 0.12);",
        background= "rgba(161, 157, 213, 0.03);",
        backdrop_filter= "blur(2px);",
        size="1"
    )

def feature_button_hstack(mobile=False):
    return rx.hstack(
        feature_button("Frontend"),
        feature_button("Backend"),
        feature_button("Hosting"),
        justify="start" if not mobile else "center",
        width="100%",
    )

def hero_section_text(mobile=False):
    return rx.vstack(
        rx.chakra.text(
            "Web apps in Pure Python.",
            text_align="left" if not mobile else "center",
            background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%)",
            font_size="54px" if not mobile else "30px",
            background_clip="text",
            font_weight="bold",
            line_height="1",
            
        ),
        rx.chakra.text(
            "Deploy with a single command.",
            text_align="left" if not mobile else "center",
            color="#6C6C81",
            font_size="54px" if not mobile else "30px",
            font_weight="bold",
            line_height="1",
            max_width="650px",
        ),
        align_items="center",
        
    )

def hero_section_buttons(mobile=False):
    return rx.hstack(
        rx.link(
            rx.button(
                "Get Started",
                color="#FFFFFF",
                background="linear-gradient(180deg, #6151F3 0%, #5646ED 100%)",
                box_shadow="0px 2px 9px -4px rgba(64, 51, 192, 0.70), 0px 0px 6px 2px rgba(255, 255, 255, 0.12) inset, 0px 0px 0px 1px rgba(255, 255, 255, 0.09) inset",
                size="4"
            ),
            href="/docs/getting-started",        
        ),
        rx.link(
            rx.button(
                "Get a demo",
                variant="ghost",
                border_radius="8px",
                border="2px solid rgba(186, 199, 247, 0.12)",
                background="rgba(161, 157, 213, 0.03)",
                backdrop_filter="blur(2px)",
                color="white",
                size="4"
            ),
            href="https://5dha7vttyp3.typeform.com/to/hQDMLKdX", 
            margin_left="1em",        
        ),
        padding_top="1em",
        align_items="center",
        justify="start" if not mobile else "center",
        width="100%",
    )

def hero_section() -> rx.Component:
    """Render the hero section of the landing page."""
    return rx.center(
        rx.chakra.vstack(
            landing(),
            rx.desktop_only(rx.vstack(
                feature_button_hstack(),
                hero_section_text(),
                hero_section_buttons(),
                padding_left="3em",
                spacing="3",
                align_items="left",
            )),
            rx.mobile_and_tablet(
                rx.vstack(
                    feature_button_hstack(mobile=True),
                    hero_section_text(mobile=True),
                    hero_section_buttons(mobile=True),
                    spacing="3",
                ),
            ),
            spacing="4",
            direction="column",
            align_items="left", # align_items=["center","center", "center","center", "left" ,"left"],
        ),
        width="100%",
    )


def top() -> rx.Component:
    return rx.container(
        hero_section(),
        padding_top="3em",
        padding_bottom="3em",
    )

@webpage(path="/", title="Reflex · Web apps in Pure Python")
def index() -> rx.Component:
    """Get the main Reflex landing page."""
    return rx.flex(
        top(),
        rx.container(
            demos(),
            stats(),
            padding_x="1em",
        ),
        width="100%",
        direction="column",
    )
