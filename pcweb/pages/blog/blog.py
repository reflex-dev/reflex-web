import reflex as rx
from pcweb.templates.webpage import webpage
from .page import page
from .paths import blog_data
from .gallery import blogs

blog_routes = [blogs]
for path, document in blog_data.items():
    # Get the docpage component.
    route = f"/{path.replace('.md', '')}"
    title = rx.utils.format.to_snake_case(path.rsplit("/", 1)[1].replace(".md", ""))
    comp = webpage(path=route, title=document.metadata["title"]+ " · Reflex Blog")(
        lambda doc=document: page(doc, route)
    )

    # Add the route to the list of routes.
    blog_routes.append(comp)
