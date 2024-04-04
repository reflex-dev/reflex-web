import reflex as rx
from pcweb.templates.docpage import docpage

from .source import Source, generate_docs

modules = [
    rx.App,
    rx.Base,
    rx.Component,
    rx.Config,
    rx.event.Event,
    rx.event.EventHandler,
    rx.event.EventSpec,
    rx.Model,
    rx.State,
    rx.Var,
]

pages = []
for module in modules:
    s = Source(module=module)
    name = module.__name__.lower()
    docs = generate_docs(name, s)
    title = name.replace("_", " ").title()
    pages.append(docpage(f"/docs/api-reference/{name}", title)(docs))
