from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def setters():
    return flexdown.render_file("docs/events/setters.md")