from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def metadata():
    return flexdown.render_file("docs/pages/metadata.md")