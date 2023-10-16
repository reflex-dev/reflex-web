from pcweb import flexdown
from pcweb.templates.docpage import docpage


@docpage()
def self_hosting():
    return flexdown.render_file("docs/hosting/self-hosting.md")