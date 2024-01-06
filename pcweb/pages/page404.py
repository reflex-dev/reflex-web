import reflex as rx


from pcweb import styles

from pcweb.components.footer import footer
from pcweb.components.navbar import navbar


def _404():
    return rx.center(
        rx.vstack(
            rx.heading(rx.constants.Page404.TITLE),
            rx.text(
                "Oups, the page at ",
                rx.code(rx.State.router.page.raw_path),
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
