from .cli import cli
from .special_events import special_events
from .event_triggers import event_triggers

import pynecone as pc

from pcweb.templates.docpage import docpage
from .source import Source, generate_docs


modules = [
    pc.Base,
    pc.Component,
    pc.Config,
    pc.Model,
    pc.State,
]

for module in modules:
    s = Source(module=module)
    name = module.__name__.lower()
    docs = generate_docs(name, s)
    print("module", name)
    title = f"{name.replace('_', ' ').title()} | Pynecone"
    locals()[name] = docpage(f"/docs/api-reference/{name}", title)(docs)
