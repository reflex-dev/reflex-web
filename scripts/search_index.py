from pcweb.pages import routes
import pynecone as pc
from pcweb.pages.docs.component import multi_docs
from pcweb.tsclient import client
from pynecone.components.base.bare import Bare


def get_strings(comp):
    """Get the strings from a component."""
    strings = []
    for child in comp.children:
        if isinstance(child, Bare):
            s = child._render().contents.removeprefix("{`").removesuffix("`}")
            if not s.startswith("{"):
                strings.append(s)
        else:
            strings += get_strings(child)
    return strings


from collections import defaultdict


def get_text(comp, href):
    """Get the text from a component."""
    text = []
    for child in comp.children:
        if isinstance(child, pc.Heading):
            text.append(("heading", get_strings(child), href))
        if isinstance(child, pc.Text):
            text.append(("text", get_strings(child), href))
        else:
            text += get_text(child, href)
    return text


def postprocess(texts):
    headings = defaultdict(list)
    current_heading = None
    for typ, text, href in texts:
        if typ == "heading" and len(text) > 0:
            current_heading = text[0], href
        if current_heading is None:
            continue
        if typ == "text":
            headings[current_heading] += text
    for _, _, href in texts:
        if ("Base Events Triggers", href) in headings:
            del headings[("Base Events Triggers", href)]
    # del headings["Base Event Triggers"]
    dud = "Site Documentation Resources Copyright © 2023 Pynecone, Inc."
    return {
        key: " ".join(value).replace("  ", " ").replace(dud, "")
        for key, value in headings.items()
    }


class Doc(pc.Base):
    heading: str
    description: str
    href: str


out = {}
from pcweb.component_list import component_list

for key in component_list:
    for component_group in component_list[key]:
        path = f"/docs/library/{key.lower()}/{component_group[0].__name__.lower()}"
        comp = multi_docs(path=path, component_list=component_group).component()
        texts = get_text(comp, path)
        out |= postprocess(texts)

for route in routes:
    comp = route.component()
    texts = get_text(comp, route.path)
    out |= postprocess(texts)

import json
import os
import sys
import typesense

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


docs = []
for key, text in out.items():
    docs.append({"heading": key[0], "description": text, "href": key[1]})

for doc in docs:
    print(doc)
    client.collections["search-auto"].documents.create(doc)
