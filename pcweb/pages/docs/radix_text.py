from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def radix_text():
    return flexdown.render_file("docs/radix_text.md")