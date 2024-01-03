from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def special_events_docs():
    return flexdown.render_file("docs/events/special_events.md")