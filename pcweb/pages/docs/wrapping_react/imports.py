from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def imports():
    return flexdown.render_file("docs/wrapping-react/imports.md")
