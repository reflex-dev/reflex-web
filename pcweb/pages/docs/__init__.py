from pcweb.route import Route
from .advanced_guide import *
from .api_reference import *
from .components import *
from .component_lib import *
from .database import *
from .gallery import gallery
from .getting_started import *
from .hosting import *
from .recipes import *
from .library import library
from .styling import *
from .resources import resources
from .tutorial import *
from .wrapping_react import *
from .datatable_tutorial import *
from .assets import *
from .dynamic_rendering import *
from .pages import *
from .ui_overview import ui_overview
from .events import *
from .vars import *
from .substates import *
from .utility_methods import *
from .state_overview import state_overview
from .api_routes import *
from .client_storage import *
from .conditional_rendering import conditional_rendering
from .rendering_iterables import rendering_iterables

doc_routes = [r for r in locals().values() if isinstance(r, Route)]
doc_routes = [gallery, library, resources]


def to_title_case(text: str) -> str:
    return " ".join(word.capitalize() for word in text.split("_"))


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
        comp = multi_docs(path=route, comp=d, component_list=clist, title=title)
    elif doc.startswith("docs/library"):
        clist = [eval(c) for c in d.metadata["components"]]
        component_list[category].append(clist)
        comp = multi_docs(path=route, comp=d, component_list=clist, title=title)
    else:
        comp = docpage(set_path=route, t=to_title_case(title))(
            lambda doc=d: xd.render(doc)
        )
        # Get the namespace.
        namespace = rx.utils.format.to_snake_case(doc.split("/")[1])
        # Create a namespace if it doesn't exist.
        if namespace not in locals():
            locals()[namespace] = SimpleNamespace()
            print(doc, "->", locals()[namespace].path)

        # Add the component to the namespace.
        setattr(locals()[namespace], title, comp)

    # Add the route to the list of routes.
    doc_routes.append(comp)
