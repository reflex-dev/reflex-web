import reflex as rx
from .form_implementations.profile_form import profile_form

class State(rx.State):
    clicked: str = "Profile"

    def set_clicked(self, option: str):
        self.clicked = option

    def get_clicked(self):
        return self.clicked

def sidebar_button(name, is_selected):
    return rx.button(
        name,
        background=rx.cond(
            is_selected,
            "#909090",
            "transparent",
        ),
        style={"text_align": "left"},
        on_click=lambda: State.set_clicked(name),
        width="100%",
    )

def account_form():
    return rx.vstack(
        rx.text("Account Form", color="red"),
        rx.text("Account details go here", color="red"),
        width="80%",
        height="100%",
    )

def appearance_form():
    return rx.vstack(
        rx.text("Appearance Form", color="red"),
        rx.text("Appearance settings go here", color="red"),
        width="80%",
        height="100%",
    )

def notifications_form():
    return rx.vstack(
        rx.text("Notifications Form", color="red"),
        rx.text("Notification settings go here", color="red"),
        width="80%",
        height="100%",
    )

def display_form():
    return rx.vstack(
        rx.text("Display Form", color="red"),
        rx.text("Display settings go here", color="red"),
        width="80%",
        height="100%",
    )

FORM_CONTENT = {
    "Profile": profile_form,
    "Account": account_form,
    "Appearance": appearance_form,
    "Notifications": notifications_form,
    "Display": display_form,
}

def sidebar():
    return rx.vstack(
        sidebar_button("Profile", State.clicked == "Profile"),
        sidebar_button("Account", State.clicked == "Account"),
        sidebar_button("Appearance", State.clicked == "Appearance"),
        sidebar_button("Notifications", State.clicked == "Notifications"),
        sidebar_button("Display", State.clicked == "Display"),
        align_item="start",
        width="20%",
        height="100%",
    )

def form_content():
    return rx.match(
        State.clicked,
        ("Profile", profile_form()),
        ("Account", profile_form()),
        ("Appearance", profile_form()),
        ("Notifications", profile_form()),
        ("Display", profile_form()),
        rx.vstack(
            rx.text("No form selected", color="black"),
            width="80%",
            height="100%",
        ),
    )

def settings():
    return rx.vstack(
        rx.text(
            "Settings", 
            color="#FFFFFF",
            padding_left="15px",
        ),
        rx.text(
            "Manage your account settings and set e-mail preferences.",
            color="#FFFFFF",
            padding_left="15px",
        ),
        height="20%",
        width="100%",
        align_items="left",
        justify_content="center",
    )

def content():
    return rx.hstack(
        sidebar(),
        form_content(),
        height="80%",
        width="100%",
    )

def forms():
    return rx.vstack(
        settings(),
        content(),
        height="100%",
        width="100%",
    )
