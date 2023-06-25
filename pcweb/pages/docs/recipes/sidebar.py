import reflex as rx

from pcweb.templates.docpage import (
    doccode,
    docheader,
    docpage,
    doctext,
    subheader,
)

code_example1 = """rx.text('hello world', color='blue')"""


@docpage()
def sidebar():
    return rx.box(
        docheader("Sidebar", first=True),
        doctext(
            "Similar to a navigation bar, a sidebar is a common UI element found on the side of a webpage or application. ",
        ),
        subheader("Recipe"),
        doctext(
            "In this recipe, we will create a sidebar component than can help with navigation in a web app. ",
        ),
        doctext(
            "In this example we want the sidebar to stick to the left side of the page, so we will use the ",
            rx.code('position= "fixed"'),
            " prop to make the sidebar fixed to the left side of the page. ",
            "We will also use the ",
            rx.code("left= 0"),
            " and ",
            rx.code("z_index=1"),
            " props to make sure the sidebar is always on top of the screen and above the other components on the page. ",
        ),
        doccode(
            """
            import reflex as rx

            def sidebar():
                return rx.box(
                    rx.vstack(
                        rx.image(src="/favicon.ico", margin="0 auto"),
                        rx.heading("Sidebar", text_align="center", margin_bottom="1em"),
                        rx.menu(...),
                        width="250px",
                        padding_x="2em",
                        padding_y="1em",
                    ),
                    position="fixed",
                    height="100%",
                    left="0px",
                    top="0px",
                    z_index="500",
                )
            """
        ),
    )
