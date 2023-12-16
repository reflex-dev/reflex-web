from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def page_load_events():
    return flexdown.render_file("docs/events/page_load_events.md")