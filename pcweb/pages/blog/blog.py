import os
import re
import sys

import yaml

import reflex as rx
from pcweb import constants, styles
from pcweb.templates.docpage import doccode, docheader, doclink, doctext, subheader
from pcweb.templates.webpage import webpage
from reflex import el

from pcweb.styles import text_colors as tc
from pcweb.styles import colors as c

PAGES_PATH = "blog/"


def parse_markdown_front_matter(markdown_content):
    # Define the regular expression pattern to match front matter
    pattern = r"^---\s*\n(.+?)\n---\s*\n(.*)$"
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
        path = path.replace(".md", "")
        blogs[path] = (front_matter, output)
    return blogs


def get_route(path: str):
    """Get the route for a page."""
    return path.replace(PAGES_PATH, "").replace(".md", "")


def page(meta, markup) -> rx.Component:
    """Create a page."""

    return rx.container(
        rx.heading(meta["title"], mt=12, mb=4, font_weight="semibold"),
        rx.hstack(
            rx.avatar(name=meta["author"], size="xs"),
            rx.text(meta["author"], font_size="0.9rem"),
            rx.text(" · "),
            rx.text(str(meta["date"]), font_size="0.9rem"),
        ),
        rx.image(
            src=f"/{meta['image']}",
            object_fit="contain",
            shadow="sm",
            my=8,
            border_radius="8px",
        ),
        el.div(
            *markup,
            class_name="prose prose-a:!underline prose-a:!decoration-violet-200 hover:prose-a:!decoration-inherit prose-a:!transition-all prose-a:underline-offset-2 prose-headings:!my-1 prose-p:!my-1 prose-p:text-gray-600",
        ),
    )


paths = get_all_markdown_files(PAGES_PATH)
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
    for path, blog in blogs.items():
        meta, _ = blog
        posts.append(
            rx.link(
                rx.box(
                    height="10rem",
                    background_image=meta["image"],
                    background_size="cover",
                    background_position="center",
                    background_repeat="no-repeat",
                    w="100%",
                ),
                rx.box(
                    rx.heading(
                        meta["title"],
                        font_size="1.2rem",
                        mb="0.5em",
                    ),
                    rx.text(
                        meta["description"],
                        font_size="0.8rem",
                    ),
                    rx.divider(),
                    rx.hstack(
                        rx.vstack(
                            rx.text("Written by", font_size="0.6rem"),
                            rx.hstack(
                                rx.avatar(
                                    name=meta["author"],
                                    size="sm",
                                    bg=c["indigo"][800],
                                    color="#DACEEE",
                                ),
                                rx.text(meta["author"], font_size="0.8rem"),
                            ),
                            align_items="left",
                        ),
                        rx.spacer(),
                        rx.vstack(
                            rx.text("Published on", font_size="0.6rem"),
                            rx.text(str(meta["date"]), font_size="0.8em"),
                            align_items="left",
                        ),
                        color=tc["docs"]["body"],
                        padding_bottom="0.5em",
                    ),
                    p=4,
                ),
                border="1px solid #eee",
                border_radius="8px",
                overflow="hidden",
                bg_color="white",
                _hover={
                    "box_shadow": "0px 0px 0px 1px rgba(52, 46, 92, 0.12), 0px 2px 3px rgba(3, 3, 11, 0.1), 0px 12px 8px rgba(3, 3, 11, 0.04), 0px 8px 12px -4px rgba(3, 3, 11, 0.02)"
                },
                href=path,
            ),
        )
    return rx.box(
        rx.responsive_grid(*posts, columns=[1, 2, 2, 2, 3], gap=4),
    )


@webpage(path="/blog/index")
def blg():
    return rx.container(
        rx.vstack(
            rx.box(
                rx.heading("Reflex Blog", font_size=styles.H1_FONT_SIZE, mt=12, mb=4),
                rx.text(
                    "The latest news from the Reflex team. ",
                    color=tc["docs"]["body"],
                ),
                rx.divider(),
                text_align="left",
                width="100%",
            ),
            component_grid(),
            align_items="stretch",
            min_height="80vh",
            margin_bottom="4em",
            padding_y="2em",
        ),
        flex_direction="column",
        max_width="960px",
    )


for path, blog in blogs.items():
    meta, contents = blog
    path = path.replace(".md", "")
    
    @webpage(path=path)
    def p():
        return page(meta, contents)
