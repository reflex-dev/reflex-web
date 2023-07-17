import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo, doctext

example = """rx.vstack(
    rx.html("<h1>Hello World</h1>"),
    rx.html("<h2>Hello World</h2>"),
    rx.html("<h3>Hello World</h3>"),
    rx.html("<h4>Hello World</h4>"),
    rx.html("<h5>Hello World</h5>"),
    rx.html("<h6>Hello World</h6>"),
)
"""

example2 = """ rx.vstack(
    rx.html("<img src='https://reflex.dev/reflex_banner.png' />"),
)
"""


def render_html():
    return rx.vstack(
        doctext(
            "The html component can be used to render raw html code.",
            "This is useful for rendering html code that is not supported by the reflex library.",
            "It takes in a string of html code and renders it.",
        ),
        docdemo(example),
        doctext(
            "Here is another example of the html component. In this example, we render an image."
        ),
        docdemo(example2),
    )
