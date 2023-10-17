from pcweb import flexdown
from pcweb.templates.docpage import (
    docpage,
)

code_example1 = "rx.image(src = '/Reflex.svg', width = '5em')"


@docpage()
def assets():
    return flexdown.render_file("docs/components/assets.md")
