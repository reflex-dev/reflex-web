import pynecone as pc

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

    return pc.box(
        docheader("Project Structure", first=True),
        subheader("Directory Structure"),
        doctext("Let's create a new app called ", pc.code("hello"), "."),
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
            pc.code("pc init"),
            " creates.",
        ),
        subheader(".web"),
        doctext(
            "The Pynecone frontend compiles down to a ",
            doclink("NextJS", href=constants.NEXTJS_URL),
            " app. ",
            "The output is stored in the ",
            pc.code(".web"),
            " directory. ",
            "You will never need to touch this directory, "
            " but it can be useful for debugging.",
        ),
        doctext(
            "Each Pynecone page will compile to a corresponding ",
            pc.code(".js"),
            " file in the ",
            pc.code(".web/pages"),
            " directory. ",
        ),
        subheader("Assets"),
        doctext(
            "The ",
            pc.code("assets"),
            " directory is where you can store any static assets "
            " you want to be publicly available. ",
            "This includes images, fonts, and other files. ",
        ),
        doctext(
            "For example, if you save an image to ",
            pc.code("assets/image.png"),
            " you can display it from your app like this: ",
        ),
        doccode(
            """pc.image(src="image.png")""",
        ),
        subheader("Main Project"),
        doctext(
            "Initializing your project creates a directory with the same name as your app. ",
            "This is where you will write your app's logic. ",
        ),
        doctext(
            "Pynecone generates a default app within the ",
            pc.code("hello/hello.py"),
            " file. ",
            "You can modify this file to customize your app. ",
        ),
        subheader("Config"),
        doctext(
            "The ",
            pc.code("pcconfig.py"),
            " file contains configuration for your app. ",
            " By default it looks something like this: ",
        ),
        doccode(
            """import pynecone as pc


config = pc.Config(
    app_name="hello",
    bun_path="$HOME/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
""",
        ),
        doctext(
            "Pynecone uses ",
            doclink("bun", href=constants.BUN_URL),
            " to manage Javascript libraries. "
            "Bun is installed automatically when you run ",
            pc.code("pc init"),
            " at ",
            pc.code("~/.bun/bin/bun"),
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
            pc.code("pc.Env.DEV"),
            " or ",
            pc.code("pc.Env.PROD"),
            ". See the ",
            doclink("self hosting", href=self_hosting.path),
            " section for more details. ",
        ),
        subheader("Next Steps"),
        doctext(
            "Continue reading to see how to customize your app. ",
        ),
    )
