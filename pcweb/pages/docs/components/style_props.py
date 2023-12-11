from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def style_props():
    return flexdown.render_file("docs/components/style_props.md")