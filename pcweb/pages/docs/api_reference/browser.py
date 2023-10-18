from pcweb import flexdown
from pcweb.templates.docpage import docpage



@docpage()
def browser():
    return flexdown.render_file("docs/api-reference/browser_storage.md")