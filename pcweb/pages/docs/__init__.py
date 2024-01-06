from pcweb.route import Route
from .advanced_guide import *
from .api_reference import *
from .component_lib import *
from .gallery import gallery
from .recipes import *
from .library import library
from .resources import resources

doc_routes = [r for r in locals().values() if isinstance(r, Route)]

from types import SimpleNamespace
from pcweb.templates.docpage import docpage, component_docpage
import flexdown

flexdown_docs = flexdown.utils.get_flexdown_files("docs/")
for doc in flexdown_docs:
    if doc.startswith("docs/library/chakra"):
        continue
    if doc.endswith("-style.md"):
        continue

    # Get the docpage component.
    route = f"/{doc.replace('.md', '')}"
    title = rx.utils.format.to_snake_case(doc.rsplit("/", 1)[1].replace(".md", ""))
    if doc.startswith("docs/library"):
        comp = component_docpage(set_path=route.strip("/"), t=rx.utils.format.to_title_case(title))
    else:
        comp = docpage(set_path=route, t=rx.utils.format.to_title_case(title))(lambda doc=doc: flexdown.render_file(doc))


    # Get the namespace.
    namespace = rx.utils.format.to_snake_case(doc.split("/")[1])

    # Create a namespace if it doesn't exist.
    if namespace not in locals():
        locals()[namespace] = SimpleNamespace()

    # Add the component to the namespace.
    setattr(locals()[namespace], title, comp)

    # Add the route to the list of routes.
    doc_routes.append(comp)