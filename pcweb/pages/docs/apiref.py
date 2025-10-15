import reflex as rx
from reflex.utils.imports import ImportVar

from pcweb.templates.docpage import docpage

from .source import Source, generate_docs

modules = [
    rx.App,
    rx.Base,
    rx.Component,
    rx.ComponentState,
    (rx.Config, rx.config.BaseConfig),
    rx.event.Event,
    rx.event.EventHandler,
    rx.event.EventSpec,
    rx.Model,
    # rx.testing.AppHarness,
    rx.state.StateManager,
    # rx.state.BaseState,
    rx.State,
    ImportVar,
    rx.Var,
]

from .env_vars import env_vars_doc

pages = []
for module in modules:
    if isinstance(module, tuple):
        module, *extra_modules = module
        extra_fields = []
        for extra_module in extra_modules:
            s_extra = Source(module=extra_module)
            extra_fields.extend(s_extra.get_fields())
    else:
        extra_fields = None
    s = Source(module=module)
    name = module.__name__.lower()
    docs = generate_docs(name, s, extra_fields=extra_fields)
    title = name.replace("_", " ").title()
    page_data = docpage(f"/docs/api-reference/{name}/", title)(docs)
    page_data.title = page_data.title.split("·")[0].strip()
    pages.append(page_data)

pages.append(env_vars_doc)
