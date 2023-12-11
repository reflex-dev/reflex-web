from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def ui_overview():
    return flexdown.render_file("docs/ui_overview.md")
