from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def components_overview():
    return flexdown.render_file("docs/components/overview.md")
