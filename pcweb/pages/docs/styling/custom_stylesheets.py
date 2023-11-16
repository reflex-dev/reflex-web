from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def custom_stylesheets():
    return flexdown.render_file("docs/styling/customstylesheets.md")
