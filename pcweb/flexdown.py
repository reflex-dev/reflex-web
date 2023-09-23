import os
import re
import sys

import yaml

import reflex as rx

from pcweb import constants, styles
from pcweb.templates.docpage import doccode, docheader, docheader2, doclink, doctext, subheader, subheader2, doclink2


component_map = {
    "h1": docheader2,
    "h2": subheader2,
    "a": doclink2,
    "p": doctext,
    "code": lambda source: rx.code(source, color="#1F1944", bg="#EAE4FD"),
}

custom_styles = {
    "a": styles.LINK_STYLE,
    "p": {
        "as_": "p",
        "margin_y": "1em",
        "font_family": styles.SANS,
    },
    "code": {
        "color": "#1F1944",
        "bg": "#EAE4FD",
    },
    "pre": {
        "border_radius": styles.DOC_BORDER_RADIUS,
        "background": "transparent",
        "code_tag_props": {
            "style": {
                "fontFamily": "inherit"
            }
        }
    }
}

def md(source: str):
    return rx.markdown(
        source,
        component_map=component_map
    )

def parse_markdown_front_matter(markdown_content):
    # Define the regular expression pattern to match front matter
    pattern = r"^---\s*\n(.+?)\n---\s*\n(.*)$"
    # Extract the front matter and content using the pattern
    match = re.match(pattern, markdown_content, re.DOTALL)
    if match:
        front_matter = match.group(1)
        content = match.group(2)
        # Parse the front matter as YAML
        try:
            front_matter_data = yaml.safe_load(str(front_matter))
        except yaml.scanner.ScannerError:
            front_matter_data = front_matter

        if isinstance(front_matter_data, str):
            front_matter_data = front_matter

        return front_matter_data, content
    else:
        return None, markdown_content

def evaluate_template_string(input_string, scope):
    # Regular expression to match the template placeholders
    template_regex = r"{(.*?)}"
    matches = re.findall(template_regex, input_string)

    for match in matches:
        try:
            # Evaluate the Python expression and replace the template placeholder
            eval_result = str(eval(match, scope))
            input_string = input_string.replace("{" + match + "}", eval_result)
        except Exception as e:
            # If the evaluation fails, leave the template placeholder unchanged
            print(f"Failed to evaluate expression '{match}': {e}")

    return input_string

def parse(source: str, md=md):
    """Parse out code blocks annotated with ```reflex
    and replace them with the output of the code block.
    The surrounding Markdown should be left untouched.
    """
    front_matter, source = parse_markdown_front_matter(source)
    if isinstance(front_matter, str):
        exec(front_matter)
    elif isinstance(front_matter, dict):
        py_front_matter, source = parse_markdown_front_matter(source)
        if isinstance(py_front_matter, str):
            exec(py_front_matter)

    lines = source.split("\n")
    output = []
    in_reflex_block = False
    current_block = []

    for line in lines:
        if not in_reflex_block:
            if line == "" and not in_reflex_block:
                # End normal block.
                output.append(md("\n".join(current_block)))
                current_block = []

        if line.startswith("```reflex"):
            line = line[len("```reflex") :]
            in_reflex_block = True
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
            current_block.append(evaluate_template_string(line, scope=locals()))

    return front_matter, output

def read(filename: str):
    """Read a markdown file and parse it."""
    source = open(filename).read()
    return parse(source)


def get_all_markdown_files(path: str):
    """Get all markdown files in a directory and its subdirectories."""
    markdown_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))
                
    return markdown_files

