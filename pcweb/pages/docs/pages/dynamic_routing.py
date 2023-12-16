from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def dynamic_routing():
    return flexdown.render_file("docs/pages/dynamic_routing.md")