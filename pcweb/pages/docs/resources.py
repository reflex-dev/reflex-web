import reflex as rx
from pcweb.templates.docpage import docpage, h1_comp, h2_comp, text_comp


def video(title, author, url):
    return rx.link(
        rx.chakra.list_item(
            rx.hstack(
                rx.text(title, font_size="1.2em"),
                rx.badge(author, color_scheme="green", margin_left="1em"),
            )
        ),
        href=url,
    )


colors = {"Reddit": "red", "Hacker News": "orange"}


def launch(title, platform, url):
    return rx.link(
        rx.chakra.list_item(
            rx.hstack(
                rx.text(title, font_size="1.2em"),
                rx.badge(platform, color_scheme=colors[platform], margin_left="1em"),
            )
        ),
        href=url,
    )


intro_videos = [
    {
        "title": "The End of React? Pynecone!",
        "author": "Nomad Coders",
        "url": "https://www.youtube.com/watch?v=47BL6WLZJ1g&t=6s",
    },
    {
        "title": "Pynecone: The Python-Only Web Framework",
        "author": "NeuralNine",
        "url": "https://www.youtube.com/watch?v=ur4fCNMPp0I",
    },
    {
        "title": "Pynecone: What Is It?",
        "author": "CodingJQ",
        "url": "https://www.youtube.com/watch?v=p8pJq93snUs",
    },
    {
        "title": "Building Web Apps With Python Has Never Been Easier",
        "author": "CodingTheSmartWay.com",
        "url": "https://www.youtube.com/watch?v=LYl-kxYUnCc&t=891s",
    },
]

tutorial_videos = [
    {
        "title": "Python Pynecone Login Form Tutorial: How to Build a Modern Login UI",
        "author": "Line Indent",
        "url": "https://www.youtube.com/watch?v=zhCT0SnikOw",
    },
    {
        "title": "Create a language translator using Pynecone, Python, OpenAI and GPT-3",
        "author": "AshishCodes",
        "url": "https://www.youtube.com/watch?v=6C37BUOuEx4",
    },
    {
        "title": "Pynecone-io | A Python FullStack Framework",
        "author": "AshishCodes",
        "url": "https://www.youtube.com/watch?v=EkIOjJf7wKs",
    },
    {
        "title": "Build a Python Only Web App with Pynecone! Full-Stack Dev Report.",
        "author": "CodingJQ",
        "url": "https://www.youtube.com/watch?v=qj0truW76EM",
    },
    {
        "title": "How to Build a Memory Match Game in Python: A Step-by-Step Tutorial",
        "author": "Line Indent",
        "url": "https://www.youtube.com/watch?v=PjcjkQZCXRI",
    },
    {
        "title": "Python Tutorial: How to Build a To-Do List",
        "author": "Line Indent",
        "url": "https://www.youtube.com/watch?v=y5E-mj1kRDc",
    },
    {
        "title": "Pynecone State Tutorial",
        "author": "CodingJQ",
        "url": "https://www.youtube.com/@codingjq",
    },
    {
        "title": "Reflex Styling Tutorial",
        "author": "CodingJQ",
        "url": "https://www.youtube.com/watch?v=mitRjfRm7uY",
    },
]

blog_posts = [
    {
        "title": "Pynecone | An Easier way to Build Web Apps",
        "author": "Demetri Petuskey",
        "url": "https://medium.com/@demetri_60494/pynecone-an-easier-way-to-build-web-apps-645601cf20c7",
    },
    {
        "title": "Pynecone: Web Apps in Pure Python",
        "author": "Alek99",
        "url": "https://hackernoon.com/how-to-build-web-apps-in-pure-python",
    },
    {
        "title": "Building Web Apps With Python Has Never Been Easier ",
        "author": "Sebastian",
        "url": "https://medium.com/codingthesmartway-com-blog/building-web-apps-with-python-has-never-been-easier-get-started-with-pynecone-a9f60c1532c",
    },
    {
        "title": "Pynecone Applied | Search",
        "author": "Demetri Petuskey",
        "url": "https://medium.com/@demetri_60494/pynecone-applied-search-9ae4a6d544c6",
    },
]

launches = [
    {
        "title": "Pynecone Show Hacker News",
        "platform": "Hacker News",
        "url": "https://news.ycombinator.com/item?id=33922754",
    },
    {
        "title": "r/Programming",
        "platform": "Reddit",
        "url": "https://www.reddit.com/r/programming/comments/zh0uov/i_made_a_way_to_build_web_apps_in_pure_python/",
    },
    {
        "title": "r/Python",
        "platform": "Reddit",
        "url": "https://www.reddit.com/r/Python/comments/zh0pmy/pynecone_web_apps_in_pure_python/",
    },
]


@docpage()
def resources():
    return rx.flex(
        rx.hstack(
            rx.box(
                h1_comp(text="Resources"),
                text_comp(
                    text="Here are some resources to help you get started with Reflex."
                ),
                text_comp(
                    text="All of the following content is unpaid endorsements from the Reflex community. If you have a video you would like to add to this list, please contact us at alek@pynecone.io "
                    "and we will be happy to add it.",
                ),
                rx.chakra.divider(),
                rx.vstack(
                    h2_comp(text="Launches"),
                    rx.chakra.unordered_list(
                        *[launch(**v) for v in launches],
                        padding_left="2em",
                    ),
                    h2_comp(text="Introduction Videos"),
                    rx.chakra.unordered_list(
                        *[video(**v) for v in intro_videos],
                        padding_left="2em",
                    ),
                    h2_comp(text="Tutorial Videos"),
                    rx.chakra.unordered_list(
                        *[video(**v) for v in tutorial_videos],
                        padding_left="2em",
                    ),
                    h2_comp(text="Blog Posts"),
                    rx.chakra.unordered_list(
                        *[video(**v) for v in blog_posts],
                        padding_left="2em",
                    ),
                    align_items="left",
                ),
                text_align="left",
            ),
            align_items="start",
        ),
        flex_direction="column",
        height="100%",
        margin_bottom="4em",
    )
