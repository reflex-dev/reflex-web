from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def api_routes_overview():
    return flexdown.render_file("docs/api_routes/api_routes_overview.md")