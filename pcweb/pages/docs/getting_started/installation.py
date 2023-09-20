import reflex as rx
from pcweb import constants, flexdown
from pcweb.templates.docpage import (
    docalert,
    doccode,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader,
)

app_name = "my_app_name"
default_url = "http://localhost:3000"


@docpage()
def installation():
    # Get the file.
    front_matter, output = flexdown.read("docs/getting-started/02-installation.md")
    return rx.box(
        *output,
    )