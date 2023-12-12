from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def chaining_events():
    return flexdown.render_file("docs/events/chaining_events.md")