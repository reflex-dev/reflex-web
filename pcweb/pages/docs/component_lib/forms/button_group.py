import reflex as rx

from pcweb.templates.docpage import docpage
from pcweb import flexdown

@docpage()
def button_group():
    _, output = flexdown.read("docs/library/forms/button_group.md")
    return rx.box(
        *output,
    )
