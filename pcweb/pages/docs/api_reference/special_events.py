import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo, docheader, docpage, doctext
from pcweb import flexdown

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
        "fn": rx.console_log,
        "example": """rx.button("Log", on_click=rx.console_log("Hello World!"))""",
    },
    {
        "fn": rx.redirect,
        "example": f"""rx.button("Redirect", on_click=rx.redirect("{special_events.path}"))""",
    },
    {
        "fn": rx.set_clipboard,
        "example": """rx.button("Copy 'Hello World' to clipboard", on_click=rx.set_clipboard("Hello World"))""",
    },
    {
        "fn": rx.set_cookie,
        "example": """rx.button("Set cookie", on_click=rx.set_cookie("key", "my_value"))""",
    },
    {
        "fn": rx.remove_cookie,
        "example": """rx.button("Remove cookie", on_click=rx.remove_cookie("key")) """,
    },
    {
        "fn": rx.set_local_storage,
        "example": """rx.button("Set Local Storage", on_click=rx.set_local_storage("key", "my_value"))""",
    },
    {
        "fn": rx.remove_local_storage,
        "example": """rx.button("Remove Local Storage", on_click=rx.remove_local_storage("key"))""",
    },
    {
        "fn": rx.clear_local_storage,
        "example": """rx.button("Clear all Local Storage", on_click=rx.clear_local_storage())""",
    },
    {
        "fn": rx.set_value,
        "example": """rx.hstack(rx.input(id="input1"), rx.button("Erase", on_click=rx.set_value("input1", "")))""",
    },
    {
        "fn": rx.window_alert,
        "example": """rx.button("Alert", on_click=rx.window_alert("Hello World!"))""",
    },
    {
        "fn": rx.download,
        "example": """rx.button("Download", on_click=rx.download(url="/reflex_logo.png", filename="different_name_logo.png"))""",
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


@docpage()
def special_events_flex_docs():
    _, output = flexdown.read("docs/api-reference/special-events.md")
    return rx.box(
        *output,
    )
