"""Script to index docs to Typesense."""

import argparse
import json
import os
from collections import defaultdict

import mistletoe
import reflex as rx
from reflex.components.base.bare import Bare
from reflex.components.radix.themes.typography import Heading
from reflex.components.radix.themes.typography.text import Text

from pcweb.pages import routes
from pcweb.tsclient import client
from pcweb.flexdown import xd

from flexdown import Document
from flexdown.blocks import MarkdownBlock


def index_flexdown(source: str, href: str) -> list[tuple[str, str, str]]:
    """Index a flexdown document.

    Args:
        source: The source code of the document.
        href: The href of the document.

    Returns:
        A list of tuples of the form (type, text, href).
    """
    source = Document.from_source(source)

    # The environment used for execing and evaling code.
    env = source.metadata
    env["__xd"] = xd

    # Get the content of the document.
    source = source.content

    # Get the blocks in the source code.
    # Note: we must use reflex-web's special flexdown instance xd here - it knows about all custom block types (like DemoBlock)
    blocks = xd.get_blocks(source, href)

    content_pieces = []
    for block in blocks:
        # Render all blocks for their side effect of env augmentation
        # Unexpected, but hey!
        # TODO Probably better to return env as part of return
        _ = block.render(env=env)
        if isinstance(block, MarkdownBlock):
            # Now we should have all the env entries we need
            content = block.get_content(env)
            content_pieces.append(content)

    content = "\n".join(content_pieces)

    def get_strings(comp):
        """Get the strings from markdown component."""
        strings = []

        # Skip line breaks.
        if isinstance(comp, mistletoe.span_token.LineBreak):
            return strings

        # Recursively get the strings from the children.
        for child in comp.children:
            if isinstance(child, mistletoe.block_token.Heading):
                content = get_strings(child)[0][1]
                strings.append(("heading", [content], href))
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
        if isinstance(child, Heading):
            text.append(("heading", get_strings(child), href))
        if isinstance(child, Text):
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
    path = "/" + path.replace(".md", "")
    texts = index_flexdown(contents, path)

    # Add the heading if it exists.
    if heading is not None:
        texts.insert(0, ("heading", [heading.title()], path))

    # Postprocess the texts.
    return postprocess(texts, join_char="")


def index_routes():
    """Index the routes."""
    out = {}
    for route in routes:
        # We do not want to index the docs for Chakra based components.
        if route.path.startswith("/docs/library/chakra/"):
            continue
        flexdown_path = f"{route.path.strip('/')}.md"
        if os.path.exists(flexdown_path):
            out |= index_flexdown_file(flexdown_path)
        else:
            comp = route.component()
            out |= postprocess(index_component(comp, route.path))
    return out


def determine_category(path):
    if path.startswith("/docs/library/"):
        return "Component"
    elif path.startswith("/blog/"):
        return "Blog"
    elif path.startswith("/docs/api-reference/"):
        return "API Reference"
    else:
        return "Learn"


def index_everything():
    """Index everything."""
    everything = index_routes()
    everything_with_categories = {}
    for key, text in everything.items():
        category = determine_category(key[1])
        new_key = (key[0], key[1], category)
        everything_with_categories[new_key] = text
    return everything_with_categories


def create_collection(collection_name: str):
    """Create the collection."""
    try:
        client.collections[collection_name].delete()
    except Exception as e:
        pass

    create_response = client.collections.create(
        {
            "name": collection_name,
            "fields": [
                {"name": "heading", "type": "string"},
                {"name": "description", "type": "string"},
                {"name": "href", "type": "string"},
                {"name": "category", "type": "string"},
            ],
        }
    )


def upload_docs(collection_name: str, docs: list[Doc]):
    """Upload the docs."""
    for doc in docs:
        print("Uploading")
        print(doc)
        client.collections[collection_name].documents.create(doc)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--upload", action="store_true", default=False)
    parser.add_argument("--collection-name")
    args = parser.parse_args()

    if bool(args.upload) != bool(args.collection_name):
        raise ValueError("Must set both or neither of --upload and --collection-name.")

    print("Generating index documents.")
    out = index_everything()
    docs = []
    for key, text in out.items():
        docs.append(
            {"heading": key[0], "description": text, "href": key[1], "category": key[2]}
        )
    print(f"{len(docs)} documents done.")
    if args.upload:
        print(f"Recreating Typesense collection {args.collection_name}.")
        create_collection(args.collection_name)
        print("Uploading documents to Typesense.")
        upload_docs(args.collection_name, docs)
        print("\033[92mUpload complete!")
    else:
        print(json.dumps(docs, indent=4))
        print(
            "\033[96m[set --upload and --collection-name to actually publish to Typesense Cloud]"
        )
