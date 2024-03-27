import pandas as pd

import reflex as rx
from pcweb import constants, styles
from pcweb.styles import text_colors as tc
from pcweb.templates.webpage import webpage

# every app must have at least one tag in order to be rendered
apps_list = [
    {
        "name": "Reflex",
        "difficulty": "Advanced",
        "tags": ["Multi-Page", "Graphs", "Forms", "Data Table", "Database"],
        "description": "This website!",
        "img": "/gallery/pcweb.png",
        "gif": "",
        "url": "https://reflex.dev/",
        "source": "https://github.com/reflex-dev/reflex-web",
    },
    {
        "name": "Chat App",
        "difficulty": "Advanced",
        "tags": ["Multi-Page", "AI", "React Components"],
        "description": "An AI chat app.",
        "img": "/gallery/chat.gif",
        "gif": "",
        "url": "https://webui-teal-star.reflex.run/",
        "source": "https://github.com/reflex-dev/reflex-chat",
    },
    {
        "name": "Email Gen",
        "difficulty": "Intermediate",
        "tags": ["AI", "Database"],
        "description": "A sales email generator using OpenAI's GPT3 API.",
        "img": "/gallery/sales.png",
        "gif": "",
        "url": "https://sales.reflex.run",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/sales",
    },
    {
        "name": "DALL-E",
        "difficulty": "Beginner",
        "tags": ["AI"],
        "description": "An app to generate images using OpenAI's DALL-E model.",
        "img": "/gallery/dalle.png",
        "gif": "/gallery/dalle.gif",
        "url": "https://dalle.dev.reflexcorp.run",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/dalle",
    },
    {
        "name": "Graphing Traversal",
        "difficulty": "Intermediate",
        "tags": ["Graphs"],
        "description": "A graphing traversal app.",
        "img": "/gallery/traversal.png",
        "gif": "",
        "url": "https://traversal.reflex.run",
        "source": "https://github.com/reflex-dev/reflex-examples/tree/main/traversal",
    },
    {
        "name": "Counter",
        "difficulty": "Beginner",
        "tags": ["Intro"],
        "description": "A counter app.",
        "img": "/gallery/counter.png",
        "gif": "/gallery/counter.gif",
        "url": "https://counter-radix.reflex.run",
        "source": "https://github.com/reflex-dev/reflex-examples/tree/main/counter",
    },
    {
        "name": "GPT Q&A",
        "difficulty": "Advanced",
        "tags": ["AI", "Auth", "Database"],
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
        "tags": ["Graphs", "Database", "Data Table"],
        "description": "An interactive dashboard for NBA data.",
        "img": "/gallery/nba.png",
        "gif": "/gallery/nba.gif",
        "url": "https://nba.dev.reflexcorp.run",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/nba",
    },
    {
        "name": "Quiz",
        "difficulty": "Intermediate",
        "tags": ["Forms", "Data Table", "Database"],
        "description": "A quiz app that will test your Python knowledge.",
        "img": "/gallery/quiz.png",
        "gif": "/gallery/quiz.gif",
        "url": "https://quiz.dev.reflexcorp.run",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/quiz",
    },
    {
        "name": "Todo",
        "difficulty": "Beginner",
        "tags": ["Intro"],
        "description": "A todo list app.",
        "img": "/gallery/todo.png",
        "gif": "/gallery/todo.gif",
        "url": "",
        # "url": "https://todo.pynecone.app/",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/todo",
    },
    {
        "name": "Twitter Clone",
        "difficulty": "Beginner",
        "tags": ["Auth", "Database", "Multi-Page"],
        "description": "A twitter clone with a login system and database.",
        "img": "/gallery/twitter.png",
        "gif": "/gallery/twitter.gif",
        "url": "",
        # "url": "https://twitter.pynecone.app/",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/twitter",
    },
    {
        "name": "Translator",
        "difficulty": "Beginner",
        "tags": ["Intro"],
        "description": "A translator app.",
        "img": "/gallery/translator.png",
        "gif": "/gallery/translator.gif",
        "url": "https://translator.dev.reflexcorp.run",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/translator",
    },
    {
        "name": "Clock",
        "difficulty": "Intermediate",
        "tags": ["Intro"],
        "description": "An analog clock with different time zones.",
        "img": "/gallery/clock.png",
        "gif": "/gallery/clock.gif",
        "url": "https://clock.dev.reflexcorp.run",
        "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/clock",
    },
    {
        "name": "Simple Background Tasks",
        "difficulty": "Intermediate",
        "tags": ["Streaming"],
        "description": "An app that showcases simple Background tasks.",
        "img": "/gallery/simple_background_tasks.png",
        "gif": "/gallery/simple_background_tasks.gif",
        "url": "https://simple-background-tasks.reflex.run",
        "source": "https://github.com/reflex-dev/reflex-examples/tree/main/lorem-stream",
    },
]


