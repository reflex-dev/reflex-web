import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo, docheader, docpage, doctext


@docpage()
def server_side():
    return pc.flex(
        pc.hstack(
            pc.box(
                docheader("Server Side Events", first=True),
                doctext(
                    "There are a few built-in Pynecone events that can be triggered on the server side."
                ),
                pc.divider(),
                component_grid(),
                text_align="left",
            ),
            align_items="start",
        ),
        flex_direction="column",
        height="100%",
        margin_bottom="4em",
    )


SERVER_SIDE_EVENTS = [
    {
        "fn": pc.redirect,
        "state": f"""class RedirectState(State):
    def redirect(self):
        return pc.redirect("{server_side.path}")
""",
        "example": """pc.button("Redirect", on_click=RedirectState.redirect)""",
    },
    {
        "fn": pc.console_log,
        "state": """class ConsoleState(State):
    def log(self):
        return pc.console_log("Hello World!")
""",
        "example": """pc.button("Log", on_click=ConsoleState.log)""",
    },
    {
        "fn": pc.window_alert,
        "state": """class AlertState(State):
    def alert(self):
        return pc.window_alert("Hello World!")
""",
        "example": """pc.button("Alert", on_click=AlertState.alert)""",
    },
]
for i in SERVER_SIDE_EVENTS:
    exec(i["state"])


def component_grid():
    events = []
    for event in SERVER_SIDE_EVENTS:
        events.append(
            pc.vstack(
                docheader(event["fn"].__name__),
                doctext(event["fn"].__doc__.split("\n")[0]),
                docdemo(
                    event["example"],
                    state=event["state"],
                    comp=eval(event["example"]),
                    context=True,
                ),
                align_items="left",
            )
        )

    return pc.box(*events)
