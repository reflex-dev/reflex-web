
import reflex as rx

from .auth.auth import auth
from .forms.forms import forms
from .dashboard.dashboard import dashboard
from .image_gen.image_gen import image_gen

class DemoState(rx.State):

    demo = "Image Generator"

    def set_demo(self, demo):
        self.demo = demo

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
            align_items="left"
        ),
        rx.box(
            rx.match(
                DemoState.demo,
                ("Forms", forms()),
                ("Dashboard", dashboard()),
                ("Auth", auth()),
                ("Image Generator", image_gen()),
                image_gen()
            ),
            border_radius= "10px;",
            border= "1px solid #2F2B37;",
            background= "linear-gradient(218deg, #1D1B23 -35.66%, #131217 100.84%);",
            width="100%", 
        ),
        padding_bottom="4em",
        width="100%",
    )

