import reflex as rx

from pcweb.templates.docpage import (
    doccode,
    docheader,
    docpage,
    doctext,
    subheader,
)


@docpage()
def telemetry():
    return rx.box(
        docheader("Anonymous Telemetry", first=True),
        doctext(
            "Reflex collects completely anonymous telemetry data about general usage. Participation in this anonymous program is optional, and you may opt-out if you'd not like to share any information. ",
        ),
        subheader("What is being collected?"),
        doctext(
            "Telemetry allows us to understand how Reflex is used, what features are most important, and how we can improve the product. ",
        ),
        doctext(
            "The categories of data collected are: ",
            rx.code("user_os"),
            ", ",
            rx.code("cpu_count"),
            ", ",
            rx.code("memory"),
            ", ",
            rx.code("reflex_version"),
            ", and ",
            rx.code("python_version"),
            ". ",
        ),
        subheader("How to opt-out?"),
        doctext(
            "To disable telemetry, set ",
            rx.code("telemetry_enabled = False"),
            " in your ",
            rx.code("rxconfig.py"),
        ),
        doccode(
            """config = rx.Config(
    app_name="hello",
    bun_path="$HOME/.bun/bin/bun",
    db_url="sqlite:///reflex.db",
    telemetry_enabled=False,
)
""",
        ),
    )
