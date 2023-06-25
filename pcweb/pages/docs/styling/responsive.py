import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import (
    doccode,
    docdemo,
    docheader,
    docpage,
    doctext,
    subheader,
)

code1 = """rx.text(
    "Hello World", 
    color=["orange", "red", "purple",  "blue", "green"]
)"""
code2 = """rx.vstack(
    rx.desktop_only(
        rx.text("Desktop View"),
    ),
    rx.tablet_only(
        rx.text("Tablet View"),
    ),
    rx.mobile_only(
        rx.text("Mobile View"),
    ),
    rx.mobile_and_tablet(
        rx.text("Visible on Mobile and Tablet"),
    ),
    rx.tablet_and_desktop(
        rx.text("Visible on Desktop and Tablet"),
    ),
)"""

code3 = """
rx.vstack(
    rx.text("Hello World", color="green", display=["none", "none", "none", "none", "flex"]),
    rx.text("Hello World", color="blue", display=["none", "none", "none", "flex", "flex"]),
    rx.text("Hello World", color="red", display=["none", "none", "flex", "flex", "flex"]),
    rx.text("Hello World", color="orange", display=["none", "flex", "flex", "flex", "flex"]),
    rx.text("Hello World", color="yellow", display=["flex", "flex", "flex", "flex", "flex"]),
)
"""


@docpage()
def responsive():
    return rx.box(
        docheader("Responsive", first=True),
        doctext(
            "Reflex apps can be made responsive to look good on mobile, tablet, and desktop."
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
        doctext("Reflex provides useful helper components for this."),
        docdemo(code2),
        subheader("Specifying Display Breakpoints"),
        doctext(
            "You can specify the breakpoints to use for the responsive components by using the ",
            rx.code("display"),
            " style property.",
        ),
        docdemo(code3),
    )
