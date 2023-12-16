from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def computed_vars():
    return flexdown.render_file("docs/vars/computed_vars.md")