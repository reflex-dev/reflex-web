import pynecone as pc

from pcweb.templates.docpage import docpage
from .source import Source, generate_docs


s = Source(module=pc.Config)


@docpage()
def config():
    return generate_docs("Config", s)
