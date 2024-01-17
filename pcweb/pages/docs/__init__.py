from collections import defaultdict
from types import SimpleNamespace

import flexdown

import reflex as rx
from pcweb.flexdown import xd
from pcweb.pages.docs.component import multi_docs
from pcweb.templates.docpage import docpage

from .gallery import gallery
from .library import library
from .resources import resources

doc_routes = [gallery, library, resources]


def to_title_case(text: str) -> str:
    return " ".join(word.capitalize() for word in text.split("_"))


flexdown_docs = flexdown.utils.get_flexdown_files("docs/")

chakra_components = defaultdict(list)
radix_components = defaultdict(list)
component_list = defaultdict(list)
from reflex.components.radix.themes.base import RadixThemesComponent
import os
from pcweb.route import Route


def should_skip_compile(doc, prefix=""):
    # Check if the doc has been compiled already.
    compiled_output = f".web/pages/{doc.replace('.md', '.js').replace('library/', f'library/{prefix}')}"
    # Get the timestamp of the compiled file.
    compiled_time = (
        os.path.getmtime(compiled_output) if os.path.exists(compiled_output) else 0
    )
    # Get the timestamp of the source file.
    source_time = os.path.getmtime(doc)
    return compiled_time > source_time


for doc in sorted(flexdown_docs):
    if doc.endswith("-style.md"):
        continue

    # Get the docpage component.
    route = f"/{doc.replace('.md', '')}"
    title = rx.utils.format.to_snake_case(doc.rsplit("/", 1)[1].replace(".md", ""))
    category = doc.split("/")[-2].title()

    # Skip the doc if it has already been compiled.
    if doc.startswith("docs/library/chakra"):
        if should_skip_compile(doc):
            continue
        d = flexdown.parse_file(doc)
        clist = [title, *[eval(c) for c in d.metadata["components"]]]
        component_list[category].append(clist)
        comp = multi_docs(path=route, comp=d, component_list=clist, title=title)
    elif doc.startswith("docs/library"):
        d = flexdown.parse_file(doc)
        clist = [title, *[eval(c) for c in d.metadata["components"]]]
        if issubclass(clist[1], RadixThemesComponent):
            radix_components[category].append(clist)
            route = route.replace("library/", "library/radix/")
            prefix = "radix/"
        else:
            component_list[category].append(clist)
            prefix = ""
        if should_skip_compile(doc, prefix=prefix):
            continue
        comp = multi_docs(path=route, comp=d, component_list=clist, title=title)
    else:
        # Get the namespace.
        namespace = rx.utils.format.to_snake_case(doc.split("/")[1])

        # Create a namespace if it doesn't exist.
        if namespace not in locals():
            locals()[namespace] = SimpleNamespace()

        # Add the component to the namespace.
        setattr(locals()[namespace], title, Route(path=route, title="", component=lambda: ""))

        if should_skip_compile(doc):
            continue

        d = flexdown.parse_file(doc)
        comp = docpage(set_path=route, t=to_title_case(title))(
            lambda d=d, doc=doc: xd.render(d, doc)
        )

    # Add the route to the list of routes.
    doc_routes.append(comp)
