import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo, docheader, docpage, doctext


@docpage()
def special_events():
    return pc.flex(
        pc.hstack(
            pc.box(
                docheader("Special Events", first=True),
                doctext(
                    "Pynecone has some special built-in events that can be attached to event triggers or returned from event handlers like any other event."
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


SPECIAL_EVENTS = [
    {
        "fn": pc.set_value,
        "example": """pc.hstack(pc.input(id="input1"), pc.button("Erase", on_click=pc.set_value("input1", "")))""",
    },
    {
        "fn": pc.redirect,
        "example": f"""pc.button("Redirect", on_click=pc.redirect("{special_events.path}"))""",
    },
    {
        "fn": pc.console_log,
        "example": """pc.button("Log", on_click=pc.console_log("Hello World!"))""",
    },
    {
        "fn": pc.window_alert,
        "example": """pc.button("Alert", on_click=pc.window_alert("Hello World!"))""",
    },
]


def component_grid():
    events = []
    for event in SPECIAL_EVENTS:
        events.append(
            pc.vstack(
                docheader(event["fn"].__name__),
                doctext(event["fn"].__doc__.split("\n")[0]),
                docdemo(
                    event["example"],
                    context=True,
                ),
                align_items="left",
            )
        )

    return pc.box(*events)
