import reflex as rx
from pcweb import styles
from pcweb.templates import webpage
from reflex_chat import chat

from .demos_on_landing_page.auth.auth import auth
from .demos_on_landing_page.forms.forms import forms
from .demos_on_landing_page.dashboard.dashboard import dashboard

from .landing_page_components.logo import landing


link_style = {
    "color": "black",
    "font_weight": styles.BOLD_WEIGHT,
    "_hover": {"color": rx.color("accent")},
}

button_style_landing = {
    "border_radius": "50px;",
    "border": "1px solid rgba(186, 199, 247, 0.12);",
    "background": "rgba(161, 157, 213, 0.03);",
    "backdrop_filter": "blur(2px);",
    "padding": "7px 12px;",
    "align_items": "center;",
    "color": "#848496;",
}


features_url = "https://github.com/reflex-dev/reflex/issues?q=is%3Aopen"
contribution_url = "https://github.com/reflex-dev/reflex/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22"
github_url = "https://github.com/reflex-dev/reflex"
bugs_url = "https://github.com/reflex-dev/reflex/issues?q=is%3Aopen+is%3Aissue"


def container(*children, **kwargs):
    kwargs = {"max_width": "1440px", "padding_x": ["1em", "2em", "3em"], **kwargs}
    return rx.chakra.container(
        *children,
        **kwargs,
    )


class DemoState(rx.State):

    demo = "Image Generator"

    def set_demo(self, demo):
        self.demo = demo


try:
    import openai

    openai_client = openai.OpenAI()
except:
    openai_client = None


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
        response = openai_client.images.generate(prompt=prompt, n=1, size="512x512")
        self.image_url = response.data[0].url
        self.processing, self.complete = False, True


