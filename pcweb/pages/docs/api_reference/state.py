import pynecone as pc

from pcweb.templates.docpage import docpage
from .source import Source, generate_docs


s = Source(module=pc.State)


@docpage()
def state_reference():
    return generate_docs("State", s)
