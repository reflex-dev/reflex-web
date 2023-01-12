import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import (
    doccode,
    docdemo,
    docheader,
    docpage,
    doctext,
    subheader,
)

code1 = """pc.text(
    "Hello World", 
    color=["orange", "red", "purple",  "blue", "green"]
)"""
code2 = """pc.vstack(
    pc.desktop_only(
        pc.text("Desktop View"),
    ),
    pc.tablet_only(
        pc.text("Tablet View"),
    ),
    pc.mobile_only(
        pc.text("Mobile View"),
    ),
    pc.mobile_and_tablet(
        pc.text("Visible on Mobile and Tablet"),
    ),
    pc.tablet_and_desktop(
        pc.text("Visible on Desktop and Tablet"),
    ),
)"""

code3="""
pc.vstack(
    pc.text("Hello World", color="green", display=["none", "none", "none", "none", "flex"]),
    pc.text("Hello World", color="blue", display=["none", "none", "none", "flex", "flex"]),
    pc.text("Hello World", color="red", display=["none", "none", "flex", "flex", "flex"]),
    pc.text("Hello World", color="orange", display=["none", "flex", "flex", "flex", "flex"]),
    pc.text("Hello World", color="yellow", display=["flex", "flex", "flex", "flex", "flex"]),
)
"""


@docpage()
def responsive():
    return pc.box(
        docheader("Responsive", first=True),
        doctext(
            "Pynecone apps can be made responsive to look good on mobile, tablet, and desktop."
        ),
        doctext(
            "You can pass a list of values to any style property to specify it's value on different screen sizes. "
        ),
        docdemo(code1),
        doctext(
            "The text will change color based on your screen size. ",
            "If you are on desktop, try changing the size of your browser window to see the color change.",
        ),
        doctext(
            "The default breakpoints are shown below. ",
        ),
        doccode(
            """"sm": '30em',
"md": '48em',
"lg": '62em',
"xl": '80em',
"2xl": '96em',
""",
            language="json",
        ),
        subheader("Showing Components Based on Display"),
        doctext(
            "A common use case for responsive is to show different components based on the screen size."
        ),
        doctext("Pynecone provides useful helper components for this."),
        docdemo(code2),
        subheader("Specifying Display Breakpoints"),
        doctext(
            "You can specify the breakpoints to use for the responsive components by using the ",
            pc.code("display"),
            " style property."
        ),
        docdemo(code3),
    )
