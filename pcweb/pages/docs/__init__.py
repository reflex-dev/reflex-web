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
from reflex.compiler import compiler

from .gallery import gallery
from .library import library
from .resources import resources


def should_skip_compile(doc: flexdown.Document, prefix: str=""):
    """Skip compilation if the markdown file has not been modified since the last compilation."""
    if not os.environ.get("REFLEX_PERSIST_WEB_DIR", False):
        return False
    os.environ["REFLEX_PERSIST_WEB_DIR"] = "1"
    # Check if the doc has been compiled already.
    compiled_output = f".web/pages/{doc.replace('.md', '.js').replace('library/', f'library/{prefix}')}"
    # Get the timestamp of the compiled file.
    compiled_time = (
        os.path.getmtime(compiled_output) if os.path.exists(compiled_output) else 0
    )
    # Get the timestamp of the source file.
    source_time = os.path.getmtime(doc)
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


def get_components_from_metadata(current_doc):
    components = []
    for comp_str in current_doc.metadata.get("components", []):
        component = eval(comp_str)
        if isinstance(component, type):
            components.append(component)
        elif hasattr(component, "__self__"):
            components.append(component.__self__)
        elif isinstance(component, SimpleNamespace) and hasattr(component, "__call__"):
            components.append(component.__call__.__self__)
    return components


flexdown_docs = flexdown.utils.get_flexdown_files("docs/")

chakra_components = defaultdict(list)
radix_components = defaultdict(list)
component_list = defaultdict(list)
docs_ns = SimpleNamespace()


def exec_blocks(doc, href):
    """Execute the exec and demo blocks in the document."""
    source = doc.content
    env = doc.metadata.copy()
    env["__xd"] = xd
    env["__exec"] = True
    blocks = xd.get_blocks(source, href)
    # Get only the exec and demo blocks.
    blocks = [b for b in blocks if b.__class__.__name__ in ["ExecBlock", "DemoBlock"]]
    for block in blocks:
        block.render(env)

outblocks = []

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
    d = flexdown.parse_file(doc)
    if doc.startswith("docs/library/chakra"):
        if should_skip_compile(doc):
            outblocks.append((d, route))
            return
        clist = [title, *get_components_from_metadata(d)]
        component_list[category].append(clist)
        return multi_docs(path=route, comp=d, component_list=clist, title=title2)
    if doc.startswith("docs/library"):
        clist = [title, *get_components_from_metadata(d)]
        if issubclass(
            clist[1],
            (RadixThemesComponent, RadixPrimitiveComponent),
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
            outblocks.append((d, route))
            return
        return multi_docs(path=route, comp=d, component_list=clist, title=title2)

    if should_skip_compile(doc):
        outblocks.append((d, route))
        return

    return docpage(set_path=route, t=to_title_case(title))(
        lambda d=d, doc=doc: (d, doc)
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
        doc_routes.append(comp)

for name, ns in docs_ns.__dict__.items():
    locals()[name] = ns
