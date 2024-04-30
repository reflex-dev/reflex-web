import reflex as rx
from pcweb.templates.webpage import webpage

contents = f"""
# Page Not Found

The page at `{rx.State.router.page.raw_path}` doesn't exist.
"""


@webpage(path="/404", title="Page Not Found · Reflex.dev", add_as_page=False)
def page404():
    return rx.center(
        rx.vstack(
            rx.markdown(contents),
            rx.spacer(),
        ),
        height="80vh",
        width="100%",
        color="white",
    )
