from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def yield_events():
    return flexdown.render_file("docs/events/yield_events.md")