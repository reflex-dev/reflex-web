from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def page_meta_data():
    return flexdown.render_file("docs/pages/page_meta_data.md")