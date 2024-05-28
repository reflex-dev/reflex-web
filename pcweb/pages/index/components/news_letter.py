import reflex as rx

from pcweb.signup import IndexState

def news_letter_text() -> rx.Component:
    return rx.vstack(
        rx.chakra.text(
            "Join Our Newsletter!",
            text_align="left",
            background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%)",
            font_size=["20px", "20px", "28px", "42px", "42px", "42px"],
            background_clip="text",
            font_weight="bold",
            line_height="1",            
        ),
        rx.chakra.text(
            " Get the latest updates and news about Reflex.",
            text_align="left",
            color="#6C6C81",
            font_weight="bold",
            line_height="2",
            max_width=["200px", "300px", "400px", "650px", "650px", "650px"],
        ),
        align_items="left",
        width="100%",
    )

def message_group():
    return rx.vstack(
        rx.chakra.text(
            "Welcome to the Reflex Community!",
            text_align="left",
            background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%)",
            font_size=["12px", "15px", "22px", "28px", "35px", "35px"],
            background_clip="text",
            font_weight="bold",
            line_height="1",            
        ),
        rx.link(
            "Sign up for another email",
            href="#",
            color="#FFFFFF",
            underline="always",
            on_click=IndexState.signup_for_another_user().prevent_default,
        )
    )

def news_letter_form() -> rx.Component:
    return rx.el.form(
        rx.chakra.input_group(
            rx.chakra.input_right_element(
                rx.chakra.button(
                    "Subscribe ->",
                    type_="submit",
                    color="#FFF",
                    background="linear-gradient(180deg, #6151F3 0%, #5646ED 100%)",
                    box_shadow="0px 2px 9px -4px rgba(64, 51, 192, 0.70), 0px 0px 6px 2px rgba(255, 255, 255, 0.12) inset, 0px 0px 0px 1px rgba(255, 255, 255, 0.09) inset",
                    border_left="2px solid rgba(186, 199, 247, 0.12)",
                    border_top_left_radius="0px",
                    border_bottom_left_radius="0px",
                    size="lg",
                    _hover={"linear-gradient(180deg, #6151F3 0%, #5646ED 100%);"},
                ),
                height="100%",
                width="25%",
                align="left",
            ),
            rx.chakra.input(
                name="input_email",
                placeholder="Enter your email address here",
                color="#fff",
                background="rgba(161, 157, 213, 0.03)",
                border="2px solid rgba(186, 199, 247, 0.12)",
                border_radius="8px",
                height="48px",
            ),
        ),
        width="100%",
        height="48px",
        on_submit=IndexState.signup,
    )

def news_letter_section() -> rx.Component:
    return rx.center(
        rx.cond(
            IndexState.signed_up,
            message_group(),
            rx.vstack(
                news_letter_text(),
                news_letter_form(),
                width="80%",
            ),
        ),
        width="100%",
        padding = "3em",
    )