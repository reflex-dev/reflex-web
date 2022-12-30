import pynecone as pc

from pcweb import constants
from pcweb.templates.docpage import (
    copy_to_clipboard,
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
                doclink("NodeJS 12.22.0+", href=constants.NODEJS_URL),
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
            "$ pip install pynecone-io",
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
                    "Note that the port may be different if you have another app running on port ",
                    pc.code("3000"),
                    ".",
                ),
                status="warning",
            ),
        ),
        subheader("Fast Refresh"),
        doctext(
            "Now you can modify the source code in ",
            pc.code(f"{app_name}/{app_name}.py"),
            ". Pynecone has fast refreshes so you can see your changes instantly when you save your code. ",
        ),
        doctext("Continue reading to learn how to customize your app."),
    )
