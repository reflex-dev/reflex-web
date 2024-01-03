from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def client_storage_overview():
    return flexdown.render_file("docs/client_storage/client_storage_overview.md")