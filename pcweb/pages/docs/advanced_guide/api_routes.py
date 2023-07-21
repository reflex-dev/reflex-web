import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import (
    docdemo,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader,
    doccode,
)


example = """
async def api_test(item_id: int):
    return {"my_result": item_id}

app = rx.App()
app.api.add_api_route("/items/{item_id}", api_test)
app.compile()
"""


@docpage()
def api_routes():
    return rx.box(
        docheader("Backend API Routes", first=True),
        doctext(
            "In addition to your frontend app, Reflex also uses a FastAPI backend to serve your app. "
        ),
        doctext(
            "To add additional endpoints to the backend API, you can use ",
            rx.code("app.add_api_route"),
            " and add a route that returns JSON. ",
        ),
        doccode(example),
        doctext(
            "Now you can access the endpoint at ",
            rx.code("localhost:8000/items/23"),
            " and get the result.",
        ),
        doctext(
            "This is useful for creating a backend API that can be used for purposes other than your Reflex app. ",
        ),
        subheader("Reserved Routes"),
        doctext(
            "Some routes on the backend are reserved for the runtime of Reflex, and should not be overriden unless you know what you are doing"
        ),
        subheader("Ping", level=2),
        doctext(
            rx.code("localhost:8000/ping/"),
            ": You can use this route to check the health of the backend.",
        ),
        doctext(
            "The expected return is ",
            rx.code('"pong"'),
        ),
        subheader("Event", level=2),
        doctext(
            rx.code("localhost:8000/_event"),
            ": the frontend will use this route to notify the backend that an event occurred",
        ),
        rx.alert(
            icon=True,
            title="Overriding this route will break the event communication",
            status="error",
        ),
        subheader("Upload", level=2),
        doctext(
            rx.code("localhost:8000/_upload"),
            ": This route is used for the upload of file when using ",
            rx.code("rx.upload()"),
        ),
    )
