from pcweb import flexdown
from pcweb.templates.docpage import docpage


@docpage()
def queries():
    return flexdown.render_file("docs/database/queries.md")
