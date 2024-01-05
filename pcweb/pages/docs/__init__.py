from pcweb.route import Route
from .advanced_guide import *
from .api_reference import *
from .components import *
from .component_lib import *
from .database import *
from .gallery import gallery

# from .getting_started import *
from .hosting import *
from .recipes import *
from .library import *
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

from types import SimpleNamespace
from pcweb.templates.docpage import docpage
import flexdown

getting_started = SimpleNamespace()
flexdown_docs = flexdown.utils.get_flexdown_files("docs/")
for doc in flexdown_docs:
    if not doc.startswith("docs/getting-started") and not doc.startswith("docs/tutorial"):
        continue
    route = f"/{doc.replace('.md', '')}"
    title = rx.utils.format.to_snake_case(doc.rsplit("/", 1)[1].replace(".md", ""))
    comp = docpage(set_path=route, t=rx.utils.format.to_title_case(title))(lambda doc=doc: flexdown.render_file(doc))
    setattr(getting_started, title, comp)
    doc_routes.append(comp)