def config_button():
    return rx.menu.root(
        rx.menu.trigger(
            rx.button(rx.icon("ellipsis"), variant="soft"),
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
    )


def setting_section():
    return rx.vstack(
        rx.heading("Settings"),
        rx.radix.input.root(rx.input(placeholder="Seed"), width="100%"),
        rx.select(
            ["Model 1", "Model 2", "Model 3"], default_value="Model 1", width="100%"
        ),
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
        padding="1.25em",
        align_items="start",
        justify_content="center",
    )


def generator():
    return rx.form(
        rx.cond(
            ImageGenState.processing,
            rx.text("Processing..."),
            rx.image(src=ImageGenState.image_url, width="100%"),
        ),
        rx.vstack(
            rx.input(placeholder="Enter description", name="prompt", width="100%"),
            rx.button(
                "Generate Image ->", width="100%", disabled=ImageGenState.processing
            ),
        ),
        on_submit=ImageGenState.get_image,
    )


def image_gen():
    return rx.theme(
        rx.hstack(
            rx.flex(
                rx.hstack(
                    config_button(),
                    width="100%",
                    justify_content="right",
                ),
                rx.center(
                    generator(),
                    width="100%",
                    height="100%",
                ),
                direction="column",
                width="60%",
                height="24em",
                padding_top="0.5em",
            ),
            setting_section(),
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
        background=rx.cond(
            DemoState.demo == text,
            "#282828",
            "rgba(161, 157, 213, 0.03);",
        ),
        backdrop_filter="blur(2px);",
        on_click=lambda: DemoState.set_demo(text),
    )


def demos():
    return rx.vstack(
        rx.vstack(
            rx.chakra.text(
                "Build web apps, faster.",
                font_size=["24px", "30px", "44px", "44px", "44px", "44px"],
                text_align="left",
                color="#D6D6ED",
                font_weight="bold",
                line_height="1",
            ),
            rx.chakra.text(
                "Create your whole app in a single language. Don't worry about writing APIs to connect your frontend and backend.",
                color="#6C6C81",
                font_size=[".8em", "1em", "1.2em", "1.2em", "1.2em", "1.2em"],
                text_align="center",
            ),
            padding_y="2em",
        ),
        rx.hstack(
            example_button("Image Generator"),
            example_button("Forms"),
            example_button("Auth"),
            example_button("Dashboard"),
            rx.spacer(),
            rx.box(),
            align_items="left",
        ),
        rx.box(
            rx.match(
                DemoState.demo,
                ("Forms", forms()),
                ("Dashboard", dashboard()),
                ("Auth", auth()),
                ("Image Generator", image_gen()),
                image_gen(),
            ),
            border_radius="10px;",
            border="1px solid #2F2B37;",
            background="linear-gradient(218deg, #1D1B23 -35.66%, #131217 100.84%);",
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
        box_shadow="0px 27px 44px -13px rgba(214, 214, 237, 0.10) inset, 0px 0px 27px -4px rgba(0, 0, 0, 0.30);",
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
    return rx.badge(
        rx.text(name, font_size="12px", weight="bold"),
        size="2",
        variant="outline",
        color_scheme="gray",
    )


def feature_button_hstack(mobile=False):
    return rx.hstack(
        feature_button("Frontend"),
        feature_button("Backend"),
        feature_button("Hosting"),
        justify="center" if not mobile else "center",
        width="100%",
        spacing="3",
        padding="0.75em 0em",
    )


def hero_section_text(title: str):
    return rx.chakra.heading(
        title,
        background="linear-gradient(to top right, #d6d6eb, #6b6b7f)",
        font_size=["22px", "28px", "38px", "46px", "50px"],
        background_clip="text",
        font_weight="bold",
        transition="all 550ms ease",
        text_align="center",
    )


def hero_section_buttons(title: str, type: str, path: str):
    return rx.button(
        rx.link(
            rx.text(
                title,
                color="rgba(255, 255, 255, 0.81)",
            ),
            href=path,
            text_decoration="none",
        ),
        size="3",
        radius="small",
        variant=type,
        cursor="pointer",
    )


def opacity():
    return {
        "position": "relative",
        f"@keyframes opacity": {
            "0%": {"opacity": "0"},
            "100%": {"opacity": "1"},
        },
        "animation": "opacity 2s",
    }


def fade_in_border():
    return rx.box(
        width="100%",
        border="solid",
        border_image="linear-gradient(to right, rgba(0, 0, 0, 0), rgb(49, 49, 49),  rgba(0, 0, 0, 0)) 2 / 4px",
        border_image_width="0px 0px 2px 0px",
    )


def hero_section() -> rx.Component:
    """Render the hero section of the landing page."""
    return rx.vstack(
        rx.box(
            landing(),
            width="100%",
            display="flex",
            justify_content="center",
            align_items="start",
            **opacity(),
        ),
        rx.vstack(
            hero_section_text("Build web apps in pure Python"),
            hero_section_text("Deploy with a single command"),
            width="100%",
            display="flex",
            justify_content="center",
            align_items="center",
        ),
        rx.spacer(),
        rx.hstack(
            hero_section_buttons("Get Started", "classic", "/docs/getting-started"),
            hero_section_buttons(
                "See Demo", "surface", "https://5dha7vttyp3.typeform.com/to/hQDMLKdX"
            ),
            width="100%",
            justify_content="center",
            spacing="4",
            padding="2em 0em",
        ),
        *[rx.spacer() for _ in range(15)],
        fade_in_border(),
        rx.hstack(
            rx.text(
                "This entire website is built using Reflex!",
                color="rgba(255, 255, 255, 0.71)",
                weight="bold",
            ),
            width="100%",
            padding="1em 0em",
            display="flex",
            justify_content="center",
            align_items="center",
            spacing="0",
        ),
        fade_in_border(),
        *[rx.spacer() for _ in range(15)],
        width="100%",
    )


def top() -> rx.Component:
    return rx.box(
        hero_section(),
        width="100%",
    )


@webpage(path="/", title="Reflex · Web Apps in Pure Python")
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
