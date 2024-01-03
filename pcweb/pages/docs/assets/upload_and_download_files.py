from pcweb import flexdown
from pcweb.templates.docpage import (
    docpage,
)

code_example1 = "rx.image(src = '/Reflex.svg', width = '5em')"


@docpage()
def upload_and_download_files():
    return flexdown.render_file("docs/assets/upload_and_download_files.md")
