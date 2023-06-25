import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo, docheader, docpage, doctext


@docpage()
def special_events():
    return rx.flex(
        rx.hstack(
            rx.box(
                docheader("Special Events", first=True),
                doctext(
                    "Reflex has some special built-in events that can be attached to event triggers or returned from event handlers like any other event."
                ),
                rx.divider(),
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
        "fn": rx.set_value,
        "example": """rx.hstack(rx.input(id="input1"), rx.button("Erase", on_click=rx.set_value("input1", "")))""",
    },
    {
        "fn": rx.redirect,
        "example": f"""rx.button("Redirect", on_click=rx.redirect("{special_events.path}"))""",
    },
    {
        "fn": rx.console_log,
        "example": """rx.button("Log", on_click=rx.console_log("Hello World!"))""",
    },
    {
        "fn": rx.window_alert,
        "example": """rx.button("Alert", on_click=rx.window_alert("Hello World!"))""",
    },
]


def component_grid():
    events = []
    for event in SPECIAL_EVENTS:
        events.append(
            rx.vstack(
                docheader(event["fn"].__name__),
                doctext(event["fn"].__doc__.split("\n")[0]),
                docdemo(
                    event["example"],
                    context=True,
                ),
                align_items="left",
            )
        )

    return rx.box(*events)
