from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def styling_overview():
    return flexdown.render_file("docs/styling/overview.md")