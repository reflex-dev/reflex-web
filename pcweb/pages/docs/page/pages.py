from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def pages():
    return flexdown.render_file("docs/components/pages.md")
