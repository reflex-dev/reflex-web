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
            "The HTML component can be used to render raw HTML code. ",
            "It takes in a string of HTML code and renders it.",
        ),
        doctext(
            "Before you reach for this component, consider using Reflex's raw HTML element support instead."
        ),
        docdemo(example),
        doctext(
            "Here is another example of the HTML component. In this example, we render an image."
        ),
        docdemo(example2),
    )
