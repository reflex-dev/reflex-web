import reflex as rx

from pcweb.templates.docpage import (
    definition,
    docalert,
    doccode,
    docdemo,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader,
)

code_example1 = """rx.text('Hello World!', color='blue', font_size="1.5em")"""
code_example2 = """
rx.hstack(
    rx.circular_progress(
        rx.circular_progress_label("50", color="green"),
        value=50,
    ),
    rx.circular_progress(
        rx.circular_progress_label("∞", color="rgb(107,99,246)"),
        is_indeterminate=True,
    ),
)
"""


definitions = [
    definition(
        "Children",
        rx.unordered_list(
            rx.list_item("Other Reflex components nested inside a component."),
            rx.list_item(
                "They are passed in as ",
                rx.span("positional arguments", font_weight="bold"),
                " to the component.",
            ),
        ),
    ),
    definition(
        "Props",
        rx.unordered_list(
            rx.list_item(
                "Attributes that affect the behavior and appearance of a component."
            ),
            rx.list_item(
                "They are passed in as ",
                rx.span("keyword arguments", font_weight="bold"),
                " to the component.",
            ),
        ),
    ),
]


@docpage()
def components_overview():
    from pcweb.pages.docs.components.props import props

    # from pcweb.pages.docs.components.composition import composition
    from pcweb.pages.docs.library import library

    return rx.box(
        docheader("Components", first=True),
        doctext(
            """Components are the building blocks of Reflex's frontend. 
            They let you split the UI into independent, reusable pieces, and let you think about each piece in isolation."""
        ),
        doctext(
            "If you are familiar with React, Reflex components are simply wrappers around React components. ",
        ),
        doctext(
            "Components are created with Python functions.",
            "They can be configured with keyword arguments, called ",
            doclink("props", href=props.path),
            ", and can be nested to create  complex UIs.",
        ),
        subheader("Component Basics"),
        doctext(
            "Components are made up of children and props.",
        ),
        rx.mobile_only(
            rx.vstack(
                *definitions,
                margin_bottom="1em",
            ),
        ),
        rx.tablet_and_desktop(
            rx.hstack(
                *definitions,
                margin_bottom="1em",
            ),
        ),
        doctext(
            "Let's take a look at the ",
            rx.code("rx.text"),
            " component.",
        ),
        docdemo(code_example1),
        doctext(
            "Here ",
            rx.code('"Hello World!"'),
            " is the child text to display, while ",
            rx.code("color"),
            " and ",
            rx.code("font_size"),
            " are props that modify the appearance of the text.",
        ),
        docalert(
            "Regular Python data types can be passed in as children to components. ",
            "This is useful for passing in text, numbers, and other simple data types. ",
            status="success",
        ),
        subheader("Another Example"),
        doctext(
            "Now let's take a look at a more complex component, which has other components nested inside it. ",
            "The ",
            rx.code("rx.hstack"),
            " component is a container that arranges its children horizontally.",
        ),
        docdemo(code_example2),
        doctext(
            "Some props are specific to a component. For example, the ",
            rx.code("value"),
            " prop of the ",
            rx.code("rx.circular_progress"),
            " component controls the progress bar's value. ",
        ),
        doctext(
            "Styling props like ",
            rx.code("color"),
            " are shared across many components. ",
        ),
        doctext(
            rx.alert(
                rx.alert_icon(),
                rx.alert_title(
                    "You can find all the props for a component by checking its documentation page in the ",
                    doclink("component library", href=library.path),
                    ".",
                ),
                status="info",
            ),
        ),
        subheader("Pages"),
        doctext(
            """Reflex apps are organized into pages. Pages link a specific URL route to a component."""
        ),
        doctext(
            "You can create a page by defining a function that returns a component. ",
            "By default, the function name will be used as the path, but you can also specify a path explicitly.",
        ),
        doccode(
            """
        def index():
            return rx.text('Root Page')

        def about():
            return rx.text('About Page')

        app = rx.App()
        app.add_page(index, route="/")
        app.add_page(about, route="/about")
    """
        ),
        doctext(
            "In this example we add a page called ",
            rx.code("index"),
            " at the root route. ",
            " If you're running in ",
            rx.code("dev"),
            " mode, you can access it at ",
            rx.code("http://localhost:3000"),
            ". ",
        ),
        doctext(
            "Similarly, the ",
            rx.code("about"),
            " page will be available at ",
            rx.code("http://localhost:3000/about"),
            ".",
        ),
    )
