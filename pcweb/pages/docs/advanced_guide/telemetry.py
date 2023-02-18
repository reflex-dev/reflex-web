import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import (
    doccode,
    docdemo,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader,
)


@docpage()
def telemetry():
    from pcweb.pages.docs.components.overview import components_overview
    from pcweb.pages.docs.styling.overview import styling_overview

    return pc.box(
        docheader("Anonymous Telemetry", first=True),
        doctext(
            "Pynecone collects completely anonymous telemetry data about general usage. Participation in this anonymous program is optional, and you may opt-out if you'd not like to share any information. ",
        ),
        subheader("What is being collected?"),
        doctext(
            "Telemetry allows us to understand how Pynecone is used, what features are most important, and how we can improve the product. ",
        ),
        doctext(
            "The categories of data collected are: ",
            pc.code("user_os"),
            ", ",
            pc.code("cpu_count"),
            ", ",
            pc.code("memory"),
            ", ",
            pc.code("pynecone_version"),
            ", and ",
            pc.code("python_version"),
            ". ",
        ),
        subheader("How to opt-out?"),
        doctext(
            "To disable telemetry, set ",
            pc.code("telemetry_enabled = False"),
            " in your ",
            pc.code("pcconfig.py"),
        ),
        doccode(
            """config = pc.Config(
    app_name="hello",
    bun_path="$HOME/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
    telemetry_enabled=False,
)
""",
        ),
    )
