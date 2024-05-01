import reflex as rx
from .form_implementations.profile_form import profile_form
from ..style import demo_height

class FormsState(rx.State):
    clicked: str = "Account"

    def set_clicked(self, option: str):
        self.clicked = option

    def get_clicked(self):
        return self.clicked

def sidebar_button(name, is_selected):
    return rx.button(
        rx.text(
            name,
            width="100%",
            padding_left="5px",
        ),
        background=rx.cond(
            is_selected,
            rx.color("mauve", 2),
            "transparent",
        ),
        text_align="left",
        width="100%",
    )

def sidebar():
    return rx.vstack(
        sidebar_button("General", FormsState.clicked == "General"),
        sidebar_button("Account", FormsState.clicked == "Account"),
        sidebar_button("Payments", FormsState.clicked == "Payments"),
        sidebar_button("Advanced", FormsState.clicked == "Advanced"),
        width="20%",
        height="100%",
        align_items="start",
        display=["none", "none", "flex", "flex", "flex", "flex"],
    )

def form_content():
    return profile_form()

def settings():
    return rx.vstack(
        rx.heading(
            "Platform Settings", 
            color=rx.color("mauve", 12),
            font_weight="600",
            size="5"
        ),
        rx.text(
            "All of your settings and preferences in one place.",
            color=rx.color("mauve", 11),
            size="1",
        ),
        height="20%",
        width="100%",
        align_items="left",
        padding_bottom="1em",
        border_bottom=f"1px solid {rx.color('mauve', 4)}",
    )

def content():
    return rx.hstack(
        sidebar(),
        form_content(),
        height="100%",
        width="100%",
        align_items="start",
    )

def forms():
    return rx.fragment(
        rx.box(
            rx.theme(
                rx.vstack(
                    settings(),
                    content(),
                    width="100%",
                    padding_x="15px",
                    padding_top="15px",
                    height=demo_height,
                    overflow_y="hidden",
                ),
                appearance="dark",
            ),
            display="flex",
        ),
    )