import reflex as rx
from flexdown.document import Document

from pcweb.flexdown import xd2 as xd
from pcweb.templates.highlightpage import highlight_page

document = Document.from_file("pcweb/pages/use_cases/use_cases.md")


def use_cases_content() -> rx.Component:
    return rx.box(
        rx.el.h1(
            "Use Cases by Industry",
            class_name="text-slate-12 text-4xl font-bold mb-6 text-center",
        ),
        xd.render(document, document.filename),
    )


@highlight_page(
    path="/use-cases",
    title="Use Cases by Industry - Reflex",
    description="How organizations use Reflex for finance, healthcare, government, and consulting. Python web apps for dashboards, CRUD, and internal tools.",
)
def use_cases_page():
    return use_cases_content()
