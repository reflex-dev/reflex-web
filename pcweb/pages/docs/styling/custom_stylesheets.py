import pynecone as pc
from pcweb.pages.docs.components.assets import assets
from pcweb.templates.docpage import (
    doccode,
    docdemo,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader,
)

code1 = """pc.text(
    "Check out my font",
    font_family="Silkscreen",
    font_size="1.5em",
)
"""

code2 = """@font-face {
    font-family: MyFont;
    src: url("MyFont.otf") format("opentype");
}

@font-face {
    font-family: MyFont;
    font-weight: bold;
    src: url("MyFont.otf") format("opentype");
}
"""


@docpage()
def custom_stylesheets():
    return pc.box(
        docheader("Custom Stylesheets", first=True),
        doctext(
            (
                "Pynecone allows you to add custom stylesheets. "
                "Simply pass the URLs of the stylesheets to "
            ),
            pc.code("pc.App"),
            ":",
        ),
        doccode(
            """app = pc.App(
    stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    ],
)"""
        ),
        subheader("Local Stylesheets"),
        doctext(
            "You can also add local stylesheets. Just put the stylesheet under ",
            pc.code(doclink("assets/", assets.path)),
            " and pass the path to the stylesheet to ",
            pc.code("pc.App"),
            ":",
        ),
        doccode(
            """app = pc.App(
    stylesheets=[
        "styles.css",  # This path is relative to assets/
    ],
)"""
        ),
        subheader("Fonts"),
        doctext(
            "You can take advantage of Pynecone's support for custom stylesheets to add"
            " custom fonts to your app."
        ),
        doctext(
            "Then you can use the font in your app by setting the ",
            pc.code("font_family"),
            " prop.",
        ),
        doctext(
            "In this example, we will use the ",
            doclink("Silkscreen", href="https://fonts.google.com/specimen/Silkscreen"),
            " font from Google Fonts.",
        ),
        docdemo(code1),
        subheader("Local Fonts"),
        doctext(
            "By making use of the two previous points, we can also make a stylesheet"
            " that allow you to use a font hosted on your server."
        ),
        doctext(
            "If your font is called ",
            pc.code("MyFont.otf"),
            ", copy it in ",
            pc.code("assets/fonts"),
        ),
        doctext(
            "Now we have the font ready, let's create the stylesheet ",
            pc.code("myfont.css"),
        ),
        doccode(code2, language="css"),
        doctext("Add the reference to your new Stylesheet in your App"),
        doccode(
            """app = pc.App(
            stylesheets=[
                "font/myfont.css",  # This path is relative to assets/
            ],
        )"""
        ),
        doctext(
            "And that's it! You can now use ",
            pc.code("MyFont"),
            " like any other FontFamily to style your components",
        ),
    )
