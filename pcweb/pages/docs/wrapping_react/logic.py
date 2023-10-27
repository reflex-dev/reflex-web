from pcweb import flexdown

from pcweb.templates.docpage import docpage

@docpage()
def logic():
    return flexdown.render_file("docs/wrapping-react/logic.md")  