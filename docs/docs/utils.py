"""Utilities for the docs."""
import os
import sys

import reflex as rx

PAGES_PATH = "docs/pages/"


def parse(source: str):
    """Parse out code blocks annotated with ```reflex
    and replace them with the output of the code block.
    The surrounding Markdown should be left untouched.
    """
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
    return output


def get_all_markdown_files(path: str):
    """Get all markdown files in a directory and its subdirectories."""
    markdown_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))
    return markdown_files


def get_route(path: str):
    """Get the route for a page."""
    return path.replace(PAGES_PATH, "").replace(".md", "")


def add_pages(app, component):
    """Add all pages in the docs to the app."""
    for path in get_all_markdown_files(PAGES_PATH):
        with open(path) as f:
            parsed = parse(f.read())
            app.add_page(component(parsed), route=get_route(path))
