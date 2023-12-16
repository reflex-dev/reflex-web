from pcweb import flexdown
from pcweb.templates.docpage import docpage


@docpage()
def event_arguments():
    return flexdown.render_file("docs/events/event_arguments.md")