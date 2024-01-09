from collections import defaultdict
from types import SimpleNamespace

import flexdown

import reflex as rx
from pcweb.flexdown import xd
from pcweb.templates.docpage import docpage

from .gallery import gallery
from .library import library
from .resources import resources

doc_routes = [gallery, library, resources]


def to_title_case(text: str) -> str:
    return " ".join(word.capitalize() for word in text.split("_"))


from pcweb.pages.docs.component import multi_docs

flexdown_docs = flexdown.utils.get_flexdown_files("docs/")

chakra_components = defaultdict(list)
component_list = defaultdict(list)

for doc in sorted(flexdown_docs):
    if doc.endswith("-style.md"):
        continue

    # Get the docpage component.
    route = f"/{doc.replace('.md', '')}"
    title = rx.utils.format.to_snake_case(doc.rsplit("/", 1)[1].replace(".md", ""))
    category = doc.split("/")[-2].title()
    d = flexdown.parse_file(doc)
    if doc.startswith("docs/library/chakra"):
        clist = [eval(c) for c in d.metadata["components"]]
        chakra_components[category].append(clist)
        comp = multi_docs(path=route, comp=d, component_list=clist)
    elif doc.startswith("docs/library"):
        clist = [eval(c) for c in d.metadata["components"]]
        component_list[category].append(clist)
        comp = multi_docs(path=route, comp=d, component_list=clist)
    else:
        comp = docpage(set_path=route, t=to_title_case(title))(
            lambda doc=doc: xd.render_file(doc)
        )

    # Get the namespace.
    namespace = rx.utils.format.to_snake_case(doc.split("/")[1])

    # Create a namespace if it doesn't exist.
    if namespace not in locals():
        locals()[namespace] = SimpleNamespace()

    # Add the component to the namespace.
    setattr(locals()[namespace], title, comp)

    # Add the route to the list of routes.
    doc_routes.append(comp)
