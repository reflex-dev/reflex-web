import os
from collections import defaultdict
from types import SimpleNamespace

import reflex as rx
import flexdown

from pcweb.flexdown import xd
from pcweb.pages.docs.component import multi_docs
from pcweb.route import Route
from pcweb.templates.docpage import docpage, get_toc
from pcweb.whitelist import _check_whitelisted_path
from reflex.components.chakra.base import ChakraComponent
from reflex.components.radix.primitives.base import RadixPrimitiveComponent
from reflex.components.radix.themes.base import RadixThemesComponent

from .gallery import gallery
from .library import library
from .recipes_overview import overview
from .resources import resources
from .custom_components import custom_components
from .apiref import pages as apiref_pages


def should_skip_compile(doc: flexdown.Document):
    """Skip compilation if the markdown file has not been modified since the last compilation."""
    if not os.environ.get("REFLEX_PERSIST_WEB_DIR", False):
        return False

    # Check if the doc has been compiled already.
    compiled_output = f".web/pages/{doc.replace('.md', '.js')}"
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


flexdown_docs = [
    doc.replace("\\", "/") for doc in flexdown.utils.get_flexdown_files("docs/")
]

chakra_components = defaultdict(list)
component_list = defaultdict(list)
recipes_list = defaultdict(list)
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
    route = rx.utils.format.to_kebab_case(f"/{doc.replace('.md', '')}")
    title2 = to_title_case(title)
    category = os.path.basename(os.path.dirname(doc)).title()

    if not _check_whitelisted_path(route):
        return

    d = flexdown.parse_file(doc)

    if doc.startswith("docs/library/chakra"):
        if should_skip_compile(doc):
            outblocks.append((d, route))
            return
        clist = [title, *get_components_from_metadata(d)]
        chakra_components[category].append(clist)
        return multi_docs(path=route, comp=d, component_list=clist, title=title2)
    if doc.startswith("docs/library"):
        clist = [title, *get_components_from_metadata(d)]
        if issubclass(
            clist[1],
            (RadixThemesComponent, RadixPrimitiveComponent),
        ):
            component_list[category].append(clist)
        elif issubclass(clist[1], ChakraComponent):
            # Workaround for Chakra components outside of chakra directory (like Html).
            component_list[category].append(clist)
            route = route.replace("library/", "library/chakra/")
        else:
            component_list[category].append(clist)
        if should_skip_compile(doc):
            outblocks.append((d, route))
            return
        return multi_docs(path=route, comp=d, component_list=clist, title=title2)

    if should_skip_compile(doc):
        outblocks.append((d, route))
        return

    return docpage(set_path=route, t=to_title_case(title))(
        lambda d=d, doc=doc: (get_toc(d, doc), xd.render(d, doc))
    )


doc_routes = [gallery, library, resources, custom_components, overview] + apiref_pages

for api_route in apiref_pages:
    title = rx.utils.format.to_snake_case(api_route.title)
    build_nested_namespace(docs_ns, ["api_reference"], title, api_route)

for doc in sorted(flexdown_docs):
    path = doc.split("/")[1:-1]
    title = rx.utils.format.to_snake_case(os.path.basename(doc).replace(".md", ""))
    title2 = to_title_case(title)
    route = rx.utils.format.to_kebab_case(f"/{doc.replace('.md', '')}")
    comp = get_component(doc, title)

    if path[0] == "library" and isinstance(library, Route):
        locals()["library_"] = library

    # Add the component to the nested namespaces.
    build_nested_namespace(
        docs_ns, path, title, Route(path=route, title=title2, component=lambda: "")
    )

    if comp is not None:
        if isinstance(comp, tuple):
            for c in comp:
                doc_routes.append(c)
        else:
            doc_routes.append(comp)


for doc in flexdown_docs:
    if 'recipes' in doc:
        category = doc.split('/')[2]
        recipes_list[category].append(doc)

for name, ns in docs_ns.__dict__.items():
    locals()[name] = ns
