import reflex as rx

from pcweb import flexdown
from pcweb.templates.docpage import docpage

@docpage()
def wrapping_react():
    front_matter, output = flexdown.read("docs/advanced-guide/wrapping-react.md")
    return rx.box(*output)