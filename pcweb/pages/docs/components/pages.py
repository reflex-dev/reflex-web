import pynecone as pc

from pcweb.templates.docpage import doccode, docheader, docpage, doctext, subheader


@docpage()
def pages():
    return pc.box(
        docheader("Pages", first=True),
        doctext(
            "Pages specify the component to render for a given URL.",
        ),
        subheader("Adding a Page"),
        doctext(
            "You can create a page by defining a function that returns a component. ",
            "By default, the function name will be used as the route, but you can also specify a route.",
        ),
        doccode(
            """
        def index():
            return pc.text('Root Page')

        def about():
            return pc.text('About Page')

        def custom():
            return pc.text('Custom Route')

        app = pc.App()
        app.add_page(index)
        app.add_page(about)
        app.add_page(custom, route="/custom-route")
    """
        ),
        doctext(
            "In this example we create three pages: ",
        ),
        doctext(
            pc.unordered_list(
                pc.vstack(
                    pc.list_item(
                        pc.code("index"),
                        " - The root route, available at ",
                        pc.code("/"),
                        width="100%",
                    ),
                    pc.list_item(
                        pc.code("about"),
                        " - available at ",
                        pc.code("/about"),
                        width="100%",
                    ),
                    pc.list_item(
                        pc.code("custom"),
                        " - available at ",
                        pc.code("/custom-route"),
                        width="100%",
                    ),
                )
            )
        ),
        subheader("Nested Routes"),
        doctext(
            "Pages can also have nested routes.",
        ),
        doccode(
            """
        def nested_page():
            return pc.text('Nested Page')

        app = pc.App()
        app.add_page(nested_page, route="/nested/page")
"""
        ),
        doctext(
            "This component will be available at ",
            pc.code("/nested/page"),
            ".",
        ),
        subheader("Dynamic Routes", coming_soon=True),
        doctext(
            "For more complex applications, you may need a dynamic route that passes an argument to the component. ",
            "This feature is coming soon.",
        ),
        subheader("Page Metadata"),
        doctext(
            "You can add page metadata such as: ",
        ),
        pc.unordered_list(
            pc.vstack(
                pc.list_item(
                    pc.text("The title that will appear in the browser tab"),
                    width="100%",
                ),
                pc.list_item(
                    pc.text("The description that will appear in search results"),
                    width="100%",
                ),
                pc.list_item(
                    pc.text(
                        "The image that will appear when the page is shared on social media"
                    ),
                    width="100%",
                ),
            )
        ),
        doccode(
            """
def index():
    return pc.text('A Beautiful App')

def about():
    return pc.text('About Page')

app = pc.App()
app.add_page(index, title="My Beautiful App", description="A beautiful app built with Pynecone", image="/splash.png")
app.add_page(about, title="About Page")
            """
        ),
        subheader("Page Load Events"),
        doctext(
            "You can also specify a function to run when the page loads. ",
            "This can be useful for fetching data once vs on every render or state change.",
        ),
        doctext("In this example, we fetch data when the page loads:"),
        doccode(
            """
            class State(pc.State):
                data: Dict[str, Any]

                def get_data():
                    # Fetch data
                    self.data = fetch_data()
            def index():
                return pc.text('A Beautiful App')
            add_page(index, on_load=State.get_data)
            """
        ),
    )
