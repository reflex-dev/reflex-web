import pynecone as pc

from pcweb.templates.docpage import docpage
from .source import Source, generate_docs


s = Source(module=pc.Component)


@docpage()
def component():
    return generate_docs("Component", s)
