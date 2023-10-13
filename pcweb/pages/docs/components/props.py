from pcweb.templates.docpage import docpage
from pcweb import flexdown

@docpage()
def props():
    return flexdown.render_file("docs/components/props.md")