import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import (
    docalert,
    doccode,
    docheader,
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
def theming():
    return pc.box(
        docheader("Theming", first=True),
        doctext(
            "You can also add a dark mode toggle by adding ",
            pc.code("pc.toggle_color_mode"),
            " to an event trigger. This will change the whole app to dark mode. ",
        ),
        doctext(
            "Here is an example of a button that will change the app to dark mode:",
        ),
        doccode(
            """
            pc.button(
                pc.icon(tag="moon"),
                on_click=pc.toggle_color_mode,
            )
            """
        ),
        docalert(
            "Any custom colors you add will not be overwritten by the dark mode toggle.",
            status="warning",
        ),
        doctext("More theming options are coming soon!"),
    )
