from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def files_router_methods():
    return flexdown.render_file("docs/utility_methods/files_router_methods.md")