from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def conditional_props():
    return flexdown.render_file("docs/components/conditional_props.md")