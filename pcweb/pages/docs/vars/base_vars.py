from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def base_vars():
    return flexdown.render_file("docs/vars/base_vars.md")