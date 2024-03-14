import flexdown

import reflex as rx
from pcweb import styles
from pcweb.flexdown import xd
from pcweb.styles import colors as c
from pcweb.styles import text_colors as tc
from pcweb.templates.webpage import webpage
from pcweb.templates.docpage import h1_comp
from pcweb import constants, styles

PAGES_PATH = "blog/"


def get_blog_data(paths):
    blogs = {}
    for path in reversed(sorted(paths)):
        document = flexdown.parse_file(path)
        path = path.replace(".md", "")
        blogs[path] = document
    return blogs


def get_route(path: str):
    """Get the route for a page."""
    return path.replace(PAGES_PATH, "").replace(".md", "")


def back():
    return rx.box(
       rx.text("<- Back to Blog", color="#6C6C81"),
        rx.flex(
            rx.flex(
                rx.link(
                    rx.image(src="/companies/dark/linkedin.svg", height="2em"),
                    href=constants.LINKEDIN_URL,
                ),
                rx.link(
                    rx.image(src="/companies/dark/twitter.svg", height="2em"),
                    href=constants.TWITTER_URL,
                ),
                rx.link(
                    rx.image(src="/companies/dark/yc.svg", height="2em"),
                    href=constants.TWITTER_URL,
                ),
                rx.link(
                    rx.image(src="/companies/dark/reddit.svg", height="2em"),
                    href=constants.LINKEDIN_URL,
                ),
                direction="column",
                spacing="2",
            ),
            direction="column",
            width="100%",
            position="fixed",
            margin_top="5em",
            justify="start",
        ),
        padding_left="2em",
        display=["none", "none", "none", "none", "flex", "flex"],
        width="10em",
        z_index=-1,
        position="absolute"
    )

def content(document, meta):
    return rx.vstack(
        rx.box(
            rx.center(
                rx.flex(
                    rx.flex(
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
                        rx.text(str(meta["date"]),color="#6C6C81",  size="3"),
                        spacing="2",
                        justify_content="center",
                    ),
                    rx.flex(
                        rx.chakra.text(
                                meta["title"],
                                font_size="64px;",
                                background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%);",
                                text_align="center",
                                width="650px",
                                background_clip="text",
                                font_weight="bold",
                                letter_spacing= "-1.28px;",
                        ),
                        justify_content="center",
                    ),
                    direction="column",
                    justify_content="center",
                    width="100%"
                )
            ),
            rx.image(
                src=f"{meta['image']}",
                border_radius="8px",
            ),
            border_radius= "40px;",
            background= "linear-gradient(180deg, #131217 0.5%, rgba(0, 0, 0, 0.00) 122.33%);",
            mix_blend_mode= "plus-lighter;",
            width="60%",
            padding= "80px 80px 0px 80px;"
        ),
        rx.container(
            xd.render(document, "blog.md"),
            margin_x="auto",
            size="2",
        ),
        padding_bottom="8em",
        size="3",
        width="100%",
    )


def page(document) -> rx.Component:
    """Create a page."""
    meta = document.metadata
    return rx.container(
        h1_comp(text=meta["title"]),
        rx.hstack(
            rx.chakra.avatar(name=meta["author"], size="xs"),
            rx.text(meta["author"], size="3"),
            rx.text(" · "),
            rx.text(str(meta["date"]), size="3"),
            padding_bottom="1em",
        ),
        rx.image(
            src=f"{meta['image']}",
            margin_y="1em",
            border_radius="8px",
        ),
        xd.render(document, "blog.md"),
        padding_bottom="8em",
        margin_top="120px",
        margin_x="auto",
        size="2",
    )


paths = flexdown.utils.get_flexdown_files(PAGES_PATH)
blogs = get_blog_data(paths)


class Gallery(rx.Model):
    name: str
    date: str
    tags: list[str]
    description: str
    img: str
    gif: str
    url: str
    source: str


def component_grid():
    posts = []
    for path, document in blogs.items():
        meta = document.metadata
        posts.append(
            rx.link(
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
                                        color="#867BF1",
                                    ),
                                    rx.text(meta["author"], font_size="0.8rem", color="#8E8EA8"),
                            ),
                            rx.spacer(),
                            rx.text(str(meta["date"]), font_size="0.8em"),
                            color="#8E8EA8",
                            padding_bottom="0.5em",
                            width="100%",
                        ),
                        width="100%",
                        padding_top="1em",
                        align_items="start",
                        height="12em",
                    ),
                    direction="column",
                ),
                overflow="hidden",
                href=path,
            ),
        )
    return rx.flex(
        rx.grid(
            *posts, 
            columns="3",
            spacing="4",
            width="80%"
        ),
        justify_content="center",
        padding_top="4em"
    )


@webpage(path="/blog", title="Reflex Blog")
def blg():
    return rx.center(
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
                    "Reflex Blog Latest News and Updates", 
                    font_size="64px;",
                    background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%);",
                    text_align="center",
                    width="650px",
                    background_clip="text",
                    font_weight="bold",
                    letter_spacing= "-1.28px;",
                ),
                rx.text(
                    "Stay current with all the relevant details for Reflex",
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
    )


blog_routes = [blg]
for path, document in blogs.items():
    # Get the docpage component.
    route = f"/{path.replace('.md', '')}"
    title = rx.utils.format.to_snake_case(path.rsplit("/", 1)[1].replace(".md", ""))
    comp = webpage(path=route, title=document.metadata["title"]+ " · Reflex Blog")(
        lambda doc=document: page(doc)
    )

    # Add the route to the list of routes.
    blog_routes.append(comp)
