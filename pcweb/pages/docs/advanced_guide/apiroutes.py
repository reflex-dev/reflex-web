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
            "If you want to create a backend API, you can use ",
            pc.code("app.add_api_route"),
            " to add a route that returns JSON. ",
        ),
        doctext(
            "This is useful for creating a backend API that can be used by a frontend app other than your own Pynecone app. ",
        ),
        doccode(example),
    )
