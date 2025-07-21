import reflex as rx
from pcweb.templates.webpage import webpage
from pcweb.flexdown import markdown_with_shiki

contents = f"""
# Page Not Found

The page at `{rx.State.router.url}` doesn't exist.
"""


@webpage(path="/404", title="Page Not Found · Reflex.dev", add_as_page=False)
def page404():
    return rx.box(
        markdown_with_shiki(contents),
        class_name="h-[80vh] w-full flex flex-col items-center justify-center",
    )
