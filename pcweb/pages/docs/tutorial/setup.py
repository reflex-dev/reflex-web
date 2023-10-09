import reflex as rx
from pcweb import constants
from pcweb.templates.docpage import (
    doccode,
    docheader,
    doclink,
    docpage,
    doctext,
)


@docpage()
def setup():
    return rx.box(
        docheader("Setting up Your Project", first=True),
        doctext(
            "We will start by creating a new project and setting up our development environment. ",
            "First, create a new directory for your project and navigate to it. ",
        ),
        doccode(
            """~ $ mkdir chatapp
~ $ cd chatapp""",
            language="bash",
        ),
        doctext(
            "Next, we will create a virtual environment for our project. ",
            "This is optional, but recommended. ",
            "In this example, we will use ",
            doclink("venv", href=constants.VENV_URL),
            " to create our virtual environment. ",
        ),
        doccode(
            """chatapp $ python3 -m venv venv
$ source venv/bin/activate""",
            language="bash",
        ),
        doctext(
            "Now, we will install Reflex and create a new project. ",
            "This will create a new directory structure in our project directory. ",
        ),
        doccode(
            """chatapp $ pip install reflex
chatapp $ reflex init
────────────────────────────────── Initializing chatapp ───────────────────────────────────
Success: Initialized chatapp
chatapp $ ls
assets          chatapp         rxconfig.py     venv""",
            language="bash",
        ),
        doctext(
            "You can run the template app to make sure everything is working. ",
        ),
        doccode(
            """chatapp $ reflex run
─────────────────────────────────── Starting Reflex App ───────────────────────────────────
Compiling:  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 1/1 0:00:00
─────────────────────────────────────── App Running ───────────────────────────────────────
App running at: http://localhost:3000""",
            language="bash",
        ),
        doctext(
            "You should see your app running at ",
            doclink("http://localhost:3000", href="http://localhost:3000"),
            ".",
        ),
        doctext(
            "Reflex also starts the backend server which handles all the state management and communication with the frontend. ",
            "You can test the backend server is running by navigating to ",
            doclink("http://localhost:8000/ping", href="http://localhost:8000/ping"),
            ". ",
        ),
        doctext(
            "Now that we have our project set up, in the next section we will start building our app! ",
        ),
    )
