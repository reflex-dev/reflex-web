import pynecone as pc

from pcweb.templates.docpage import (
    doccode,
    docheader,
    docpage,
    doctext,
    subheader,
)

code_example1 = """pc.text('hello world', color='blue')"""


@docpage()
def cli():
    return pc.box(
        docheader("CLI", first=True),
        doctext(
            "The ",
            pc.code("pc"),
            " command line interface (CLI) is a tool for creating and managing Pynecone apps. ",
        ),
        doctext(
            "To see a list of all available commands, run ",
            pc.code("pc --help"),
            ".",
        ),
        doccode(
            """$ pc --help
Usage: pc [OPTIONS] COMMAND [ARGS]...

Options:
  --help   Show this message and exit.

Commands:
  deploy   Deploy the app to the Pynecone hosting service.
  export   Export the app to a zip file.
  init     Initialize a new Pynecone app in the current directory.
  run      Run the app in the current directory.
  version  Get the Pynecone version.""",
            language="bash",
        ),
        subheader("Init"),
        doctext(
            "The ",
            pc.code("pc init"),
            " command creates a new Pynecone app in the current directory. ",
            "If a ",
            pc.code("pcconfig.py"),
            " file already exists already, it will re-initialize the app with the latest template. ",
        ),
        doccode(
            """ ~/my_app $ pc init
[...] Initializing the web directory.                                                                                                                            utils.py:421
[...] Finished Initializing: my_app
my_app $ tree
.
├── assets
│   └── favicon.ico
├── my_app
│   ├── __init__.py
│   └── my_app.py
└── pcconfig.py
 """,
            language="bash",
        ),
    )
