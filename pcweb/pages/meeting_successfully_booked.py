import reflex as rx

from pcweb.flexdown import markdown_with_shiki
from pcweb.templates.webpage import webpage

contents = """
# Thanks for Submitting a Demo Request

Meeting successfully booked!
"""


@webpage(
    path="/meeting-successfully-booked",
    title="Meeting Successfully Booked · Reflex.dev",
    add_as_page=False,
)
def page_meeting_successfully_booked():
    return rx.box(
        markdown_with_shiki(contents),
        class_name="h-[80vh] w-full flex flex-col items-center justify-center",
    )
