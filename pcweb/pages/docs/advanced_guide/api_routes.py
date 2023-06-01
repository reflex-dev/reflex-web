import pynecone as pc

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

app = pc.App(state=MyState)
app.api.add_api_route("/items/{item_id}", api_test)
app.compile()
"""


@docpage()
def api_routes():
    return pc.box(
        docheader("Backend API Routes", first=True),
        doctext(
            "In addition to your frontend app, Pynecone also uses a FastAPI backend to serve your app. "
        ),
        doctext(
            "To add additional endpoints to the backend API, you can use ",
            pc.code("app.add_api_route"),
            " and add a route that returns JSON. ",
        ),
        doccode(example),
        doctext(
            "Now you can access the endpoint at ",
            pc.code("localhost:8000/items/23"),
            " and get the result.",
        ),
        doctext(
            "This is useful for creating a backend API that can be used for purposes other than your Pynecone app. ",
        ),
        subheader("Reserved Routes"),
        doctext(
            "Some routes on the backend are reserved for the runtime of Pynecone, and should not be overriden unless you know what you are doing"
        ),
        subheader("Ping", level=2),
        doctext(
            pc.code("localhost:8000/ping/"),
            ": You can use this route to check the health of the backend.",
        ),
        doctext(
            "The expected return is ",
            pc.code('"pong"'),
        ),
        subheader("Event", level=2),
        doctext(
            pc.code("localhost:8000/event"),
            ": the frontend will use this route to notify the backend that an event occurred",
        ),
        pc.alert(
            icon=True,
            title="Overriding this route will break the event communication",
            status="error",
        ),
        subheader("Upload", level=2),
        doctext(
            pc.code("localhost:8000/upload"),
            ": This route is used for the upload of file when using ",
            pc.code("pc.upload()"),
        ),
    )
