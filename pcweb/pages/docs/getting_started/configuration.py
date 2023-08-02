import reflex as rx

from pcweb.templates.docpage import (
    doccode,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader,
)

CONFIG_REF_URL = "/docs/api-reference/config"

config_example1 = """
# rxconfig.py
import reflex as rx
class ExpConfig(rx.Config):
    pass
    
config = ExpConfig(
    env_path = "path/to/env/file",
    ...
)

"""

config_example2 = """
# rxconfig.py
import reflex as rx
class ExpConfig(rx.Config):
    env_path = "path/to/env/file"

config = ExpConfig(
    ...
)

"""


@docpage()
def configuration():
    return rx.box(
        docheader("Configuration"),
        doctext(
            "Reflex apps can be configured using a ",
            "configuration file, environment variables, and command line arguments. ",
        ),
        subheader("Configuration File"),
        doctext(
            "Running ",
            rx.code("reflex init"),
            " will create an ",
            rx.code("rxconfig.py"),
            " file in your root directory. ",
            "You can pass keyword arguments to the ",
            rx.code("Config"),
            " class to configure your app.",
        ),
        doctext(
            "For example: ",
        ),
        doccode(
            """# rxconfig.py
import reflex as rx

config = rx.Config(
    app_name="my_app_name",
    # Connect to your own database.
    db_url="postgresql://user:password@localhost:5432/my_db",
    # Change the frontend port.
    frontend_port=3001,
)
"""
        ),
        rx.text(
            "See the ",
            doclink("config reference ", href=CONFIG_REF_URL),
            " for all the parameters available.",
        ),
        subheader("Environment Variables"),
        doctext(
            "You can override the configuration file by setting environment variables. ",
            "For example, to override the ",
            rx.code("frontend_port"),
            " setting, you can set the ",
            rx.code("FRONTEND_PORT"),
            " environment variable.",
        ),
        doccode(
            """$ FRONTEND_PORT=3001 reflex run""",
            language="bash",
        ),
        subheader("Command Line Arguments"),
        doctext(
            "Finally, you can override the configuration file and environment variables ",
            "by passing command line arguments to ",
            rx.code("reflex run"),
            ".",
        ),
        doccode(
            """$ reflex run --frontend-port 3001""",
            language="bash",
        ),
        doctext(
            "See the ",
            doclink("CLI reference", href="/docs/api-reference/cli"),
            " for all the arguments available.",
        ),
    )
