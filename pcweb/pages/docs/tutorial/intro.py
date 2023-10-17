from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def intro():
    return flexdown.render_file("docs/tutorial/intro.md")
