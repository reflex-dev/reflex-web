from pcweb.templates.docpage import docpage
from pcweb.flexdown import component_map
import flexdown


@docpage()
def installation():
    return flexdown.render_file(
        "docs/getting-started/02-installation.md", component_map=component_map
    )
