import pynecone as pc

from pcweb.templates.docpage import (
    doccode,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader,
docalert
)

CONFIG_REF_URL = "/docs/api-reference/config"

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

@docpage()
def configuration():
    return pc.box(
        docheader("Configuration"),
        doctext("There are 3 ways to configure your Pynecone application."),
        subheader("PCConfig Arguments"),
        doctext(
            "The first place to configure your Pynecone application is ",
            "by setting the different options in the ",
            pc.code("pcconfig.py"),
            " file.",
        ),
        pc.text(
            "Refer to the ",
            doclink("Config API Reference ", href=CONFIG_REF_URL),
            " for the details of all options available."
        ),
        subheader("Environment Arguments"),
        doctext(
            "By default, Pynecone looks for a .env file in your root directory.",
            " You can change this setting by specifying a custom path to a ",
            pc.code(".env"),
            " file using the ",
            pc.code("env_path"),
            " keyword argument (or overriding the ",
            pc.code("env_path"),
            " attribute in your custom config class).",
            doccode(config_example1),
            "or alternatively: ",
            doccode(config_example2),
            "Environment variables set in a ",
            pc.code(".env"),
            " file overrides os environment variables by default. To change this setting, set the ",
            pc.code("override_os_envs"),
            " argument or attribute to ",
            pc.code("False.")
        ),
        docalert(
            pc.text(
                "If the ",
                pc.code("override_os_envs"),
                "argument is set to ",
                pc.code("True"),
                " (which is the default), the order of precedence of "
                "environment variables from highest to lowest will be :",
                pc.code(".env file >> os environment or commandline args >> pcconfig args."),
                " However, if set to ",
                pc.code("False"),
                ", the order of precedence becomes: ",
                pc.code("os environment or commandline args >> .env file >> pcconfig args.")
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
