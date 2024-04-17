import reflex as rx
from .form_implementations.profile_form import profile_form

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
        sidebar_button("Account", FormsState.clicked == "Account"),
        sidebar_button("Privacy", FormsState.clicked == "Privacy"),
        sidebar_button("Payments", FormsState.clicked == "Payments"),
        sidebar_button("Advanced", FormsState.clicked == "Advanced"),
        width="20%",
        height="100%",
        align_items="start",
    )

def form_content():
    return profile_form()

def settings():
    return rx.vstack(
        rx.heading(
            "Platform Settings", 
            color="#FFFFFF",
            font_weight="600",
        ),
        rx.text(
            "All of your settings in one place.",
            color="#FFFFFF",
        ),
        rx.divider(),
        padding_top="10px",
        padding_bottom="10px",
        height="20%",
        width="100%",
        align_items="left",
        justify_content="center",
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
            rx.image(src="/landing/form.png"),
            display=["flex", "flex", "none", "none"],
        ),
        rx.box(
            rx.theme(
                rx.vstack(
                    settings(),
                    content(),
                    height="100%",
                    width="100%",
                    padding_x="15px",
                ),
                appearance="dark",
            ),
            display=["none", "none", "flex", "flex"],
        ),
    )