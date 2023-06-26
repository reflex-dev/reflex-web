import reflex as rx

from pcweb import constants, styles
from pcweb.templates.docpage import docheader, docpage, doctext

difficulty_colors = {"Beginner": "green", "Intermediate": "orange", "Advanced": "red"}
example_list = [
    {
        "name": "Pynecone to Reflex",
        "date": "11/30/21",
        "tags": ["Multi-Page"],
        "author": "Alek Petuskey",
        "img": "/gallery/pcweb.png",
        "gif": "",
        "url": "https://pynecone.io/",
        "source": "https://github.com/pynecone-io/pcweb",
    },
    {
        "name": "AI Template",
        "date": "11/30/21",
        "tags": ["OpenAI", "Database"],
        "author": "Nikhil Rao",
        "img": "/gallery/sales.png",
        "gif": "",
        "url": "",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/sales",
    }
]


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
    sidebar = []
    for category in example_list:
        sidebar.append(
            rx.vstack(
                rx.box(
                    height="10em",
                    background_image=category["img"],
                    background_size="cover",
                    background_position="center",
                    background_repeat="no-repeat",
                    _hover={
                        "background_size": "cover",
                    },
                    rounded="lg",
                ),
                rx.heading(category["name"], style={"fontSize": "1em"}),
                rx.hstack(
                    rx.avatar(name=category["author"], size="xs"),
                    rx.text(category["author"], style={"fontSize": "0.75em"}),
                    rx.spacer(),
                    rx.text(category["date"], style={"fontSize": "0.75em"}),
                ),
                align_items="left",
                row_span=3,
                col_span=1,
                box_shadow="lg",
                border_radius="1em",
                bg_color="white",
                padding="1em",
                _hover={
                    "box_shadow": "rgba(38, 57, 77, .3) 0px 20px 30px -10px",
                },
            )
        )
    return rx.box(
        rx.responsive_grid(*sidebar, columns=[1, 2, 2, 2, 3], gap=4),
    )


@docpage()
def blog():
    return rx.flex(
        rx.hstack(
            rx.box(
                docheader("Blog", first=True),
                doctext("Here are some examples of what you can make with Reflex. "),
                rx.divider(),
                component_grid(),
                text_align="left",
            ),
            align_items="start",
        ),
        flex_direction="column",
        height="100%",
        margin_bottom="4em",
    )
