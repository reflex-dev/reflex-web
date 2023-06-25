import reflex as rx

from pcweb import constants
from pcweb.templates.docpage import (
    doccode,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader,
)

app_name = "my_app_name"
default_url = "http://localhost:3000"


@docpage()
def project_structure():
    from pcweb.pages.docs.database.overview import database_overview
    from pcweb.pages.docs.hosting.self_hosting import self_hosting

    return rx.box(
        docheader("Project Structure", first=True),
        subheader("Directory Structure"),
        doctext("Let's create a new app called ", rx.code("hello"), "."),
        doccode(
            """$ mkdir hello
$ cd hello
$ pc init""",
            language="bash",
        ),
        doctext(
            "This will create a directory structure like this:",
        ),
        doccode(
            """hello
├── .web
├── assets
├── hello
│   ├── __init__.py
│   └── hello.py
└── pcconfig.py""",
            language="bash",
        ),
        doctext(
            "Let's go over what ",
            rx.code("pc init"),
            " creates.",
        ),
        subheader(".web"),
        doctext(
            "The Reflex frontend compiles down to a ",
            doclink("NextJS", href=constants.NEXTJS_URL),
            " app. ",
            "The output is stored in the ",
            rx.code(".web"),
            " directory. ",
            "You will never need to touch this directory, "
            " but it can be useful for debugging.",
        ),
        doctext(
            "Each Reflex page will compile to a corresponding ",
            rx.code(".js"),
            " file in the ",
            rx.code(".web/pages"),
            " directory. ",
        ),
        subheader("Assets"),
        doctext(
            "The ",
            rx.code("assets"),
            " directory is where you can store any static assets "
            " you want to be publicly available. ",
            "This includes images, fonts, and other files. ",
        ),
        doctext(
            "For example, if you save an image to ",
            rx.code("assets/image.png"),
            " you can display it from your app like this: ",
        ),
        doccode(
            """rx.image(src="image.png")""",
        ),
        subheader("Main Project"),
        doctext(
            "Initializing your project creates a directory with the same name as your app. ",
            "This is where you will write your app's logic. ",
        ),
        doctext(
            "Reflex generates a default app within the ",
            rx.code("hello/hello.py"),
            " file. ",
            "You can modify this file to customize your app. ",
        ),
        subheader("Config"),
        doctext(
            "The ",
            rx.code("pcconfig.py"),
            " file contains configuration for your app. ",
            " By default it looks something like this: ",
        ),
        doccode(
            """import reflex as rx


config = rx.Config(
    app_name="hello",
    bun_path="$HOME/.bun/bin/bun",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
    port=3000,
)
""",
        ),
        doctext(
            "Reflex uses ",
            doclink("bun", href=constants.BUN_URL),
            " to manage Javascript libraries. "
            "Bun is installed automatically when you run ",
            rx.code("pc init"),
            " at ",
            rx.code("~/.bun/bin/bun"),
            ". ",
            "You can specify a different path in your config. ",
        ),
        doctext(
            "The database url is discussed in the ",
            doclink("database", href=database_overview.path),
            " section. ",
        ),
        doctext(
            "The environment can be set to ",
            rx.code("rx.Env.DEV"),
            " or ",
            rx.code("rx.Env.PROD"),
            ". See the ",
            doclink("self hosting", href=self_hosting.path),
            " section for more details. ",
        ),
        subheader("Next Steps"),
        doctext(
            "Continue reading to see how to customize your app. ",
        ),
    )
