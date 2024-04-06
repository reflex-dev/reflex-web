import reflex as rx

def sidebar():
    return rx.vstack(
        # rx.text("Profile"),
        # rx.text("Account"),
        # rx.text("Appearance"),
        # rx.text("Notifications"),
        # rx.text("Display"),
        rx.text("Hello world", color="red"),
        rx.text("Hello world", color="red"),
        rx.text("Hello world", color="red"),
        rx.text("Hello world", color="red"),
        rx.text("Hello world", color="red"),
        border="1px solid blue",
        width="20%",
    )

def form_content():
    return rx.vstack(
        rx.text("Hello world", color="red"),
        rx.text("Hello world", color="red"),
        rx.text("Hello world", color="red"),
        rx.text("Hello world", color="red"),
        rx.text("Hello world", color="red"),
        border="1px solid gold",
        width="80%",
    )

def settings():
    return rx.vstack(
        rx.text("Settings", color="gold"),
        rx.text("Manage your account settings and set e-mail preferences.", color="gold"),
        height="20%",
        width="100%",
        border="1px solid red",
    )

def content():
    return rx.hstack(
        sidebar(),
        form_content(),
        height="100%",
        width="100%",
        border="2px solid #FFFFFF",
    )

def forms():
    return rx.vstack(
        settings(),
        content(),
    )