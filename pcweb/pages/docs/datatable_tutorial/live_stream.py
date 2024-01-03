from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def live_stream():
    return flexdown.render_file("docs/datatable-tutorial/live_stream.md")
