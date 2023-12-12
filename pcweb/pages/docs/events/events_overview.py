from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def events_overview():
    return flexdown.render_file("docs/events/events_overview.md")