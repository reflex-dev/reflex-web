from pcweb import flexdown
from pcweb.templates.docpage import (
    docpage,
)


@docpage()
def file_handling():
    return flexdown.render_file("docs/assets/file-handling.md")