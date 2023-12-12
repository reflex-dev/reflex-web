from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def meta_data():
    return flexdown.render_file("docs/pages/meta_data.md")