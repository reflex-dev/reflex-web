from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def substates():
    return flexdown.render_file("docs/state/substates.md")

