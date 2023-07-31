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
    subheader
)
from pcweb.constants import CHAT_APP_URL


@docpage()
def intro():
    return rx.box(
        docheader("Interactive Tutorial: Chat App"),
        doctext(
            """
            This tutorial will walk you through building an ai chat app with Reflex. This app is fairly complex, but don't worry we'll break it down into small steps. You can find the full source code for this app 
            """,
            doclink("here", href=CHAT_APP_URL),
            ".",
        ),
        subheader("What you'll do"),
        doctext(   
            """
            In this tutorial you'll learn how to:
            """,
            rx.ordered_list(
                rx.list_item("Define and style your UI"),
                rx.list_item("Add interactivity to your Reflex app"),
                rx.list_item("Deploy your Reflex app"),
                margin_top=".5em",
            )
        )
    )
