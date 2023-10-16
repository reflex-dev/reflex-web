from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def introduction():
    return flexdown.render_file("docs/getting-started/introduction.md")
