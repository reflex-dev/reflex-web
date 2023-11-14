from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def simple_table():
    return flexdown.render_file("docs/datatable-tutorial/simple_table.md")

