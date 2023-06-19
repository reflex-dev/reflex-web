import pynecone as pc

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
    return pc.box(
        docheader("Installation", first=True),
        subheader("Prerequisites"),
        doctext(
            "Pynecone requires the following to get started:",
        ),
        pc.unordered_list(
            pc.list_item("Python 3.7+"),
            pc.list_item(
                doclink("NodeJS 16.8.0+", href=constants.NODEJS_URL),
            ),
            padding_left="2em",
        ),
        pc.divider(),
        subheader("Virtual Environment (Optional)"),
        doctext(
            "We recommend creating a virtual environment for your project. ",
        ),
        doctext(
            "Below are some tools you can use to manage environments:",
        ),
        pc.unordered_list(
            pc.list_item(doclink("poetry", href=constants.POETRY_URL)),
            pc.list_item(doclink("pipenv", href=constants.PIPENV_URL)),
            pc.list_item(
                doclink("venv", href=constants.VENV_URL),
            ),
            pc.list_item(
                doclink("virtualenv", href=constants.VIRTUALENV_URL),
            ),
            pc.list_item(doclink("conda", href=constants.CONDA_URL)),
            padding_left="2em",
            padding_bottom="1em",
        ),
        subheader("Installing"),
        doctext(
            "Pynecone is available as a ",
            doclink("pip", href=constants.PIP_URL),
            " library:",
        ),
        doccode(
            "$ pip install pynecone",
            language="bash",
        ),
        subheader("Create a Project"),
        doctext(
            "Installing Pynecone also installs the ",
            pc.code("pc"),
            " command line tool. ",
        ),
        doctext(
            "Test that the install was successful by creating a new project. Replace ",
            pc.code(app_name),
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
            pc.alert(
                pc.alert_icon(),
                pc.alert_title(
                    "You can run your app on a different port with the ",
                    pc.code("--frontend-port"),
                    " flag. ",
                ),
                status="success",
            ),
        ),
        docalert(
            "Running on Windows",
            "We strongly advise you to use Windows Subsystem for Linux (WSL) for optimal performance"
            " when using Pynecone. Due to compatibility issues with one of our dependencies, Bun,"
            " you may experience slower performance on Windows. By using WSL, you can expect to "
            "see a significant speed increase.",
            status="warning",
        ),
        doctext(
            "Pynecone also starts a ",
            doclink("FastAPI", href=constants.FASTAPI_URL),
            " server at port ",
            pc.code("8000"),
            ". All of your event handlers run on this server, ",
            " and state changes are sent to the client via websockets. ",
        ),
        doctext(
            "You can debug your app by setting the ",
            pc.code("--loglevel"),
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
            "Pynecone has fast refresh built in when running in development mode. ",
            "You can modify the source code in ",
            pc.code(f"{app_name}/{app_name}.py"),
            " and see your changes in the browser instantly when you save your code. ",
        ),
        docalert(
            "Fast Refresh on Windows",
            "When running on windows, the hot reload feature may not work as "
            "expected if you're running a project that resides on a different "
            "file system (eg. running your Pynecone project from Windows with "
            "your project residing on the WSL file system). This is as a result "
            "of incompatibilities between the the windows file system and that of WSL."
            " It is however, recommended "
            "to run your app on the same file system your app resides.",
            status="error",
        ),

        doctext("Continue reading to learn how to customize your app."),
    )
