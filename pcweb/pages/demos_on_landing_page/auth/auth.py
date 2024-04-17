import reflex as rx

def auth_form():
    return rx.flex(
        rx.box(height="24px"),
        rx.flex(
            rx.text(
                "Login",
                font_size="24px",
                line_height="2em",
                weight="bold",
                color="#FFFFFF",
                align="center",
                height="32px",
                width="350px",
                margin_buttom="8px",
            ),
            rx.box(height="8px"),
            rx.text(
                "Example authentication form.",
                font_size="14px",
                line_height="2em",
                color="#A1A1AA",
                align="center",
                height="20px",
                width="350px",
            ),
            direction="column",
        ),
        rx.flex(
            rx.box(height="24px"),
            rx.flex(
                rx.input(
                    placeholder="name@example.com",
                    font_size="14px",
                    line_height="2em",
                    height="36px",
                    variant="surface"
                ),
                rx.box(height="8px"),
                rx.button(
                    "Sign in with Email",
                    font_size="14px",
                    line_height="2em",
                    width="350px",
                    height="36px",
                ),
                direction="column",
            ),
            rx.divider(
                color="#A1A1AA",
            ),
            rx.button(
                "Google",
                height="36px",
                width="350px",
                variant="outline",
                _hover={
                    "background_color": "#A1A1AA",
                },
            ),
            rx.button(
                "Facebook",
                height="36px",
                width="350px",
                variant="outline",
                _hover={
                    "background_color": "#A1A1AA",
                },
            ),
            direction="column",
            spacing="2",
        ),
        rx.flex(
            rx.text(
                "Get started with a free account.",
                color=rx.color("mauve", 7),
                font_size=".8em",
                line_height="2em",
                align="center",
                justify="center",
            ),
            direction="column",
        ),
        direction="column",
        width="350px",
        height="375px",
    )

def auth():
    return rx.theme(rx.center(
        auth_form(),
        width="100%",
        height="100%",
    ),
    appearance="dark",
    )