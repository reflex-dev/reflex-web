import pynecone as pc

from pcweb import constants, styles
from pcweb.templates.docpage import docheader, docpage, doctext

difficulty_colors = {"Beginner": "green", "Intermediate": "orange", "Advanced": "red"}
example_list = [
    {
        "name": "Clock",
        "difficulty": "Intermediate",
        "tags": ["Styling", "Animation"],
        "description": "A analog clock with different time zones.",
        "img": "/gallery/clock.png",
        "gif": "/gallery/clock.gif",
        "url": "https://clock.pynecone.app/",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/clock",
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
        "name": "GPT Q&A",
        "difficulty": "Advanced",
        "tags": ["ML", "Login"],
        "description": "An UI around Open AI's GPT3 API.",
        "img": "/gallery/gpt.png",
        "gif": "/gallery/gpt.gif",
        "url": "https://gpt.pynecone.app/",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/gpt",
    },
    {
        "name": "NBA",
        "difficulty": "Intermediate",
        "tags": ["Data Science", "Graph"],
        "description": "A an interactive dashboard for NBA data.",
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
]


def component_grid():
    sidebar = []
    for category in example_list:
        sidebar.append(
            pc.vstack(
                pc.box(
                    height="10em",
                    background_image=category["img"],
                    background_size="cover",
                    background_repeat="no-repeat",
                    _hover={
                        "background_image": category["gif"],
                        "background_size": "cover",
                    },
                    rounded="lg",
                ),
                pc.hstack(
                    pc.spacer(),
                    pc.badge(
                        category["difficulty"],
                        color_scheme=difficulty_colors[category["difficulty"]],
                    ),
                ),
                pc.heading(category["name"], style={"fontSize": "1.5em"}),
                pc.box(
                    category["description"],
                    color=styles.DOC_REG_TEXT_COLOR,
                    height="2.5em",
                    overflow="scroll",
                    background="linear-gradient(transparent .5em, white)",
                ),
                pc.divider(),
                pc.hstack(
                    *[
                        pc.badge(tag, border_radius="15px", padding_x=".5em")
                        for tag in category["tags"]
                    ],
                    padding_bottom=".5em",
                ),
                pc.vstack(
                    pc.link(
                        pc.hstack(
                            pc.text("Source Code"), pc.icon(tag="external_link")
                        ),
                        href=category["source"],
                    ),
                    pc.link(
                        pc.hstack(pc.text("Live App"), pc.icon(tag="view")),
                        href=category["url"],
                    ),
                    align_items="left",
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
    return pc.box(
        pc.responsive_grid(*sidebar, columns=[1, 2, 2, 2, 3], gap=4),
    )


@docpage()
def gallery():
    return pc.flex(
        pc.hstack(
            pc.box(
                docheader("Gallery", first=True),
                doctext("Here are some examples of what you can make with Pynecone. "),
                pc.divider(),
                component_grid(),
                text_align="left",
            ),
            align_items="start",
        ),
        flex_direction="column",
        height="100%",
        margin_bottom="4em",
    )
