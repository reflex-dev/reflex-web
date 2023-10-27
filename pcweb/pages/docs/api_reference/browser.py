from pcweb import flexdown
from pcweb.templates.docpage import docpage



@docpage()
def browser_storage():
    return flexdown.render_file("docs/api-reference/browser_storage.md")


@docpage("/docs/api-reference/browser_javascript")
def browser_javascript():
    return flexdown.render_file("docs/api-reference/browser_javascript.md")