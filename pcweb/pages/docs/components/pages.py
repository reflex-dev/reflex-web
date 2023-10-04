import reflex as rx

from pcweb.templates.docpage import docpage
from pcweb import flexdown

@docpage()
def pages():
    # Get the file.
    _, output = flexdown.read("docs/components/pages.md")
    return rx.box(
        *output,
    )
