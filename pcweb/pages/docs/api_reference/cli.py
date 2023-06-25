import reflex as rx

from pcweb.templates.docpage import (
    doccode,
    docheader,
    docpage,
    doctext,
    subheader,
)

code_example1 = """rx.text('hello world', color='blue')"""


@docpage()
def cli():
    return rx.box(
        docheader("CLI", first=True),
        doctext(
            "The ",
            rx.code("pc"),
            " command line interface (CLI) is a tool for creating and managing Reflex apps. ",
        ),
        doctext(
            "To see a list of all available commands, run ",
            rx.code("pc --help"),
            ".",
        ),
        doccode(
            """$ pc --help
Usage: pc [OPTIONS] COMMAND [ARGS]...

Options:
  --help   Show this message and exit.

Commands:
  deploy   Deploy the app to the Reflex hosting service.
  export   Export the app to a zip file.
  init     Initialize a new Reflex app in the current directory.
  run      Run the app in the current directory.
  version  Get the Reflex version.""",
            language="bash",
        ),
        subheader("Init"),
        doctext(
            "The ",
            rx.code("pc init"),
            " command creates a new Reflex app in the current directory. ",
            "If a ",
            rx.code("pcconfig.py"),
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
            rx.code("pc run"),
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
  --frontend-only                 Execute only frontend.
  --backend-only                  Execute only backend.
  --loglevel [debug|info|warning|error|critical]
                                  The log level to use.  [default:
                                  LogLevel.ERROR]
  --frontend-port TEXT            Specify a different frontend port.
  --backend-host TEXT             Specify a different backend host.
  --backend-port TEXT             Specify a different backend port.
  --help                          Show this message and exit.
  """,
            language="bash",
        ),
        subheader("Export"),
        doctext(
            "You can export your app's frontend and backend to zip files using the ",
            rx.code("pc export"),
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
  --for-pc-deploy  Whether export the app for Reflex Deploy Service.
  --help           Show this message and exit.
  """,
            language="bash",
        ),
    )
