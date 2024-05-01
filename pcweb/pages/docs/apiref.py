import reflex as rx
from pcweb.templates.docpage import docpage

from .source import Source, generate_docs

modules = [
    rx.App,
    rx.Base,
    rx.Component,
    rx.ComponentState,
    rx.Config,
    rx.event.Event,
    rx.event.EventHandler,
    rx.event.EventSpec,
    rx.Model,
    # rx.testing.AppHarness,
    rx.state.StateManager,
    # rx.state.BaseState,
    rx.State,
    rx.Var,
]

pages = []
for module in modules:
    s = Source(module=module)
    name = module.__name__.lower()
    docs = generate_docs(name, s)
    title = name.replace("_", " ").title()
    page_data = docpage(f"/docs/api-reference/{name}", title)(docs)
    page_data.title = page_data.title.split('·')[0].strip()
    pages.append(page_data)
