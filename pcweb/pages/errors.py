import reflex as rx
from pcweb.templates.webpage import webpage
from pcweb.flexdown import xd2 as xd


def desktop_view():
    return rx.theme(
            rx.container(
                rx.vstack(
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
                    xd.render_file("errors.md"),
                    align_items="center",
                    margin_bottom="4em",
                    padding_y="2em",
                ),
                margin_x="auto",
                padding_bottom="4em",
                size="2",
                overflow="hidden",
                background="#131217",
                max_width=["90vw", "90vw","100%","100%","100%","100%"]
            ),
            appearance="dark",
        )

def mobile_view():
    return rx.theme(
            rx.container(
                rx.vstack(
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
                    xd.render_file("errors.md"),
                    align_items="center",
                    margin_bottom="4em",
                    padding_y="2em",
                ),
                margin_x="auto",
                padding_bottom="4em",
                size="2",
                overflow="hidden",
                background="#131217",
                max_width=["90vw", "90vw","100%","100%","100%","100%"]
            ),
            appearance="dark",
        )

@webpage(path="/errors", title="Common Errors · Reflex")
def errors():
    return rx.container(
        rx.vstack(
            rx.mobile_only(mobile_view()),
            rx.tablet_and_desktop(desktop_view()),
        )
    ) 
