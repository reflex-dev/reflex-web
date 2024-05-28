import reflex as rx
from ..style import demo_height

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
        response = openai_client.images.generate(
            prompt=prompt, n=1, size="512x512"
        )
        self.image_url = response.data[0].url
        self.processing, self.complete = False, True

def config_button():
    return rx.menu.root(
        rx.menu.trigger(
            rx.button(
                rx.icon("ellipsis"),
                variant="soft",
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
    )

def setting_section():
    return rx.vstack(
        rx.heading("Settings"),
        rx.input(placeholder="Seed", width="100%"),
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
        padding="1.25em",
        align_items="start",
        justify_content="center",
        spacing="2",
        display=["none", "none", "flex", "flex", "flex", "flex"],
    )

def content():
    return rx.flex(
        rx.hstack(
            config_button(),
            width="100%", 
            justify_content="right", 
        ),
        rx.center(
            generator(),
            width="100%",
            height="100%",
            overflow="hidden",
        ),
        direction="column",
        width=["100%", "100%", "60%", "60%", "60%", "60%"],
        height="100%",
        padding="1.25em",
    )

def generator():
    return rx.form(
        rx.vstack(
            rx.cond(
                ImageGenState.processing,
                rx.center("Processing...", width="15em", height="15em"),
                rx.cond(
                    ImageGenState.image_url,
                    rx.image(src=ImageGenState.image_url, width="15em", height="15em"),
                    rx.center(rx.icon("images"), width="15em", height="15em"),
                ),
            ),
            rx.input(placeholder="Enter description", name="prompt", width="100%"),
            rx.button("Generate Image ->", width="100%", disabled=ImageGenState.processing),
        ),
        on_submit=ImageGenState.get_image,
    )

def image_gen():
    return rx.theme(
        rx.hstack(
        content(),
        setting_section(),
        padding_x="1em",
        height=demo_height,
    ),
    appearance="dark",
    )
