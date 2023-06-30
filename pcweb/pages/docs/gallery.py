import reflex as rx

from pcweb import constants, styles
from pcweb.templates.docpage import docheader, docpage, doctext

difficulty_colors = {"Beginner": "green", "Intermediate": "orange", "Advanced": "red"}
example_list = [
    {
        "name": "Reflex",
        "difficulty": "Advanced",
        "tags": ["Multi-Page"],
        "description": "This website!",
        "img": "/gallery/pcweb.png",
        "gif": "",
        "url": "https://pynecone.io/",
        "source": "https://github.com/pynecone-io/pcweb",
    },
    {
        "name": "Email Gen",
        "difficulty": "Intermediate",
        "tags": ["OpenAI", "Database"],
        "description": "A sales email generator using OpenAI's GPT3 API.",
        "img": "/gallery/sales.png",
        "gif": "",
        "url": "",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/sales",
    },
    {
        "name": "DALL-E",
        "difficulty": "Beginner",
        "tags": ["ML", "Image Generation"],
        "description": "An app to generate images using OpenAI's DALL-E model.",
        "img": "/gallery/dalle.png",
        "gif": "/gallery/dalle.gif",
        "url": "https://dalle.pynecone.app/",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/dalle",
    },
    {
        "name": "Graphing Trav",
        "difficulty": "Intermediate",
        "tags": ["DFS", "BFS", "Graph"],
        "description": "A graphing traversal app.",
        "img": "/gallery/traversal.png",
        "gif": "",
        "url": "",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/traversal",
    },
    {
        "name": "Counter",
        "difficulty": "Beginner",
        "tags": ["Tutorial"],
        "description": "A counter app.",
        "img": "/gallery/counter.png",
        "gif": "/gallery/counter.gif",
        "url": "https://counter.pynecone.app/",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/counter",
    },
    {
        "name": "GPT Q&A",
        "difficulty": "Advanced",
        "tags": ["ML", "Login"],
        "description": "An UI around Open AI's GPT3 API.",
        "img": "/gallery/gpt.png",
        "gif": "/gallery/gpt.gif",
        "url": "",
        # "url": "https://gpt.pynecone.app/",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/gpt",
    },
    {
        "name": "NBA",
        "difficulty": "Intermediate",
        "tags": ["Data Science", "Graph"],
        "description": "An interactive dashboard for NBA data.",
        "img": "/gallery/nba.png",
        "gif": "/gallery/nba.gif",
        "url": "https://nba.pynecone.app/",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/nba",
    },
    {
        "name": "Quiz",
        "difficulty": "Intermediate",
        "tags": ["Data Science", "Graph"],
        "description": "A quiz app that will test your Python knowledge.",
        "img": "/gallery/quiz.png",
        "gif": "/gallery/quiz.gif",
        "url": "https://quiz.pynecone.app/",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/quiz",
    },
    {
        "name": "Todo",
        "difficulty": "Beginner",
        "tags": ["Short"],
        "description": "A todo list app.",
        "img": "/gallery/todo.png",
        "gif": "/gallery/todo.gif",
        "url": "https://todo.pynecone.app/",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/todo",
    },
    {
        "name": "Twitter Clone",
        "difficulty": "Beginner",
        "tags": ["Login", "Database"],
        "description": "A twitter clone with a login system and database.",
        "img": "/gallery/twitter.png",
        "gif": "/gallery/twitter.gif",
        "url": "https://twitter.pynecone.app/",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/twitter",
    },
    {
        "name": "Translator",
        "difficulty": "Beginner",
        "tags": ["Short"],
        "description": "A translator app.",
        "img": "/gallery/translator.png",
        "gif": "/gallery/translator.gif",
        "url": "https://translator.pynecone.app/",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/translator",
    },
    {
        "name": "Clock",
        "difficulty": "Intermediate",
        "tags": ["Styling", "Animation"],
        "description": "An analog clock with different time zones.",
        "img": "/gallery/clock.png",
        "gif": "/gallery/clock.gif",
        "url": "https://clock.pynecone.app/",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/clock",
    },
]


class Gallery(rx.Model):
    name: str
    difficulty: str
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
                rx.hstack(
                    rx.heading(category["name"], style={"fontSize": "1em"}),
                    rx.spacer(),
                    rx.hstack(
                        rx.link(
                            rx.box(
                                rx.image(src="/icons/code.svg", width="1em"),
                                padding_x="0.5em",
                                border_radius="15px",
                                box_shadow="0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14)",
                            ),
                            href=category["source"],
                        ),
                        rx.link(
                            rx.box(
                                rx.image(src="/icons/eye.svg", width="1em"),
                                padding_x="0.5em",
                                border_radius="15px",
                                box_shadow="0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14)",
                            ),
                            href=category["source"],
                        )
                        if category["url"]
                        else rx.box(),
                        align_items="left",
                    ),
                    width="100%",
                    border_bottom="1px solid #e2e8f0",
                    border_top="1px solid #e2e8f0",
                    padding_y="0.5em",
                ),
                rx.box(
                    category["description"],
                    color=styles.DOC_REG_TEXT_COLOR,
                    height="2.5em",
                    overflow="scroll",
                    background="linear-gradient(transparent .5em, white)",
                ),
                rx.spacer(),
                rx.wrap(
                    rx.badge(
                        category["difficulty"],
                        border_radius="15px",
                        color_scheme=difficulty_colors[category["difficulty"]],
                    ),
                    *[
                        rx.badge(tag, border_radius="15px", padding_x=".5em")
                        for tag in category["tags"]
                    ],
                    padding_bottom=".5em",
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
def gallery():
    return rx.flex(
        rx.hstack(
            rx.box(
                docheader("Gallery", first=True),
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
