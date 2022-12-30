import pynecone as pc

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

code_example1 = """pc.text('Hello World!', color='blue', font_size="1.5em")"""
code_example2 = """
pc.hstack(
    pc.circular_progress(
        pc.circular_progress_label("50", color="green"),
        value=50,
    ),
    pc.circular_progress(
        pc.circular_progress_label("∞", color="rgb(107,99,246)"),
        is_indeterminate=True,
    ),
)
"""


definitions = [
    definition(
        "Children",
        pc.unordered_list(
            pc.list_item("Other Pynecone components nested inside a component."),
            pc.list_item(
                "They are passed in as ",
                pc.span("positional arguments", font_weight="bold"),
                " to the component.",
            ),
        ),
    ),
    definition(
        "Props",
        pc.unordered_list(
            pc.list_item(
                "Attributes that affect the behavior and appearance of a component."
            ),
            pc.list_item(
                "They are passed in as ",
                pc.span("keyword arguments", font_weight="bold"),
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

    return pc.box(
        docheader("Components", first=True),
        doctext(
            """Components are the building blocks of Pynecone's frontend. 
            They let you split the UI into independent, reusable pieces, and let you think about each piece in isolation."""
        ),
        doctext(
            "If you are familiar with React, Pynecone components are simply wrappers around React components. ",
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
        pc.mobile_only(
            pc.vstack(
                *definitions,
                margin_bottom="1em",
            ),
        ),
        pc.tablet_and_desktop(
            pc.hstack(
                *definitions,
                margin_bottom="1em",
            ),
        ),
        doctext(
            "Let's take a look at the ",
            pc.code("pc.text"),
            " component.",
        ),
        docdemo(code_example1),
        doctext(
            "Here ",
            pc.code('"Hello World!"'),
            " is the child text to display, while ",
            pc.code("color"),
            " and ",
            pc.code("font_size"),
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
            pc.code("pc.hstack"),
            " component is a container that arranges its children horizontally.",
        ),
        docdemo(code_example2),
        doctext(
            "Some props are specific to a component. For example, the ",
            pc.code("value"),
            " prop of the ",
            pc.code("pc.circular_progress"),
            " component controls the progress bar's value. ",
        ),
        doctext(
            "Styling props like ",
            pc.code("color"),
            " are shared across many components. ",
        ),
        doctext(
            pc.alert(
                pc.alert_icon(),
                pc.alert_title(
                    "You can find all the props for a component by checking its documentation page in the ",
                    doclink("component library", href=library.path),
                    ".",
                ),
                status="info",
            ),
        ),
        subheader("Pages"),
        doctext(
            """Pynecone apps are organized into pages. Pages link a specific URL route to a component."""
        ),
        doctext(
            "You can create a page by defining a function that returns a component. ",
            "By default, the function name will be used as the path, but you can also specify a path explicitly.",
        ),
        doccode(
            """
        def index():
            return pc.text('Root Page')

        def about():
            return pc.text('About Page')

        app = pc.App()
        app.add_page(index, path="/")
        app.add_page(about, path="/about")
    """
        ),
        doctext(
            "In this example we add a page called ",
            pc.code("index"),
            " at the root route. ",
            " If you're running in ",
            pc.code("dev"),
            " mode, you can access it at ",
            pc.code("http://localhost:3000"),
            ". ",
        ),
        doctext(
            "Similarly, the ",
            pc.code("about"),
            " page will be available at ",
            pc.code("http://localhost:3000/about"),
            ".",
        ),
    )
