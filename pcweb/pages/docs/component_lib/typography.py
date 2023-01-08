import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo, doclink, doctext

# Typography

basic_text_example = """pc.text("Hello World!", font_size="2em")"""
as_text_example = """pc.vstack(
    pc.text("Hello World!", as_="i"),
    pc.text("Hello World!", as_="s"),
    pc.text("Hello World!", as_="mark"),
    pc.text("Hello World!", as_="sub"),
)
"""


def render_text():
    return pc.vstack(
        doctext("The text component displays a paragraph of text."),
        docdemo(basic_text_example),
        doctext(
            "The text element can be visually modified using the ",
            pc.code("as_"),
            " prop. ",
        ),
        pc.center(
            pc.hstack(
                pc.box(
                    pc.unordered_list(
                        pc.list_item(pc.code("b"), ": Bold text"),
                        pc.list_item(pc.code("strong"), ": Important text"),
                        pc.list_item(pc.code("i"), ": Italic text"),
                        pc.list_item(pc.code("em"), ": Emphasized text"),
                        pc.list_item(pc.code("mark"), ": Marked text"),
                    )
                ),
                pc.box(
                    pc.unordered_list(
                        pc.list_item(pc.code("small"), ": Smaller text"),
                        pc.list_item(pc.code("del"), ": Deleted text"),
                        pc.list_item(pc.code("ins"), ": Inserted text"),
                        pc.list_item(pc.code("sub"), ": Subscript text"),
                        pc.list_item(pc.code("sup"), ": Superscript text"),
                    )
                ),
            ),
            width="100%",
        ),
        docdemo(as_text_example),
        align_items="start",
    )


heading_example = """pc.heading("Hello World!")"""

styled_heading_example = """pc.vstack(
    pc.heading("Hello World!", size= "sm", color="red"),
    pc.heading("Hello World!", size= "md", color="blue"),
    pc.heading("Hello World!", size= "lg", color="green"),
    pc.heading("Hello World!", size= "xl", color="blue"),
    pc.heading("Hello World!", size= "2xl", color="red"),
    pc.heading("Hello World!", size= "3xl", color="blue"),
    pc.heading("Hello World!", size= "4xl", color="green"),
)
"""

heading_example_3 = """pc.heading("Hello World!", font_size="2em")"""


def render_heading():
    return pc.vstack(
        doctext(
            "The heading component takes in a string and displays it as a heading."
        ),
        docdemo(heading_example),
        doctext("Size can be changed using the ", pc.code("size"), " prop."),
        docdemo(styled_heading_example),
        doctext("It can also be styled using regular CSS styles."),
        docdemo(heading_example_3),
        align_items="start",
    )


codemarkdown = """pc.vstack(
    pc.markdown("# Hello World!"),
    pc.markdown("## Hello World!"),
    pc.markdown("### Hello World!")
)
"""


codemarkdown1 = """
pc.markdown('''
Support us at **[Pynecone](https://pynecone.io)**.
Format your `inline_code` easily.
'''
)
"""

codemarkdown11 = r"""
pc.markdown(r'$ \\int_a^b x^2 dx $')
"""

codemarkdown2 = """
pc.markdown('''
- Lorem ipsum dolor sit amet
'''
)
"""

codemarkdown3 = """
pc.markdown('''
![The San Juan Mountains are beautiful!](/logo.png "San Juan Mountains")
'''
)
"""


def render_markdown():
    return pc.vstack(
        doctext("The markdown component renders a Markdown string as formatted text."),
        docdemo(codemarkdown),
        doctext("A more complex example of markdown."),
        docdemo(codemarkdown1),
        doctext("Render math equations using LaTeX."),
        docdemo(codemarkdown11),
        align_items="start",
    )


codespan1 = """pc.box(
    "Write some ",
    pc.span("stylized ", color="red"),    
    pc.span("text ", color="blue"),
    pc.span("using spans.", font_weight="bold")
)"""


def render_span():
    return pc.vstack(
        doctext(
            "The span component can be used to style inline text.",
        ),
        docdemo(codespan1),
        align_items="start",
    )
