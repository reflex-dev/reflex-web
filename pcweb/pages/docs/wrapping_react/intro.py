from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def intro():
    return flexdown.render_file("docs/wrapping-react/wrapping-react.md")        