import reflex as rx

from pcweb.templates.docpage import (
    doccode,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader,
    docalert,
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
        doctext("There are 3 ways to configure your Reflex application."),
        subheader("RXConfig Arguments"),
        doctext(
            "The first place to configure your Reflex application is ",
            "by setting the different options in the ",
            rx.code("rxconfig.py"),
            " file.",
        ),
        rx.text(
            "Refer to the ",
            doclink("Config API Reference ", href=CONFIG_REF_URL),
            " for the details of all options available.",
        ),
        subheader("Environment Arguments"),
        doctext(
            "By default, Reflex looks for a .env file in your root directory.",
            " You can change this setting by specifying a custom path to a ",
            rx.code(".env"),
            " file using the ",
            rx.code("env_path"),
            " keyword argument (or overriding the ",
            rx.code("env_path"),
            " attribute in your custom config class).",
            doccode(config_example1),
            "or alternatively: ",
            doccode(config_example2),
            "Environment variables set in a ",
            rx.code(".env"),
            " file overrides os environment variables by default. To change this setting, set the ",
            rx.code("override_os_envs"),
            " argument or attribute to ",
            rx.code("False."),
        ),
        docalert(
            rx.text(
                "If the ",
                rx.code("override_os_envs"),
                "argument is set to ",
                rx.code("True"),
                " (which is the default), the order of precedence of "
                "environment variables from highest to lowest will be :",
                rx.code(
                    ".env file >> os environment or commandline args >> rxconfig args."
                ),
                " However, if set to ",
                rx.code("False"),
                ", the order of precedence becomes: ",
                rx.code(
                    "os environment or commandline args >> .env file >> rxconfig args."
                ),
            ),
        ),
        subheader("Command line Arguments"),
        doctext(
            "These are the arguments that you pass when using ",
            rx.code("reflex run"),
            ".",
        ),
        doctext(
            "The arguments to pass when running your app are defined ",
            doclink("here", href="/docs/api-reference/cli"),
        ),
    )
