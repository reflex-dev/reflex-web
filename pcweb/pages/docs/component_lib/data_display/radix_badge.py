from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def radix_badge():
    return flexdown.render_file("docs/library/datadisplay/radix_badge.md")