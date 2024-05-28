import reflex as rx
from pcweb.templates.webpage import webpage
from .paths import blog_data

def card_content(meta, path):
    return rx.link(
        rx.flex(
            rx.box(
                height="12rem",
                width="100%",
                background_image=f'url({meta["image"]})',
                background_size="cover",
                background_position="center",
                background_repeat="no-repeat",
                border_radius="12px"
            ),
            rx.vstack(
                rx.vstack(
                    rx.heading(
                        meta["title"],
                        size="5",
                        color="#D6D6ED"
                    ),
                    rx.text(meta["description"], size="2", color="#8E8EA8"),
                    align_items="start",
                ),
                rx.box(
                    flex_grow=1,
                ),
                rx.hstack(
                    rx.hstack(
                            rx.avatar(
                                fallback=meta["author"][0],
                                background_color="rgba(68, 53, 212, .2)",
                                color="#9085ff",
                            ),
                            rx.text(
                                meta["author"], 
                                font_size="0.85rem", 
                                color="#8E8EA8", 
                                weight="medium",
                            ),
                    ),
                    rx.spacer(),
                    rx.text(
                        str(meta["date"]),
                        font_size="0.85em",
                        weight="medium",
                        padding_right="0.75em",
                    ),
                    color="#8E8EA8",
                    padding_bottom="0.5em",
                    width="100%",
                ),
                width="100%",
                padding_top="1em",
                align_items="start",
                height="13.5em",
            ),
            direction="column",
        ),
        overflow="hidden",
        href=path,
    )

def blog_card(meta, path):
    return rx.flex(
        card_content(meta, path),
        padding="15px",
        align_items="center",
        justify_content="center",
        border_radius="12px",
        bg="#211F26",
    )

def component_grid():
    posts = []
    for path, document in blog_data.items():
        meta = document.metadata
        posts.append(
            blog_card(meta, path)
        )
    return rx.flex(
        rx.chakra.responsive_grid(*posts, columns=[1, 2, 2, 3, 3], gap=4),
        justify_content="center",
    )


@webpage(path="/blog", title="Reflex Blog")
def blogs():
    return rx.container(
        rx.vstack(
            rx.vstack(
                rx.vstack(
                    rx.flex(
                        rx.chakra.text(
                            "Blog posts", 
                            background_image="linear-gradient(95deg, #B1A9FB 25.71%, #867BF1 83.81%);",
                            text_align="center",
                            background_clip="text",
                            padding_x="1em"
                        ),
                        border_radius= "15px;",
                        border= "1px solid #4435D4;",
                        background= "linear-gradient(180deg, rgba(97, 81, 243, 0.20) 0%, rgba(86, 70, 237, 0.20) 100%);",
                        box_shadow= "0px 3px 6px -3px rgba(34, 25, 121, 0.60), 0px 0px 4px -1px rgba(27, 21, 90, 0.40);"
                    ),
                    rx.chakra.text(
                        "Reflex Blog", 
                        font_size="3em",
                        background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%);",
                        text_align="center",
                        background_clip="text",
                        font_weight="bold",
                        letter_spacing= "-1.28px;",
                    ),
                    rx.text(
                        "Stay current with the latest news from Reflex",
                        color="#6C6C81",
                    ),
                    align_items="center",
                    text_align="left",
                    width="100%",
                    spacing="1",
                ),
                component_grid(),
                max_width="110em",
                align_items="center",
                min_height="80vh",
                margin_bottom="4em",
                padding_y="2em",
                width="100%"
            ),
            flex_direction="column",
            width="100%",
            overflow="hidden",
        ),
        padding_x="1em",
    )