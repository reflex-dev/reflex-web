from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def vars():
    return flexdown.render_file("docs/state/vars.md")