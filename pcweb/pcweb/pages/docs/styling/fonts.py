import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import (
    doccode,
    docdemo,
    docheader,
    doclink,
    docpage,
    doctext,
)

code1 = """pc.text(
    "Check out my font",
    font_family="Silkscreen",
    font_size="1.5em",
)
"""


@docpage()
def fonts():
    return pc.box(
        docheader("Fonts", first=True),
        doctext(
            "You can add different fonts to your app by linking the stylesheet to your app."
        ),
        doctext(
            "In this example, we will use the ",
            doclink("Silkscreen", href="https://fonts.google.com/specimen/Silkscreen"),
            " font from Google Fonts.",
        ),
        doctext(
            "You can pass a list of stylesheets to your app, and they will be available. ",
        ),
        doccode(
            """app = pc.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Silkscreen&display=swap",
    ],
)"""
        ),
        doctext(
            "Then you can use the font in your app by setting the ",
            pc.code("font_family"),
            " prop.",
        ),
        docdemo(code1),
    )
