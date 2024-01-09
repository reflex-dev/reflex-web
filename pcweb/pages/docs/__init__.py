from collections import defaultdict

import reflex as rx
from pcweb.route import Route

from .gallery import gallery
from .library import library
from .resources import resources

doc_routes = [r for r in locals().values() if isinstance(r, Route)]

from types import SimpleNamespace

import flexdown

from pcweb.flexdown import xd
from pcweb.templates.docpage import component_docpage, docpage


def to_title_case(text: str) -> str:
    return " ".join(word.capitalize() for word in text.split("_"))


from pcweb.pages.docs.component import multi_docs

flexdown_docs = flexdown.utils.get_flexdown_files("docs/")

chakra_components = defaultdict(list)

for doc in sorted(flexdown_docs):
    if doc.endswith("-style.md"):
        continue

    # Get the docpage component.
    route = f"/{doc.replace('.md', '')}"
    title = rx.utils.format.to_snake_case(doc.rsplit("/", 1)[1].replace(".md", ""))
    if doc.startswith("docs/library/chakra"):
        d = flexdown.parse_file(doc)
        category = doc.split("/")[-2].title()
        component_list = [eval(c) for c in d.metadata["components"]]
        chakra_components[category].append(component_list)
        comp = multi_docs(path=route, comp=d, component_list=component_list)
    elif doc.startswith("docs/library"):
        comp = component_docpage(set_path=route.strip("/"), t=to_title_case(title))
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
