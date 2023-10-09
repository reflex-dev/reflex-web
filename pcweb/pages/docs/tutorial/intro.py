import reflex as rx
from pcweb.templates.docpage import (
    docheader,
    doclink,
    docpage,
    doctext,
    subheader,
)
from pcweb.constants import CHAT_APP_URL


@docpage()
def intro():
    return rx.box(
        docheader("Interactive Tutorial: AI Chat App"),
        doctext(
            "This tutorial will walk you through building an AI chat app with Reflex. ",
            "This app is fairly complex, but don't worry - we'll break it down into small steps. ",
        ),
        doctext(
            "You can find the full source code for this app ",
            doclink("here", href=CHAT_APP_URL),
            ".",
        ),
        subheader("What You'll Learn"),
        doctext(
            "In this tutorial you'll learn how to: ",
            rx.ordered_list(
                rx.list_item(
                    "Install ",
                    rx.code("reflex"),
                    " and set up your development environment.",
                ),
                rx.list_item("Create components to define and style your UI."),
                rx.list_item("Use state to add interactivity to your app."),
                rx.list_item("Deploy your app to share with others."),
                margin_top=".5em",
            ),
        ),
        min_height="70vh",
    )
