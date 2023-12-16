from pcweb import flexdown
from pcweb.templates.docpage import (
    docpage,
)


@docpage()
def referencing_assets():
    return flexdown.render_file("docs/assets/referencing_assets.md")