from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def frontend():
    return flexdown.render_file("docs/tutorial/frontend.md")
