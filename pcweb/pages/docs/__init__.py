import os
from collections import defaultdict
from pathlib import Path
from types import SimpleNamespace

import reflex as rx
import flexdown
from flexdown.document import Document

# External Components
from reflex_pyplot import pyplot as pyplot

from pcweb.flexdown import xd
from pcweb.pages.docs.component import multi_docs
from pcweb.route import Route
from pcweb.templates.docpage import docpage, get_toc
from pcweb.whitelist import _check_whitelisted_path

from .library import library
from .recipes_overview import overview
from .custom_components import custom_components
from .apiref import pages as apiref_pages
from .cloud_cliref import pages as cloud_cliref_pages
from pcweb.pages.library_previews import components_previews_pages
from .cloud import pages as cloud_pages


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
            components.append((component, comp_str))
        elif hasattr(component, "__self__"):
            components.append((component.__self__, comp_str))
        elif isinstance(component, SimpleNamespace) and hasattr(component, "__call__"):
            components.append((component.__call__.__self__, comp_str))
        else:
            raise ValueError(f"Invalid component: {component}")

    return components


flexdown_docs = [
    str(doc).replace("\\", "/") for doc in flexdown.utils.get_flexdown_files("docs/")
]

graphing_components = defaultdict(list)
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


manual_titles = {
    "docs/database/overview.md": "Database Overview",
    "docs/custom-components/overview.md": "Custom Components Overview",
    "docs/custom-components/command-reference.md": "Custom Component CLI Reference",
    "docs/api-routes/overview.md": "API Routes Overview",
    "docs/client_storage/overview.md": "Client Storage Overview",
    "docs/state_structure/overview.md": "State Structure Overview", 
    "docs/state/overview.md": "State Overview",
    "docs/styling/overview.md": "Styling Overview",
    "docs/ui/overview.md": "UI Overview",
    "docs/wrapping-react/overview.md": "Wrapping React Overview",
    "docs/library/html/html.md": "HTML Elements",
    "docs/recipes-overview.md": "Recipes Overview",
    "docs/events/special_events.md": "Special Events Docs",
    "docs/library/graphing/general/tooltip.md": "Graphing Tooltip",
    "docs/recipes/content/grid.md": "Grid Recipe",
}


def get_component(doc: str, title: str):
    if doc.endswith("-style.md"):
        return

    if doc.endswith("-ll.md"):
        return

    # Get the docpage component.
    doc = doc.replace("\\", "/")
    route = rx.utils.format.to_kebab_case(f"/{doc.replace('.md', '/')}")
    # Handle index files: /folder/index/ -> /folder/
    if route.endswith("/index/"):
        route = route[:-7] + "/"
    if doc in manual_titles.keys():
        title2 = manual_titles[doc]
    else:
        title2 = to_title_case(title)
    category = os.path.basename(os.path.dirname(doc)).title()

    if not _check_whitelisted_path(route):
        return

    d = Document.from_file(doc)

    if doc.startswith("docs/library/graphing"):
        if should_skip_compile(doc):
            outblocks.append((d, route))
            return
        clist = [title, *get_components_from_metadata(d)]
        graphing_components[category].append(clist)
        return multi_docs(path=route, comp=d, component_list=clist, title=title2)
    if doc.startswith("docs/library"):
        clist = [title, *get_components_from_metadata(d)]
        component_list[category].append(clist)
        if should_skip_compile(doc):
            outblocks.append((d, route))
            return
        return multi_docs(path=route, comp=d, component_list=clist, title=title2)

    if should_skip_compile(doc):
        outblocks.append((d, route))
        return

    def comp():
        return (get_toc(d, doc), xd.render(d, doc))

    doc_path = Path(doc)
    doc_module = ".".join(doc_path.parts[:-1])
    doc_file = doc_path.stem

    comp.__module__ = doc_module
    comp.__name__ = doc_file
    comp.__qualname__ = doc_file

    return docpage(set_path=route, t=title2)(comp)


doc_routes = (
    [
        library,
        custom_components,
        overview,
        *components_previews_pages,
    ]
    + apiref_pages
    + cloud_cliref_pages
    # + ai_builder_pages
    + cloud_pages
)

for cloud_page in cloud_pages:
    title = rx.utils.format.to_snake_case(cloud_page.title)
    build_nested_namespace(docs_ns, ["cloud"], title, cloud_page)

for api_route in apiref_pages:
    title = rx.utils.format.to_snake_case(api_route.title)
    build_nested_namespace(docs_ns, ["api_reference"], title, api_route)

for ref in cloud_cliref_pages:
    title = rx.utils.format.to_snake_case(ref.title)
    build_nested_namespace(docs_ns, ["cloud"], title, ref)

for doc in sorted(flexdown_docs):
    path = doc.split("/")[1:-1]

    title = rx.utils.format.to_snake_case(os.path.basename(doc).replace(".md", ""))
    title2 = to_title_case(title)
    route = rx.utils.format.to_kebab_case(f"/{doc.replace('.md', '/')}")
    # Handle index files: /folder/index/ -> /folder/
    if route.endswith("/index/"):
        route = route[:-7] + "/"

    comp = get_component(doc, title)

    # # Check if the path starts with '/docs/cloud/', and if so, replace 'docs' with an empty string
    # if route.startswith("/docs/cloud/"):
    #     route = route.replace("/docs", "")

    if path[0] == "library" and isinstance(library, Route):
        locals()["library_"] = library

    # print(route)

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
    if "recipes" in doc:
        category = doc.split("/")[2]
        recipes_list[category].append(doc)

for name, ns in docs_ns.__dict__.items():
    # if name == "cloud":
    #     print(name, ns)
    locals()[name] = ns

build_nested_namespace(
    docs_ns, 
    ["library", "tables_and_data_grids"], 
    "ag_grid", 
    Route(path="https://reflex.dev/docs/enterprise/ag-grid/", title="AG Grid", component=lambda: "")
)
