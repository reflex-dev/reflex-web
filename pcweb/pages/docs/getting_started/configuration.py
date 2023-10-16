from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def configuration():
    return flexdown.render_file("docs/getting-started/configuration.md")
