from pcweb.templates.docpage import docpage
from pcweb import flexdown


@docpage()
def project_structure():
    return flexdown.render_file("docs/getting-started/project-structure.md")
