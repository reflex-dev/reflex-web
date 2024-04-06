import reflex as rx

def auth_form():
    return rx.flex(
        rx.flex(
            rx.text(
                 "Create an account",
                font_size="24px",
                line_height="2em",
                weight="bold",
                color="#FFFFFF",
                align="center",
                height="32px",
                width="350px",
            ),
            rx.box(
                height="8px",
                wdith="350px",
            ),
            rx.text(
                "Enter your email below to create your account",
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
            rx.box(
                height="24px",
            ), # margin 24px
            rx.flex(
                rx.input(
                    placeholder="name@example.com",
                    font_size="14px",
                    line_height="2em",
                    color="#A1A1AA",
                    background="transparent",
                    border="1px solid #A1A1AA",
                    height="36px",
                    focus_border_color="#404040",
                ),
                rx.box(
                    height="8px",
                ),
                rx.button(
                    "Sign in with Email",
                    color="#000000",
                    background="#FFFFFF",
                    font_size="14px",
                    line_height="2em",
                    width="350px",
                    height="36px",
                    _hover={
                        "background_color": "#e6e3e3",
                    }
                ),
                direction="column",
            ),
            rx.flex( 
                rx.box(
                    height="24px",
                ),
                rx.text(
                    "--------  OR CONTINUE WITH  --------",
                    color="#A1A1AA",
                    font_size="14px",
                    height="16px",
                    align="center",
                    justify="center",
                ),
                rx.box(
                    height="24px",
                ),
                direction="column",
            ),
            rx.button(
                "GitHub",
                height="36px",
                width="350px",
                background="transparent",
                border="1px solid #A1A1AA",
                _hover={
                    "background_color": "#A1A1AA",
                },
            ), #github
            direction="column",
        ),
        rx.flex(
            rx.box(
                height="24px",
            ),
            rx.text(
                "By clicking continue, you agree to our Term of Service and Privacy Policy.",
                color="#A1A1AA",
                font_size="14px",
                line_height="2em",
                height="40px",
                align="center",
                justify="center",
            ),
            direction="column",
        ),
        direction="column",
        width="350px",
        height="348px",
    )

def auth():
    return rx.center(
        auth_form(),
        width="100%",
        height="100%",
    )