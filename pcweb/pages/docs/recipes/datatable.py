from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def datatable_tutorial():
    return flexdown.render_file("docs/recipes/datatable.md")