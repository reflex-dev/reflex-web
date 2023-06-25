import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo, doclink, doctext

# Typography

basic_text_example = """rx.text("Hello World!", font_size="2em")"""
as_text_example = """rx.vstack(
    rx.text("Hello World!", as_="i"),
    rx.text("Hello World!", as_="s"),
    rx.text("Hello World!", as_="mark"),
    rx.text("Hello World!", as_="sub"),
)
"""


def render_text():
    return rx.vstack(
        doctext("The text component displays a paragraph of text."),
        docdemo(basic_text_example),
        doctext(
            "The text element can be visually modified using the ",
            rx.code("as_"),
            " prop. ",
        ),
        rx.center(
            rx.hstack(
                rx.box(
                    rx.unordered_list(
                        rx.list_item(rx.code("b"), ": Bold text"),
                        rx.list_item(rx.code("strong"), ": Important text"),
                        rx.list_item(rx.code("i"), ": Italic text"),
                        rx.list_item(rx.code("em"), ": Emphasized text"),
                        rx.list_item(rx.code("mark"), ": Marked text"),
                        rx.list_item(rx.code("kdb"), ": Inserted text"),
                        rx.list_item(rx.code("cite"), ": Inserted text"),
                        rx.list_item(rx.code("abbr"), ": Inserted text"),
                    )
                ),
                rx.box(
                    rx.unordered_list(
                        rx.list_item(rx.code("u"), ": Inserted text"),
                        rx.list_item(rx.code("small"), ": Smaller text"),
                        rx.list_item(rx.code("del"), ": Deleted text"),
                        rx.list_item(rx.code("ins"), ": Inserted text"),
                        rx.list_item(rx.code("samp"), ": Inserted text"),
                        rx.list_item(rx.code("s"), ": Inserted text"),
                        rx.list_item(rx.code("sub"), ": Subscript text"),
                        rx.list_item(rx.code("sup"), ": Superscript text"),
                    )
                ),
            ),
            width="100%",
        ),
        docdemo(as_text_example),
        align_items="start",
    )


heading_example = """rx.heading("Hello World!")"""

styled_heading_example = """rx.vstack(
    rx.heading("Hello World!", size= "sm", color="red"),
    rx.heading("Hello World!", size= "md", color="blue"),
    rx.heading("Hello World!", size= "lg", color="green"),
    rx.heading("Hello World!", size= "xl", color="blue"),
    rx.heading("Hello World!", size= "2xl", color="red"),
    rx.heading("Hello World!", size= "3xl", color="blue"),
    rx.heading("Hello World!", size= "4xl", color="green"),
)
"""

heading_example_3 = """rx.heading("Hello World!", font_size="2em")"""


def render_heading():
    return rx.vstack(
        doctext(
            "The heading component takes in a string and displays it as a heading."
        ),
        docdemo(heading_example),
        doctext("Size can be changed using the ", rx.code("size"), " prop."),
        docdemo(styled_heading_example),
        doctext("It can also be styled using regular CSS styles."),
        docdemo(heading_example_3),
        align_items="start",
    )


highlight_example_1 = """rx.highlight("Hello World, we have some highlight", query=['World','some'], styles={ 'px': '2', 'py': '1', 'rounded': 'full', 'bg': 'grey' })"""


def render_highlight():
    return rx.vstack(
        doctext(
            "The highlight component take in a string and display some of the words as highlighted text."
        ),
        doctext(
            "The words to highlight can be selected using the ",
            rx.code("query"),
            " prop.",
        ),
        doctext(
            "You can also customize how the hightlight will be rendered with the ",
            rx.code("styles"),
            " prop.",
        ),
        docdemo(highlight_example_1),
    )


codemarkdown = """rx.vstack(
    rx.markdown("# Hello World!"),
    rx.markdown("## Hello World!"),
    rx.markdown("### Hello World!")
)
"""


codemarkdown1 = """
rx.markdown('''
Support us at **[Reflex](https://pynecone.io)**.
Format your `inline_code` easily.
'''
)
"""

codemarkdown11 = r"""
rx.markdown(r'$ \\int_a^b x^2 dx $')
"""

codemarkdown2 = """
rx.markdown('''
- Lorem ipsum dolor sit amet
'''
)
"""

codemarkdown3 = """
rx.markdown('''
![The San Juan Mountains are beautiful!](/logo.png "San Juan Mountains")
'''
)
"""


def render_markdown():
    return rx.vstack(
        doctext("The markdown component renders a Markdown string as formatted text."),
        docdemo(codemarkdown),
        doctext("A more complex example of markdown."),
        docdemo(codemarkdown1),
        doctext("Render math equations using LaTeX."),
        docdemo(codemarkdown11),
        align_items="start",
    )


codespan1 = """rx.box(
    "Write some ",
    rx.span("stylized ", color="red"),    
    rx.span("text ", color="blue"),
    rx.span("using spans.", font_weight="bold")
)"""


def render_span():
    return rx.vstack(
        doctext(
            "The span component can be used to style inline text.",
        ),
        docdemo(codespan1),
        align_items="start",
    )
