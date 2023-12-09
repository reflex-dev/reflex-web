from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage()
def rendering_iterables():
    return flexdown.render_file("docs/rendering_iterables.md")