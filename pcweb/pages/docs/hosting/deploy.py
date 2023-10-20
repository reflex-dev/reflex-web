from pcweb import flexdown
from pcweb.templates.docpage import docpage


@docpage()
def deploy():
    return flexdown.render_file("docs/hosting/deploy.md")
