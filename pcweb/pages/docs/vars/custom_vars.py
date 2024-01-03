from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def custom_vars():
    return flexdown.render_file("docs/vars/custom_vars.md")