import reflex as rx
from pcweb import styles
from pcweb.base_state import State
from pcweb.templates.docpage import (
    doc_section,
    doccode,
    docdemobox,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader_comp,
    text_comp,
    definition,
    docalert,
)


@docpage()
def deployment():
    return rx.box()
