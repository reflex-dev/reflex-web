import os
import re
import sys
import yaml

import reflex as rx

from pcweb import constants, styles
from pcweb.templates.webpage import webpage
from pcweb.templates.docpage import docheader, doctext, doclink, doccode


PAGES_PATH = "blog/"

def parse_markdown_front_matter(markdown_content):
    # Define the regular expression pattern to match front matter
    pattern = r'^---\s*\n(.+?)\n---\s*\n(.*)$'
    # Extract the front matter and content using the pattern
    match = re.match(pattern, markdown_content, re.DOTALL)
    if match:
        front_matter = match.group(1)
        content = match.group(2)
        # Parse the front matter as YAML
        front_matter_data = yaml.safe_load(front_matter)
        return front_matter_data, content
    else:
        return None, markdown_content


def parse(source: str):
    """Parse out code blocks annotated with ```reflex
    and replace them with the output of the code block.
    The surrounding Markdown should be left untouched.
    """
    front_matter, source = parse_markdown_front_matter(source)
    lines = source.split("\n")
    output = []
    in_reflex_block = False
    current_block = []
    for line in lines:
        if line.startswith("```reflex"):
            # End normal block.
            line = line[len("```reflex") :]
            in_reflex_block = True
            output.append(rx.markdown("\n".join(current_block)))
            current_block = []
        elif in_reflex_block and line.startswith("```"):
            # End reflex block.
            in_reflex_block = False
            try:
                result = eval("\n".join(current_block))
            except Exception as e:
                print(f"Error in reflex block: {str(e)}")
                sys.exit(1)
            output.append(result)
            current_block = []
        else:
            current_block.append(line)
    return front_matter, output


def get_all_markdown_files(path: str):
    """Get all markdown files in a directory and its subdirectories."""
    markdown_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def get_blog_data(paths):
    blogs = {}
    for path in paths:
        front_matter, output = parse(open(path).read())
        print(front_matter, output)
        path = path.replace(".md", "")
        blogs[path] = (front_matter, output)
    return blogs


def get_route(path: str):
    """Get the route for a page."""
    return path.replace(PAGES_PATH, "").replace(".md", "")

def page(markup) -> rx.Component:
    """Create a page."""
    print("Creating page", markup)
    return rx.container(
        *markup,
    )

paths = get_all_markdown_files(PAGES_PATH)
blogs = get_blog_data(paths)

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
    # {
    #     "name": "AI Template",
    #     "date": "11/30/21",
    #     "tags": ["OpenAI", "Database"],
    #     "author": "Nikhil Rao",
    #     "img": "/gallery/sales.png",
    #     "gif": "",
    #     "url": "",
    #     "source": "https://github.com/pynecone-io/pynecone-examples/tree/main/sales",
    # },
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
    for path, blog in blogs.items():
        meta, output = blog
        sidebar.append(
            rx.link(
                rx.vstack(
                    rx.box(
                        height="10em",
                        # background_image=meta["image"],
                        background_size="cover",
                        background_position="center",
                        background_repeat="no-repeat",
                        _hover={
                            "background_size": "cover",
                        },
                        rounded="lg",
                    ),
                    rx.heading(meta["title"], style={"fontSize": "1em"}),
                    rx.hstack(
                        rx.avatar(name=meta["author"], size="xs"),
                        rx.text(meta["author"], style={"fontSize": "0.75em"}),
                        rx.spacer(),
                        # rx.text(str(meta["date"]), style={"fontSize": "0.75em"}),
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
                ),
                href=path,
            ),
        )
    return rx.box(
        rx.responsive_grid(*sidebar, columns=[1, 2, 2, 2, 3], gap=4),
    )


@webpage(path="/blog/index")
def blg():
    return rx.container(
        rx.hstack(
            rx.box(
                docheader("Blog", first=True),
                doctext("The latest news from the Reflex team. "),
                rx.divider(),
                component_grid(),
                text_align="left",
            ),
            align_items="start",
            min_height="100vh",
            margin_bottom="4em",
            padding_y="2em",
        ),
        flex_direction="column",
    )


for path, blog in blogs.items():
    meta, contents = blog
    print(meta, contents)
    path = path.replace(".md", "")
    print("adding page", path)
    @webpage(path=path)
    def p():
        return page(contents)