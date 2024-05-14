import reflex as rx
from pcweb import styles
from pcweb.pages.docs.gallery import gallery
from pcweb.templates.docpage import doclink
from pcweb.templates.webpage import webpage

error_items = [
    {
        "E": "Add an error message here",
        "S": rx.text(
            "Add a solution here"
        ),
    },
    {
        "E": "What can I build with Reflex?",
        "S": rx.vstack(
            rx.text(
                """
            With Reflex, data scientists and software engineers can create high-quality web applications quickly and easily without needing to learn specific web development technologies. Whether you want to build a single purpose user interface for a data science project/internal app, or a large multi-page web app, Reflex has the tools and features to handle both and scale up as your project grows.            """
            ),
            rx.text(
                "Check out our ",
                rx.chakra.span(doclink("gallery", href=gallery.path)),
                " to see what ur community has already built with Reflex.",
            ),
            align_items="flex-start",
            width="100%",
        ),
    },
]


def error_item(question, answer, index):
    return rx.chakra.accordion(rx.chakra.accordion_item(
        rx.chakra.accordion_button(
            rx.heading(
                question, color="#D6D6ED", font_size=styles.H3_FONT_SIZE
            ),
            rx.chakra.spacer(),
            rx.chakra.accordion_icon(color="#6C6C81"),
            _hover={},
            padding_y="1em",
        ),
        rx.chakra.accordion_panel(answer, color="#6C6C81"),
        border="none",
    ),
    allow_multiple=True,
    border_radius= "12px;",
    border= "1px solid #37363F;",
    background= "rgba(47, 43, 55, 0.50);",
    box_shadow= "0px 3px 22px -2px #0C0B0F;",
    width="100%",
)

def error_item_mobile(question, answer, index):
    return rx.chakra.accordion(
        rx.chakra.accordion_item(
            rx.chakra.accordion_button(
                rx.heading(
                    question, color="#D6D6ED", font_size="1em",
                ),
                rx.chakra.spacer(),
                rx.chakra.accordion_icon(color="#6C6C81"),
                padding_y="1em",
            ),
            rx.chakra.accordion_panel(answer, color="#6C6C81"),
            border="none",
        ),
        allow_multiple=True,
        border_radius="12px",
        border="1px solid #37363F",
        background="rgba(47, 43, 55, 0.50)",
        box_shadow="0px 3px 22px -2px #0C0B0F",
        width="90%",  # Adjust the width to a smaller value, e.g., 90%
        max_width="375px",  # Set a maximum width for the accordion
        margin="0 auto",  # Center the accordion horizontally
    )

def desktop_view():
    return rx.vstack(
        rx.vstack(
            rx.flex(
                rx.chakra.text(
                    "Common Errors",
                    background_image="linear-gradient(95deg, #B1A9FB 25.71%, #867BF1 83.81%);",
                    text_align="center",
                    background_clip="text",
                    padding_x="1em"
                ),
                border_radius="15px;",
                border="1px solid #4435D4;",
                background="linear-gradient(180deg, rgba(97, 81, 243, 0.20) 0%, rgba(86, 70, 237, 0.20) 100%);",
                box_shadow="0px 3px 6px -3px rgba(34, 25, 121, 0.60), 0px 0px 4px -1px rgba(27, 21, 90, 0.40);"
            ),
            rx.chakra.text(
                "Reflex Errors",
                font_size="64px;",
                background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%);",
                text_align="center",
                width="650px",
                background_clip="text",
                font_weight="bold",
                letter_spacing="-1.28px;",
            ),
            rx.text(
                "We've compiled a list of the most common errors users face when using Reflex. If you have encountered an error that isn't answered here, feel free to reach out to us on our Discord.",
                color="#6C6C81",
            ),
            align_items="center",
            text_align="left",
            width="100%",
            spacing="1",
            margin_bottom="2em",
        ),
        *[
            error_item(item["E"], item["S"], index)
            for index, item in enumerate(error_items)
        ],
        align_items="center",
        margin_bottom="4em",
        padding_y="2em",
    )

def mobile_view():
    return rx.vstack(
        rx.vstack(
            rx.flex(
                rx.chakra.text(
                    "Common Errors",
                    background_image="linear-gradient(95deg, #B1A9FB 25.71%, #867BF1 83.81%);",
                    text_align="center",
                    background_clip="text",
                    padding_x="1em",
                ),
                padding_buttom="1em",
                border_radius="15px;",
                border="1px solid #4435D4;",
                background="linear-gradient(180deg, rgba(97, 81, 243, 0.20) 0%, rgba(86, 70, 237, 0.20) 100%);",
                box_shadow="0px 3px 6px -3px rgba(34, 25, 121, 0.60), 0px 0px 4px -1px rgba(27, 21, 90, 0.40);"
            ),
            rx.chakra.text(
                "Reflex Errors",
                font_size="28px;",
                background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%);",
                text_align="center",
                width="650px",
                background_clip="text",
                font_weight="medium",
                letter_spacing="-1.28px;",
            ),
            rx.box(
                rx.text(
                    "We've compiled a list of the most common errors users face when using Reflex. If you have encountered an error that isn't answered here, feel free to reach out to us on our Discord.",
                    color="#6C6C81",
                    width="360px",
                    align="center",
                ),
            ),
            align_items="center",
            text_align="left",
            width="100%",
            spacing="1",
            margin_bottom="2em",
        ),
        *[
            error_item_mobile(item["E"], item["S"], index)
            for index, item in enumerate(error_items)
        ],
        align_items="center",
        margin_bottom="4em",
        padding_y="2em",
    )

@webpage(path="/errors", title="Common Errors · Reflex")
def errors():
    return rx.container(
        rx.vstack(
            rx.mobile_only(mobile_view()),
            rx.tablet_and_desktop(desktop_view()),
        )
    )