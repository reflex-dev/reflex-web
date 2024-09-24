import reflex as rx
import flexdown
from pcweb.flexdown import xd2 as xd
from pcweb.templates.gallery_app_page import gallery_app_page


def content(document):
    return (
        rx.box(
            xd.render(document, "blog.md"),
        ),
    )


GALLERY_APPS_PATH = "gallery-apps/"


def get_gallery_apps(paths):
    gallery_apps = {}
    for path in reversed(sorted(paths)):
        document = flexdown.parse_file(path)
        path = path.replace(".md", "/")
        gallery_apps[path] = document
    return gallery_apps


def get_route(path: str):
    """Get the route for a page."""
    return path.replace(GALLERY_APPS_PATH, "").replace(".md", "")


paths = flexdown.utils.get_flexdown_files(GALLERY_APPS_PATH)
gallery_apps_data = get_gallery_apps(paths)

gallery_apps_routes = []
for path, document in gallery_apps_data.items():
    # Get the docpage component.
    route = f"/gallery/{document.metadata['title'].replace(' ', '-').lower()}"
    title = rx.utils.format.to_snake_case(path.rsplit("/", 1)[1].replace(".md", ""))
    comp = gallery_app_page(
        path=route,
        title=document.metadata["title"],
        description=document.metadata["description"],
        image=document.metadata["image"],
        demo=document.metadata["demo"],
        meta=document.metadata["meta"],
    )(lambda doc=document: content(document))

    # # Add the route to the list of routes.
    gallery_apps_routes.append(comp)

print(gallery_apps_routes)
