from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def special_events():
    return flexdown.render_file("docs/api-reference/special_events.md")
