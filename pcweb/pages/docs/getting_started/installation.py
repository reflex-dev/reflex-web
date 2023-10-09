from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def installation():
    return flexdown.render_file("docs/getting-started/02-installation.md")
