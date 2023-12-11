from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def component_props():
    return flexdown.render_file("docs/components/component_props.md")
