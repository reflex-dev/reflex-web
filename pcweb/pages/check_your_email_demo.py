import reflex as rx

from pcweb.flexdown import markdown_with_shiki
from pcweb.templates.webpage import webpage

contents = """
# Thanks for Submitting a Demo Request

Check your email, we sent a calendar link to get access.
"""


@webpage(
    path="/thank-you",
    title="Thanks for Submitting a Demo Request · Reflex.dev",
    add_as_page=False,
)
def page_thank_you():
    return rx.box(
        markdown_with_shiki(contents),
        class_name="h-[80vh] w-full flex flex-col items-center justify-center",
    )
