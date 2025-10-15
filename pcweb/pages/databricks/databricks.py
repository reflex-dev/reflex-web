import reflex as rx
from flexdown.document import Document

from pcweb.flexdown import xd2 as xd
from pcweb.templates.highlightpage import highlight_page

document = Document.from_file("pcweb/pages/databricks/databricks.md")


def databricks_content() -> rx.Component:
    return rx.box(xd.render(document, document.filename))


@highlight_page(path="/databricks", title="Databricks - Reflex")
def databricks_page():
    return databricks_content()
