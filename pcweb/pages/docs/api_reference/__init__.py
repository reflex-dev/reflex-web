from .cli import cli
from .special_events import special_events
from .event_triggers import event_triggers

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
    rx.Middleware,
    rx.middleware.HydrateMiddleware,
    rx.State,
    rx.Var,
]

for module in modules:
    s = Source(module=module)
    name = module.__name__.lower()
    docs = generate_docs(name, s)
    title = name.replace("_", " ").title()
    locals()[f"{name}_ref"] = docpage(f"/docs/api-reference/{name}", title)(docs)
