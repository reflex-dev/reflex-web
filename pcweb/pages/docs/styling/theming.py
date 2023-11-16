from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def theming():
    return flexdown.render_file("docs/styling/theming.md")
