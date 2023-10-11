"""Script to index docs to Typesense."""

import os
from collections import defaultdict

import mistletoe
import reflex as rx
from reflex.components.base.bare import Bare

from pcweb.component_list import component_list
from pcweb.pages import routes, doc_routes, changelog_routes, faq_routes, blog_routes
from pcweb.pages.docs.component import multi_docs
from pcweb.tsclient import client


from flexdown import Document, Flexdown
from flexdown.blocks import MarkdownBlock


routes = [
    *routes,
    *doc_routes,
    *changelog_routes,
    *faq_routes,
    *blog_routes,
]


def index_flexdown(source: str, href: str) -> list[tuple[str, str, str]]:
    """Index a flexdown document.

    Args:
        source: The source code of the document.
        href: The href of the document.

    Returns:
        A list of tuples of the form (type, text, href).
    """
    flexdown = Flexdown()
    source = Document.from_source(source)

    # The environment used for execing and evaling code.
    env = source.metadata

    # Get the content of the document.
    source = source.content

    # Get the blocks in the source code.
    blocks = flexdown.get_blocks(source)
    flexdown.process_blocks(blocks, env)

    # Get all the markdown blocks.
    markdown_blocks = [block for block in blocks if block.type == MarkdownBlock.type]
    content = "\n".join([block.get_content(env) for block in markdown_blocks])

    def get_strings(comp):
        """Get the strings from markdown component."""
        strings = []

        # Skip line breaks.
        if isinstance(comp, mistletoe.span_token.LineBreak):
            return strings

        # Recursively get the strings from the children.
        for child in comp.children:
            if isinstance(child, mistletoe.block_token.Heading):
                strings.append(("heading", [child.content], href))
            if isinstance(child, mistletoe.span_token.RawText):
                strings.append(("text", child.content, href))
            else:
                strings += get_strings(child)

        return strings

    # Parse the markdown, and extract the strings.
    doc = mistletoe.Document(content)
    texts = get_strings(doc)
    return texts


def get_strings(comp: rx.Component) -> list[str]:
    """Get the strings from a Reflex component.

    Args:
        comp: The component to extract strings from.

    Returns:
        A list of strings from the component.
    """
    strings = []

    # Recursively get the strings from the children.
    for child in comp.children:
        # Base case is rx.Bare
        if isinstance(child, Bare):
            # Remove var formatting.
            s = child._render().contents.removeprefix("{`").removesuffix("`}")
            if not s.startswith("{"):
                strings.append(s)
        else:
            strings += get_strings(child)

    return strings


def postprocess(
    texts: list[tuple[str, str, str]], join_char: str = " "
) -> dict[tuple[str, str], str]:
    """Postprocess the text.

    Args:
        texts: The texts to postprocess.
        join_char: The character to join the strings with.

    Returns:
        A dictionary of the form {(heading, href): text}
    """
    headings = defaultdict(list)
    current_heading = None

    dud = "Copyright © 2023 Pynecone, Inc."
    # Group the texts by heading.
    for typ, text, href in texts:
        # If the text is a heading, set the current heading.
        if typ == "heading" and len(text) > 0:
            t = text if isinstance(text, str) else text[0]
            current_heading = t, href
        if current_heading is None:
            continue

        # Add the text to the current heading.
        if typ == "text":
            headings[current_heading] += text

    # Remove the base event triggers heading.
    for href in set([href for _, _, href in texts]):
        if ("Base Event Triggers", href) in headings:
            del headings[("Base Event Triggers", href)]
        if ("Component Specific Triggers", href) in headings:
            del headings[("Component Specific Triggers", href)]

    # Remove the dud text.
    dud = "Copyright © 2023 Pynecone, Inc."
    return {
        key: join_char.join(value).replace("  ", " ").replace(dud, "")
        for key, value in headings.items()
    }


class Doc(rx.Base):
    heading: str
    description: str
    href: str


def index_component(comp: rx.Component, href: str) -> list[tuple[str, str, str]]:
    """Index the text from a component.

    Args:
        comp: The component to index.
        href: The href of the component.

    Returns:
        A list of tuples of the form (type, text, href).
    """
    text = []
    for child in comp.children:
        if isinstance(child, rx.Heading):
            text.append(("heading", get_strings(child), href))
        if isinstance(child, rx.Text):
            text.append(("text", get_strings(child), href))
        else:
            text += index_component(child, href)
    return text


def index_flexdown_file(
    path: str, heading: str | None = None
) -> dict[tuple[str, str], str]:
    """Index a flexdown file.

    Args:
        path: The path of the flexdown file.
        heading: The heading of the file.

    Returns:
        A dictionary of the form {(heading, href): text}
    """
    # Index the flexdown file.
    contents = open(path).read()
    texts = index_flexdown(contents, path)
    path = "/" + path.replace(".md", "")

    # Add the heading if it exists.
    if heading is not None:
        texts.insert(0, ("heading", [heading.title()], path))

    # Postprocess the texts.
    return postprocess(texts, join_char="")


def index_components():
    """Index the components."""
    out = {}
    # Iterate over the component list.
    for key in component_list:
        for component_group in component_list[key]:
            # Skip the group if it is a string (category name)
            if isinstance(component_group[0], str):
                continue

            # Get the component name and path.
            comp_name = component_group[0].__name__.lower()
            path = f"/docs/library/{key.lower()}/{comp_name}"

            # Check if a flexdown file exists.
            flexdown_path = f"{path.strip('/')}.md"
            if os.path.exists(flexdown_path):
                out |= index_flexdown_file(flexdown_path, heading=comp_name)
            else:
                comp = multi_docs(path=path, component_list=component_group).component()
                out |= postprocess(index_component(comp, path))

    return out


def index_routes():
    """Index the routes."""
    out = {}
    for route in routes:
        flexdown_path = f"{route.path.strip('/')}.md"
        if os.path.exists(flexdown_path):
            out |= index_flexdown_file(flexdown_path)
        else:
            comp = route.component()
            out |= postprocess(index_component(comp, route.path))
    return out


def index_docs():
    """Index the docs."""
    return {
        **index_routes(),
        **index_components(),
    }


def create_collection():
    """Create the collection."""
    try:
        client.collections["search-auto"].delete()
    except Exception as e:
        pass

    create_response = client.collections.create(
        {
            "name": "search-auto",
            "fields": [
                {"name": "heading", "type": "string"},
                {"name": "description", "type": "string"},
                {"name": "href", "type": "string"},
            ],
        }
    )
    print(create_response)


def upload_docs(docs: list[Doc]):
    """Upload the docs."""
    for doc in docs:
        print(doc)
        client.collections["search-auto"].documents.create(doc)


if __name__ == "__main__":
    # create_collection()
    out = index_docs()
    docs = []
    for key, text in out.items():
        docs.append({"heading": key[0], "description": text, "href": key[1]})
    # upload_docs(docs)
