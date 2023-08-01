import reflex as rx

from pcweb.templates.docpage import docheader, docpage, doctext, doccode, doclink

code1 = """
class State(rx.State):
    @rx.var
    def client_ip(self):
        return self.get_client_ip()

    @rx.var
    def current_page(self):
        return self.get_current_page()

    @rx.var
    def cookies(self):
        return str(self.get_cookies())


def index():
    return rx.vstack(
        rx.text(State.client_ip),
        rx.text(State.current_page),
        rx.text(State.cookies),
    )


app = rx.App(state=State)
app.add_page(index)
"""


@docpage()
def utility_methods():
    return rx.box(
        docheader("State utility methods", first=True),
        doctext(
            "The State object has several methods that return information "
            "about the current page, user and session."
        ),
        doctext("Some examples:", padding_bottom="0.4em"),
        rx.unordered_list(
            rx.list_item(
                rx.text(
                    rx.code("get_client_ip()"), ": Returns the IP of current user."
                ),
            ),
            rx.list_item(
                rx.text(
                    rx.code("get_current_page()"), ": Returns the URL the current page."
                ),
            ),
            rx.list_item(
                rx.text(
                    rx.code("get_cookies()"),
                    ": Returns the current user's browser cookies.",
                ),
            ),
            padding_bottom="0.7em",
        ),
        doccode(code1),
        doctext(
            "Check out the ",
            doclink(
                "State class definition",
                href="https://github.com/reflex-dev/reflex/blob/main/reflex/state.py",
            ),
            " to see all available methods.",
            padding_top="1em",
        ),
    )
