import reflex as rx


from pcweb import styles

from pcweb.base_state import State
from pcweb.components.footer import footer
from pcweb.components.navbar import navbar


class State404(State):
    @rx.var
    def origin_url(self) -> str:
        return self.router_data.get("asPath", "")


def _404():
    return rx.center(
        rx.vstack(
            rx.heading(rx.constants.Page404.TITLE),
            rx.text(
                "Oups, the page at ",
                rx.code(State404.origin_url),
                " doesn't exist.",
            ),
            rx.spacer(),
        ),
        height="80vh",
        width="100%",
    )


def index():
    # Wrap the component in the template.
    return rx.box(
        navbar(),
        _404(),
        footer(),
        font_family=styles.SANS,
        width="100vw",
    )
