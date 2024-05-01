import reflex as rx
from ..style import demo_height


def content():
    return rx.flex(
            rx.input(
                placeholder="name@example.com",
                variant="surface"
            ),
            rx.button(
                "Sign up with Email",
            ),
            rx.divider(
                color="#A1A1AA",
            ),
            rx.button(
                "Google",
                variant="outline",
            ),
            rx.button(
                "Facebook",
                variant="outline",
            ),
            direction="column",
            spacing="2",
            width="100%",
        )

def auth_form():
    return rx.fragment(
        rx.box(
            rx.card(
                rx.flex(
                    rx.text(
                        "Create an Account",
                        weight="bold",
                        size="3"
                    ),
                    rx.text(
                        "Example authentication form.",
                        size="1"
                    ),
                    content(),
                    rx.text(
                        "Get started with a free account.",
                        size="1"
                    ),
                    direction="column",
                    align_items="center",
                    width="100%",
                    spacing="2",
                ),
                width="20em",
            ),
            display="flex",
            height=demo_height,
            align_items="center",
            justify_content="center",
        ),
    )

def auth():
    return rx.theme(rx.center(
        auth_form(),
        width="100%",
        height="100%",
    ),
    appearance="dark",
    )