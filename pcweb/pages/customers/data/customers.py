import flexdown
import reflex as rx
from flexdown.document import Document

from pcweb.flexdown import xd2 as xd
from pcweb.templates.storypage import CaseStudy, storypage

CUSTOMERS_PATH = "case-studies/"


def content(document):
    return rx.box(xd.render(document, document.filename))


def get_customer_data(paths):
    customers = {}
    for path in sorted(paths, reverse=True):
        document = Document.from_file(path)
        customers[str(path).replace(".md", "/")] = document
    return customers


paths = flexdown.utils.get_flexdown_files(CUSTOMERS_PATH)
customer_data = get_customer_data(paths)

customers_routes = []
for document in customer_data.values():
    study = CaseStudy.from_document(document)
    comp = storypage(study)(lambda doc=document: content(doc))
    customers_routes.append(comp)
