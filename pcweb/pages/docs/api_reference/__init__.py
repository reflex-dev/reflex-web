from .cli import cli
from .special_events import special_events
from .event_triggers import event_triggers

import pynecone as pc

from pcweb.templates.docpage import docpage
from .source import Source, generate_docs


modules = [
    pc.App,
    pc.Base,
    pc.Component,
    pc.Config,
    pc.event.Event,
    pc.event.EventHandler,
    pc.event.EventSpec,
    pc.Model,
    pc.Middleware,
    pc.middleware.HydrateMiddleware,
    pc.State,
    pc.Var,
]

for module in modules:
    s = Source(module=module)
    name = module.__name__.lower()
    docs = generate_docs(name, s)
    title = f"{name.replace('_', ' ').title()} | Pynecone"
    locals()[f"{name}_ref"] = docpage(f"/docs/api-reference/{name}", title)(docs)
