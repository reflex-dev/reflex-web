from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def substates_overview():
    return flexdown.render_file("docs/substates/substates_overview.md")