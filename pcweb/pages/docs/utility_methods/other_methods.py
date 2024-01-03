from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def other_methods():
    return flexdown.render_file("docs/utility_methods/other_methods.md")