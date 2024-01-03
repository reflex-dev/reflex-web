from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def routes():
    return flexdown.render_file("docs/pages/routes.md")
