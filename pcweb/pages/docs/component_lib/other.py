import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo, doctext

example = """pc.vstack(
    pc.html("<h1>Hello World</h1>"),
    pc.html("<h2>Hello World</h2>"),
    pc.html("<h3>Hello World</h3>"),
    pc.html("<h4>Hello World</h4>"),
    pc.html("<h5>Hello World</h5>"),
    pc.html("<h6>Hello World</h6>"),
)
"""

example2 = """ pc.vstack(
    pc.html("<img src='https://pynecone.io/logo.png' />"),
)
"""

def render_html():
    return pc.vstack(
        doctext(
            "The html component can be used to render raw html code.",
            "This is useful for rendering html code that is not supported by the pynecone library.",
            "It takes in a string of html code and renders it.",
        ),
        docdemo(example),
        doctext(
            "Here is another example of the html component. In this example, we render an image."
        ),
        docdemo(example2),
    )