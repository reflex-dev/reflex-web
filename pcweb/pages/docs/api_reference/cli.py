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
~/my_app $ tree
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
        subheader("Run"),
        doctext(
            "The ",
            pc.code("pc run"),
            " command runs the app in the current directory. ",
        ),
        doctext(
            "By default it runs your app in development mode. ",
            "This means that the app will automatically reload when you make changes to the code. ",
            "You can also run in production mode which will create an optimized build of your app. ",
        ),
        doctext(
            "You can configure the mode, as well as other options through flags. ",
        ),
        doccode(
            """$ pc run --help
Usage: pc run [OPTIONS]

  Run the app in the current directory.

Options:
  --env [dev|prod]                The environment to run the app in.
                                  [default: Env.DEV]
  --no-frontend                   Disable frontend execution.  [default: True]
  --no-backend                    Disable backend execution.  [default: True]
  --loglevel [debug|info|warning|error|critical]
                                  The log level to use.  [default:
                                  LogLevel.ERROR]
  --port TEXT                     Specify a different port.
  --help                          Show this message and exit.
  """,
            language="bash",
        ),
        subheader("Export"),
        doctext(
            "You can export your app's frontend and backend to zip files using the ",
            pc.code("pc export"),
            " command. ",
        ),
        doctext(
            "The frontend is a compiled NextJS app, which can be deployed to a static hosting service like ",
            "Github Pages or Vercel. ",
            "However this is just a static build, so you will need to deploy the backend separately. ",
            "See the self-hosting guide for more information. ",
        ),
        doccode(
            """$ pc export --help
Usage: pc export [OPTIONS]

  Export the app to a zip file.

Options:
  --no-zip         Disable zip for backend and frontend exports.  [default:
                   True]
  --backend-only   Export only backend.
  --frontend-only  Export only frontend.
  --for-pc-deploy  Whether export the app for Pynecone Deploy Service.
  --help           Show this message and exit.
  """,
            language="bash",
        ),
    )
