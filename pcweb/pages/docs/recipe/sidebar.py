import pynecone as pc

from pcweb.templates.docpage import (
    doccode,
    docheader,
    docpage,
    doctext,
    subheader,
)

code_example1 = """pc.text('hello world', color='blue')"""


@docpage()
def sidebar():
    return pc.box(
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
            pc.code('position= "fixed"'),
            " prop to make the sidebar fixed to the left side of the page. ",
            "We will also use the ",
            pc.code("left= 0"),
            " and ",
            pc.code('z_index="1'),
            " props to make sure the sidebar is always on top of the screen and above the other components on the page. ",
        ),
        doccode(
            """
            import pynecone as pc

            def sidebar():
                return pc.box(
                    pc.vstack(
                        pc.image(src="/favicon.ico", margin="0 auto"),
                        pc.heading("Sidebar", text_align="center", margin_bottom="1em"),
                        pc.menu(...),
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
