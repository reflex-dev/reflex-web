from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def files():
    return flexdown.render_file("docs/components/files.md")
