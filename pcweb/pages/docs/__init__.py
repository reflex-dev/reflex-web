import os
from collections import defaultdict
from types import SimpleNamespace

import reflex as rx
import flexdown

from pcweb.flexdown import xd
from pcweb.pages.docs.component import multi_docs
from pcweb.route import Route
from pcweb.templates.docpage import docpage
from reflex.components.chakra.base import ChakraComponent
from reflex.components.radix.primitives.base import RadixPrimitiveComponent
from reflex.components.radix.themes.base import RadixThemesComponent

from .gallery import gallery
from .library import library
from .resources import resources

def should_skip_compile(doc, prefix=""):
    # Check if the doc has been compiled already.
    compiled_output = f".web/pages/{doc.replace('.md', '.js').replace('library/', f'library/{prefix}')}"
    # Get the timestamp of the compiled file.
    compiled_time = (
        os.path.getmtime(compiled_output) if os.path.exists(compiled_output) else 0
    )
    # Get the timestamp of the source file.
    source_time = os.path.getmtime(doc)
    if compiled_time > source_time:
        return True
    return compiled_time > source_time


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
os.environ["REFLEX_PERSIST_WEB_DIR"] = "1"


def get_component(doc: str, title: str):
    if doc.endswith("-style.md"):
        return

    if doc.endswith("-ll.md"):
        return

    # Get the docpage component.
    doc = doc.replace("\\", "/")
    route = f"/{doc.replace('.md', '')}"
    title2 = to_title_case(title)
    category = os.path.basename(os.path.dirname(doc)).title()
    if doc.startswith("docs/library/chakra"):
        if should_skip_compile(doc):
            return
        d = flexdown.parse_file(doc)
        clist = [title, *[eval(c) for c in d.metadata["components"]]]
        component_list[category].append(clist)
        return multi_docs(path=route, comp=d, component_list=clist, title=title2)
    if doc.startswith("docs/library"):
        d = flexdown.parse_file(doc)
        clist = [title, *[eval(c) for c in d.metadata["components"]]]
        if issubclass(
            clist[1],
            (RadixIconComponent, RadixThemesComponent, RadixPrimitiveComponent),
        ):
            radix_components[category].append(clist)
            prefix=""
        elif issubclass(clist[1], ChakraComponent):
            # Workaround for Chakra components outside of chakra directory (like Html).
            component_list[category].append(clist)
            route = route.replace("library/", "library/chakra/")
            prefix = ""
        else:
            component_list[category].append(clist)
            prefix = ""
        if should_skip_compile(doc, prefix=prefix):
            return
        return multi_docs(path=route, comp=d, component_list=clist, title=title2)

    if should_skip_compile(doc):
        return

    d = flexdown.parse_file(doc)
    return docpage(set_path=route, t=to_title_case(title))(
        lambda d=d, doc=doc: xd.render(d, doc)
    )


doc_routes = [gallery, library, resources]


for doc in sorted(flexdown_docs):
    path = doc.split("/")[1:-1]
    title = rx.utils.format.to_snake_case(os.path.basename(doc).replace(".md", ""))
    title2 = to_title_case(title)
    route = f"/{doc.replace('.md', '')}"
    comp = get_component(doc, title)

    if path[0] == "library" and isinstance(library, Route):
        locals()["library_"] = library

    # Add the component to the nested namespaces.
    build_nested_namespace(docs_ns, path, title, Route(path=route, title=title2, component=lambda: ""))

    # Add the route to the list of routes.
    if comp:
        print("Adding route", route, "to doc_routes")
        doc_routes.append(comp)

for name, ns in docs_ns.__dict__.items():
    locals()[name] = ns
