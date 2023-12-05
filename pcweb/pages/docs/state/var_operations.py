from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def var_operations():
    
    return flexdown.render_file("docs/state/var-operations.md")
 