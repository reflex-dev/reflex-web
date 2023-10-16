from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def setup():
    return flexdown.render_file("docs/tutorial/setup.md")
