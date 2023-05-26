import pynecone as pc

from pcweb.templates.docpage import docpage
from .source import Source, generate_docs


s = Source(module=pc.Base)


@docpage()
def base():
    return generate_docs("Base", s)
