from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def example():
    return flexdown.render_file("docs/wrapping-react/complex-example.md")
