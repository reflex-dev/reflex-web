import reflex as rx

from pcweb.templates.docpage import doccode, docheader, docpage, doctext, subheader


@docpage()
def pages():
    return rx.box(
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
            return rx.text('Root Page')

        def about():
            return rx.text('About Page')

        def custom():
            return rx.text('Custom Route')

        app = rx.App()
        app.add_page(index)
        app.add_page(about)
        app.add_page(custom, route="/custom-route")
    """
        ),
        doctext(
            "In this example we create three pages: ",
        ),
        doctext(
            rx.unordered_list(
                rx.vstack(
                    rx.list_item(
                        rx.code("index"),
                        " - The root route, available at ",
                        rx.code("/"),
                        width="100%",
                    ),
                    rx.list_item(
                        rx.code("about"),
                        " - available at ",
                        rx.code("/about"),
                        width="100%",
                    ),
                    rx.list_item(
                        rx.code("custom"),
                        " - available at ",
                        rx.code("/custom-route"),
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
            return rx.text('Nested Page')

        app = rx.App()
        app.add_page(nested_page, route="/nested/page")
"""
        ),
        doctext(
            "This component will be available at ",
            rx.code("/nested/page"),
            ".",
        ),
        subheader("Dynamic Routes"),
        doctext(
            "For more complex applications, you may need a dynamic route that changes based on the URL. ",
        ),
        doctext(
            "You can specify dynamic arguments with square brackets in the route. ",
        ),
        doccode(
            """
class State(rx.State):
    @rx.var
    def post_id(self):
        return self.get_query_params().get("pid", "no pid")

def post():
    \"""A page that updates based on the route.\"""
    return rx.heading(State.post_id)

app = rx.App(state=State)
app.add_page(post, route="/post/[pid]")
"""
        ),
        doctext(
            "When you visit ",
            rx.code("/post/123"),
            ", the page will render with the text ",
            rx.code("123"),
            ".",
        ),
        doctext(
            "You can also specify multiple dynamic arguments, ",
            "and they will be available in the ",
            rx.code("get_query_params"),
            " dictionary.",
        ),
        doctext(
            "We also provide methods to get the current page, as well as the token of the user who made the request. ",
        ),
        doccode(
            """
class State(rx.State):
    @rx.var
    def post_id(self):
        return self.get_query_params().get("pid", "no pid")

    @rx.var
    def current_page(self):
        return self.get_current_page()

    @rx.var
    def token(self):
        return self.get_token()

def post():
    \"""A page that updates based on the route.\"""
    return rx.vstack(
        rx.text(State.post_id), 
        rx.text(State.current_page),
        rx.text(State.token),
    )

app = rx.App(state=State)
app.add_page(post, route="/post/[pid]")
"""
        ),
        subheader("Page Metadata"),
        doctext(
            "You can add page metadata such as: ",
        ),
        rx.unordered_list(
            rx.vstack(
                rx.list_item(
                    rx.text("The title that will appear in the browser tab"),
                    width="100%",
                ),
                rx.list_item(
                    rx.text("The description that will appear in search results"),
                    width="100%",
                ),
                rx.list_item(
                    rx.text(
                        "The image that will appear when the page is shared on social media"
                    ),
                    width="100%",
                ),
                rx.list_item(
                    rx.text("The optional metadata that you want to add"),
                    width="100%",
                ),
            )
        ),
        doccode(
            """
def index():
    return rx.text('A Beautiful App')

def about():
    return rx.text('About Page')

meta = [
    {"name": "theme_color", "content": "#FFFFFF"},
    {"char_set": "UTF-8"},
    {"property": "og:url", "content": "url"},
]

app = rx.App()
app.add_page(index, meta=meta, title="My Beautiful App", description="A beautiful app built with Reflex", image="/splash.png")
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
            class State(rx.State):
                data: Dict[str, Any]

                def get_data(self):
                    # Fetch data
                    self.data = fetch_data()
            def index():
                return rx.text('A Beautiful App')
            app.add_page(index, on_load=State.get_data)
            """
        ),
        subheader("Route Decorator"),
        doctext(
            "You can also use the ",
            rx.code("@rx.route"),
            " decorator to add a page.",
        ),
        doccode(
            """
            @rx.route(route="/", title="My Beautiful App")
            def index():
                return rx.text('A Beautiful App')
            """
        ),
        doctext(
            "This is equivalent to calling ",
            rx.code("app.add_page"),
            " with the same arguments.",
        ),
    )
