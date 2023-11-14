from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def state_overview():
    return flexdown.render_file("docs/state/overview.md")
