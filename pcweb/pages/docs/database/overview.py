from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def database_overview():
    return flexdown.render_file("docs/database/overview.md")