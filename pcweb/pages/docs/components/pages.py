from pcweb.templates.docpage import docpage
from pcweb.flexdown import component_map
import flexdown


@docpage()
def pages():
    return flexdown.render_file("docs/components/pages.md", component_map=component_map)
