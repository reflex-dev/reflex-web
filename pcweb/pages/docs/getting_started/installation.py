import reflex as rx

from pcweb import constants
from pcweb.templates.docpage import (
    docalert,
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
def installation():
    return rx.box(
        docheader("Installation", first=True),
        subheader("Prerequisites"),
        doctext(
            "Reflex requires the following to get started:",
        ),
        rx.unordered_list(
            rx.list_item("Python 3.7+"),
            rx.list_item(
                doclink("NodeJS 16.8.0+", href=constants.NODEJS_URL),
            ),
            padding_left="2em",
        ),
        rx.divider(),
        subheader("Virtual Environment (Optional)"),
        doctext(
            "We recommend creating a virtual environment for your project. ",
        ),
        doctext(
            "Below are some tools you can use to manage environments:",
        ),
        rx.unordered_list(
            rx.list_item(doclink("poetry", href=constants.POETRY_URL)),
            rx.list_item(doclink("pipenv", href=constants.PIPENV_URL)),
            rx.list_item(
                doclink("venv", href=constants.VENV_URL),
            ),
            rx.list_item(
                doclink("virtualenv", href=constants.VIRTUALENV_URL),
            ),
            rx.list_item(doclink("conda", href=constants.CONDA_URL)),
            padding_left="2em",
            padding_bottom="1em",
        ),
        subheader("Installing"),
        doctext(
            "Reflex is available as a ",
            doclink("pip", href=constants.PIP_URL),
            " library:",
        ),
        doccode(
            "$ pip install reflex",
            language="bash",
        ),
        subheader("Create a Project"),
        doctext(
            "Installing Reflex also installs the ",
            rx.code("pc"),
            " command line tool. ",
        ),
        doctext(
            "Test that the install was successful by creating a new project. Replace ",
            rx.code(app_name),
            " with your project name:",
        ),
        doccode(
            "\n".join(
                [
                    f"$ mkdir {app_name}",
                    f"$ cd {app_name}",
                    "$ pc init",
                ]
            ),
            language="bash",
        ),
        doctext("This initializes a template app in your new directory. "),
        subheader("Run the App"),
        doctext("You can run this app in development mode: "),
        doccode(
            "\n".join(
                [
                    "$ pc run",
                ]
            ),
            language="bash",
        ),
        doctext(
            "You should see your app running at ",
            doclink(default_url, href=default_url),
            ".",
        ),
        doctext(
            rx.alert(
                rx.alert_icon(),
                rx.alert_title(
                    "You can run your app on a different port with the ",
                    rx.code("--frontend-port"),
                    " flag. ",
                ),
                status="success",
            ),
        ),
        docalert(
            "Running on Windows.",
            "We strongly advise you to use Windows Subsystem for Linux (WSL) for optimal performance"
            " when using Reflex. Due to compatibility issues with one of our dependencies, Bun,"
            " you may experience slower performance on Windows. By using WSL, you can expect to "
            "see a significant speed increase.",
            status="warning",
        ),
        doctext(
            "Reflex also starts a ",
            doclink("FastAPI", href=constants.FASTAPI_URL),
            " server at port ",
            rx.code("8000"),
            ". All of your event handlers run on this server, ",
            " and state changes are sent to the client via websockets. ",
        ),
        doctext(
            "You can debug your app by setting the ",
            rx.code("--loglevel"),
            " flag. ",
        ),
        doccode(
            "\n".join(
                [
                    "$ pc run --loglevel debug",
                ]
            ),
            language="bash",
        ),
        subheader("Fast Refresh"),
        doctext(
            "Reflex has fast refresh built in when running in development mode. ",
            "You can modify the source code in ",
            rx.code(f"{app_name}/{app_name}.py"),
            " and see your changes in the browser instantly when you save your code. ",
        ),
        docalert(
            "Fast Refresh on Windows.",
            "When running on windows, the hot reload feature may not work as "
            "expected if you're running a project that resides on a different "
            "file system (eg. running your Reflex project from Windows with "
            "your project residing on the WSL file system). This is as a result "
            "of incompatibilities between the the windows file system and that of WSL."
            " It is however, recommended "
            "to run your app on the same file system your app resides.",
            status="error",
        ),
        doctext("Continue reading to learn how to customize your app."),
    )
