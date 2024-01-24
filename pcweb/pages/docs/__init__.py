import os
from collections import defaultdict
from types import SimpleNamespace

import flexdown

import reflex as rx
from pcweb.flexdown import xd
from pcweb.pages.docs.component import multi_docs
from pcweb.route import Route
from pcweb.templates.docpage import docpage
from reflex.components.chakra.base import ChakraComponent
from reflex.components.radix.themes.base import RadixThemesComponent
from reflex.components.radix.primitives.base import RadixPrimitiveComponent

from .gallery import gallery
from .library import library
from .resources import resources

doc_routes = [gallery, library, resources]


def to_title_case(text: str) -> str:
    return " ".join(word.capitalize() for word in text.split("_"))


def build_nested_namespace(
    parent_namespace: SimpleNamespace, path: list, title: str, comp
):
    namespace = rx.utils.format.to_snake_case(path[0])

    if (
        isinstance(parent_namespace, SimpleNamespace)
        and getattr(parent_namespace, namespace, None) is None
    ):
        setattr(parent_namespace, namespace, SimpleNamespace())

    nested_namespace = getattr(parent_namespace, namespace)

    if len(path) == 1:
        setattr(nested_namespace, title, comp)
    else:
        setattr(
            parent_namespace,
            namespace,
            build_nested_namespace(
                nested_namespace,
                path[1:],
                title,
                comp,
            ),
        )
    return parent_namespace


flexdown_docs = flexdown.utils.get_flexdown_files("docs/")

chakra_components = defaultdict(list)
radix_components = defaultdict(list)
component_list = defaultdict(list)
from reflex.components.chakra.base import ChakraComponent
from reflex.components.radix.themes.base import RadixThemesComponent
from reflex.components.radix.themes.components.icons import RadixIconComponent

docs_ns = SimpleNamespace()

for doc in sorted(flexdown_docs):
    if doc.endswith("-style.md"):
        continue

    # Get the docpage component.
    route = f"/{doc.replace('.md', '')}"
    path = doc.split("/")[1:-1]
    title = rx.utils.format.to_snake_case(os.path.basename(doc).replace(".md", ""))
    category = os.path.basename(os.path.dirname(doc)).title()
    d = flexdown.parse_file(doc)
    if doc.startswith("docs/library/chakra"):
        clist = [title, *[eval(c) for c in d.metadata["components"]]]
        component_list[category].append(clist)
        comp = multi_docs(path=route, comp=d, component_list=clist, title=title)
    elif doc.startswith("docs/library"):
        clist = [title, *[eval(c) for c in d.metadata["components"]]]
        if issubclass(clist[1], (RadixIconComponent, RadixThemesComponent, RadixPrimitiveComponent)):
            radix_components[category].append(clist)
            route = route.replace("library/", "library/radix/")
        elif issubclass(clist[1], ChakraComponent):
            # Workaround for Chakra components outside of chakra directory (like Html).
            component_list[category].append(clist)
            route = route.replace("library/", "library/chakra/")
        else:
            component_list[category].append(clist)
        comp = multi_docs(path=route, comp=d, component_list=clist, title=title)
    else:
        comp = docpage(set_path=route, t=to_title_case(title))(
            lambda d=d, doc=doc: xd.render(d, doc)
        )

    # Get the namespace.
    namespace = rx.utils.format.to_snake_case(doc.split("/")[1])
    # Create a namespace if it doesn't exist.

    if path[0] == "library" and isinstance(library, Route):
        locals()["library_"] = library

    # Add the component to the nested namespaces.
    build_nested_namespace(docs_ns, path, title, comp)

    # Add the route to the list of routes.
    doc_routes.append(comp)

for name, ns in docs_ns.__dict__.items():
    locals()[name] = ns
