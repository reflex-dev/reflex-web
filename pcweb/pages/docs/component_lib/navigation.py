import reflex as rx

from pcweb.templates.docpage import docdemo, doctext

basic_breadcrumb = """rx.breadcrumb(
    rx.breadcrumb_item(rx.breadcrumb_link("Home", href="#")),
    rx.breadcrumb_item(rx.breadcrumb_link("Docs", href="#")),
    rx.breadcrumb_item(rx.breadcrumb_link("Breadcrumb", href="#")),
)
"""

breadcrumb_separator = """rx.breadcrumb(
    rx.breadcrumb_item(rx.breadcrumb_link("Home", href="#")),
    rx.breadcrumb_item(rx.breadcrumb_link("Docs", href="#")),
    rx.breadcrumb_item(rx.breadcrumb_link("Breadcrumb", href="#")),
    separator=">",
    color="rgb(107,99,246)"
)
"""


# Navigation
def render_breadcrumb():
    return rx.vstack(
        doctext(
            "Breadcrumbs, or a breadcrumb navigation, can help enhance how users navigate to previous page levels of a website."
        ),
        doctext("This is userful for websites with a lot of pages."),
        docdemo(basic_breadcrumb),
        doctext("The separator prop can be used to change the default separator."),
        docdemo(breadcrumb_separator),
        align_items="start",
    )


link_example = (
    """rx.link("Example", href="https://reflex.dev", color="rgb(107,99,246)")"""
)

button_link = """rx.link(rx.button("Example"), href="https://reflex.dev", color="rgb(107,99,246)", button=True)
"""

local_link = """rx.link("Example", href="/docs/library", color="rgb(107,99,246)")"""

anchor_example = """rx.box("Example", id="example")"""


def render_link():
    return rx.vstack(
        doctext("Links are accessible elements used primarily for navigation."),
        docdemo(link_example),
        doctext(
            "You can also provide local links to other pages in your project without writing the full url."
        ),
        docdemo(local_link),
        doctext(
            "The link component can be used to wrap other components to make them link to other pages."
        ),
        docdemo(button_link),
        doctext(
            "You can also create anchors to link to specific parts of a page using the id prop."
        ),
        docdemo(anchor_example),
        doctext(
            "To reference an anchor, you can use the href prop of the link component. ",
            "The href should be in the format of the page you want to link to followed by a # and the id of the anchor.",
        ),
        docdemo(
            """rx.link("Example", href="/docs/library/navigation/link#example", color="rgb(107,99,246)")"""
        ),
        align_items="start",
    )


code97 = """rx.link_overlay(
    rx.box("Example", bg="black", color="white", font_size=30),
)
"""


def render_linkoverlay():
    return rx.vstack(
        doctext(
            "Link overlay provides a semantic way to wrap elements (cards, blog post, articles, etc.) in a link."
        ),
        docdemo(code97),
        align_items="start",
    )
