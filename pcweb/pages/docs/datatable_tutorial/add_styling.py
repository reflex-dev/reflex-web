from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def add_styling():
    return flexdown.render_file("docs/datatable-tutorial/add_styling.md")
