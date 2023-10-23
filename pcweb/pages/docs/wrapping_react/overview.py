from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage() 
def overview():
    return flexdown.render_file("docs/wrapping-react/wrapping-react.md")                    