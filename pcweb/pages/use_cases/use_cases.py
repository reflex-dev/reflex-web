import flexdown
import reflex as rx
from pcweb.flexdown import xd2 as xd

from pcweb.templates.highlightpage import highlight_page

document = flexdown.parse_file("pcweb/pages/use_cases/use_cases.md")


def use_cases_content() -> rx.Component:
    return rx.box(xd.render(document, document.filename))


@highlight_page(path="/use-cases", title="Use Cases - Reflex")
def use_cases_page():
    return use_cases_content()
