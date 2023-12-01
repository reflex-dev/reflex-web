from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def add_interactivity():
    return flexdown.render_file("docs/datatable-tutorial/add_interactivity.md")
