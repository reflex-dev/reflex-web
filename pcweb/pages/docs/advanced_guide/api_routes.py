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
    )
