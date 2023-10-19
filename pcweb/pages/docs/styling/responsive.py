from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def responsive():
    return flexdown.render_file("docs/styling/responsive.md")