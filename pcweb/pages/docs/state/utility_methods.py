from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def utility_methods():
    return flexdown.render_file("docs/state/utility-methods.md")