community_apps_list = [
    # {
    #     "name": "Reflex",
    #     "difficulty": "Advanced",
    #     "tags": ["Multi-Page", "Graphs", "Forms", "Data Table", "Database"],
    #     "description": "This website!",
    #     "img": "/gallery/pcweb.png",
    #     "gif": "",
    #     "url": "https://pynecone.io/",
    #     "source": "https://github.com/pynecone-io/pcweb",
    # },
    {
        "name": "Half Truth",
        "difficulty": "Intermediate",
        "tags": ["AI"],
        "description": "A game where half the statements are facts and half are fibbs.",
        "img": "/gallery/half_truth.png",
        "gif": "",
        "url": "https://halftruth.reflex.run",
        "source": "https://github.com/romankouz/hacktoberfest/tree/5050_official/submissions/miscellaneous/romankouz_half_truth",
    },
    {
        "name": "Git Gold Book",
        "difficulty": "Intermediate",
        "tags": [],
        "description": "An overview about about pull requests for a particular repo.",
        "img": "/gallery/git_gold_book.png",
        "gif": "",
        "url": "https://git-app-gold-book.reflex.run",
        "source": "https://github.com/reflex-dev/hacktoberfest/tree/main/submissions/data_visualizations/ashish_git_App",
    },
    {
        "name": "Dataframe Chatbot",
        "difficulty": "Intermediate",
        "tags": ["AI"],
        "description": "Users can interact with their dataframe using natural language.",
        "img": "/gallery/dataframechatbot.png",
        "gif": "",
        "url": "https://interactwithyourcsv.reflex.run",
        "source": "https://github.com/reflex-dev/hacktoberfest/tree/main/submissions/interactive_db/emmanuel/my_dataframe_chatbot",
    },
    {
        "name": "Text Summarizer",
        "difficulty": "Intermediate",
        "tags": [],
        "description": "An app to summarize text.",
        "img": "/gallery/text_summarizer.png",
        "gif": "",
        "url": "https://textsummarizer.reflex.run",
        "source": "https://github.com/reflex-dev/hacktoberfest/tree/main/submissions/ai_apps/emmanuel/text_summarizer",
    },
    {
        "name": "Reflex Rave",
        "difficulty": "Intermediate",
        "tags": [],
        "description": "A movie recommendation system.",
        "img": "/gallery/reflexrave.png",
        "gif": "",
        "url": "https://reflexrave.reflex.run",
        "source": "https://github.com/HeetVekariya/hacktoberfest/tree/heet/ReflexRave",
    },
    {
        "name": "Fynesse",
        "difficulty": "Intermediate",
        "tags": [],
        "description": "Spotify recommendations generator with control.",
        "img": "/gallery/fynesse.png",
        "gif": "",
        "url": "https://fynesse.reflex.run",
        "source": "https://github.com/wightwick/fynesse",
    },
    {
        "name": "User Landing Page",
        "difficulty": "Intermediate",
        "tags": [],
        "description": "Site for representing user links of interest and social networks.",
        "img": "/gallery/mouredev.jpg",
        "gif": "",
        "url": "https://moure.dev",
        "source": "https://github.com/mouredev/python-web",
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


apps_df = pd.DataFrame(apps_list)


def create_list_of_tags(dataframe: pd.DataFrame) -> list:
    """This function takes our pandas dataframe and returns all types of tags
    that exist across all our apps
    .
    """
    # Extract the "tags" column from the DataFrame
    tags_column = dataframe["tags"]

    # Convert the "tags" column to a list
    tags_list = tags_column.tolist()

    # Flatten the list of lists into a single list
    flattened_tags = [tag for sublist in tags_list for tag in sublist]

    # Create a set of unique tags
    unique_tags_set = set(flattened_tags)

    # Convert the set back to a list if needed
    unique_tags_list = list(unique_tags_set)
    return unique_tags_list


list_of_tags = create_list_of_tags(apps_df)


class SideBarState(rx.State):
    """Side Bar State."""

    community_apps_list: list[dict[str, str]] = community_apps_list

    chosen_tags_dict: dict[str, bool] = {key: False for key in list_of_tags}

    def update_tag(self, name: str):
        self.chosen_tags_dict[name] = not self.chosen_tags_dict[name]

    @rx.cached_var
    def true_tags(self) -> list:
        """This function returns a list of the tags selected in the UI, if no tags
        are selected then it returns all the tags
        .
        """
        true_keys = [key for key, value in self.chosen_tags_dict.items() if value]
        if not true_keys:
            return list(self.chosen_tags_dict)
        return list(true_keys)

    @rx.cached_var
    def data_to_return(self) -> list[dict[str, str]]:
        """This function iterates over all the apps we have and if the app has one of the
        tags we have selected in true_tags then it will render this app in the UI
        .
        """
        selected_examples = []
        for example_dict in apps_list:
            example_tags = set(example_dict["tags"])
            if example_tags.intersection(self.true_tags):
                selected_examples.append(example_dict)
        return selected_examples


border_radius = ("0.375rem",)
box_shadow = ("0px 0px 0px 1px rgba(84, 82, 95, 0.14)",)
border = "1px solid #F4F3F6"
text_color = "black"
accent_text_color = "#1A1060"
accent_color = "#F5EFFE"


def add_item(category):
    return rx.chakra.vstack(
        rx.inset(
            rx.image(
                src=category["img"],
            ),
        ),
        rx.chakra.hstack(
            rx.heading(category["name"], style={"fontSize": "1em"}),
            rx.chakra.spacer(),
            rx.chakra.hstack(
                rx.link(
                    rx.chakra.box(
                        rx.image(src="/icons/code.svg", width="1em"),
                        padding_x="0.5em",
                        border_radius="15px",
                        box_shadow="0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14)",
                    ),
                    href=category["source"],
                ),
                rx.cond(
                    category["url"],
                    rx.link(
                        rx.chakra.box(
                            rx.image(src="/icons/eye.svg", width="1em"),
                            padding_x="0.5em",
                            border_radius="15px",
                            box_shadow="0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14)",
                        ),
                        href=category["url"],
                    ),
                ),
                align_items="left",
            ),
            width="100%",
            border_bottom="1px solid #e2e8f0",
            border_top="1px solid #e2e8f0",
            padding_y="0.5em",
        ),
        rx.chakra.box(
            category["description"],
            color=tc["docs"]["body"],
            height="2.5em",
            background="linear-gradient(transparent .5em, white)",
        ),
        rx.chakra.spacer(),
        rx.chakra.wrap(
            rx.badge(
                category["difficulty"],
                border_radius="15px",
            ),
            rx.foreach(
                category["tags"],
                lambda tag: rx.badge(tag, border_radius="15px", padding_x=".5em"),
            ),
            padding_bottom=".5em",
        ),
        align_items="left",
        row_span=3,
        col_span=1,
        border_radius="1em",
        bg_color="white",
        padding="1em",
        box_shadow="rgba(38, 57, 77, .1) 0px 20px 30px -10px",
        _hover={
            "box_shadow": "rgba(38, 57, 77, .3) 0px 20px 30px -10px",
        },
    )


def component_grid():
    return rx.chakra.box(
        rx.chakra.responsive_grid(
            rx.foreach(SideBarState.data_to_return, add_item),
            columns=[1, 2, 2, 2, 3],
            gap=4,
        ),
    )


def community_component_grid():
    return rx.chakra.box(
        rx.chakra.responsive_grid(
            rx.foreach(SideBarState.community_apps_list, add_item),
            columns=[1, 2, 2, 2, 3],
            gap=4,
        ),
    )


def sidebar_component_grid(tags):
    return rx.chakra.wrap(
        *[
            rx.chakra.button(
                tag,
                border_radius="15px",
                padding_x=".5em",
                is_active=SideBarState.chosen_tags_dict[tag],
                on_click=SideBarState.update_tag(tag),
                color="#5646ED",
                bg="#F5EFFE",
                _hover={
                    "boxShadow": "0px 0px 0px 3px rgba(149, 128, 247, 0.6), 0px 2px 3px rgba(3, 3, 11, 0.2), 0px 4px 8px rgba(3, 3, 11, 0.04), 0px 4px 10px -2px rgba(3, 3, 11, 0.02), inset 0px 2px 0px rgba(255, 255, 255, 0.01), inset 0px 0px 0px 1px rgba(32, 17, 126, 0.4), inset 0px -20px 12px -4px rgba(234, 228, 253, 0.36);",
                },
                _active={
                    "color": "white",
                    "bg": "#5646ED",
                },
                _checked={
                    "color": "white",
                    "bg": "#5646ED",
                },
            )
            for tag in tags
        ],
        padding_y="1em",
        padding_x=".5em",
    )


heading_style3 = {}


def sidebar():
    return rx.chakra.box(
        rx.chakra.vstack(
            rx.chakra.vstack(
                rx.heading(
                    "Filters",
                    padding_left=".5em",
                ),
                sidebar_component_grid(list_of_tags),
                width="100%",
                align_items="left",
            ),
            rx.chakra.spacer(),
            height="100vh",
        ),
        min_width="20em",
        width="25%",
        height="100%",
        padding_y="2em",
        display=["none", "none", "none", "none", "flex"],
    )


def gallery_with_no_sidebar():
    return rx.chakra.container(
        rx.chakra.vstack(
            component_grid(),
            rx.chakra.box(
                rx.heading("Community Gallery"),
                rx.chakra.divider(),
                rx.text(
                    "Here are some examples of what the community has made with Reflex. ",
                    margin_bottom="1em",
                ),
                community_component_grid(),
                rx.chakra.alert(
                    rx.chakra.alert_icon(),
                    rx.chakra.alert_title(
                        "If you have an app you'd like to share, please fill out this ",
                        rx.link(
                            "form",
                            href=constants.GALLERY_FORM_URL,
                            color="rgb(107,99,246)",
                        ),
                        ".",
                    ),
                    status="info",
                    margin_top="2em",
                ),
                padding_top="2em",
            ),
            align_items="stretch",
            min_height="80vh",
            margin_bottom="4em",
            padding_y="2em",
        ),
        flex_direction="column",
        max_width="1260px",
        # height="100%",
        # margin_bottom="4em",
    )


@webpage(path="/docs/gallery", title="Gallery · Reflex")
def gallery() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.vstack(
            rx.heading("Gallery", font_size="2em"),
            rx.text(
                "Browse our growing library of example apps. Use them as they are, right out of the box, or customize them to suit your needs.",
                color="#342E5C",
                font_size="1.2em",
                font_family=styles.SANS,
                text_align="center",
            ),
            rx.chakra.divider(),
            width="100%",
            align_items="center",
            padding_x="4em",
        ),
        rx.chakra.hstack(
            rx.chakra.spacer(),
            sidebar(),
            gallery_with_no_sidebar(),
            rx.spacer(),
            align_items="flex-start",
        ),
        max_width="80em",
        margin_x="auto",
        margin_top="80px",
        height="100%",
    )
