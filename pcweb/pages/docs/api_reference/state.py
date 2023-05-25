import pynecone as pc

from pcweb.templates.docpage import (
    doccode,
    docheader,
    docpage,
    doctext,
    subheader,
)


# Get all the fields for the state class.
state_fields = pc.State.__fields__.ke


@docpage()
def events_and_state():
    return pc.box(
        docheader("Events and State", first=True),
        docheader("State"),
    )
