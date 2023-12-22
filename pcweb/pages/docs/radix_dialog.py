from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def radix_dialog():
    return flexdown.render_file("docs/radix_dialog.md")