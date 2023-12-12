from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def utility_methods_overview():
    return flexdown.render_file("docs/utility_methods/utility_methods_overview.md")