import flexdown
import reflex as rx
from flexdown.document import Document

from pcweb.flexdown import xd2 as xd
from pcweb.templates.storypage import storypage


def content(document):
    return (
        rx.box(
            xd.render(document, document.filename),
        ),
    )


CUSTOMERS_PATH = "case-studies/"


def get_customer_data(paths):
    customers = {}
    for path in sorted(paths, reverse=True):
        document = Document.from_file(path)
        path = str(path).replace(".md", "/")
        customers[path] = document
    return customers


def get_route(path: str):
    """Get the route for a page."""
    return path.replace(CUSTOMERS_PATH, "").replace(".md", "")


paths = flexdown.utils.get_flexdown_files(CUSTOMERS_PATH)
customer_data = get_customer_data(paths)

customers_routes = []
for path, document in customer_data.items():
    # Get the docpage component.
    route = f"/customers/{document.metadata['company'].lower()}"
    title = rx.utils.format.to_snake_case(path.rsplit("/", 1)[1].replace(".md", ""))
    comp = storypage(
        path=route,
        company=document.metadata["company"],
        description=document.metadata["description"],
        domain=document.metadata["domain"],
        founded=document.metadata["founded"],
        investors=document.metadata["investors"],
        stats=document.metadata["stats"],
        meta=document.metadata["meta"],
    )(lambda doc=document: content(doc))

    # # Add the route to the list of routes.
    customers_routes.append(comp)
