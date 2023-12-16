from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def conditional_rendering():
    return flexdown.render_file("docs/conditional_rendering.md")

