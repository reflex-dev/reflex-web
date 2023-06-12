import pynecone as pc

from pcweb import constants
from pcweb.templates.docpage import (
    doccode,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader,
docalert
)


config_example1 = """
# pcconfig.py
import pynecone as pc
class ExpConfig(pc.Config):
    pass
    
config = ExpConfig(
    env_path = "path/to/env/file",
    ...
)

"""

config_example2 = """
# pcconfig.py
import pynecone as pc
class ExpConfig(pc.Config):
    env_path = "path/to/env/file"

config = ExpConfig(
    ...
)

"""
CONFIG_REF_URL = "/docs/api-reference/config"
@docpage()
def configuration():
    return pc.box(
        docheader("Configuration"),
        doctext("There are 3 ways to configure your pynecone application."),
        doctext(""),
        subheader("PCConfig Arguments"),
        doctext(
            "The first place to configure your pynecone application is ",
            "by setting the different options in the",
            pc.code("pcconfig.py"),
            " file.",
        ),
        pc.text(
            "Refer to the ",
            doclink("Config API Reference ", href=CONFIG_REF_URL),
            "for the details of all options availables."
        ),
        subheader("Environment Arguments"),
        doctext(
            "By default, pynecone looks for a .env file (with ",
            pc.code(".env"),
            "as file name) in your root directory.",
            "You can change this setting by specifying a custom path to a .env file using the ",
            pc.code("env_path"),
            " keyword argument(or overriding the ",
            pc.code("env_path"),
            " attribute in your custom config class).",
            doccode(config_example1),
            "or alternatively: ",
            doccode(config_example2),
            "Environment variables set in a .env file overrides os environment variables by default. To change this setting, set the",
            pc.code("override_os_envs"),
            "argument or attribute to",
            pc.code("False.")
        ),
        doctext(
            "Any environment options will prevail over the one defined in ",
            pc.code("pcconfig.py"),
        ),
        docalert(
            pc.text(
                "If the ",
                pc.code("override_os_envs", bg="#bee3f8"),
                "argument is set to True( which is the default ), the order of precedence of "
                "environment variables from highest to lowest will be :",
                pc.code(".env file >> os environment or commandline args >> pcconfig args.", bg="#bee3f8"),
                "However, if set to False, the order of precedence becomes: ",
                pc.code("os environment or commandline args >> .env file >> pcconfig args.", bg="#bee3f8")
            ),

        ),
        subheader("Command line Arguments"),
        doctext(
            "These are the arguments that you pass when using ", pc.code("pc run"), "."
        ),
        doctext(
            "The arguments to pass when running your app are defined ",
            doclink("here", href="/docs/api-reference/cli"),
        ),
    )
