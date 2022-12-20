import pynecone as pc

from pcweb.templates.docpage import (
    doccode,
    docdemo,
    docheader,
    docpage,
    doctext,
    subheader,
)

code_example1 = "pc.image(src = '/logo.png', width = '5em')"


@docpage()
def assets():
    return pc.box(
        docheader("Assets", first=True),
        doctext(
            "Static files such as images can be placed in ",
            pc.code("assets/"),
            " folder of the project. These files can be referenced within your app.",
        ),
        subheader("Referencing Assets"),
        doctext(
            "To reference an image in the ",
            pc.code("assets/"),
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
            pc.code("pc.image"),
            " component:",
        ),
        docdemo(code_example1),
        subheader("Favicon"),
        doctext(
            "The favicon is the small icon that appears in the browser tab. ",
        ),
        doctext(
            "You can add a ",
            pc.code("favicon.ico"),
            " file to the ",
            pc.code("assets/"),
            " folder to change the favicon.",
        ),
    )
