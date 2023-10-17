from pcweb import flexdown
from pcweb.templates.docpage import docpage


@docpage()
def tables():
    return flexdown.render_file("docs/database/tables.md")
