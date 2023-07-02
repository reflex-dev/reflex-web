import reflex as rx

from pcweb.templates.docpage import (
    doccode,
    docdemo,
    docheader,
    docpage,
    doctext,
    subheader,
)

code_example1 = "rx.image(src = '/Reflex.svg', width = '5em')"


@docpage()
def assets():
    return rx.box(
        docheader("Assets", first=True),
        doctext(
            "Static files such as images and stylesheets can be placed in ",
            rx.code("assets/"),
            " folder of the project. These files can be referenced within your app.",
        ),
        subheader("Referencing Assets"),
        doctext(
            "To reference an image in the ",
            rx.code("assets/"),
            " simply pass the relative path as a prop.",
        ),
        doctext("For example, you can store your logo in your assets folder: "),
        doccode(
            """assets
└── logo.png""",
            language="bash",
        ),
        doctext(
            "Then you can display it using a ",
            rx.code("rx.image"),
            " component:",
        ),
        docdemo(code_example1),
        subheader("Favicon"),
        doctext(
            "The favicon is the small icon that appears in the browser tab. ",
        ),
        doctext(
            "You can add a ",
            rx.code("favicon.ico"),
            " file to the ",
            rx.code("assets/"),
            " folder to change the favicon.",
        ),
    )
